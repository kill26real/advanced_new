import datetime
from flask import Flask, render_template, request, redirect, g
from flask_babel import Babel, _

app = Flask(__name__)

# Flask-Babel Konfiguration
app.config['BABEL_DEFAULT_LOCALE'] = 'de'
app.config['BABEL_SUPPORTED_LOCALES'] = ['de', 'ru', 'en']
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


def get_locale():
    locale = request.cookies.get('locale')
    if locale:
        return locale

    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


babel = Babel(app, locale_selector=get_locale)



@app.route('/change_language/<language>')
def change_language(language):
    if language not in app.config['BABEL_SUPPORTED_LOCALES']:
        language = app.config['BABEL_DEFAULT_LOCALE']

    response = redirect(request.referrer)
    response.set_cookie('locale', language)  # Die gewählte Sprache im Cookie speichern
    return response


# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
