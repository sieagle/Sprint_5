from random import randint

class User:
    user_name = 'Серафима'
    email = f'serafima_orlova_42@yandex.ru'
    password = f'Seo12345'

class NewRandomUser:
    user_name = 'Тестовый'
    email = f'serafima_orlova_42_{randint(0, 999)}@yandex.ru'
    password = f'Seo{randint(10000, 99999)}'

    def generate(self):
        self.email = f'serafima_orlova_42_{randint(0, 999)}@yandex.ru'
        self.password = f'Seo{randint(10000, 99999)}'
        return self