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

@flaskrouter.route('/heroes')
@flaskrouter.route('/heroes?sort=<int:sort>?filtering=<string:filtering>')
@flaskrouter.route('/heroes?sort=<int:sort>?page=<int:page>?filtering=<string:filtering>')
def heroes(page=None, sort=None, filtering=None):
    """
    The various playable heroes page
    """
    if page == None:
      page = 1
    if sort == None:
      sort = 0
    if filtering == None:
      filtering = "all"
    if sort == 0:
      if filtering == "all":
  
        data = db.session.query(Hero).order_by(models.Hero.hero_name.asc()).all()
      else:
        data = db.session.query(Hero).order_by(models.Hero.hero_name.asc()).filter(Hero.role == filtering)
    else:
      if filtering == "all":
        data = db.session.query(Hero).order_by(models.Hero.hero_name.desc()).all()
      else:
        data = db.session.query(Hero).order_by(models.Hero.hero_name.desc()).filter(Hero.role == filtering)
    per_page = 6
    output = data[per_page*(page-1) : per_page*page]
    if filtering == "all":
      pagination = Hero.query.paginate(per_page=per_page, page=page)
    else:
      pagination = Hero.query.filter(Hero.role == filtering).paginate(per_page=per_page, page=page)
  
    return render_template('heroes.html', output=output, pagination = pagination, page_num = page, sort=sort, filtering = filtering)

@flaskrouter.route('/heroes/<int:hero_id>')
def hero(hero_id):
    data = models.Hero.query.get(hero_id)
    return render_template('heroes_instance.html', data = data)

@flaskrouter.route('/players')
@flaskrouter.route('/players/page/<int:page>')
def players(page=None):
    """
    A page for top-rated players
    """
    if page == None:
      page = 1
    per_page = 9
    data = db.session.query(TopPlayer).all()
    output = data[per_page*(page-1) : per_page*page]
    pagination = TopPlayer.query.paginate(per_page=per_page, page=page)
    return render_template('players.html', output=output,pagination=pagination, page_num=page)

@flaskrouter.route('/players/<int:top_player_id>')
def player(top_player_id):
    data = models.TopPlayer.query.get(top_player_id)
    return render_template('player_instance.html', data=data)

@flaskrouter.route('/skins')
@flaskrouter.route('/skins/page/<int:page>')
def skins(page=None):
    """
    A page for in-game skins
    """
    if page == None:
      page = 1
    per_page = 9
    data = db.session.query(Skin).all()
    output = data[per_page*(page-1) : per_page*page]
    pagination = Skin.query.paginate(per_page=per_page, page=page)
    return render_template('skins.html', output=output, pagination=pagination, page_num=page)

@flaskrouter.route('/skins/<int:skin_id>')
def skin(skin_id):
    data = models.Skin.query.get(skin_id)
    return render_template('skin_instance.html', data = data)

@flaskrouter.route('/items')
@flaskrouter.route('/items/page/<int:page>')
def items(page=None):
    """
    The page for in-game items 
    """
    if page == None:
      page = 1
    per_page = 15
    data = db.session.query(Item).filter(Item.hero_id != None)
    output = data[per_page*(page-1) : per_page*page]
    pagination = Item.query.filter(Item.hero_id != None).paginate(per_page=per_page, page=page)
    return render_template('items.html', output=output, pagination=pagination, page_num=page)
@flaskrouter.route('/items/<int:item_id>')
def item(item_id):
    data = models.Item.query.get(item_id)
    return render_template('item_instance.html',data = data)



@flaskrouter.route('/achievements')
@flaskrouter.route('/achievements/page/<int:page>')
def achievements(page=None):
    """
    The different types of achievements page
    """
    if page == None:
      page = 1
    per_page = 12
    data = db.session.query(Achievement).all()
    output = data[per_page*(page-1) : per_page*page]
    pagination = Achievement.query.paginate(per_page=per_page, page=page)
    return render_template('achievements.html', output=output, pagination=pagination, page_num=page)


@flaskrouter.route('/achievements/<int:achievement_id>')
def achievement(achievement_id):
    data = models.Achievement.query.get(achievement_id)
    return render_template('achievement_instance.html',data = data)



@flaskrouter.route('/events')
@flaskrouter.route('/events/page/<int:page>')
def events(page=None):
    """
    The different in-game events page
    """
    if page == None:
      page = 1
    per_page = 9
    data = db.session.query(Event).all()
    output = data[per_page*(page-1) : per_page*page]
    pagination = Event.query.paginate(per_page=per_page, page=page)
    return render_template('events.html', output=output, pagination=pagination, page_num=page)


@flaskrouter.route('/events/<int:event_id>')
def event(event_id):
    data = models.Event.query.get(event_id)
    return render_template('event_instance.html', data = data)




