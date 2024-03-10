import allure

from tests.web_tests.web_base import WebBase


@allure.feature('Web - demoqa.com')
class TestElementsTextBox(WebBase):

    @allure.title('Заполнение поля "Full Name"')
    @allure.severity('critical')
    def test_fill_field_full_name(self):
        # Открываем страницу Elements
        self.APP.any_pages.open_page_elements_demoqa()
        # Открываем Text Box
        self.APP.fw_text_box.open_text_box()
        # Заполняем поле Full Name
        name_user = 'Кораблев Николай'
        self.APP.fw_text_box.fill_field_full_name(name_user)
        # Нажимаем кнопку Submit
        self.APP.fw_text_box.click_button_submit()
        # Проверяем что имя сохранено
        assert name_user == self.APP.fw_text_box.get_name_user().replace('Name:', '')

    @allure.title('Заполнение поля "Email"')
    @allure.severity('critical')
    def test_fill_field_email(self):
        # Открываем страницу Elements
        self.APP.any_pages.open_page_elements_demoqa()
        # Открываем Text Box
        self.APP.fw_text_box.open_text_box()
        # Заполняем поле Email
        email_user = 'example@mail.ru'
        self.APP.fw_text_box.fill_field_email(email_user)
        # Нажимаем кнопку Submit
        self.APP.fw_text_box.click_button_submit()
        # Проверяем что имя сохранено
        assert email_user == self.APP.fw_text_box.get_email()

    @allure.title('Заполнение поля "Current Address"')
    @allure.severity('critical')
    def test_fill_field_current_address(self):
        # Открываем страницу Elements
        self.APP.any_pages.open_page_elements_demoqa()
        # Открываем Text Box
        self.APP.fw_text_box.open_text_box()
        # Заполняем поле Current Address
        current_address_user = 'New City'
        self.APP.fw_text_box.fill_field_current_address(current_address_user)
        # Нажимаем кнопку Submit
        self.APP.fw_text_box.click_button_submit()
        # Проверяем что имя сохранено
        assert current_address_user == self.APP.fw_text_box.get_email()