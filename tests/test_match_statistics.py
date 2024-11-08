from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:/Users/ekWor/Desktop/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://127.0.0.1:5000/")

team1_select = driver.find_element(By.ID, "team1")
team1_select.send_keys("Team A")
team2_select = driver.find_element(By.ID, "team2")
team2_select.send_keys("Team B")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Проверка статистики
assert "Владение мячом" in driver.page_source
assert "Фолы" in driver.page_source
driver.save_screenshot("screenshots/screenshot_match_statistics.png")
driver.quit()

