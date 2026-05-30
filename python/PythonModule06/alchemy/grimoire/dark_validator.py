from alchemy.grimoire.dark_spellbook import dark_spell


def validate_dark_spell(spell: str) -> str:
    result = dark_spell()
    if spell in result:
        return f"Dark spell '{spell}' is valid: {result}"
    return f"Dark spell '{spell}' is invalid"
