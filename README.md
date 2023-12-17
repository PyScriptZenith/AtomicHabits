# AtomicHabits: Трекер полезных привычек
Данное приложение реализует REST API и предназначено для отслеживания Ваших полезных привычек и поможет Вам стать лучшей версией себя!

## Исползуемые технологии
  * python
  * django
  * django rest framework
  * drf-yasg
  * postgresql
  * redis
  * celery
  * django-celery-beat
  * cors
  * simple jwt

## Сущности системы
  ### Привычка
  * пользователь
  * место выполнения
  * время выполнения
  * действие
  * связанная привычка (опционально)
  * признак приятной привычки
  * периодичность
  * вознаграждение
  * время на выполнение
  * признак публичности

### Пользователь
* почта
* пароль
* телефон 
* город 
* аватар
* telegram id 


## Документация API
Документация для API реализована с помощью drf-yasg и находится на следующих эндпоинтах:
* http://127.0.0.1:8000/docs/
* http://127.0.0.1:8000/redoc/

## CORS
Для безопасности API реализован CORS с помощью django-cors-headers. 

В модуле ``settings.py`` необходимо внести изменения в следующие настройки, если у Вас есть сторонние домены, обращающиеся к Вашему API:

```
CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com",
]
```
## Как использовать данный проект?

- Убедитесь, что у вас установлен docker и docker-compose
- Склонировать репозиторий и перейти в директорию

- Клонировать репозиторий и перейти в директорию
  
  В терминале необходимо ввести команды:
  ```
  git clone https://github.com/sudarev91/AtomicHabits
  ```
  ```
  cd AtomicHabits/
  ```
- Создать файл ``.env``, который необходимо заполнить данными из файла ``env.sample``
- Запустить проект
  
  В терминале ввести команду
  ```
  docker-compose up --build
  ```
- Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к приложению.

## Контакты

Если у Вас возникли вопросы или пожелания по развитию проекта, пожалуйста, свяжитесь со мной.

tg: opensda91
