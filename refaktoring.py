def _set_bank_codes(self, bank_codes_sf: str | None) -> list[int]:
    """Setter bankkoder som skal lastes."""
    if self.bank_codes == "ALLE_BANKER":
        return [
            int(code)
            for code in get_value_from_samspar_config_key(key="sdvh_banker")  # type: ignore
        ]
    elif self.bank_codes:
        return [int(code) for code in self.bank_codes]
    elif bank_codes_sf == "ALLE_BANKER":
        return [
            int(code)
            for code in get_value_from_samspar_config_key(key="sdvh_banker")  # type: ignore
        ]
    elif bank_codes_sf is not None:
        return [int(code) for code in bank_codes_sf.split(",")]
    else:
        raise ValueError(
            "Må spesifisere banker. Hvis ikke bankspesifikk, sett ALLE_BANKER i styretabellen."
        )


def _set_bank_codes(self, bank_codes_sf: str | None) -> list[int]:
    """Setter bankkoder som skal lastes."""
    if self.bank_codes != "ALLE_BANKER" and self.bank_codes:
        return [int(code) for code in self.bank_codes]
    elif self.bank_codes == "ALLE_BANKER" and bank_codes_sf not in [
        None,
        "ALLE_BANKER",
    ]:
        return [int(code) for code in bank_codes_sf.split(",")]
    elif self.bank_codes == "ALLE_BANKER" or bank_codes_sf == "ALLE_BANKER":
        return [
            int(code)
            for code in get_value_from_samspar_config_key(key="sdvh_banker")
        ]
    elif bank_codes_sf not in [None, "ALLE_BANKER"]:
        return [int(code) for code in bank_codes_sf.split(",")]
    else:
        raise ValueError(
            "Må spesifisere banker. Hvis ikke bankspesifikk, sett ALLE_BANKER i styretabellen."
        )


def _parse_bank_codes(self, codes: str | list[str]) -> list[int]:
    """Parser bankkoder til en liste med integers."""
    if isinstance(codes, str):
        codes = codes.split(",")
    return [int(code) for code in codes]

def _get_all_bank_codes(self) -> list[int]:
    """Henter alle bankkoder fra samspar_config."""
    return get_value_from_samspar_config_key(key="sdvh_banker")  # type: ignore

def _single_banks_are_specified_in_flow(self) -> bool:
    """Sjekker om bankkoder er angitt i flowen."""
    return self.bank_codes and self.bank_codes != "ALLE_BANKER"  # type: ignore

def _single_banks_are_specified_in_sf(self, bank_codes_sf: str | None) -> bool:
    """Sjekker om bankkoder er angitt i Snowflake-konfigurasjonstabell."""
    return bank_codes_sf not in [None, "ALLE_BANKER"]

def _all_banks_are_specified(self, bank_codes_sf: str | None) -> bool:
    """
    Sjekker om alle banker er angitt i flowen eller i Snowflake-konfigurasjonen.
    self.bank_codes er verdiene som er angitt i flowen, mens bank_codes_sf er verdiene som er
    hentet fra Snowflake-konfigurasjonstabell.
    """
    return self.bank_codes == "ALLE_BANKER" or bank_codes_sf == "ALLE_BANKER"

def _set_bank_codes(self, bank_codes_sf: str | None) -> list[int]:
    """Setter bankkoder som skal lastes."""
    if self._single_banks_are_specified_in_flow():
        return self._parse_bank_codes(self.bank_codes)  # type: ignore
    elif self._single_banks_are_specified_in_sf(bank_codes_sf):
        return self._parse_bank_codes(bank_codes_sf)  # type: ignore
    elif self._all_banks_are_specified(bank_codes_sf):
        return self._get_all_bank_codes()  # type: ignore
    else:
        raise ValueError(
            "Må spesifisere banker. Hvis ikke bankspesifikk, sett ALLE_BANKER i styretabellen."
        )