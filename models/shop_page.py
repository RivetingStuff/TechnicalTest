import logging

from playwright.async_api import Page

from models.base_page import BasePage


class ShopPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_url = self.construct_url("shop")
        self.header_banner_text = page.get_by_text("We welcome your feedback")
        self.shop_listitems = page.get_by_role("listitem")

    async def get_product_listitem(self, product_name):
        logging.info("Looking for {product_name} in shop page")
        product_locator = self.shop_listitems.filter(has=self.page.get_by_text(product_name))
        logging.debug(f"Product locator {product_locator}")
        return product_locator

    async def buy_product(self, product_name, count=1):
        """ 
        Given a product name this function finds the corresponding <li> element 
        on the shop page, finds the associated buy button, and clicks it a 
        specified number of times.

        Parameters:
            product_name (String): Name of product being examined
            count (int): Number of times to buy an item
        """
        logging.info(f"Pressing clicking buy button {count} time(s) for {product_name}")
        buy_button = (await self.get_product_listitem(product_name)).get_by_role(
            "link", name="Buy"
        )
        logging.debug(f"Buy button locator: {buy_button}")
        for index in range(1, count+1):
            logging.debug(f"Buying '{product_name}' number {index}/{count}")
            await buy_button.click()
