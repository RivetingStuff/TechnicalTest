from playwright.async_api import expect
from behave import *
import re

from models.shop_page import ShopPage
from models.cart_page import CartPage
from models.base_page import BasePage
from environment import async_run_until_complete


@When("the user buys the following items")
@async_run_until_complete
async def buy_items_by_table(context):
    current_page = ShopPage(context.page)
    for row in context.table:
        await current_page.buy_product(row["item_name"], int(row["amount"]))


@Then("the itemized cart prices match the following")
@async_run_until_complete
async def verify_cart_table(context):
    current_page = CartPage(context.page)
    for row in context.table:
        price_cell = await current_page.get_cart_price_cell_by_product(row["item_name"])
        await expect(price_cell).to_have_text(f"${row['price']}")


@Then("the itemized cart subtotals match the following")
@async_run_until_complete
async def verify_cart_table(context):
    current_page = CartPage(context.page)
    for row in context.table:
        subtotal_cell = await current_page.get_cart_subtotal_cell_by_product(
            row["item_name"]
        )
        await expect(subtotal_cell).to_have_text(f"${row['subtotal']}")


@Then('the total cost displayed is "{cart_total_value}"')
@async_run_until_complete
async def verify_cart_subtotal_for_product(context, cart_total_value):
    current_page = CartPage(context.page)
    await expect(current_page.cart_total_text).to_have_text(
        re.compile(f".*{cart_total_value}.*")
    )
