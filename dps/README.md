Запустить приложение
  docker-compose up --build -d

Команды:
  docker-compose exec web python manage.py set_data -----> создать случайные данные для теста приложения

urls API:
  api/ ^stations/$ [name='station-list']
  api/ ^stations\.(?P<format>[a-z0-9]+)/?$ [name='station-list']
  api/ ^stations/(?P<pk>[^/.]+)/$ [name='station-detail']
  api/ ^stations/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='station-detail']
  api/ ^$ [name='api-root']
  api/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
  api/ api-auth/
  пример: http://0.0.0.0:3434/api/stations/1/,
          http://0.0.0.0:3434/api/stations/1/?format=json формат(json)

Cтек:
    Django, django-rest_framework, postgres, nginx

Окружение:
  Docker version 18.06.1-ce,
  4.15.0-36-generic #39-Ubuntu SMP Mon Sep 24 16:19:09 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux,


Задача:
  Необходимо разработать сервис обработки данных. Сервис получает и отдает данные по API.
  Пример входных данных:

  {
    "station_config":
    {
      "station_id": 823,
      "longitude": 46.813806,
      "latitude": -71.218833,
      "timezone": MSK,
    },
    "data":
    {
      "2016-12-30 10:00 UTC":
      {
        "t_air": -18.9,
      },
      "2016-12-30 10:00 UTC": { ... }, ...
    }
  }
  Требуется:

  1. Изобразить возможную архитектуру системы, зная, что данные с одной станции обрабатываются каждые 30 минут; количество станций 3000.

  2. Реализовать в коде обработку данных, заключающуюся в возвращении true, при переходе температуры через 0, и false при отсутствии перехода через 0 во входных данных.

  3. Создать конфигурационный файл docker-compose