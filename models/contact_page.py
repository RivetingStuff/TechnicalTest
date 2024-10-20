from enum import Enum

from playwright.async_api import Page

from models.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_url = self.construct_url("contact")
        self.welcome_banner = page.get_by_text("We welcome your feedback").locator("..")
        self.submit_button = page.get_by_role("link", name="Submit")

        self.forename_text_input = page.get_by_role("textbox", name="forename")
        self.email_text_input = page.get_by_role("textbox", name="email")
        self.message_text_input = page.get_by_role("textbox", name="message")

        self.feedback_header = page.get_by_text("Sending Feedback")

    async def submit_form(self):
        await self.submit_button.click()

    async def input_forename(self, forename):
        await self.forename_text_input.fill(forename)

    async def input_email(self, forename):
        await self.email_text_input.fill(forename)

    async def input_message(self, forename):
        await self.message_text_input.fill(forename)
