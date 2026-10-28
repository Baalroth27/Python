from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spellbook.light_spell_allowed_ingredients()
    if any(ingredient in ingredients.lower() for ingredient in allowed):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
