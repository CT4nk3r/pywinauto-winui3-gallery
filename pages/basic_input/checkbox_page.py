from utils.ui_helper import UIHelper

class CheckboxPage:
    def __init__(self, main_win):
        self.helper = UIHelper(main_win)

    def reset_to_checkbox_section(self):
        self.helper.wait_and_click("Home", "ListItem")
        self.open_basic_input()
        self.open_checkbox_section()

    def open_basic_input(self):
        self.helper.wait_and_click("Basic input", "ListItem", found_index=0)

    def open_checkbox_section(self):
        self.helper.wait_and_click("CheckBox", "ListItem")

    def click_two_state_checkbox(self):
        self.helper.wait_and_click("Two-state", "CheckBox")

    def get_two_state_checked_text(self):
        return self.helper.get_wrapper("You checked the box.", "Text")

    def get_two_state_unchecked_text(self):
        return self.helper.get_wrapper("You unchecked the box.", "Text")

    def click_three_state_checkbox(self):
        self.helper.wait_and_click("Three-state", "CheckBox")

    def get_three_state_checkbox_state(self):
        return self.helper.get_checkbox_state("Three-state", "CheckBox")

    def get_three_state_checked_text(self):
        return self.helper.get_wrapper("CheckBox is checked.", "Text")

    def get_three_state_indeterminate_text(self):
        return self.helper.get_wrapper("CheckBox state is indeterminate.", "Text")

    def get_three_state_unchecked_text(self):
        return self.helper.get_wrapper("CheckBox is unchecked.", "Text")

    def click_select_all_checkbox(self, found_index=0):
        return self.helper.get_checkbox_state("Select all", "CheckBox")
        
    def get_select_all_checkbox(self, found_index=0):
        self.helper.wait_and_click("Select all", "CheckBox", found_index=found_index)

    def click_option_checkbox(self, option_text):
        self.helper.wait_and_click(option_text, "CheckBox")

