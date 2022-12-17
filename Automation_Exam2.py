import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class AutomationExamTwo():
    def category_norway(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://itera-qa.azurewebsites.net/home/automation")

        dropdwon = driver.find_element(By.TAG_NAME, "select")
        dd = Select(dropdwon)

        dd.select_by_index(1)
        time.sleep(3)

        dd.select_by_value("1")
        time.sleep(3)

        time.sleep(4)
        driver.close()

submitbutton = AutomationExamTwo()
submitbutton.category_norway()
