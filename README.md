# photo_editor
## Как открыть проект
Если нет инструмента virtualenv, его необходимо установить \
`pip install virtualenv` 

Создать виртуальное окружение \
`python3 -m venv env`

Перейти в env/Scripts/ и выбрать activate 

Установить необходимые пакеты \
`pip install -r requirements.txt` 

Скачать проект с github \
`git clone https://github.com/verachecheneva/photo_editor.git`

Внутри папки с проектом выполнить миграции\
`python manage.py makemigrations` \
`python manage.py migrate` \
`python manage.py runserver`

Чтобы запустить тесты используйте команду: \
`python manage.py test`

## Особенности проекта 

- В форму добавления картинки можно добавить либо картинку, либо ссылку на изображение
- Если на странице изображения отправить пустую форму, вернется картинка без изменений
- Если на странице изображения отправить только один параметр, вернтся изображение пропорциональное основному
- Если на странице изображения отправить оба параметра, вернется картинка по заданным параметрам без сохранения пропорциональности

