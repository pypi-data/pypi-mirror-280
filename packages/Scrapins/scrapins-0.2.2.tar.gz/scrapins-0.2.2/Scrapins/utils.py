import json
import re

from bs4 import BeautifulSoup
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from typing import Union

def create_driver(is_headless: bool, browser: str):
    """
    Create a web driver instance based on the specified browser and headless mode.

    Args:
        is_headless (bool): Determines whether the browser should run in headless mode.
        browser (str): The browser to use. Currently, supports "chrome".

    Returns:
        webdriver.Chrome: An instance of the Chrome web driver configured based on the input parameters.

    Raises:
        ValueError: If an unsupported browser is specified.
    """
    if browser == "chrome":
        driver = webdriver.Chrome(options=configure_driver(is_headless))
        return driver
    else:
        raise ValueError(f"Unsupported browser: {browser}")

def configure_driver(is_headless: bool):
    """
    Configure the web driver options for Chrome.

    Args:
        is_headless (bool): Determines whether the browser should run in headless mode.

    Returns:
        Options: The Chrome options configured based on the input parameters.
    """
    options = Options()
    options.headless = is_headless
    return options

def save_html(output_file: str, html: str):
    """
    Save the given HTML content to a file.

    Args:
        output_file (str): The path to the output file where the HTML content should be saved.
        html (str): The HTML content to save.

    Returns:
        None
    """
    with open(output_file, 'w') as file:
        file.write(html)

def load_html(file_path: str):
    """
    Load and return the HTML content from a file.

    Args:
        file_path (str): The path to the file containing the HTML content.

    Returns:
        str: The HTML content loaded from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_json(data: Union[dict, str, list], file_name: str):
    """
    Enregistre un dictionnaire, une chaîne de caractères JSON ou une liste dans un fichier.

    Args:
    - data (Union[dict, str, list]): Les données à enregistrer, soit sous forme de dict, de string ou de list.
    - file_name (str): Le nom du fichier dans lequel enregistrer les données JSON.
    """
    # Si les données sont une chaîne de caractères, vérifier et convertir les single quotes en double quotes
    if isinstance(data, str):
        # Utiliser des expressions régulières pour remplacer les single quotes par des doubles quotes
        # Remplacer les single quotes autour des clés et des valeurs par des doubles quotes
        json_string = re.sub(r"(?<!\\)'", '"', data)

        # Charger le JSON pour s'assurer qu'il est valide
        try:
            data_dict = json.loads(json_string)
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON: {e}")
            return
    elif isinstance(data, (dict, list)):
        data_dict = data
    else:
        print("Le type de données n'est ni un dictionnaire, ni une liste, ni une chaîne JSON valide.")
        return

    # Enregistrer les données dans un fichier JSON
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data_dict, file, ensure_ascii=False, indent=4)

    print(f"Les données ont été enregistrées avec succès dans {file_name}.")

def load_json(file_path: str):
    """
    Load and return the JSON data from a file.

    Args:
        file_path (str): The path to the file containing the JSON data.

    Returns:
        dict: The JSON data loaded from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def prettify_html_file(input_file: str, output_file: str):
    """
    Prettify and save the HTML content from an input file to an output file.

    Args:
        input_file (str): The path to the input file containing the HTML content to prettify.
        output_file (str): The path to the output file where the prettified HTML content should be saved.

    Returns:
        None
    """
    # Load the HTML content from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Use prettify to format the HTML
    pretty_html = soup.prettify()

    # Write the formatted HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(pretty_html)

def log_el_content(el):
    """
    Log the content in multiline of an element.

    Args:
        el (WebElement): The element to log the content of.

    Returns:
        None
    """
    soup = BeautifulSoup(el.get_attribute("outerHTML"), 'html.parser')
    pretty_html = soup.prettify()
    print(pretty_html)