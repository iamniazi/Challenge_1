from playwright.sync_api import Page

class BasePage:
 
    def __init__(self, page: Page):
        self.page = page

    def navigation(self, url: str):
       
        self.page.goto(url)

    def take_snapshots(self, name: str):
      
        self.page.screenshot(path=f"snapshots/{name}.png")
