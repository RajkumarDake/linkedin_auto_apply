'''
LinkedIn login: checking login state and performing (auto or manual) login.
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from datetime import datetime

from config.secrets import username, password
from config.settings import logs_folder_path

from modules.open_chrome import *
from modules.helpers import *
from modules.clickers_and_finders import *
from modules import state


def _screenshot_login_failure() -> str:
    '''
    Saves a screenshot of the current page so a failed login can be diagnosed visually
    (e.g. LinkedIn showing a "Continue as [saved account]" screen or a checkpoint instead
    of the plain username/password form).
    '''
    name = "login_failure_{}.png".format(str(datetime.now()).replace(":", "."))
    path = (logs_folder_path + "/screenshots/" + name).replace("//", "/")
    try:
        driver.save_screenshot(path)
        print_lg(f'Saved login-failure screenshot to "{path}"')
    except Exception as e:
        print_lg("Failed to save login-failure screenshot.", e)
    return path


def _first_visible(elements: list) -> object | bool:
    '''
    Returns the first element in `elements` that is actually displayed and enabled, or
    `False` if none are. LinkedIn's login page renders duplicate desktop/mobile variants
    of the same form simultaneously - `find_element` (singular) always returns the FIRST
    DOM match, which can be the permanently-hidden copy, so a naive wait would time out
    forever even though a usable, visible copy exists later in the DOM.
    '''
    for el in elements:
        try:
            if el.is_displayed() and el.is_enabled():
                return el
        except Exception:
            continue
    return False


def _find_visible(by, selector: str, time: float = 3.0) -> object | bool:
    '''
    Waits up to `time` seconds for at least one visible+enabled element matching
    `(by, selector)` to appear, and returns it. Returns `False` on timeout.
    '''
    try:
        return WebDriverWait(driver, time).until(lambda d: _first_visible(d.find_elements(by, selector)))
    except Exception:
        return False


def _fill_login_field(locators: list[tuple], value: str, field_name: str, time_each: float = 3.0) -> bool:
    '''
    Tries each `(By.X, "selector")` in `locators` in turn, waiting up to `time_each` seconds
    for a visible copy to appear, and fills the first one found with `value`.
    * Returns `True` if a field was found and filled, `False` if all locators failed.
    * Multiple fallback locators guard against LinkedIn renaming the field `id` (which is
      exactly what broke the previous single By.ID("username")/By.ID("password") lookup -
      current LinkedIn uses React's auto-generated, non-deterministic `id="«r0»"` style ids).
    '''
    for by, selector in locators:
        field = _find_visible(by, selector, time_each)
        if field:
            field.send_keys(Keys.CONTROL + "a")
            field.send_keys(value)
            return True
    print_lg(f"Couldn't find {field_name} field with any known locator.")
    return False


def is_logged_in_LN() -> bool:
    '''
    Function to check if user is logged-in in LinkedIn
    * Returns: `True` if user is logged-in or `False` if not
    '''
    if driver.current_url == "https://www.linkedin.com/feed/": return True
    if try_linkText(driver, "Sign in"): return False
    if try_xp(driver, '//button[@type="submit" and contains(text(), "Sign in")]'):  return False
    if try_linkText(driver, "Join now"): return False
    print_lg("Didn't find Sign in link, so assuming user is logged in!")
    return True


def login_LN() -> None:
    '''
    Function to login for LinkedIn
    * Tries to login using given `username` and `password` from `secrets.py`
    * If failed, tries to login using saved LinkedIn profile button if available
    * If both failed, asks user to login manually
    '''
    # Find the username and password fields and fill them with user credentials
    driver.get("https://www.linkedin.com/login")
    if username == "username@example.com" and password == "example_password":
        msg = "User did not configure username and password in secrets.py, hence can't login automatically! Please login manually!"
        print_lg(msg)
        state.log_event("info", msg)
        manual_login_retry(is_logged_in_LN, 2)
        return
    try:
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Forgot password?")))
        _fill_login_field([
            (By.XPATH, "//input[contains(@autocomplete,'username') and @type='email']"),
            (By.ID, "username"),
            (By.XPATH, "//label[contains(normalize-space(),'Email') or contains(normalize-space(),'Phone')]/following::input[1]"),
            (By.XPATH, "//input[@type='text' or @type='email']"),
        ], username, "username")
        _fill_login_field([
            (By.XPATH, "//input[contains(@autocomplete,'current-password') and @type='password']"),
            (By.ID, "password"),
            (By.XPATH, "//label[contains(normalize-space(),'Password')]/following::input[1]"),
            (By.XPATH, "//input[@type='password']"),
        ], password, "password")
        # Find the login submit button and click it (LinkedIn's "Sign in" button is a plain
        # <button type="button"> with the label in a nested <span>, not a <button type="submit">
        # with direct text - contains(text(),...) would never match it)
        submit_button = _find_visible(By.XPATH, "//button[.//span[normalize-space(text())='Sign in']]", 3.0)
        if submit_button:
            submit_button.click()
        else:
            raise Exception("Couldn't find Sign in button")
    except Exception as e1:
        try:
            profile_button = find_by_class(driver, "profile__details")
            profile_button.click()
        except Exception as e2:
            # print_lg(e1, e2)
            print_lg("Couldn't Login!")
            _screenshot_login_failure()

    try:
        # Wait until successful redirect, indicating successful login
        wait.until(EC.url_to_be("https://www.linkedin.com/feed/"))
        return print_lg("Login successful!")
    except Exception as e:
        print_lg("Seems like login attempt failed! Possibly due to wrong credentials or already logged in! Try logging in manually!")
        # print_lg(e)
        _screenshot_login_failure()
        manual_login_retry(is_logged_in_LN, 2)
