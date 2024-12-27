import openai
from ai.personality_model import generate_clan_personality

# OpenAI API key setup
openai.api_key = "your-openai-api-key"

def generate_tweet(clan_name, custom_message=""):
    """
    Generate a tweet based on the clan's personality using AI.
    :param clan_name: str, name of the clan (Uzumaki, Hyuga, Senju, Uchiha)
    :param custom_message: str, optional custom message to include in the tweet
    :return: str, the generated tweet
    """
    personality_prompt = generate_clan_personality(clan_name)
    
    # OpenAI GPT-3 prompt for generating a tweet
    prompt = f"{personality_prompt} {custom_message}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7
    )

    tweet = response.choices[0].text.strip()
    return tweet
