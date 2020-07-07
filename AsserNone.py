import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)


if __name__ == "__main__":
    unittest.main()
