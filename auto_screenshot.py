import asyncio
import os
from playwright.async_api import async_playwright

# THAY LINK APP CỦA BẠN
APP_URL = "YOUR_APP_URL"


async def main():

    os.makedirs("assets/screenshots", exist_ok=True)

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--disable-software-rasterizer"
            ]
        )

        page = await browser.new_page(
            viewport={
                "width": 1440,
                "height": 900
            }
        )

        await page.goto(
            APP_URL,
            wait_until="domcontentloaded",
            timeout=60000
        )

        await page.wait_for_timeout(5000)

        await page.screenshot(
            path="assets/screenshots/home.png",
            full_page=True
        )

        await browser.close()

    print("Saved: assets/screenshots/home.png")


asyncio.run(main())
