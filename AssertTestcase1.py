import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(
            executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
        driver.get("https://www.google.com/")
        title = driver.title
        # assertequal
        #self.assertEqual("Google", title, "titles are different")
        self.assertNotEqual("Google",title)


if __name__ == "__main__":
    unittest.main()
