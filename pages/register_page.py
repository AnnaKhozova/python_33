from pages.base import WebPage
from pages.elements import WebElement


class RegisterPage(WebPage):

    def __init__(self, web_driver, url=''):
        super().__init__(web_driver, url)

    firstName = WebElement(name='firstName')

    lastName = WebElement(name='lastName')

    btn = WebElement(xpath='//button[@type="submit"]')

    e_mail = WebElement(id="address")

    password1 = WebElement(id="password")

    password2 = WebElement(id="password-confirm")

    register_OK = WebElement(xpath='//div[@class="card-modal__card"]')

    error_name = WebElement(xpath='//*[@class="name-container"]/div[1]/span[contains(@class, "meta--error")]')


    error_mail = WebElement(xpath='//*[contains(@class, "email-or-phone")]/span[contains(@class, "meta--error")]')


    error_pass = WebElement(xpath='//*[contains(@class, "new-password-container__password")]/span[contains(@class, "meta--error")]')

    error_second_pass = WebElement(xpath='//*[contains(@class, "new-password-container__confirmed-password")]/span[contains(@class, "meta--error")]')




