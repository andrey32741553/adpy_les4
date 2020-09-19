from selenium import webdriver


driver = webdriver.Chrome(executable_path="c:\\Users\\Андрей\\AppData\\Local\\Google\\Chrome\\Application\\85.0.4183.102\\chromedriver.exe")
driver.get("https://passport.yandex.ru/auth")
assert "Авторизация" in driver.title
elem = driver.find_element_by_name("login")
elem.send_keys("your_login")
elem.click()
assert "No results found." not in driver.page_source
driver.close()


# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path=
#     "c:\\Users\\Андрей\\AppData\\Local\\Google\\Chrome\\Application\\85.0.4183.102\\chromedriver.exe")
#
#     def test_search_in_ya(self):
#         driver = self.driver
#         driver.get("https://passport.yandex.ru/auth")
#         self.assertIn("Авторизация", driver.title)
#         elem = driver.find_element_by_name("login")
#         elem.send_keys("your_login")
#         elem.send_keys(Keys.RETURN)
#         self.assertNotIn("No results found.", driver.page_source)
# # Ниже часть кода без которой class работает нормально
#         driver.get("https://passport.yandex.ru/auth/welcome")  # без этой строки не переходит
#                                                                # на следующую страницу, но потом сбрасывает
#         self.assertIn("Авторизация", driver.title)
#         elem = driver.find_element_by_name("passwd")  # не находит данный элемент,
#                                                       # полагаю из-за того, что не переходит на
#                                                       # следующую страницу
#         elem.send_keys("your_password")
#         elem.send_keys(Keys.RETURN)
#         self.assertNotIn("No results found.", driver.page_source)
#
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()


# В коде ниже тест не провожу, но в нём переход нп следующую страницу осуществляется

# from idlelib import browser
# from selene.api import*
# from selenium import webdriver
#
# browser.set_driver(webdriver=webdriver.Chrome(executable_path=
#     "c:\\Users\\Андрей\\AppData\\Local\\Google\\Chrome\\Application\\85.0.4183.102\\chromedriver.exe"))
#
# login_element = s('[name="login"]')
# password_element = s('[name="passwd"]')
# submit_element = s('[type="submit"]')
#
#
# def login_with(login, password):
#     browser.open_url('https://passport.yandex.ru/auth/')
#     login_element.set(login)
#     submit_element.click()
#     password_element.set(password)
#     submit_element.click()
#     assert "No results found." not in browser
#     browser.close()
#
#
# if __name__ == '__main__':
#     login_with('your_login', 'your_password')
