import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(
            executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
        driver.get("https://www.google.com/")
        title = driver.title
        # assertTrue
        # self.assertTrue(title == "Google")
        self.assertFalse(title == "Google3")


if __name__ == "__main__":
    unittest.main()
