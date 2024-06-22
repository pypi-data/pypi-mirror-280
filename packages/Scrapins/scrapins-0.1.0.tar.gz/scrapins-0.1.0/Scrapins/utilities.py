from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver(is_headless: bool, browser: str):
    if browser == "chrome":
        driver = webdriver.Chrome(options=configure_driver(is_headless))
        return driver

def configure_driver(is_headless: bool):
    options = Options()
    options.headless = is_headless
    return options

def save_html(output_file, html):
    with open(output_file, 'w') as file:
        file.write(html)

def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()