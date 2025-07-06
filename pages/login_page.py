from .base_page import BasePage


class LoginPage(BasePage):
    username_input = "input[name='username']"
    password_input = "input[name='password']"
    submit_button = "button[type='submit']"

    def open(self):
        super().open(self.page.context.base_url + "/login")

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.submit_button)
