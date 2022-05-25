# Импорт необходимых библиотек
from flask import render_template, url_for, Flask
import os
from wallhaven_api_functions import get_wallpaper_path, get_wallpaper_alt

# Инициализация Flask
app = Flask(__name__)

# Оъявление переменных
wallhaven_apikey = 'E2gtqjkHhdHKf9qYMMZPjzPT71u8BXoZ'
site_url = 'http://127.0.0.1:5000'


# Корень
@app.route('/')
def index():
    global wallhaven_apikey
    # Получение прямой ссылки рандомных обоев
    wallpaper_path = get_wallpaper_path(apikey=wallhaven_apikey, categories=100, sorting='random')
    # Получение названия рандомных обоев
    wallpaper_alt = get_wallpaper_alt(wallhaven_apikey, wallpaper_path)
    # Получаем пути к ресурсам
    site_icon_path = url_for('static', filename='img/logo.png')
    css_path = url_for('static', filename='css/main.css')
    icon_path = url_for('static', filename='img/icon.png')
    profile_path = url_for('static', filename='img/profile.png')
    script_path = url_for('static', filename='script/main_script.js')
    question_mark_path = url_for('static', filename='img/question_mark.png')

    # Рендерим страницу
    return render_template('main.html', wallpaper_path=wallpaper_path, wallpaper_alt=wallpaper_alt, icon_path=icon_path,
                           site_icon_path=site_icon_path, site_url=site_url, css_path=css_path,
                           profile_path=profile_path, script_path=script_path, question_mark_path=question_mark_path)


# Профиль
@app.route('/profile')
def profile():
    # Получаем пути к ресурсам
    css_path = url_for('static', filename='css/profile.css')
    icon_path = url_for('static', filename='img/icon.png')
    site_icon_path = url_for('static', filename='img/logo.png')
    avatar_path = url_for('static', filename='img/avatar.jpg')
    script_path = url_for('static', filename='script/profile_script.js')
    question_mark_path = url_for('static', filename='img/question_mark.png')

    # Рендерим страницу
    return render_template('profile.html', site_url=site_url, css_path=css_path, icon_path=icon_path,
                           site_icon_path=site_icon_path, avatar_path=avatar_path, script_path=script_path, question_mark_path=question_mark_path)


# Профиль
@app.route('/faq')
def faq():
    # Получаем пути к ресурсам
    css_path = url_for('static', filename='css/faq.css')
    icon_path = url_for('static', filename='img/icon.png')
    site_icon_path = url_for('static', filename='img/logo.png')
    profile_path = url_for('static', filename='img/profile.png')
    like_button_path = url_for('static', filename='img/like_button.png')
    # Рендерим страницу
    return render_template('faq.html', site_url=site_url, css_path=css_path, icon_path=icon_path,
                           site_icon_path=site_icon_path, profile_path=profile_path, like_button_path=like_button_path)


# Запуск
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)