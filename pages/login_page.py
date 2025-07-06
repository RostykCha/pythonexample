from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page, base_url: str):
        super().__init__(page)
        self.base_url = base_url.rstrip('/')

    def load(self):
        self.goto(self.base_url)

    def login(self, username: str, password: str):
        self.page.fill('#username', username)
        self.page.fill('#password', password)
        self.page.click('button[type="submit"]')
