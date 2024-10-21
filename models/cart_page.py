import logging
from models.base_page import BasePage

from playwright.async_api import Page


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_url = self.construct_url("cart")

        self.cart_table_row = page.get_by_role("row")
        self.cart_total_text = page.get_by_text("Total:")

    async def get_cart_price_cell_by_product(self, product_name):
        """
        Takes a product name, finds a correspondting table row, and extracts
        the pricing information.

        Expected cart table structure: Product name > Price > Quantity > Subtotal

        Parameters:
            product_name (String): Name of product being examined

        Returns:
        Locator: Element locator for the pricing cell of the table row

        """
        logging.info(f"Extracting cart price cell for {product_name}")
        product_row = self.cart_table_row.filter(
            has=self.page.get_by_text(product_name)
        )
        logging.debug(product_row)
        return product_row.locator("td").nth(1)

    async def get_cart_subtotal_cell_by_product(self, product_name):
        """
        Takes a product name, finds a correspondting table row, and extracts
        the subtotal information.

        Expected cart table structure: Product name > Price > Quantity > Subtotal

        Parameters:
            product_name (String): Name of product being examined

        Returns:
        Locator: Element locator for the subtotal cell of the table row

        """
        logging.info(f"Extracting cart subtotal cell for {product_name}")
        product_row = self.cart_table_row.filter(
            has=self.page.get_by_text(product_name)
        )
        logging.debug(product_row)
        return product_row.locator("td").nth(3)
