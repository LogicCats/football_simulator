#python -m unittest discover tests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service = Service("C:/Users/ekWor/Desktop/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to the application
driver.get("http://127.0.0.1:5000/")

# Fill in team selections
team1_select = driver.find_element(By.ID, "team1")
team1_select.send_keys("Team A")

team2_select = driver.find_element(By.ID, "team2")
team2_select.send_keys("Team B")

# Click the submit button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Print the page source for debugging
print(driver.page_source)

# Wait for the results to be displayed
try:
    # Update the XPath to match the correct text
    WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Результаты матча')]")))


    # Check if the expected result is in the page source
    assert "Результаты матча" in driver.page_source

    # Take a screenshot if the assertion passes
    driver.save_screenshot("screenshots/screenshot_simulate_match.png")
except AssertionError:
    print("The result 'Результаты матча' was not found in the page source.")
finally:
    # Clean up and close the browser
    driver.quit()

