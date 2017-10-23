from flask import Flask, render_template

flaskrouter = Flask(__name__)

@flaskrouter.route('/')
def index():
    """
    Home and root directory of our site
    """
    return render_template('index.html')


@flaskrouter.route('/about')
def about():
    """
    The about page
    """
    return render_template('about.html')


@flaskrouter.route('/achievements')
def achievements():
    """
    The different types of achievements page
    """
    return render_template('achievements.html')


@flaskrouter.route('/events')
def events():
    """
    The different in-game events page
    """
    return render_template('events.html')


@flaskrouter.route('/heroes')
def heroes():
    """
    The various playable heroes page
    """
    return render_template('heroes.html')


@flaskrouter.route('/items')
def items():
    """
    The page for in-game items 
    """
    return render_template('items.html')


@flaskrouter.route('/players')
def players():
    """
    A page for top-rated players
    """
    return render_template('players.html')


@flaskrouter.route('/skins')
def skins():
    """
    A page for in-game skins
    """
    return render_template('skins.html')

if __name__ == '__main__':
   flaskrouter.run()
