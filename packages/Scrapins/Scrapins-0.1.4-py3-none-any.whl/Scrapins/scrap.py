from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def get_el(driver: WebDriver, type: str, value: str, timeout: int):
    """
    Get an element by type and value with a timeout.

    Args:
        type (str): The type of the element to find.
        value (str): The value of the element to find.
        timeout (int): The maximum time to wait for the element to be found.

    Returns:
        WebElement: The element found.
    """
    if type == "id":
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, value))
        )
    elif type == "class":
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, value))
        )
    elif type == "xpath":
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, value))
        )
    elif type == "css":
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, value))
        )
    else:
        raise ValueError(f"Unsupported element type: {type}")