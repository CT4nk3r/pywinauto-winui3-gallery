import subprocess
import time
import pytest
from pywinauto.application import Application
from pywinauto import Desktop
from utils.ui_helper import UIHelper

@pytest.fixture(scope="session")
def helper():
    subprocess.run(['explorer.exe', 'shell:AppsFolder\\Microsoft.WinUI3ControlsGallery_8wekyb3d8bbwe!App'])
    time.sleep(5)

    windows = Desktop(backend="uia").windows(title_re=".*WinUI.*Gallery.*")
    assert windows, "No matching windows found"
    chosen_handle = windows[0].handle

    app = Application(backend="uia").connect(handle=chosen_handle)
    main_win = app.window(handle=chosen_handle)

    main_win.maximize()

    main_win.set_focus()

    return UIHelper(main_win)
