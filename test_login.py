# test_login.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
    print("✅ Valid login test passed.")
    driver.quit()

def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "do not match" in error
    print("❌ Invalid login test passed.")
    driver.quit()

def test_empty_fields():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "login-button").click()
    error = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username is required" in error
    print("⚠️ Empty field login test passed.")
    driver.quit()

# ✅ Call functions manually
if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
    test_empty_fields()
