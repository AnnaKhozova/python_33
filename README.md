Files
-----

[conftest.py] содержит весь необходимый код для отлова неудачных тестовых случаев и создания снимка экрана
страницы на случай, если какой-либо тестовый пример не удастся.

[pages/base.py] Реализация PageObject pattern для Python.

[pages/elements.py] содержит вспомогательный класс для определения веб-элементов на веб-страницах.

[pages/auth_pages.py] содержит вспомогательный класс для определения веб-элементов на странице авторизации

[pages/auth_register.py] содержит вспомогательный класс для определения веб-элементов на странице регистрации

[tests/test_1.py] содержит все наши тесты для сайта компании «Ростелеком Информационные Технологии»

	test_authorisation - Авторизация зарегистрированного пользователя по электронной почте
	test_authorisation_negativ_1 - Попытка авторизации незарегистрированного пользователя
	test_authorisation_phone - Авторизация зарегистрированного пользователя по номеру телефона
	test_authorisation_negativ_2 - Попытка авторизации с паролем, где заглавные буквы заменены строчными
	test_authorisation_negativ_3 - Попытка авторизации с не правильным номером телефона
	
	test_registration - Попытка регистрации с корректными данными, в случае успеха должно появится окно "Такая учетная запить уже существует"
	test_registration_negativ_1 - Попытка регистрации с одной буквой в имени
	test_registration_2 - Попытка регистрации с двумя буквами в имени
	test_registration_negativ_2 - Попытка регистрации с тире в имени
	test_registration_negativ_3 - Попытка регистрации со знаками препинания в имени
	test_registration_negativ_4 - Попытка регистрации с именем латинскими буквами
	test_registration_negativ_5 - Попытка регистрации с некорректно заданным e-mail
	test_registration_negativ_6 - Попытка регистрации с некорректно заданным паролем (менее 8 символов)
	test_registration_negativ_7 - Попытка регистрации с некорректно заданным паролем (без заглавных букв)
	test_registration_negativ_8 - Попытка регистрации с некорректно заданным паролем (не только латинские буквы)
	test_registration_negativ_9 - Попытка регистрации с некорректно заданным паролем (пароли не совпадают)
	test_registration_negativ_10 - Регистрация пользователя с паролем, более 20 символов
	test_registration_negativ_11 - Регистрация пользователя с пробелом в середине имени
	test_registration_3 - Регистрация пользователя с 20 символами в пароле
	test_registration_4 - Регистрация пользователя с пробелом в начале имени
	test_authorisation_negativ_4 - Попытка авторизации с незаполненными полями
	
	


Как запустить тесты
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:
C:\Users\akhozov\Desktop\Python\python_33_final>pytest --driver Chrome --driver-path chromedriver.exe

4) в файл login_date.py внести e-mail, пароль и номер телефона пользователя, зарегистрированного на сайте “Ростелеком Информационные Технологии”
