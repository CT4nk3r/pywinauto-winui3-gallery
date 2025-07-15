from ui_helper import UIHelper

class ButtonPage:
    def __init__(self, main_win):
        self.helper = UIHelper(main_win)

    def open_basic_input(self):
        self.helper.wait_and_click("Basic input", "ListItem", found_index=0)

    def open_button_section(self):
        self.helper.wait_and_click("Button", "ListItem")

    def click_standard_xaml(self):
        self.helper.wait_and_click("Standard XAML", "Button", found_index=0)

    def get_result_text(self):
        return self.helper.get_wrapper("You clicked: Button1", "Text")

    def disable_button(self):
        self.helper.wait_and_click("Disable button", "CheckBox", found_index=0)

    def assert_standard_xaml_disabled(self):
        return self.helper.wait_and_assert_enabled("Standard XAML", "Button", expected_enabled=False)