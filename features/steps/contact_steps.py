import re

from playwright.async_api import expect
from behave import *

from models.contact_page import ContactPage
from environment import async_run_until_complete


@Given("the user has submitted an incomplete form")
@When("the user submits an incomplete form")
@async_run_until_complete
async def submit_empty_form(context):
    current_page = ContactPage(context.page)
    await current_page.input_message("")
    await current_page.input_email("")
    await current_page.input_forename("")
    await current_page.submit_form()


@When("the user submits the form")
@async_run_until_complete
async def submit_form(context):
    current_page = ContactPage(context.page)
    await current_page.submit_form()


@Then('the warning banner displays "{banner_message}"')
@async_run_until_complete
async def verify_warning_banner_class(context, banner_message):
    current_page = ContactPage(context.page)
    banner_element = current_page.welcome_banner
    await expect(banner_element).to_have_text(re.compile(f".*{banner_message}.*"))


@When('the user enters the forename "{forename}"')
@async_run_until_complete
async def enter_contact_info_forename(context, forename):
    current_page = ContactPage(context.page)
    await current_page.input_forename(forename)


@When('the user enters the email "{email}"')
@async_run_until_complete
async def enter_contact_info_email(context, email):
    current_page = ContactPage(context.page)
    await current_page.input_email(email)


@When('the user enters the message "{message}"')
@async_run_until_complete
async def enter_contact_info_message(context, message):
    current_page = ContactPage(context.page)
    await current_page.input_message(message)


@Then('the success banner displays the message "{banner_text}"')
@async_run_until_complete
async def verify_success_banner_class(context, banner_text):
    current_page = ContactPage(context.page)
    await current_page.feedback_header.wait_for(state="hidden")
    await expect(current_page.page.get_by_text(banner_text)).to_be_visible()
