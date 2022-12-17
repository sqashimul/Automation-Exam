import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class AutomationExamFive():
    def mouse_over(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        driver.get("https://www.daraz.com.bd/")
        driver.maximize_window()
        morebutton = driver.find_element(By.XPATH, "//li[@id='Level_1_Category_No12']//a")
        afterbutton = driver.find_element(By.XPATH, "//span[normalize-space()='Motorcycle Riding Gear']")
        achains = ActionChains(driver)
        achains.move_to_element(morebutton).perform()
        achains.move_to_element(afterbutton).perform()

        driver.find_element(By.XPATH, "//span[normalize-space()='Helmet']").click()
        time.sleep(3)

hoverover = AutomationExamFive()
hoverover.mouse_over()