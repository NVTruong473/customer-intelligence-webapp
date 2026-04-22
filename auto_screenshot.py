import asyncio
import os
from playwright.async_api import async_playwright

APP_URL = "https://a11f-34-168-243-32.ngrok-free.app/"

async def main():

    os.makedirs("assets/screenshots", exist_ok=True)

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox"]
        )

        context = await browser.new_context(
            extra_http_headers={
                "ngrok-skip-browser-warning": "true"
            }
        )

        page = await context.new_page()

        await page.set_viewport_size({
            "width": 1440,
            "height": 900
        })

        await page.goto(APP_URL, timeout=60000)
        await page.wait_for_timeout(5000)

        await page.screenshot(
            path="assets/screenshots/home.png",
            full_page=True
        )

        await browser.close()

asyncio.run(main())
