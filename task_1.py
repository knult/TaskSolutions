"""
How would you handle a StaleElementReferenceException? Please provide a code fragment or fragments,
if you know about several common ways of handling.

I will analyze raising StaleElementReferenceException(SER). If the SER raising due to a small timeout,
I'll do something like this:
element = WebDriverWait(driver, timeout, ignored_exceptions=StaleElementReferenceException)
            .until(expected_conditions.presence_of_element_located((By.ID, element_id)))
If the SER rises when the element IDs change, then I change the element search logic.
See below for possible examples.
"""


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)


# helper function
def get_buttons():
    driver.get('http://the-internet.herokuapp.com/challenging_dom')
    buttons = driver.find_elements(By.XPATH, ".//a[contains(@class,'button')]")
    return buttons


# SER exception will be raised on the second iteration
def click_all_buttons():
    for button in get_buttons():
        button.click()
        print('button 1 clicked')


# Solution 1
# If the order of the required elements in the DOM does not change
def click_all_buttons_with_update():
    for n in range(len(get_buttons())):
        get_buttons()[n].click()
        print(f'button {n} clicked')


# Solution 2
def click_all_buttons_by_full_class_name():
    driver.get('http://the-internet.herokuapp.com/challenging_dom')
    button = driver.find_element(By.XPATH, ".//a[contains(@class,'button')]")
    button.click()
    print('button 1 clicked')
    button = driver.find_element(By.XPATH, ".//a[contains(@class,'button alert')]")
    button.click()
    print('button 2 clicked')
    button = driver.find_element(By.XPATH, ".//a[contains(@class,'button success')]")
    button.click()
    print('button 3 clicked')


# Solution 3
def click_all_buttons_by_xpath():
    driver.get('http://the-internet.herokuapp.com/challenging_dom')
    button = driver.find_element(By.XPATH, "//*[@id='content']/div/div/div/div[1]/a[1]")
    button.click()
    print('button 1 clicked')
    button = driver.find_element(By.XPATH, "//*[@id='content']/div/div/div/div[1]/a[2]")
    button.click()
    print('button 2 clicked')
    button = driver.find_element(By.XPATH, "//*[@id='content']/div/div/div/div[1]/a[3]")
    button.click()
    print('button 3 clicked')


# Solution 4
def click_all_with_except():
    for button in get_buttons():
        try:
            button.click()
            print('button 1 clicked')
        except StaleElementReferenceException as err:
            print(f'SER error')
            # another code ...
        except Exception as err:
            print(f'another error')


click_all_buttons_with_update()
"""
button 0 clicked
button 1 clicked
button 2 clicked
"""
click_all_buttons_by_full_class_name()
"""
button 0 clicked
button 1 clicked
button 2 clicked
"""
click_all_buttons_by_xpath()
"""
button 0 clicked
button 1 clicked
button 2 clicked
"""
click_all_with_except()
"""
button 1 clicked
SER error
SER error
"""
click_all_buttons()
"""
button 1 clicked
SER Exception
"""

driver.quit()
