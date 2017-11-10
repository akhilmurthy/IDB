from flask import Flask, render_template, Blueprint, request, session, redirect, url_for, jsonify, abort
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

@flaskrouter.route('/api/heroes', methods = ['GET'])
def get_heroes():
    return jsonify({'heroes': db.session.query(Hero).all()})
@flaskrouter.route('/api/heroes/<int:hero_id>', methods = ['GET'])
def get_hero(hero_id):
    return jsonify({'hero': models.Hero.query.get(hero_id)})

@flaskrouter.route('/heroes/<int:hero_id>')
def hero(hero_id):
    data = models.Hero.query.get(hero_id)
    return render_template('heroes_instance.html', data = data)



@flaskrouter.route('/achievements')
@flaskrouter.route('/achievements?sort=<int:sort>?filtering=<string:filtering>')
@flaskrouter.route('/achievements?sort=<int:sort>?page=<int:page>?filtering=<string:filtering>')

def achievements(page=None, sort=None, filtering=None):
    """
    The different types of achievements page
    """
    if page == None:
      page = 1
    if sort == None:
      sort = 0
    if filtering == None:
      filtering = "all"
    per_page = 12
    if sort == 0:
      if filtering == "all":
        data = db.session.query(Achievement).order_by(models.Achievement.achievement_name.asc()).all()
      elif filtering == "hero":
        data = db.session.query(Achievement).order_by(models.Achievement.achievement_name.asc()).filter(Achievement.heroes != None)
      else:
        data = db.session.query(Achievement).order_by(models.Achievement.achievement_name.asc()).filter(Achievement.heroes == None)
    else:
      if filtering == "all":
        data = db.session.query(Achievement).order_by(models.Achievement.achievement_name.desc()).all()
      elif filtering == "hero":
        data = db.session.query(Achievement).order_by(models.Achievement.achievement_name.desc()).filter(Achievement.heroes != None)
      else:
        data = db.session.query(Achievement).order_by(models.Achievement.achievement_name.desc()).filter(Achievement.heroes == None)
    output = data[per_page*(page-1) : per_page*page]
    if filtering == "all":
      pagination = Achievement.query.paginate(per_page=per_page, page=page)
    elif filtering == "hero":
      pagination = Achievement.query.filter(Achievement.heroes != None).paginate(per_page=per_page, page=page)
    else:
      pagination = Achievement.query.filter(Achievement.heroes == None).paginate(per_page=per_page, page=page)
  
    return render_template('achievements.html', output=output, pagination = pagination, page_num = page, sort=sort, filtering = filtering)

@flaskrouter.route('/achievements/<int:achievement_id>')
def achievement(achievement_id):
    data = models.Achievement.query.get(achievement_id)
    return render_template('achievement_instance.html',data = data)


@flaskrouter.route('/events')
@flaskrouter.route('/events?sort=<int:sort>?filtering=<string:filtering>')
@flaskrouter.route('/events?sort=<int:sort>?page=<int:page>?filtering=<string:filtering>')
def events(page=None, sort=None, filtering=None):
    """
    The different in-game events page
    """
    if page == None:
      page = 1
    if sort == None:
      sort = 0
    if filtering == None:
      filtering = "all"
    if sort == 0:
      if filtering == "all":
        data = db.session.query(Event).order_by(models.Event.event_name.asc()).all()
      elif filtering == "2017":
        data = db.session.query(Event).order_by(models.Event.event_name.asc()).filter(Event.end_date == "2017-01-02")
      else:
        data = db.session.query(Event).order_by(models.Event.event_name.asc()).filter(Event.end_date != "2017-01-02")
    else:
      if filtering == "all":
        data = db.session.query(Event).order_by(models.Event.event_name.desc()).all()
      elif filtering == "2017":
        data = db.session.query(Event).order_by(models.Event.event_name.desc()).filter(Event.end_date == "2017-01-02")
      else:
        data = db.session.query(Event).order_by(models.Event.event_name.desc()).filter(Event.end_date != "2017-01-02")
    per_page = 6
    output = data[per_page*(page-1) : per_page*page]
    if filtering == "all":
      pagination = Event.query.paginate(per_page=per_page, page=page)
    elif filtering == "2017":
      pagination = Event.query.filter(Event.end_date == "2017-01-02").paginate(per_page=per_page, page=page)
    else:
      pagination = Event.query.filter(Event.end_date != "2017-01-02").paginate(per_page=per_page, page=page)
    return render_template('events.html', output=output, pagination=pagination, page_num=page, sort=sort, filtering=filtering)


@flaskrouter.route('/events/<int:event_id>')
def event(event_id):
    data = models.Event.query.get(event_id)
    return render_template('event_instance.html', data = data)

@flaskrouter.route('/skins')
@flaskrouter.route('/skins?sort=<int:sort>?filtering=<int:filtering>')
@flaskrouter.route('/skins?sort=<int:sort>?page=<int:page>?filtering=<int:filtering>')
def skins(page=None, sort=None, filtering=None):
    """
    The different in-game events page
    """
    if page == None:
      page = 1
    if sort == None:
      sort = 0
    if filtering == None:
      filtering = 25
    
    if page == None:
      page = 1
    if sort == 0:
      if filtering == 25:
        data = db.session.query(Skin).order_by(models.Skin.skin_name.asc()).all()
      else:
        data = db.session.query(Skin).order_by(models.Skin.skin_name.asc()).filter(Skin.hero_id == filtering)
    else:
      if filtering == 25:
        data = db.session.query(Skin).order_by(models.Skin.skin_name.desc()).all()
      else:
        data = db.session.query(Skin).order_by(models.Skin.skin_name.desc()).filter(Skin.hero_id == filtering)
    per_page = 6
    output = data[per_page*(page-1) : per_page*page]
    if filtering == 25:
      pagination = Skin.query.paginate(per_page=per_page, page=page)
    else:
      pagination = Skin.query.filter(Skin.hero_id == filtering).paginate(per_page=per_page, page=page)
    hero = db.session.query(Hero).all()
    return render_template('skins.html', output=output, pagination = pagination, page_num = page, sort=sort, filtering = filtering, hero=hero)

@flaskrouter.route('/skins/<int:skin_id>')
def skin(skin_id):
    data = models.Skin.query.get(skin_id)
    return render_template('skin_instance.html', data = data)

@flaskrouter.route('/items')
@flaskrouter.route('/items?sort=<int:sort>?filtering=<int:filtering>')
@flaskrouter.route('/items?sort=<int:sort>?page=<int:page>?filtering=<int:filtering>')
def items(page=None, sort=None, filtering=None):
    """
    The different in-game events page
    """
    if page == None:
      page = 1
    if sort == None:
      sort = 0
    if filtering == None:
      filtering = 25
    if sort == 0:
      if filtering == 25:
        data = db.session.query(Item).order_by(models.Item.item_name.asc()).all()
      else:
        data = db.session.query(Item).order_by(models.Item.item_name.asc()).filter(Item.hero_id == filtering)
    else:
      if filtering == 25:
        data = db.session.query(Item).order_by(models.Item.item_name.desc()).all()
      else:
        data = db.session.query(Item).order_by(models.Item.item_name.desc()).filter(Item.hero_id == filtering)
    per_page = 	15
    output = data[per_page*(page-1) : per_page*page]
    if filtering == 25:
      pagination = Item.query.paginate(per_page=per_page, page=page)
    else:
      pagination = Item.query.filter(Item.hero_id == filtering).paginate(per_page=per_page, page=page)
    hero = db.session.query(Hero).all()
    return render_template('items.html', output=output, pagination = pagination, page_num = page, sort=sort, filtering = filtering, hero=hero)

@flaskrouter.route('/items/<int:item_id>')
def item(item_id):
    data = models.Item.query.get(item_id)
    return render_template('item_instance.html',data = data)




@flaskrouter.route('/players')
@flaskrouter.route('/players?sort=<int:sort>?filtering=<int:filtering>')
@flaskrouter.route('/players?sort=<int:sort>?page=<int:page>?filtering=<int:filtering>')
def players(page=None, sort=None, filtering=None):
    """
    A page for top-rated players
    """
    if page == None:
      page = 1
    if sort == None:
      sort = 0
    if filtering == None:
      filtering = 25
    if sort == 0:
      if filtering == 25:
        data = db.session.query(TopPlayer).order_by(models.TopPlayer.top_player_name.asc()).all()
      else:
        data = db.session.query(TopPlayer).order_by(models.TopPlayer.top_player_name.asc()).filter(TopPlayer.hero_id == filtering)
    else:
      if filtering == 25:
        data = db.session.query(TopPlayer).order_by(models.TopPlayer.top_player_name.desc()).all()
      else:
        data = db.session.query(TopPlayer).order_by(models.TopPlayer.top_player_name.desc()).filter(TopPlayer.hero_id == filtering)
    per_page = 	12
    output = data[per_page*(page-1) : per_page*page]
    if filtering == 25:
      pagination = TopPlayer.query.paginate(per_page=per_page, page=page)
    else:
      pagination = TopPlayer.query.filter(TopPlayer.hero_id == filtering).paginate(per_page=per_page, page=page)
    hero = db.session.query(Hero).all()
    return render_template('players.html', output=output, pagination = pagination, page_num = page, sort=sort, filtering = filtering, hero=hero)
@flaskrouter.route('/players/<int:top_player_id>')
def player(top_player_id):
    data = models.TopPlayer.query.get(top_player_id)
    return render_template('player_instance.html', data=data)




