## Тестовое задание.

### Пути
  * / - Основная страница - список новостей
  * /news_id (число) - Страница конкретной новости по его айди
  * /by-tag - Страница новостей с поиском по тэгу
  * /admin/statistics - страница статистики просмотров новостей

### Установка
После загрузки репозитория, в папке где находится файл `pyproject` нужно выполнить команду `poetry install`, далее - `poetry shell`. Для этого вам потребуется установленный менеджер пакетов **poetry**: `pip install poetry`

### Настройка
В папке `django_news` нужно выполнить следующие команды:<br>
```
py manage.py makemigrations
py manage.py migrate
```
...для создания базы данных. Далее:
```
py manage.py createsuperuser
```
...для создания суперпользователя (админа).

Ввести команду `py manage.py collectstatic` не потребуется, т.к. проект работает в режиме отладки (т.е. `DEBUG = True`).

### Запуск
Для запуска нужно выполнить команду `py manage.py runserver`

## API
Если вы перейдёте по пути /api, то вы увидите обзор API (ApiOverview)

Касательно тех API запросов, которые требовались, чтобы были реализованы:
 * `/create` - POST запрос для создания новостей. В теле нужно отправлять следующие данные:<br>
   &emsp;"header": `header` - заголовок новости<br>
   &emsp;"text": `text` - текст новости<br>
   &emsp;"tags": `tags` - тэги новости (пример: `"tags": "nature, animals"`)<br>
   &emsp;"image": `image` - картинка новости (файл, *не ссылка*)<br>
 * `/delete/news_id` - DELETE запрос для удаления новости по его айди
 * `/get_single/news_id` - GET запрос для получения информации об одной новости по его айди
 * `/get_multiple/[start]/[end]` - GET запрос для получения информации о нескольких новостях в указанном с помощью индексов диапазоне 
