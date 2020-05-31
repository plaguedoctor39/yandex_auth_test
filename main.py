from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
import config


class YaAuthTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(config.PATH)

    def test_auth(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/')
        login = driver.find_element_by_name('login')
        login.send_keys(config.LOGIN)
        login.send_keys(Keys.RETURN)
        time.sleep(1)
        password = driver.find_element_by_name('passwd')
        password.send_keys(config.PASSWORD)
        time.sleep(1)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.get('https://passport.yandex.ru/profile')
        # print(driver.current_url)
        self.assertEqual(driver.current_url, 'https://passport.yandex.ru/profile')
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
