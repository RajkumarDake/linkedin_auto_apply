'''
LinkedIn login: checking login state and performing (auto or manual) login.
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
        try:
            text_input_by_ID(driver, "username", username, 5)
        except Exception as e:
            print_lg("Couldn't find username field.")
            # print_lg(e)
        try:
            text_input_by_ID(driver, "password", password, 5)
        except Exception as e:
            print_lg("Couldn't find password field.")
            # print_lg(e)
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
