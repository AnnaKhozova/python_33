from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    email = WebElement(id='username')

    password = WebElement(id='password')

    btn = WebElement(xpath='//button[@type="submit"]')

    register_link = WebElement(id='kc-register')