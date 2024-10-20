from behave import *

from models.base_page import BasePage
from models.contact_page import ContactPage
from models.shop_page import ShopPage
from models.cart_page import CartPage

from environment import async_run_until_complete


@Given("the user navigates to the homepage")
@async_run_until_complete
async def navigate_to_homepage(context):
    current_page = BasePage(context.page)
    await current_page.navigate()


@Given("the user clicks on the contact button")
@async_run_until_complete
async def click_on_contact_nav_button(context):
    base_page = BasePage(context.page)
    await base_page.navigate_to_contact_page()
    current_page = ContactPage(context.page)
    await current_page.page.wait_for_url(current_page.page_url)


@Given("the user clicks on the shop button")
@async_run_until_complete
async def click_on_shop_nav_button(context):
    base_page = BasePage(context.page)
    await base_page.navigate_to_shop_page()
    current_page = ShopPage(context.page)
    await current_page.page.wait_for_url(current_page.page_url)


@When("the user clicks on the Cart button")
@async_run_until_complete
async def click_on_cart_nav_button(context):
    base_page = BasePage(context.page)
    await base_page.navigate_to_cart_page()
    current_page = CartPage(context.page)
    await current_page.page.wait_for_url(current_page.page_url)
