from behave import fixture, use_fixture
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright
from models.base_page import BasePage
from utility.scenario_repeat import patch_scenario_to_repeat
from behavex_images import image_attachments
from time import time

@fixture
async def browser_chrome(context):
    base_url = context.config.userdata.get("baseURL")
    slow_mo = context.config.userdata.get("slow-mo")
    headless = context.config.userdata.get("headless") == "true"
    browser_userdata = context.config.userdata.get("browser")

    playwright = await async_playwright().start()
    if browser_userdata == "firefox":
        browser = await playwright.firefox.launch(headless=headless, slow_mo=slow_mo)
    elif browser_userdata == "chrome":
        browser = await playwright.chromium.launch(
            headless=headless, channel="chrome", slow_mo=slow_mo
        )
    else:
        browser = await playwright.chromium.launch(headless=headless, slow_mo=slow_mo)

    context.page = await browser.new_page(base_url=base_url)
    # Unfortunately this option doesn't actually seem to work
    # A hacky alternative is a static variable. I don't condone this.
    BasePage.base_url = base_url

    return context.page


@async_run_until_complete
async def before_scenario(context, scenario):
    await use_fixture(browser_chrome, context)


@async_run_until_complete
async def after_step(context, step):
    if step.status == 'failed':
            screenshot_filename = f"{''.join(step.name.split())}-{int(time())}.png"
            screenshot_path = f"./output/screenshots/{screenshot_filename}"
            await context.page.screenshot(path=screenshot_path, full_page=True)
            image_attachments.attach_image_file(context, screenshot_path)
