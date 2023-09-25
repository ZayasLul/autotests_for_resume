import pyperclip as pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from uitestingplayground_com.frameworks.framework_base import FrameworkBase


class FrameworkWebBase(FrameworkBase):

    def get_driver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver()
        return self.manager.driver_instance.driver

    def open_main_page(self):
        main_page = self.manager.settings.TestingStand[self.manager.settings.branch]['main_page']
        self.get_driver().get(main_page)

    def click_element(self, locator):
        web_element = self.find_element(locator)
        web_element.click()


    def find_element(self, locator, wait=None):
        if wait is None:
            wait = self.manager.settings.time_element_wait
        web_element = WebDriverWait(self.get_driver(), wait).until(EC.presence_of_element_located(locator))
        return web_element

    def find_elements(self, locator, wait=None):
        if wait is None:
            wait = self.manager.settings.time_element_wait
        web_element = WebDriverWait(self.get_driver(), wait).until(EC.presence_of_all_elements_located(locator))
        return web_element

    def scroll_to_element(self, locator):
        try:
            element = self.find_element(locator).location_once_scrolled_into_view
            script = "window.scrollBy(" + str(element['x'] - 180) + ", " + str(element['y'] - 180) + ")"
            self.get_driver().execute_script(script)
        except:
            pass

    def get_tag_attribute(self, locator, attribute_name):
        return self.find_element(locator).get_attribute(attribute_name)

    def get_text_alert(self):
        driver = self.get_driver()
        return driver.switch_to.alert.text.title()

    def click_accept_in_alert(self):
        driver = self.get_driver()
        return driver.switch_to.alert.accept()

    def wait_for_item_not_display(self, locator, wait):
        driver = self.get_driver()
        wait = WebDriverWait(driver, wait)
        return wait.until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator: object, text: object) -> object:
        web_element = self.find_element(locator)
        web_element.send_keys(text)

    def get_tag_text(self, locator):
        return self.find_element(locator).text

    def get_visibility_element(self, locator):
        web_element = WebDriverWait(self.get_driver(), 1).until(EC.visibility_of(locator))
        return web_element

    def move_to_element(self, locator):
        actions = ActionChains(self.get_driver())
        element = self.find_element(locator)
        actions.move_to_element(element)
        actions.perform()

    def get_shadow_root_attribute(self, shadow_host_name_element, path_attribute):
        driver = self.get_driver()
        shadow_root = driver.execute_script(f'''return document.querySelector('{shadow_host_name_element}').shadowRoot.querySelector('{path_attribute}')''')
        return shadow_root


    def get_value_in_clipboard(self):
        return pyperclip.paste()
