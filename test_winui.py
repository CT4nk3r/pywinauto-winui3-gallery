import subprocess
import time
import pytest
from pywinauto.application import Application
from pywinauto import Desktop
from ui_helper import UIHelper

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
    helper.wait_and_click("Basic input", "ListItem", found_index=0)
    helper.wait_and_click("Button", "ListItem")
    helper.wait_and_click("Standard XAML", "Button", found_index=0)

    result = helper.get_wrapper("You clicked: Button1", "Text")
    assert result is not None, "Result text not found"
    print("Correct output found:", result.window_text())

def test_disable_button(helper):
    helper.wait_and_click("Disable button", "CheckBox", found_index=0)
    time.sleep(1)

    wrapper = helper.wait_and_assert_enabled("Standard XAML", "Button", expected_enabled=False)
    assert wrapper.is_enabled() is False
    print(f"Assertion passed: 'Standard XAML' button enabled state is {wrapper.is_enabled()}")
