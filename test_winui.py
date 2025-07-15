import subprocess
import time
import pytest
from pywinauto.application import Application
from pywinauto import Desktop
from ui_helper import UIHelper
from pages.button_page import ButtonPage

@pytest.fixture(scope="session")
def helper():
    subprocess.run(['explorer.exe', 'shell:AppsFolder\\Microsoft.WinUI3ControlsGallery_8wekyb3d8bbwe!App'])
    time.sleep(5)

    windows = Desktop(backend="uia").windows(title_re=".*WinUI.*Gallery.*")
    assert windows, "No matching windows found"
    chosen_handle = windows[0].handle

    app = Application(backend="uia").connect(handle=chosen_handle)
    main_win = app.window(handle=chosen_handle)
    main_win.set_focus()

    return UIHelper(main_win)

def test_button_click(helper):
    page = ButtonPage(helper.main_win)
    page.open_basic_input()
    page.open_button_section()
    page.click_standard_xaml()
    result = page.get_result_text()
    assert result is not None

def test_disable_button(helper):
    page = ButtonPage(helper.main_win)
    page.disable_button()
    wrapper = page.assert_standard_xaml_disabled()
    assert wrapper.is_enabled() is False
