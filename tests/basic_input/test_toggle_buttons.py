import pytest
from pages.basic_input.toggle_button_page import ToggleButtonPage

@pytest.fixture
def toggle_page(helper):
    page = ToggleButtonPage(helper.main_win)
    page.open_toggle_button_section()
    return page

def test_toggle_button_on(toggle_page):
    toggle_page.reset_to_toggle_button_section()
    toggle_page.click_toggle_button()
    result = toggle_page.get_toggle_state_text("On")
    assert result is not None

def test_toggle_button_off(toggle_page):
    toggle_page.reset_to_toggle_button_section()
    toggle_page.click_toggle_button()  # ON
    toggle_page.get_toggle_state_text("On")
    toggle_page.click_toggle_button()  # OFF
    result = toggle_page.get_toggle_state_text("Off")
    assert result is not None

def test_toggle_button_disabled(toggle_page):
    toggle_page.reset_to_toggle_button_section()
    toggle_page.disable_toggle_button()
    wrapper = toggle_page.assert_toggle_button_disabled()
    assert wrapper.is_enabled() is False
