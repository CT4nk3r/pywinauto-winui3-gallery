import pytest
from pages.basic_input.button_page import ButtonPage

@pytest.fixture
def button_page(helper):
    page = ButtonPage(helper.main_win)
    page.open_basic_input()
    page.open_button_section()
    return page

def test_standard_button_click(helper):
    page = ButtonPage(helper.main_win)
    page.reset_to_button_section()
    page.click_standard_xaml()
    result = page.get_result_text_button1()
    assert result is not None

def test_disable_button(helper):
    page = ButtonPage(helper.main_win)
    page.reset_to_button_section()
    page.disable_button()
    wrapper = page.assert_standard_xaml_disabled()
    assert wrapper.is_enabled() is False

def test_pie_button_click(helper):
    page = ButtonPage(helper.main_win)
    page.reset_to_button_section()
    page.click_pie_button()
    result = page.get_result_text_button2()
    assert result is not None
