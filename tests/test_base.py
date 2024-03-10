from data.settings import Settings
from frameworks.application_manager import ApplicationManager


class TestBase:
    APP = ApplicationManager()
    settings = Settings()

