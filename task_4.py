"""
Imagine the following scenario: you click on a button that should redirect you to a new page,
but the page URL stays the same and the DOM structure stays almost the same.
Provide a code fragment to wait explicitly for the page to unload.
Waiting for the page to load is not necessary (perhaps you want to gracefully handle some errors
in case you are left on the same page).
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "my_expected_element"))
        # or another expected condition: title_contains, element_to_be_clickable ...
    )
except Exception:
    print('Error')

