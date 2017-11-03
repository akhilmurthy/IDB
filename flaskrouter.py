from flask import Flask, render_template, Blueprint, request, session, redirect, url_for
import models as models
from models import *
from sqlalchemy import or_, and_



flaskrouter = Blueprint("flaskrouter", __name__)

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



@flaskrouter.route('/events')
def events():
    """
    The different in-game events page
    """
    output = db.session.query(Event).all()
 
    return render_template('events.html', output = output)


@flaskrouter.route('/events/<int:event_id>')
def event(event_id):
    data = models.Event.query.get(event_id)
    return render_template('event_instance.html', data = data)


@flaskrouter.route('/heroes')
@flaskrouter.route('/heroes/page/<int:page>')
def heroes(page=None):
    """
    The various playable heroes page
    """
    if page == None:
      page = 1
    data = db.session.query(Hero).all()
    per_page = 6
    output = data[per_page*(page-1):per_page*page]
    pagination = Hero.query.paginate(per_page=per_page, page=page)
    return render_template('heroes.html', output=output, pagination = pagination, page_num = page)

@flaskrouter.route('/heroes/<int:hero_id>')
def hero(hero_id):
    data = models.Hero.query.get(hero_id)
    return render_template('heroes_instance.html', data = data)

@flaskrouter.route('/players')
def players():
    """
    A page for top-rated players
    """
    output = db.session.query(TopPlayer).all()
    return render_template('players.html', output=output)

@flaskrouter.route('/players/<int:top_player_id>')
def player(top_player_id):
    data = models.TopPlayer.query.get(top_player_id)
    return render_template('player_instance.html', data = data)

@flaskrouter.route('/skins')
def skins():
    """
    A page for in-game skins
    """
    output = db.session.query(Skin).all()
    return render_template('skins.html', output=output)

@flaskrouter.route('/skins/<int:skin_id>')
def skin(skin_id):
    data = models.Skin.query.get(skin_id)
    return render_template('skin_instance.html', data = data)

@flaskrouter.route('/items')
def items():
    """
    The page for in-game items 
    """
    output = db.session.query(Item).all()
    return render_template('items.html', output=output)
@flaskrouter.route('/items/<int:item_id>')
def item(item_id):
    data = models.Item.query.get(item_id)
    return render_template('item_instance.html',data = data)



@flaskrouter.route('/achievements')
def achievements():
    """
    The different types of achievements page
    """
    
    output = db.session.query(Achievement).all()
    return render_template('achievements.html', output=output)


@flaskrouter.route('/achievements/<int:achievement_id>')
def achievement(achievement_id):
    data = models.Achievement.query.get(achievement_id)
    return render_template('achievement_instance.html',data = data)


