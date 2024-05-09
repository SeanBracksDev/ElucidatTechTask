import time

from behave import given, then, when
from selenium.webdriver.common.by import By


@given("a user is on the voting page for kevin's case")
def navigate_to_kevin_case_vote(context):
    context.driver.delete_all_cookies()
    context.driver.get("https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a")
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//span[text()='START']").click()
    context.driver.find_element(By.XPATH, "//span[text()='Making a case against Kevin']").click()
    context.driver.find_element(By.XPATH, "//span[text()='JUDGE THIS']").click()


@when("a user votes that kevin is {option}")
def step(context, option: str):
    option_el = context.driver.find_element(By.XPATH, f"//span/label/strong[text()='{option}']")
    context.driver.execute_script("arguments[0].click();", option_el)
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, "//span[text()='VOTE']").click()
    time.sleep(1)


@then("the prompt should reflect that the user voted {option}")
def step(context, option: str):
    modal_headers = context.driver.find_elements(
        By.XPATH,
        "//h2[contains(@id, 'modalTitle')]/strong[contains(text(), '!')]",  # Not happy with this xpath, but I was spending too much time trying to find a better one
    )
    displayed_heading = [h for h in modal_headers if h.is_displayed()][0].text
    assert (
        displayed_heading == f"{option.upper()}!"
    ), f"Expected modal header to be '{option.upper()}!', but got '{displayed_heading}'"
