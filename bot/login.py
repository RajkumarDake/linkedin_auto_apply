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


def _fill_login_field(locators: list[tuple], value: str, field_name: str, time_each: float = 2.0) -> bool:
    '''
    Tries each `(By.X, "selector")` in `locators` in turn, waiting up to `time_each` seconds
    for it to be clickable, and fills the first one found with `value`.
    * Returns `True` if a field was found and filled, `False` if all locators failed.
    * Multiple fallback locators guard against LinkedIn renaming the field `id` (which is
      exactly what broke the previous single By.ID("username")/By.ID("password") lookup).
    '''
    for by, selector in locators:
        try:
            field = WebDriverWait(driver, time_each).until(EC.element_to_be_clickable((by, selector)))
            field.send_keys(Keys.CONTROL + "a")
            field.send_keys(value)
            return True
        except Exception:
            continue
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
            (By.ID, "username"),
            (By.XPATH, "//input[@autocomplete='username']"),
            (By.XPATH, "//label[contains(normalize-space(),'Email') or contains(normalize-space(),'Phone')]/following::input[1]"),
            (By.XPATH, "//input[@type='text' or @type='email']"),
        ], username, "username")
        _fill_login_field([
            (By.ID, "password"),
            (By.XPATH, "//input[@autocomplete='current-password']"),
            (By.XPATH, "//label[contains(normalize-space(),'Password')]/following::input[1]"),
            (By.XPATH, "//input[@type='password']"),
        ], password, "password")
        # Find the login submit button and click it
        driver.find_element(By.XPATH, '//button[@type="submit" and contains(text(), "Sign in")]').click()
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
