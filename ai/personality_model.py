def generate_clan_personality(clan_name):
    """
    Generate a personality description for each Naruto clan.
    :param clan_name: str, name of the clan (Uzumaki, Hyuga, Senju, Uchiha)
    :return: str, personality description
    """
    clan_personalities = {
        "Uzumaki": "Relentless, energetic, and determined. A true embodiment of perseverance and hope.",
        "Hyuga": "Calm, composed, and analytical. Always strategic with a focus on clarity and precision.",
        "Senju": "Wise, patient, and protective. Known for leadership, kindness, and the pursuit of peace.",
        "Uchiha": "Intense, cold, and calculated. A mind that thrives on emotion and deep internal reflection."
    }

    return f"Personality of the {clan_name} clan: {clan_personalities.get(clan_name, 'Unknown clan')}"
