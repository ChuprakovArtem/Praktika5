# Praktika5

5.7 Практическая работа
1. Установка Docker и Docker Compose:
a. Установил Docker и Docker Compose на систему.
b. Настроил Docker для работы без прав root (добавление
пользователя в группу docker).

2. Разработка программы:

a. Написал программу на python которая позволяет рисовать и
моментально сохранять изображения в формате подходящем для
обучения сверточных сетей (распознавание символов).

b. Создал репозиторий на GitHub для вашего проекта Praktika5

https://github.com/ChuprakovArtem/Praktika5

3. Создал Docker-образ для программы:

a. Создал Dockerfile для сборки образа, включающего программу и
зависимости.

b. Собрал Docker-образ из Dockerfile командой :

с. docker build -t ubuntu-vizual_pip .

4. Запуск и тестирование Python-приложения в Docker-контейнере:
a. Запустил Docker-контейнер из созданного образа, образ поместил
на https://hub.docker.com/

docker pull arch1987/ubuntu-vizual_pip

b. Проверил, что программа работает корректно внутри контейнера.

Так как программа с графическим интерфейсом необходимо
выполнить следующие манипуляции для запуска:
 1. Войти в контейнер:
docker run -it ubuntu-vizual_pip /bin/bash

2. Узнать свой IP в контейнере
ifconfig

3. Запустим Xpra внутри контейнера:

xpra start --start=xterm --bind-tcp=0.0.0.0:9009

4. Подключимся к Xpra с хоста:

k. xpra attach ws://172.17.0.2:9009

5. В Xtem ввести команду запуска python кода:

python3 gglit.py
 
В продолжении описания работы программы хочу уточнить, что
пронумерованные файлы .png сохраняются в корневую папку prog,
рядом со скриптом.

6. Работа с Docker Compose:
Создал docker-compose.yml, который запускает Docker-контейнер с программой.
Добавил комментарии в docker-compose.yml, объясняющие его структуру и команды.
#В этой строке указывается версия формата файла Docker Compose
version: '2'
#список сервисов
services:
#имя службы
 your_service:
#контейнер который нужно запускать
    image: ubuntu_hello:latest
#команда на запуск .bash скрипта
    command: bash /prog/hello.bash


Убедился, что Docker Compose позволяет запустить контейнер.



7. Оформление проекта на GitHub:
a. Поместил Dockerfile и docker-compose.yml в репозиторий на
GitHub.

b. Подготовил README.md, описывающий проект и процесс запуска
программы с помощью Docker и Docker Compose.
