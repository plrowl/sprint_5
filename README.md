Sprint_5 

Автотесты для сайта https://qa-desk.stand.praktikum-services.ru/

Структура:
tests/ - тестовые сценарии
conftest.py - фикстуры
locators.py - локаторы
data.py - вспомогательные данные

Тестовые сценарии:

Регистрация пользователя test_reg_new_user

Регистрация пользователя c email не по маске  *******@*******.***   test_reg_invalid_email_user

Регистрация уже существующего пользователя  test_reg_existing_user

Login пользователя  test_login_user

Logout пользователя test_logout_user

Создание объявления неавторизованным пользователем  test_create_ad_unauthorized

Создание объявления авторизованным пользователем test_create_ad_authorized
