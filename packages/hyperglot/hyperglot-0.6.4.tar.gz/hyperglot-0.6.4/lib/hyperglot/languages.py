"""
Helper classes to work with the lib/hyperglot/data in more pythonic way
"""
from functools import lru_cache
import os
import re
import yaml
import logging
from hyperglot import DB, LanguageValidity

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)

@lru_cache
def get_languages(**kwargs):
    """
    A _cached_ getter for a fresh Language object, saves expensive reading and
    instanting of the database.
    """
    return Languages(**kwargs)

@lru_cache
def find_language(search):
    """
    Utility method to find a language by ISO code or language name
    """

    hg = Languages(validity=LanguageValidity.TODO.value)

    search = search.lower()

    # Search as 3-letter iso code, return if matched
    if search in hg.keys():
        return [getattr(hg, search)], f"Matched from iso code {search}:"

    # Search from language names and autonyms
    # If a single match is a full 1=1 match return that
    # If a single match is a partial match, return iso and prompt with info
    # If more than one are found, return a list of isos as prompt

    matches = {}
    for iso in hg.keys():
        lang = getattr(hg, iso)
        name = lang.name.lower()
        aut = lang.autonym
        autonyms = [] if not aut else [aut.lower()]
        if "orthographies" in lang:
            for o in lang["orthographies"]:
                if "autonym" in o:
                    autonyms.append(o["autonym"].lower())

        if search == name or search in autonyms:
            return [lang], f"Matched from name match for {search}:"

        # For now let's not do any fancy input proximity checks, just partials
        search_in_autonym = len([a for a in autonyms if search in a]) > 0
        if search in name or search_in_autonym:
            matches[iso] = lang

    if len(matches) > 0:
        return matches.values(), f"Matched for search string {search}"

    return False, ""


class Languages(dict):
    """
    A dict wrapper around the language data yaml file with additional querying
    options for convenience
    """

    def __init__(
        self, 
        strict: bool = False, 
        inherit: bool = True, 
        validity: str = LanguageValidity.DRAFT.value,
    ):
        """
        @param strict (Boolean): Use Rosetta macrolanguage definitions (False)
            or ISO definitions (True). Defaults to False.
        @param inherit (Boolean): Inherit orthographies. Defaults to True.
        @param validity (Hyperglot.LanguageValidity): Minimum level of validity
            which languages must have. One of "todo", "draft", "preliminary",
            "verified". Defaults to "draft" — all languages with basic
            information, but possibly unconfirmed.
        """

        # Load raw yaml data for all languages
        for file in os.listdir(DB):
            if file.startswith(".") or not file.endswith(".yaml"):
                log.debug(f"Skipping irrelevant data file '{file}'")
                continue
            # Remove possibly appended escape underscore to get iso from
            # filename
            iso = re.sub(r"_", "", os.path.splitext(file)[0])
            
            try:
                with open(os.path.join(DB, file), "rb") as f:
                    data = yaml.load(f, Loader=yaml.Loader)
                    if not isinstance(data, dict):
                        raise ValueError("Not a dictionary")
                    self[iso] = data

            # Catch various formatting issues in the yaml files
            except ValueError as e:
                log.error(f"Malformed data in {file}: {e}")
            except yaml.scanner.ScannerError as e:
                log.error(f"Malformed data in {file}: {e}" )
            except yaml.parser.ParserError as e:
                log.error(f"Malformed data in {file}: {e}" )

        if inherit:
            self.inherit_orthographies_from_macrolanguage()
            self.inherit_orthographies()

        if not strict:
            self.lax_macrolanguages()

        self.filter_by_validity(validity)
        self.set_defaults()

    def __repr__(self):
        return "Languages DB dict with '%d' languages" % len(self.keys())

    def __getattribute__(self, iso: str):
        """
        A convenience getter returning initialized hyperglot.language.Language
        objects when their iso is used as key on this Languages.
        Where self["xxx"] returns the _raw yaml data_ self.xxx will return the
        more usable Language object
        """
        if iso != "keys" and iso in self.keys():
            # Note: Avoid circular imports so fetch Language only at this stage
            from hyperglot.language import Language
            return Language(iso, data=self[iso])

        return super().__getattribute__(iso)

    def set_defaults(self):
        """
        There are some implicit defaults we set if they are not in the data
        """
        for iso, lang in self.items():
            if "orthographies" in lang:
                if len(lang["orthographies"]) == 1 \
                        and "status" not in lang["orthographies"][0]:
                    log.debug("Implicitly setting only orthography of '%s' to "
                              "'primary'." % iso)
                    lang["orthographies"][0]["status"] = "primary"

    def lax_macrolanguages(self):
        """
        Unless specifically choosing the ISO macrolanguage model, we will
        bundle some macrolanguages and show them as single language
        This means: Remove includes attributes, remove included languages
        """
        pruned = dict(self)
        for iso, lang in self.items():
            if "preferred_as_individual" in lang:
                if "orthographies" not in lang:
                    log.warning("'%s' cannot be treated as individual, "
                                "because it does not have orthographies"
                                % iso)
                    continue

                if "includes" not in lang:
                    # This should not be the case, but let's not warn about it
                    # either; it just means there is no sub-languages to worry
                    # about
                    continue

                pruned = {key: data for key, data in pruned.items()
                          if key not in lang["includes"]}

        self.clear()
        self.update(pruned)

    def inherit_orthographies(self):
        """
        Check through all languages and if an orthography inherits from another
        language copy those orthographies
        """
        for iso, lang in self.items():
            if "orthographies" in lang:
                for o in lang["orthographies"]:
                    if "inherit" in o:
                        parent_iso = o["inherit"]
                        if len(parent_iso) != 3:
                            log.warning("'%s' failed to inherit "
                                        "orthography — not a language iso "
                                        "code" % iso)
                            continue
                        if parent_iso not in self:
                            log.warning("'%s' inherits an orthography from"
                                        " '%s', but no such language was "
                                        "found" % (iso, parent_iso))
                            continue

                        o = self.inherit_orthography(parent_iso, o, iso)

    def inherit_orthography(self, source_iso, extend, iso=""):
        """
        Return an orthography dict that has been extended by the source iso's
        orthography.

        @param source_iso str: The iso code of the language from which to
            inherit
        @param extend dict: The orthography dict of the language to which we
            inherit — existing keys are left unchanged
        @param iso str (optional): The iso code of the language to which we are
            inheriting to. If an orthography inherits more than once we do not
            have the inheriting's language context, so do not know the iso code
            to which this orthography belongs to in that case
        """
        logging.debug("Inherit orthography from '%s' to '%s'" % (source_iso,
                                                                 iso))

        ref = getattr(self, source_iso)
        if "script" in extend:
            ort = ref.get_orthography(extend["script"])
        else:
            ort = ref.get_orthography()

        if "inherit" in ort:
            logging.info("Multiple levels of inheritence from '%s'. The "
                         "language that inherited '%s' should inherit "
                         "directly from '%s' " %
                         (source_iso, source_iso, ort["inherit"]))
            ort = self.inherit_orthography(ort["inherit"], ort)

        if ort:
            log.debug("'%s' inheriting orthography from "
                      "'%s'" % (iso, source_iso))
            # Copy all the attributes we want to inherit
            # Note: No autonym inheritance
            for attr in ["base", "auxiliary", "marks", "note",
                         "combinations", "punctuation", "script",
                         "design_requirements", "design_alternates",
                         "numerals", "status"]:
                if attr in ort:
                    # Wrap in type constructor, to copy, not
                    # reference
                    ty = type(ort[attr])
                    if attr in extend:
                        log.info("'%s' skipping inheriting "
                                 "attribute '%s' from '%s': "
                                 "Already set" %
                                 (iso, source_iso, attr))
                    else:
                        extend[attr] = ty(ort[attr])
        else:
            log.warning("'%s' is set to inherit from '%s' but "
                        "no language or orthography found to "
                        "inherit from for script '%s'" %
                        (iso, source_iso, extend["script"]))

        return extend

    def inherit_orthographies_from_macrolanguage(self):
        """
        Check through all languages and if a language has no orthographies see
        if this language is included in a macrolanguage that has orthographies.
        If so, apply the macrolanguage's orthographies to this language
        """

        macrolanguages = {iso: lang for iso,
                          lang in self.items() if "includes" in lang}

        for lang in self:
            if "orthographies" not in self:

                for iso, m in macrolanguages.items():
                    if lang in m["includes"] and "orthographies" in m:
                        log.debug("Inheriting macrolanguage '%s' "
                                  "orthographies to language '%s'"
                                  % (iso, lang))
                        # Make an explicit copy to keep the two languages
                        # separate
                        self[lang]["orthographies"] = m["orthographies"].copy()

    def filter_by_validity(self, validity):
        if validity not in LanguageValidity.values():
            raise ValueError(
                "Validity level '%s' not valid, must be one of: %s" %
                (validity, ", ".join(LanguageValidity.values()))
            )

        allowed = LanguageValidity.index(validity)
        pruned = {}
        for iso, lang in self.items():
            try:
                if LanguageValidity.index(lang["validity"]) >= allowed:
                    pruned[iso] = lang
            except KeyError as e:
                # Provide more context, but escalate
                raise KeyError("Language '%s' missing attribute %s" %
                               (iso, e))

        self.clear()
        self.update(pruned)
