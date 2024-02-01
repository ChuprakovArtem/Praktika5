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

4. Запуск и тестирование bash-приложения в Docker-контейнере:

	Запустил Docker-контейнер из созданного образа, образ поместил
на https://hub.docker.com/ скачать можно по ссылке ниже
docker pull arch1987/ubuntu_hello
Проверил, что программа работает корректно внутри контейнера.b.

	Войти в контейнер:
 docker run -it ubuntu_hello:latest /bin/bash
	
	Выполнить запуск bash скрипта
source hello.bash


 
В продолжении описания работы программы хочу уточнить, что
пронумерованные файлы .png сохраняются в корневую папку prog,
рядом со скриптом.

5. Работа с Docker Compose:
  a. Создал docker-compose.yml, который запускает Docker-контейнер с
программой.
  b. Добавил комментарии в docker-compose.yml, объясняющие его
структуру и команды.

#В этой строке указывается версия формата файла Docker
Compose
 version: '2'
#список сервисов
 services:
#имя службы
 your_service:
#контейнер который нужно запускать
image: ubuntu_hello:latest
#команда на запуск .bash скрипта
command: bash /docker-prakt/hello.bash

 c. Убедился, что Docker Compose позволяет запустить контейнер.



6. Оформление проекта на GitHub:
a. Поместил Dockerfile и docker-compose.yml в репозиторий на
GitHub.

b. Подготовил README.md, описывающий проект и процесс запуска
программы с помощью Docker и Docker Compose.
