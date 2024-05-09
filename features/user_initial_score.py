import time

from behave import then, when
from selenium.webdriver.common.by import By


@given("a user is on home page")
def navigate_to_home(context):
    context.driver.delete_all_cookies()
    context.driver.get("https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a")
    time.sleep(3)


@when("a user visits the course and clicks the START button")
def step(context):
    context.driver.find_element(By.XPATH, "//span[text()='START']").click()
    time.sleep(2)


@then("the users score should be 0")
def step(context):
    expected = "Your score so far: 0"
    score = context.driver.find_element(By.XPATH, "//p[contains(text(), 'Your score so far:')]").text
    assert score == expected, f"Expected '{expected}', but got '{score}'"
