import unittest


class Test(unittest.TestCase):
    def testName(self):
        list = {"python", "selenium", "maths"}
        self.assertNotIn("ruby", list)


if __name__ == "__main__":
    unittest.main()
