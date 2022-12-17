import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class AutomationExamTree():
    def gentder_tus_fri(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://itera-qa.azurewebsites.net/home/automation")

        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "tuesday").click()
        driver.find_element(By.ID, "friday").click()
        time.sleep(4)
        driver.close()

genderday = AutomationExamTree()
genderday.gentder_tus_fri()