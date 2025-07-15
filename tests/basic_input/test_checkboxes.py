import pytest
from pages.basic_input.checkbox_page import CheckboxPage

@pytest.fixture
def checkbox_page(helper):
    page = CheckboxPage(helper.main_win)
    page.open_basic_input()
    page.open_checkbox_section()
    return page

def test_two_state_checkbox(checkbox_page):
    checkbox_page.reset_to_checkbox_section()
    checkbox_page.click_two_state_checkbox()
    result_checked = checkbox_page.get_two_state_checked_text()
    assert result_checked is not None

    checkbox_page.click_two_state_checkbox()
    result_unchecked = checkbox_page.get_two_state_unchecked_text()
    assert result_unchecked is not None

def test_three_state_checkbox(checkbox_page):
    checkbox_page.reset_to_checkbox_section()
    checkbox_page.click_three_state_checkbox()
    result_checked = checkbox_page.get_three_state_checked_text()
    assert result_checked is not None

    checkbox_page.click_three_state_checkbox()
    result_indeterminate = checkbox_page.get_three_state_indeterminate_text()
    assert result_indeterminate is not None

    checkbox_page.click_three_state_checkbox()
    result_unchecked = checkbox_page.get_three_state_unchecked_text()
    assert result_unchecked is not None

def test_select_all_checkbox(checkbox_page):
    checkbox_page.reset_to_checkbox_section()

    checkbox_page.click_select_all_checkbox()

    checkbox_state = checkbox_page.get_three_state_checkbox_state()
    assert checkbox_state == "unchecked"

    checkbox_page.click_option_checkbox("Option 2")

    checkbox_state = checkbox_page.get_three_state_checkbox_state()
    assert checkbox_state == "unchecked"