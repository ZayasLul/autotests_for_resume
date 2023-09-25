from uitestingplayground_com.data.settings import Settings
from uitestingplayground_com.frameworks.driver_instance import DriverInstance
from uitestingplayground_com.frameworks.web.any_pages import AnyPage
from uitestingplayground_com.frameworks.web.framework_web_base import FrameworkWebBase
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_ajax_data import FrameworkAjaxData
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_class_atribute import FrameworkClassAttribute
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_click import FrameworkClick
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_client_side_delay import FrameworkClientSideDelay
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_dynamic_id import FrameworkDynamicId
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_load_delay import FrameworkLoadDelay
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_mouse_over import \
    FrameworkMouseOver
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_non_breaking_space import \
    FrameworkNoneBreakingSpace
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_ovelapped_element import \
    FrameworkOverlappedElement
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_progress_bar import \
    FrameworkProgressBar
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_sample_app import \
    FrameworkSampleApp
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_scrollbars import FrameworkScrollbars
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_shadow_dom import \
    FrameworkShadowDom
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_text_input import FrameworkTextInput
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_verify_text import FrameworkVerifyText
from uitestingplayground_com.frameworks.web.frameworks_for_tests.framework_visibility import FrameworkVisibility
from uitestingplayground_com.frameworks.web.frameworks_for_tests.frameworks_dynamic_table import FrameworkDynamicTable
from uitestingplayground_com.frameworks.web.frameworks_for_tests.frameworks_hidden_layers import FrameworkHiddenLayer


class ApplicationManager:

    settings = Settings()

    def __init__(self):

        self.driver_instance = DriverInstance()
        self.framework_web_base = FrameworkWebBase(self)
        self.any_pages = AnyPage(self)
        self.framework_dynamic_id = FrameworkDynamicId(self)
        self.framework_class_attribute = FrameworkClassAttribute(self)
        self.framework_hidden_layers = FrameworkHiddenLayer(self)
        self.framework_load_delay = FrameworkLoadDelay(self)
        self.framework_ajax_data = FrameworkAjaxData(self)
        self.framework_client_side_delay = FrameworkClientSideDelay(self)
        self.framework_click = FrameworkClick(self)
        self.framework_text_input = FrameworkTextInput(self)
        self.framework_scrollbars = FrameworkScrollbars(self)
        self.framework_dynamic_table = FrameworkDynamicTable(self)
        self.framework_verify_text = FrameworkVerifyText(self)
        self.framework_progress_bar = FrameworkProgressBar(self)
        self.framework_visibility = FrameworkVisibility(self)
        self.framework_sample_app = FrameworkSampleApp(self)
        self.framework_mouse_over = FrameworkMouseOver(self)
        self.framework_non_breaking_space = FrameworkNoneBreakingSpace(self)
        self.framework_overlapped_element = FrameworkOverlappedElement(self)
        self.framework_shadow_dom = FrameworkShadowDom(self)
