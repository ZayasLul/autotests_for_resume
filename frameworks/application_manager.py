from data.settings import Settings
from frameworks.driver_instance import DriverInstance
from frameworks.web.any_pages import AnyPage
from frameworks.web.framework_web_base import FrameworkWebBase
from frameworks.web.frameworks_for_uitestingplayground_test.framework_ajax_data import FrameworkAjaxData
from frameworks.web.frameworks_for_uitestingplayground_test.framework_class_atribute import FrameworkClassAttribute
from frameworks.web.frameworks_for_uitestingplayground_test.framework_click import FrameworkClick
from frameworks.web.frameworks_for_uitestingplayground_test.framework_client_side_delay import FrameworkClientSideDelay
from frameworks.web.frameworks_for_uitestingplayground_test.framework_dynamic_id import FrameworkDynamicId
from frameworks.web.frameworks_for_uitestingplayground_test.framework_load_delay import FrameworkLoadDelay
from frameworks.web.frameworks_for_uitestingplayground_test.framework_mouse_over import FrameworkMouseOver
from frameworks.web.frameworks_for_uitestingplayground_test.framework_non_breaking_space import FrameworkNoneBreakingSpace
from frameworks.web.frameworks_for_uitestingplayground_test.framework_ovelapped_element import FrameworkOverlappedElement
from frameworks.web.frameworks_for_uitestingplayground_test.framework_progress_bar import FrameworkProgressBar
from frameworks.web.frameworks_for_uitestingplayground_test.framework_sample_app import FrameworkSampleApp
from frameworks.web.frameworks_for_uitestingplayground_test.framework_scrollbars import FrameworkScrollbars
from frameworks.web.frameworks_for_uitestingplayground_test.framework_shadow_dom import FrameworkShadowDom
from frameworks.web.frameworks_for_uitestingplayground_test.framework_text_input import FrameworkTextInput
from frameworks.web.frameworks_for_uitestingplayground_test.framework_verify_text import FrameworkVerifyText
from frameworks.web.frameworks_for_uitestingplayground_test.framework_visibility import FrameworkVisibility
from frameworks.web.frameworks_for_uitestingplayground_test.frameworks_dynamic_table import FrameworkDynamicTable
from frameworks.web.frameworks_for_uitestingplayground_test.frameworks_hidden_layers import FrameworkHiddenLayer
from frameworks.web.fw_for_demoqa_test.fw_text_box import FwTextBox


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
        self.fw_text_box = FwTextBox(self)
