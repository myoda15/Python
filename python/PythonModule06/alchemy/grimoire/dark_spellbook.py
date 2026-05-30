from alchemy.grimoire.dark_validator import validate_dark_spell


def dark_spell() -> str:
    return f"Dark spell cast: {validate_dark_spell('Tenebris')}"
