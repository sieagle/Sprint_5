from selenium.webdriver.common.by import By

class MainLocators:
    """Главная страница"""
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") #Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета
    account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета
    login_btn = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") #Кнопка войти в аккаунт
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']") #Кнопка конструктор
    bun_btn = (By.XPATH, ".//span[text() = 'Булки']") #Кнопка переключения на булки
    sauces_btn = (By.XPATH, ".//span[text() = 'Соусы']") #Кнопка переключения на соусы
    toppings_btn = (By.XPATH, ".//span[text() = 'Начинки']") #Кнопка переключения на начинки
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']") #Кнопка оформить заказ
    sauces = (By.XPATH, ".//h2[text() = 'Соусы']") #Текст соусы на главной странице
    sauces_ul = (By.XPATH, ".//span[@class = 'text text_type_main-default'][text() = 'Соусы']") #Выбор соусов на главной странице
    bun = (By.XPATH, ".//h2[text() = 'Булки']") #Текст булки на главной странице
    bun_ul = (By.XPATH, ".//span[@class = 'text text_type_main-default'][text() = 'Булки']") #Выбор булок на главной странице
    topping = (By.XPATH, ".//h2[text() = 'Начинки']") #Текст начинки на главной странице
    topping_ul = (By.XPATH, ".//span[@class = 'text text_type_main-default'][text() = 'Начинки']") #Выбор начинок на главной странице


class LoginLocators:
    """Форма авторизации"""
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета
    email_input = (By.XPATH, ".//input[@name = 'name']") #Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']") #Поле ввода пароля
    login_btn = (By.XPATH, "//button[text() = 'Войти']") #Кнопка войти
    registration_btn = (By.XPATH, "//a[text() = 'Зарегистрироваться']") #Кнопка зерегистрироваться
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']") #Кнопка конструктор
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") #Кнопка главной страницы сайта
    account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета
    login_account_btn = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") #Кнопка войти в аккаунт

class RegisterLocators:
    """Форма регистрации"""
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета
    name_input = (By.XPATH, "(.//div[@class = 'input pr-6 pl-6 input_type_text input_size_default']/label[text() = 'Имя']/../input)") #Поле ввода имени
    email_input = (By.XPATH, "(.//div[@class = 'input pr-6 pl-6 input_type_text input_size_default']/label[text() = 'Email']/../input)") #Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']") #Поле ввода пароля
    registration_btn = (By.XPATH, ".//button[text() = 'Зарегистрироваться']") #Кнопка зерегистрироваться
    login_btn = (By.XPATH, ".//a[text() = 'Войти']") #Кнопка войти
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']") #Кнопка конструктор
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") #Кнопка главной страницы сайта
    account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета
    error_message_double_reg = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']") #Ошибка при повторной регистрации
    error_message_incorrect_password = (By.XPATH, ".//p[text() = 'Некорректный пароль']") #Ошибка при вводе некорректного пароля


class RecoverLocators:
    """Форма восстановления пароля"""
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета
    email_input = (By.XPATH, ".//label[text() = 'Email']") #Поле ввода email
    login_btn = (By.XPATH, ".//a[text() = 'Войти']") #Кнопка войти
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']") #Кнопка конструктор
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") #Кнопка главной страницы сайта
    account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета


class UserLocators:
    """Форма личного кабинета"""
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']") #Форма личного кабинета
    profile_btn = (By.XPATH, ".//a[text() = 'Профиль']") #Кнопка профиль
    order_history_btn = (By.XPATH, ".//a[text() = 'История заказов']") #Кнопка история заказов
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']") #Кнопка выход
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']") #Кнопка сохранить
    cansel_btn = (By.XPATH, ".//button[text() = 'Отмена']") #Кнопка отмена
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']") #Кнопка конструктор
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") #Кнопка главной страницы сайта
    account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка личного кабинета
