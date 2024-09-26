# Tken from GroqLama3.2 is your p2 function but with a progress bar

import time
from rich.progress import track
from playwright.sync_api import sync_playwright
from datetime import datetime, timezone
from rich import print as rprint  # For rprinting

# -- Imports ---
from playwright.sync_api import sync_playwright
from datetime import datetime, timezone
from rich import print as rprint  # For rprinting

# --- User Agent and Websites ---
urls = [
    "https://www.coingecko.com/",
    "https://www.femscat.com/main.php",
    "https://www.meanbitches.com/",
]
uA = "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
c_d = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def func22():
    with sync_playwright() as p:
        rprint("[blue1][OK] Starting Playwright Script...[/blue1]")

        # Launching Browser and Navigating
        rprint("[blue1][OK] Launching Broswer...[/blue1]")
        browser = p.chromium.launch()
        page = browser.new_page(user_agent=uA)

        # Opening New Page
        rprint(f"[green3][OK] Go to page - {urls[0]}[/green3]")
        for i in track(range(1), description="Loading page..."):
            page.goto(urls[0], timeout=0)
            rez = page.goto(urls[0], timeout=0)
            rezStatus = rez.status
            rprint(f"[green3][OK] Go to page - {urls[0]} - {rezStatus}[/green3]")
            time.sleep(1)  # Simulate work being done

        # Grab Title
        rprint(f"[green3][OK] Grab Title - {urls[0]}[/green3]")
        for i in track(range(1), description="Grabbing title..."):
            rprint(page.title())
            time.sleep(1)  # Simulate work being done

        # Create sreenshot - wih current date time
        rprint(f"[green3][OK] Create screenshot - {c_d}-s1.png[/green3]")
        page.screenshot(path=f"clicks/{c_d}-s1.png", full_page=True)

        # Closing Browser
        rprint("[gold3][OK] Shutdown Browser[/gold3]")
        browser.close()
