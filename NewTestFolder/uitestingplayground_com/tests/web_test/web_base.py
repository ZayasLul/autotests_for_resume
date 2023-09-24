from NewTestFolder.uitestingplayground_com.tests.test_base import TestBase


class WebBase(TestBase):

    def setup_method(self):
        self.APP.any_pages.open_main_page()
