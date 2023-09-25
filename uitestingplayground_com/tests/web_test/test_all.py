import allure
import pytest

from selenium.common import ElementClickInterceptedException
from uitestingplayground_com.tests.web_test.web_base import WebBase

@allure.feature('Web - uitestingplayground.com')
class TestAll(WebBase):

    @allure.title('Кнопка с динамическим id')
    @allure.severity('critical')
    def test_click_button_with_dynamic_id(self):
        # Переходим на страницу
        self.APP.framework_dynamic_id.open_page_dynamic_id()
        # Нажимаем на кнопку "dynamic id"
        assert self.APP.framework_dynamic_id.click_button_dynamic_id()

    @allure.title('Атрибуты класса')
    @allure.severity('critical')
    def test_class_attribute(self):
        # Открываем страницу
        self.APP.framework_class_attribute.open_page_class_attribute()
        # Нажимаем на кнопку
        self.APP.framework_class_attribute.click_button_blue()
        # Получаем текст всплывающего окна
        message = self.APP.framework_web_base.get_text_alert()
        # Нажимаем "Ок"
        self.APP.framework_web_base.click_accept_in_alert()
        # Проверяем что была нажата нужная кнопка
        assert message.lower() == 'primary button pressed'

    @allure.title('Скрытые слои')
    @allure.severity('critical')
    @pytest.mark.xfail(raises=ElementClickInterceptedException)
    def test_hidden_layers(self):
        # Открываем страницу
        self.APP.framework_hidden_layers.open_page_hidden_layers()
        # Нажимаем на кнопку
        self.APP.framework_hidden_layers.click_button_hidden_layers()
        # Нажимаем на кнопку повторно
        self.APP.framework_hidden_layers.click_button_hidden_layers()

    @allure.title('Долгая загрузка')
    @allure.severity('critical')
    def test_load_delay(self):
        # Открываем страницу
        self.APP.framework_load_delay.open_page_load_delay()
        # Нажимаем на кнопку
        assert self.APP.framework_load_delay.click_button_appearing_after_delay()

    @allure.title('AJAX данные')
    @allure.severity('critical')
    def test_ajax_data(self):
        # Открываем страницу
        self.APP.framework_ajax_data.open_page_ajax_data()
        # Нажимаем на кнопку
        self.APP.framework_ajax_data.click_button_triggering_ajax_request()
        # Ожидаем загрузки
        assert self.APP.framework_ajax_data.wait_for_ajax_data_not_display()

    @allure.title('Клиентская задержка')
    @allure.severity('critical')
    def test_client_side_delay(self):
        # Открываем страницу
        self.APP.framework_client_side_delay.open_page_client_side_delay()
        # Нажимаем на кнопку
        self.APP.framework_client_side_delay.click_button_client_side_delay()
        # Ожидаем загрузки
        assert self.APP.framework_client_side_delay.wait_for_client_data_not_display()

    @allure.title('Нажатие на кнопку')
    @allure.severity('critical')
    def test_click(self):
        # Открываем страницу
        self.APP.framework_click.open_page_click()
        # Нажимаем на кнопку
        assert self.APP.framework_click.click_button_click()

    @allure.title('Поле ввода')
    @allure.severity('critical')
    def test_input_field(self):
        # Открываем страницу
        self.APP.framework_text_input.open_page_text_input()
        # Вводим новое имя кнопки
        new_name_button = 'NewNameWebTest'
        self.APP.framework_text_input.input_name_button(new_name_button)
        # Нажимаем на кнопку
        self.APP.framework_click.click_button_click()
        assert self.APP.framework_text_input.get_name_button() == new_name_button

    @allure.title('Скролл')
    @allure.severity('critical')
    def test_scrollbars(self):
        # Открываем страницу
        self.APP.framework_scrollbars.open_page_scrollbars()
        # Нажимаем на кнопку
        assert self.APP.framework_scrollbars.click_button_scrollbars()

    @allure.title('Динамическая таблица')
    @allure.severity('critical')
    def test_dynamic_table(self):
        # Открываем страницу
        self.APP.framework_dynamic_table.open_page_dynamic_table()
        # Получаем значение Chrome CPU из таблицы
        chrome_cpu = 'Chrome CPU: ' + self.APP.framework_dynamic_table.get_cpu_in_table()
        # Получаем значение которое должно быть
        required_value = self.APP.framework_dynamic_table.get_required_value()
        assert chrome_cpu == required_value

    @allure.title('Проверка текста')
    @allure.severity('critical')
    def test_verify_text(self):
        # Открываем страницу
        self.APP.framework_verify_text.open_page_verify_text()
        # Находим текст (Добавил проверку не только на то что текст находится но и можно его взять)
        assert self.APP.framework_verify_text.get_and_find_text() == 'Welcome UserName!'

    @allure.title('Прогресс бар')
    @allure.severity('critical')
    def test_progress_bar(self):
        # Открываем страницу
        self.APP.framework_progress_bar.open_page_progress_bar()
        # Нажимаем кногпку "Старт"
        self.APP.framework_progress_bar.click_start_button()
        # Останавливаем при прогрессе в 75
        self.APP.framework_progress_bar.click_stop_when_progress_bar_has_reached_value()
        # Получаем результат
        result = self.APP.framework_progress_bar.get_result()
        assert result == 'Result: 0'

    @allure.title('Видимость')
    @allure.severity('critical')
    def test_visibility(self):
        # Открываем страницу
        self.APP.framework_visibility.open_page_visibility()
        # Нажимаем на кнопку "Hide"
        self.APP.framework_visibility.click_button_hide()
        # Получаем массив видимости скрытых элементов
        list_visibiliti_elements = self.APP.framework_visibility.get_list_visible_elements()
        assert [True] not in list_visibiliti_elements

    @allure.title('Пример приложения (корректные данные)')
    @allure.severity('critical')
    def test_sample_app_correct(self):
        # Открываем страницу
        self.APP.framework_sample_app.open_page_sample_app()
        # Заполняем поля
        name_user = 'NewWebTestName'
        password = 'pwd'
        self.APP.framework_sample_app.fill_name_and_password_and_login(name_user, password)
        # Получаем статус входа
        status = self.APP.framework_sample_app.get_status_in()
        assert status == 'Welcome, ' + name_user + '!'

    @allure.title('Пример приложения (некорректные данные)')
    @allure.severity('critical')
    def test_sample_app_incorrect(self):
        # Открываем страницу
        self.APP.framework_sample_app.open_page_sample_app()
        # Заполняем поля
        name_user = 'NewWebTestName'
        password = '!!!'
        self.APP.framework_sample_app.fill_name_and_password_and_login(name_user, password)
        # Получаем статус входа
        status = self.APP.framework_sample_app.get_status_in()
        assert status == 'Invalid username/password'

    @allure.title('Навести курсор мыши')
    @allure.severity('critical')
    def test_mouse_over(self):
        # Открываем страницу
        self.APP.framework_mouse_over.open_page_sample_app()
        # Нажимаем 2 раза на ссылку
        self.APP.framework_mouse_over.double_click_button_click_me()
        # Получаем количество нажатий
        assert self.APP.framework_mouse_over.get_count_click() == 2

    @allure.title('Неразрывное пространство')
    @allure.severity('critical')
    def test_non_breaking_space(self):
        # Открываем страницу
        self.APP.framework_non_breaking_space.open_page_non_breaking_space()
        # Пробуем нажать на кнопку
        assert self.APP.framework_non_breaking_space.click_button_non_breaking_space()

    @allure.title('Перекрывающий элемент')
    @allure.severity('critical')
    def test_overlapped_element(self):
        # Открываем страницу
        self.APP.framework_overlapped_element.open_page_overlapped_element()
        # Вводим имя
        name = 'NewWebTestName'
        assert self.APP.framework_overlapped_element.input_name(name)

    @allure.title('Shadow_dom')
    @allure.severity('critical')
    def test_shadow_dom(self):
        self.APP.framework_shadow_dom.open_page_shadow_dom()
        # Нажимаем на кнопку генерации GUID
        self.APP.framework_shadow_dom.click_shadow_button_generate()
        # Копируем GUID
        self.APP.framework_shadow_dom.click_shadow_button_copy()
        # Получаем значение из буфера обмена
        copy_guid = self.APP.framework_shadow_dom.get_value_in_clipboard()
        # Получаем значение из поля
        input_guid_value = self.APP.framework_shadow_dom.get_value_input_field()
        assert copy_guid == input_guid_value
