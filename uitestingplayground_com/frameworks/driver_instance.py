from selenium import webdriver


class DriverInstance:

    driver = None


    def get_driver(self):
        # Назначаем driver
        self.driver = webdriver.Chrome()
        # Устанавливаем максимальное разрешение окна браузера
        self.driver.maximize_window()
        # Устанавливааем время в течении которого сценарий ждет прежде чем выдать ошибку
        self.driver.set_script_timeout(600)
        # Устанавлвиаем время ожидания загруки страници прежде чем выдать ошибку
        self.driver.set_page_load_timeout(600)
        return self.driver

    def stop_driver(self):
        # Если драйвер не пустой
        if self.driver is not None:
            # Удаляем все куки-файлы
            self.driver.delete_all_cookies()
            # Закрываем браузер и завершаем работу ChromiumDriver
            self.driver.quit()
            # Обнуляем переменную
            self.driver = None
