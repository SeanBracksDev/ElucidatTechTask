import time

from behave import then, when
from selenium.webdriver.common.by import By


@given("a user is on FINDING THE TRUTH page")
def navigate_to_home(context):
    context.driver.delete_all_cookies()
    context.driver.get("https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a")
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//span[text()='START']").click()


@when("a user visits the course and clicks Who is to blame?")
def step(context):
    context.driver.find_element(By.XPATH, "//span[text()='Who is to blame?']").click()
    time.sleep(1)


@then("the user is navigated to Case 2: What happened? page")
def step(context):
    expected = "A young man has been in an accident in the warehouse where he worked and has subsequently died."
    first_p = context.driver.find_element(By.XPATH, "//p").text
    assert first_p == expected, f"Expected '{expected}', but got '{first_p}'"
