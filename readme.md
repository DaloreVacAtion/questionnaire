<h1>Опросник</h1>

<h2>Описание:</h2>
<p>Проект представляет собой систему прохождения опросов (именно опросов, а не тестов, хотя немного
подправив модели и отрисовку результатов и можно делать и тесты).
Взаимодействие с пользователем очень простое: необходимо пройти регистрацию, введя имя пользователя и
пароль. Только зарегистрированные пользователи имеют доступ к заполнению опросов и списку "игроков", так скажем.
</p>
<p>Пройдя авторизацию вы получаете доступ к опросам. Повторное прохождение опросов лишь заменяет 
Ваши ответы, но не дает бонус "валюту".</p>
<p>За "валюту" можно изменить цвет рамки и ника, а так же задний фон на странице настроек. 
Реализовано конечно криво, так как я не бог фронтенда.</p>
<h2>Технологии:</h2>
<p>Данный проект написан на языке Python c использованием веб фреймворка Django версии 4.0.6.
Для работы API был использован Django REST Framework версии 3.13.1. В качестве БД 
была выбрана СУБД PostgreSQL 11-ой версии. Все настройки Postgre были вынесены в файл .env. 
Для того, чтобы вытащить настройки из файла .env, была использована библиотека django-dotenv 
версии 1.4.2. Все зависимости указаны в файле "requirements.txt". Фронтенд реализован с 
использованием шаблонизатора Django, сырого JS и немного JQuery.</p>

<h2>Проблемы:</h2>
<p>К сожалению, пришлось столкнуться с рядом проблем, решение которых требует некоторого времени:</p>
<ul>
<li>Хотелось прикрутить Gin индексы на поле title, чтобы реализовать поиск по названию 
опроса на странице со списком опросов, однако сделать это не удалось из-за проблем с Оп классом
Триграм. Так как это тестовое задание, то решено было двигаться дальше и найти решение проблемы позже.</li>
<li>Опять же проблемы с Postgre. По какой-то причине поиск <i>icontains</i> не работает с 
non-ASCII символами. Точнее сказать, любой поиск, который не учитвает регистр. работает только с 
ASCII символами. Скорее всего, необходимо покапаться в настройках постгреса.</li>
</ul>

<h2>О внутрянке:</h2>
<p>Проект представляет собой несколько вьюх для шаблонов и небольшое API, которое можно использовать, 
например, для мобильной версии (настройки цвета пользователя, получение списка опросов, получение 
списка пользователей и т.д.)</p>

<p>Заранее извиняюсь, если что-то написано криво и режет глаза.</p>