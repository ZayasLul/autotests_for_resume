from selenium.webdriver.common.by import By

from NewTestFolder.uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_sample_app = (By.XPATH, '//a[contains(@href, "sampleapp")]')
    input_user_name_field = (By.XPATH, '(//input)[1]')
    input_password_field = (By.XPATH, '(//input)[2]')
    button_login = (By.XPATH, '//button[@id="login"]')
    label_text = (By.XPATH, '//label[@id="loginstatus"]')


class FrameworkSampleApp(AnyPage):

    def open_page_sample_app(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_sample_app)
        # Нажимаем на ссылку
        self.click_element(Locator.url_sample_app)
        return self

    def fill_input_user_name(self, user_name):
        return self.send_keys(Locator.input_user_name_field, user_name)

    def fill_input_password(self, password):
        return self.send_keys(Locator.input_password_field, password)

    def click_button_log_in(self):
        return self.click_element(Locator.button_login)

    def fill_name_and_password_and_login(self, user_name, password):
        # Заполняем имя
        self.fill_input_user_name(user_name)
        # Заполняем пароль
        self.fill_input_password(password)
        # Нажимаем кнопку "Log In"
        self.click_button_log_in()
        return self

    def get_status_in(self):
        return self.get_tag_text(Locator.label_text)