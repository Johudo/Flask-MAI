# Лаборатортная работа

В результате лабораторной работы сделан FLASK сервер со следующим функционалом:

1. Роут "/" редиректит на роут "/users"
2. Роут "/users" выведит список всех пользователей
3. Роут "/user/\<int: id\>" выводит информацию о пользователе с данным id, если такого не существует, то выдает ошибку 404
4. Роут "/create-user" выводит страницу с формой создания нового пользователя

## Запуск проекта

```
pip install -r requirements.txt
python ./main.py
```

## Результат работы

Роут "/users"

![Роут "/users"](./md_images/users.jpg)

Роут "/user/1"

![Роут "/user/1"](./md_images/user_1.png)

Роут "/user/32231"

![Роут "/user/32231"](./md_images/user_32231.png)

Роут "/create-user"

![Роут "/create-user"](./md_images/create-user.jpg)
