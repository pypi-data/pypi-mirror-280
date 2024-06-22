import pytest
from unittest.mock import patch, mock_open, MagicMock
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver

# Import des fonctions à tester
from Scrapins.utilities import create_driver, configure_driver, save_html, load_html

def test_configure_driver():
    options = configure_driver(True)
    assert isinstance(options, Options)
    assert options.headless

    options = configure_driver(False)
    assert isinstance(options, Options)
    assert not options.headless


@patch('builtins.open', new_callable=mock_open)
def test_save_html(mock_file):
    output_file = 'test_output.html'
    html_content = '<html><body>Test</body></html>'

    save_html(output_file, html_content)

    mock_file.assert_called_once_with(output_file, 'w')
    mock_file().write.assert_called_once_with(html_content)


@patch('builtins.open', new_callable=mock_open, read_data='<html><body>Test</body></html>')
def test_load_html(mock_file):
    file_path = 'test_output.html'
    expected_html = '<html><body>Test</body></html>'

    html = load_html(file_path)

    mock_file.assert_called_once_with(file_path, 'r', encoding='utf-8')
    assert html == expected_html
