import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):
    def testname(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        print(driver.title)
        driver.find_element(By.TAG_NAME, "button").click()
        assert "I am a JS Alert" == "I am a JS Alert"
        time.sleep(2)
        driver.find_element(By.TAG_NAME, "button").click()
        assert "I am a JS Confirm" == "I am a JS Confirm"

        driver.find_element(By.TAG_NAME, "button").click()
        assert "I am a JS prompt" == "I am a JS prompt"

if __name__ == "__main__":
    unittest.main()
