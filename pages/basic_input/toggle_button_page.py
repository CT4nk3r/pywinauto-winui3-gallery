from utils.ui_helper import UIHelper

class ToggleButtonPage:
    def __init__(self, main_win):
        self.helper = UIHelper(main_win)

    def reset_to_toggle_button_section(self):
        self.helper.wait_and_click("Home", "ListItem")
        self.open_toggle_button_section()

    def open_toggle_button_section(self):
        self.helper.wait_and_click("Basic input", "ListItem", found_index=0)
        self.helper.wait_and_click("ToggleButton", "ListItem")

    def click_toggle_button(self):
        self.helper.wait_and_click("ToggleButton", "Button")

    def get_toggle_state_text(self, expected_text):
        return self.helper.get_wrapper(expected_text, "Text")

    def disable_toggle_button(self):
        self.helper.wait_and_click("Disable ToggleButton", "CheckBox")

    def assert_toggle_button_disabled(self):
        return self.helper.wait_and_assert_enabled("ToggleButton", "Button", expected_enabled=False)
