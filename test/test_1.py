from pages.auth_page import AuthPage
from pages.register_page import RegisterPage
import time
from login_date import LoginData


#Попытка регистрации с корректными данными, в случае успеха должно появится окно "Такая учетная запись уже существует"
def test_registration(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Иван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx123")

   page2.btn.click()

   assert page2.register_OK.is_visible()
   time.sleep(3)

#Попытка регистрации с одной буквой в имени
def test_registration_negativ_1(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("А")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx123")

   assert page2.error_name.is_visible()

   time.sleep(3)


#Попытка регистрации с двумя буквами в имени
def test_registration_2(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Ан")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx123")

   page2.btn.click()

   assert page2.register_OK.is_visible()

   time.sleep(3)


#Попытка регистрации с тире в имени
def test_registration_negativ_2(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("И-ван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx123")

   page2.btn.click()

   assert page2.register_OK.is_visible()
   time.sleep(3)

#Попытка регистрации со знаками препинания в имени
def test_registration_negativ_3(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Ива,н")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx123")


   assert page2.error_name.is_visible()

time.sleep(3)

#Попытка регистрации с именем латинскими буквами
def test_registration_negativ_4(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Ivan")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx123")

   assert page2.error_name.is_visible()

   time.sleep(3)

#Попытка регистрации с некорректно заданным e-mail
def test_registration_negativ_5(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Иван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys("qazwsx@@list.ru")

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx123")

   assert page2.error_mail.is_visible()

   time.sleep(3)

#Попытка регистрации с некорректно заданным паролем (менее 8 символов)
def test_registration_negativ_6(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Иван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx1")

   page2.password2.send_keys("Qazwsx1")

   assert page2.error_pass.is_visible()

   time.sleep(3)

#Попытка регистрации с некорректно заданным паролем (без заглавных букв)
def test_registration_negativ_7(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Иван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("qazwsx123")

   page2.password2.send_keys("qazwsx123")

   assert page2.error_pass.is_visible()

   time.sleep(3)


#Попытка регистрации с некорректно заданным паролем (не только латинские буквы)
def test_registration_negativ_8(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Иван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Фazwsx123")

   page2.password2.send_keys("Фazwsx123")

   assert page2.error_pass.is_visible()

   time.sleep(3)

#Попытка регистрации с некорректно заданным паролем (пароли не совпадают)
def test_registration_negativ_9(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Иван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx1234")

   page2.btn.click()

   assert page2.error_second_pass.is_visible()

   time.sleep(3)

#Регистрация пользователя с паролем, более 20 символов
def test_registration_negativ_10(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Иван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123111111111111")

   page2.password2.send_keys("Qazwsx123111111111111")

   assert page2.error_pass.is_visible()

   time.sleep(3)


#Регистрация пользователя с пробелом в середине имени
def test_registration_negativ_11(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Ива н")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx123")

   assert page2.error_name.is_visible()

   time.sleep(3)

#Регистрация пользователя с 20 символами в пароле
def test_registration_3(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys("Иван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx12311111111111")

   page2.password2.send_keys("Qazwsx12311111111111")

   page2.btn.click()

   assert page2.register_OK.is_visible()

   time.sleep(3)

#Регистрация пользователя с пробелом в начале имени
def test_registration_4(web_browser):
   page = AuthPage(web_browser)

   page.register_link.click()

   #time.sleep(10)

   page2 = RegisterPage(web_browser)

   page2.firstName.send_keys(" Иван")

   page2.lastName.send_keys("Петров")

   page2.e_mail.send_keys(LoginData.valid_email)

   page2.password1.send_keys("Qazwsx123")

   page2.password2.send_keys("Qazwsx123")

   page2.btn.click()

   assert page2.register_OK.is_visible()

   time.sleep(3)

#Авторизация зарегистрированного пользователя по электронной почте
def test_authorisation(web_browser):
   page = AuthPage(web_browser)

   page.email.send_keys(LoginData.valid_email)

   page.password.send_keys(LoginData.valid_password)

   page.btn.click()

   url = page.get_current_url()

   assert url.find('https://b2c.passport.rt.ru/account_b2c/page')==0

#Попытка авторизации незарегистрированного пользователя
def test_authorisation_negativ_1(web_browser):
   page = AuthPage(web_browser)

   page.email.send_keys("a40@gmail.ru")

   page.password.send_keys(LoginData.valid_password)

   page.btn.click()

   url = page.get_current_url()

   assert url.find('https://b2c.passport.rt.ru/account_b2c/page')==-1


#Авторизация зарегистрированного пользователя по номеру телефона
def test_authorisation_phone(web_browser):
   page = AuthPage(web_browser)

   page.email.send_keys(LoginData.valid_phone)

   page.password.send_keys(LoginData.valid_password)

   page.btn.click()

   url = page.get_current_url()

   assert url.find('https://b2c.passport.rt.ru/account_b2c/page')==0


#Попытка авторизации с паролем, где заглавные буквы заменены строчными
def test_authorisation_negativ_2(web_browser):
   page = AuthPage(web_browser)

   page.email.send_keys(LoginData.valid_email)

   page.password.send_keys("as@yahh6j9z67aw")

   page.btn.click()

   url = page.get_current_url()

   assert url.find('https://b2c.passport.rt.ru/account_b2c/page')==-1


#Попытка авторизации с не правильным номером телефона
def test_authorisation_negativ_3(web_browser):
   page = AuthPage(web_browser)

   page.email.send_keys(LoginData.invalid_phone)

   page.password.send_keys(LoginData.valid_password)

   page.btn.click()

   url = page.get_current_url()

   assert url.find('https://b2c.passport.rt.ru/account_b2c/page')==-1

#Попытка авторизации с незаполненными полями
def test_authorisation_negativ_4(web_browser):
   page = AuthPage(web_browser)

   page.btn.click()

   url = page.get_current_url()

   assert url.find('https://b2c.passport.rt.ru/account_b2c/page')==-1