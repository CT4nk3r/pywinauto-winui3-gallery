import time
import pywinauto.mouse as mouse

class UIHelper:
    def __init__(self, main_win):
        self.main_win = main_win

    def wait_and_click(self, title, control_type, timeout=10, found_index=0):
        ctrl = self.main_win.child_window(title=title, control_type=control_type, found_index=found_index)
        ctrl.wait("enabled visible ready", timeout=timeout)
        ctrl.click_input()

    def wait_and_assert_enabled(self, title, control_type, expected_enabled, timeout=10, poll_interval=0.5):
        ctrl = self.main_win.child_window(title=title, control_type=control_type)
        ctrl.wait("exists visible", timeout=timeout)
        end_time = time.time() + timeout
        while time.time() < end_time:
            wrapper = ctrl.wrapper_object()
            if wrapper.is_enabled() == expected_enabled:
                return wrapper
            time.sleep(poll_interval)
        raise AssertionError(f"Control '{title}' expected enabled={expected_enabled}, but timed out")

    def get_wrapper(self, title, control_type, timeout=10):
        ctrl = self.main_win.child_window(title=title, control_type=control_type)
        ctrl.wait("exists visible ready", timeout=timeout)
        return ctrl.wrapper_object()
    
    def get_checkbox_state(self, title, control_type="CheckBox"):
        ctrl = self.main_win.child_window(title=title, control_type=control_type)
        toggle_state = ctrl.get_toggle_state()
        if toggle_state == 0:
            return "unchecked"
        elif toggle_state == 1:
            return "checked"
        elif toggle_state == 2:
            return "indeterminate"
        else:
            raise ValueError(f"Unknown toggle state: {toggle_state}")
