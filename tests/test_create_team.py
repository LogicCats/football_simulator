from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service("C:/Users/ekWor/Desktop/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://127.0.0.1:5000/create_team")

driver.find_element(By.ID, "team_name").send_keys("New Team")
for i in range(1, 4):
    driver.find_element(By.ID, f"player{i}_name").send_keys(f"Player {i}")
    driver.find_element(By.ID, f"player{i}_speed").send_keys("50")
    driver.find_element(By.ID, f"player{i}_accuracy").send_keys("50")
    driver.find_element(By.ID, f"player{i}_stamina").send_keys("50")
    driver.find_element(By.ID, f"player{i}_defense").send_keys("50")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Проверка наличия команды на главной странице
driver.get("http://127.0.0.1:5000/")
assert "New Team" in driver.page_source
driver.save_screenshot("screenshots/screenshot_create_team.png")
driver.quit()

