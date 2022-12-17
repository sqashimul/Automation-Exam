import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class AutomationExamOne():
    def name_pho_email_pas_adre(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://itera-qa.azurewebsites.net/home/automation")

        driver.find_element(By.ID, "name").send_keys("Tanzimul Haque")
        driver.find_element(By.ID, "phone").send_keys("01713700538")
        driver.find_element(By.ID, "email").send_keys("tanzimulhaqueshimul@gmail.com")
        driver.find_element(By.ID, "password").send_keys("abcd123")
        driver.find_element(By.ID, "address").send_keys("Atghoria, Pabna")
        time.sleep(2)
        driver.find_element(By.NAME, "submit").click()
        time.sleep(4)
        driver.close()

submitbutton = AutomationExamOne()
submitbutton.name_pho_email_pas_adre()
