from playwright.async_api import Page


class BasePage:
    base_url = ""

    def __init__(self, page: Page):
        self.page = page

        self.page_url = self.base_url

        self.contact_nav_button = page.get_by_role("link", name="Contact")
        self.shop_nav_button = page.get_by_role("link", name="Shop", exact=True)
        self.cart_nav_button = page.get_by_role("link", name="Cart")

    async def navigate(self):
        await self.page.goto(self.page_url)

    async def navigate_to_contact_page(self):
        await self.contact_nav_button.click()

    async def navigate_to_shop_page(self):
        await self.shop_nav_button.click()

    async def navigate_to_cart_page(self):
        await self.cart_nav_button.click()

    def construct_url(self, endpoint):
        return f"{BasePage.base_url}{endpoint}"
