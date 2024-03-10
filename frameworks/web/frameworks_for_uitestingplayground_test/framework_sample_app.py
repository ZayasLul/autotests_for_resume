import allure
from selenium.webdriver.common.by import By

from frameworks.web.any_pages import AnyPage


class Locator:
    url_sample_app = (By.XPATH, '//a[contains(@href, "sampleapp")]')
    input_user_name_field = (By.XPATH, '(//input)[1]')
    input_password_field = (By.XPATH, '(//input)[2]')
    button_login = (By.XPATH, '//button[@id="login"]')
    label_text = (By.XPATH, '//label[@id="loginstatus"]')


class FrameworkSampleApp(AnyPage):

    @allure.step('Открываем страницу sample_app')
    def open_page_sample_app(self):
        self.open_page(Locator.url_sample_app)
        return self

    @allure.step('Заполняем поле "Имя пользователя"')
    def fill_input_user_name(self, user_name):
        return self.send_keys(Locator.input_user_name_field, user_name)

    @allure.step('Заполняем поле "Пароль"')
    def fill_input_password(self, password):
        return self.send_keys(Locator.input_password_field, password)

    @allure.step('Нажимаем на кнопку "Вход"')
    def click_button_log_in(self):
        return self.click_element(Locator.button_login)

    @allure.step('Заполняем поля "Имя пользователя" и "Пароль" и нажимаем "Вход" ')
    def fill_name_and_password_and_login(self, user_name, password):
        # Заполняем имя
        self.fill_input_user_name(user_name)
        # Заполняем пароль
        self.fill_input_password(password)
        # Нажимаем кнопку "Log In"
        self.click_button_log_in()
        return self

    @allure.step('Получаем статус входа')
    def get_status_in(self):
        return self.get_tag_text(Locator.label_text)