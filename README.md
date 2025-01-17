# ТЕСТОВОЕ ЗАДАНИЕ

## Демонстрация – https://drive.google.com/drive/folders/1GePS6uFPRmJnDA7etTYMaSrkswDZbWVf

## Как развернуть проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:OlegPrizov/testapi.git
```

```
cd newtestapi/
```

2. Создать и активировать виртуальное окружение
```
python3 -m venv venv
source venv/bin/activate
```

3. Установить библиотеки:

```
pip install -r requirements.txt
```

4. Создать и активировать миграции
```
python manage.py makemigrations
python manage.py migrate
```

5. Заполнить базу данных:
```
python manage.py datafiller
```
Используется парсинг, но если браузер устойчив к ботам, то используются заранее сохраненные вручную данные

6. Запустить проект:

```
python manage.py runserver
```

7. С помощью Postman по адресу .../api/auth/users/ зарегистрировать нового пользователя.
Для этого передать в формате JSON следующие данные:
```
{
    "username": "<ваш юзернейм>",
    "password": "<ваш пароль>"
}
```

8. Получить токен по адресу .../api/auth/jwt/create, передав туда те же данные, что и в 6 пункте.
В ответ получите токен, который нужно использовать далее для доступа к следующим адресам:

```
.../api/ads/<id> – выведет одно конкретное объявление
.../api/ads – выведет все 10 первых объявлений
```
