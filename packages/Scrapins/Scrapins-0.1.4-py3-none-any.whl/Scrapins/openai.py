import os
import json
import openai



def load_config():
    """Charge et vérifie la coniguation OpenAI depuis un fichier JSON."""
    if not os.path.exists(CONFIG_FILE_PATH):
        raise FileNotFoundError(
            f"{CONFIG_FILE_PATH} n'existe pas. Veuillez créer ce fichier avec votre clé API OpenAI.")

    with open(CONFIG_FILE_PATH, 'r') as file:
        config = json.load(file)

    if 'api_key' not in config:
        raise KeyError("Le fichier openai.json doit contenir une clé 'api_key'.")

    return config['api_key']

CONFIG_FILE_PATH = 'openai.json'
API_KEY = load_config()
CLIENT = openai.Client(API_KEY)

def ask_openai(model: str, prompt: str, max_tokens: int):
    """
    Ask OpenAI a question using the specified model and prompt.
    :param model: the model to use
    :param prompt: the prompt to use
    :param max_tokens: the maximum number of tokens to generate
    :return: the response from OpenAI
    """
    response = CLIENT.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
