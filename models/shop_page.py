from models.base_page import BasePage
import logging

from playwright.async_api import Page


class ShopPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_url = self.construct_url("shop")
        self.header_banner_text = page.get_by_text("We welcome your feedback")
        self.shop_listitems = page.get_by_role("listitem")

    async def get_product_listitem(self, product_name):
        return self.shop_listitems.filter(has=self.page.get_by_text(product_name))

    async def buy_product(self, product_name, count=1):
        buy_button = (await self.get_product_listitem(product_name)).get_by_role(
            "link", name="Buy"
        )
        for index in range(0, count):
            logging.debug(f"Buying '{product_name}' number {index}")
            await buy_button.click()
