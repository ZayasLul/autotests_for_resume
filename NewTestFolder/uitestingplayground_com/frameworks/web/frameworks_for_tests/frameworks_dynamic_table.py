from selenium.webdriver.common.by import By

from NewTestFolder.uitestingplayground_com.frameworks.web.any_pages import AnyPage


class Locator:
    url_dynamic_table = (By.XPATH, '//a[contains(@href, "dynamictable")]')
    name_in_table = (By.XPATH, '//div[@role="row"]//span[@role="cell"][1]')
    required_value = (By.XPATH, '//p[@class="bg-warning"]')

class FrameworkDynamicTable(AnyPage):

    def open_page_dynamic_table(self):
        # Прокручиваем до нужной ссылки
        self.scroll_to_element(Locator.url_dynamic_table)
        # Нажимаем на ссылку
        self.click_element(Locator.url_dynamic_table)
        return self

    def get_cpu_in_table(self):
        # Получаем количество имен в таблице
        count_name = len(self.find_elements(Locator.name_in_table))
        for i in range(1, count_name + 1):
            # Находим нужное нам имя
            xpath_name_in_table = (By.XPATH, f'(//div[@role="row"]//span[@role="cell"][1])[{i}]')
            name = self.get_tag_text(xpath_name_in_table)
            if name == 'Chrome':
                xpath_head_table = (By.XPATH, '//span[@role="columnheader"]')
                count_head_table = len(self.find_elements(xpath_head_table))
                for j in range(1, count_head_table + 1):
                    xpath_head_table = (By.XPATH, f'(//span[@role="columnheader"])[{j}]')
                    name_head_table = self.get_tag_text(xpath_head_table)
                    if name_head_table == 'CPU':
                        xpath_value_cell_in_table = (By.XPATH, f'//div[@role="row"][{i}]//span[@role="cell"][{j}]')
                        value_cpu = self.get_tag_text(xpath_value_cell_in_table)
                        return value_cpu
        return self

    def get_required_value(self):
        return self.get_tag_text(Locator.required_value)
