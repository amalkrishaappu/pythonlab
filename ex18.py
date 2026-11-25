from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/text-box")

# Wait up to 15 seconds for the form to load
wait = WebDriverWait(driver, 15)
user_name = wait.until(EC.visibility_of_element_located((By.ID, "userName")))

# Fill out the form
user_name.send_keys("John")
driver.find_element(By.ID, "userEmail").send_keys("john@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Kerala")
driver.find_element(By.ID, "permanentAddress").send_keys("India")

# Scroll down to the Submit button so ads don't block the click
submit_btn = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
submit_btn.click()

# Wait for output to appear and print it
output = wait.until(EC.visibility_of_element_located((By.ID, "output")))
print(output.text)

driver.quit()
