from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://consolebeta.incrementx.com")

try:
    # Wait for input fields to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/form/input[1]')))
    
    Last1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/form/input[1]')
    Last1.send_keys("pubnx@vertoz.com")

    Last2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/form/input[2]')
    Last2.send_keys("pubnx@123")

    driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/form/button').click()

    # Wait for login success message
    WebDriverWait(driver, 10).until(EC.url_contains("https://consolebeta.incrementx.com/home.html"))

    print("Login successfully")
    print("Run successfully")
    
   

    # Navigating to ad units page
    WebDriverWait(driver, 10).until(EC.url_contains("https://consolebeta.incrementx.com/home.html?r=4.5#/sites-apps/ad-units"))
    
    #driver.get("")
    driver.refresh()
    sleep(10)
    
    # Wait for new ad unit button to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form[1]/div/div/div[2]/div[4]/a'))).click()

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
