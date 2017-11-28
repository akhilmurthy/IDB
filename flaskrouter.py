from flask import Flask, render_template, Blueprint, request, session, redirect, url_for, jsonify, abort
import models as models
from models import *
from sqlalchemy import or_, and_



flaskrouter = Blueprint("flaskrouter", __name__)



def api(data):
    if not data:
        return jsonify([])
    return jsonify(data.json())
def apis(data, start, end):
    result=[]
    for i in range(start,end):
        temp = data.get(i)
        if temp != None:
            result.append(data.get(i).json())
    return jsonify(result)
@flaskrouter.route('/api/heroes/<int:hero_id>')
@flaskrouter.route('/api/heroes')
@flaskrouter.route('/api/heroes/')
def api_heroes(hero_id=None):
    if hero_id != None:
        return api(models.Hero.query.get(hero_id))
    else:
        return apis(models.Hero.query,1,25)
@flaskrouter.route('/api/players/<int:player_id>')
@flaskrouter.route('/api/players')
@flaskrouter.route('/api/players/')
def api_players(player_id=None):
    if player_id != None:
        return api(models.TopPlayer.query.get(player_id))
    else:
        return apis(models.TopPlayer.query, 1,194)
@flaskrouter.route('/api/achievements/<int:achievement_id>')
@flaskrouter.route('/api/achievements')
@flaskrouter.route('/api/achievements/')
def api_achievements(achievement_id=None):
    if achievement_id != None:
        return api(models.Achievement.query.get(achievement_id))
    else:
        return apis(models.Achievement.query,1,74)

@flaskrouter.route('/api/events/<int:event_id>')
@flaskrouter.route('/api/events')
def api_events(event_id=None):
    if event_id != None:
        return api(models.Event.query.get(event_id))
    else:
        return apis(models.Event.query, 1,4)

@flaskrouter.route('/api/skins/<int:skin_id>')
@flaskrouter.route('/api/skins')
@flaskrouter.route('/api/skins/')
def api_skins(skin_id=None):
    if skin_id != None:
        return api(models.Skin.query.get(skin_id))
    else:
        return apis(models.Skin.query, 1223,1856)

@flaskrouter.route('/api/items/<int:item_id>')
@flaskrouter.route('/api/items')
@flaskrouter.route('/api/items/')
def api_items(item_id=None):
    if item_id != None:
        return api(models.Item.query.get(item_id))
    else:
        return apis(models.Item.query, 1,1871)


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

@flaskrouter.route('/visualization')
def visualization():
    return render_template('visualization.html')

@flaskrouter.route('/search')
@flaskrouter.route('/search?search_str=<string:search_str>')
@flaskrouter.route('/search?search_str=<string:search_str>?current_view=<string:current_view>')
@flaskrouter.route('/search?search_str=<string:search_str>?current_view=<string:current_view>?page=<int:page>')
def search(search_str = 'No search term', current_view = 'Hero', page = None):
    if page == None:
        page = 1
    if request.args.get('search_str') !=None:
        search_str = request.args.get('search_str')
    # filt = '%'+search_str +'%'
    filt = '%' + search_str  + '%'
    per_page = 10
    hero_query = None
    player_query = None
    achievement_query = None
    event_query = None
    skin_query = None
    item_query = None
    initial = True
    for a in search_str.split(' '):
      tmp = '%' + a + '%'
      ok = or_(Hero.hero_name.ilike(tmp),Hero.description.ilike(tmp),Hero.role.ilike(tmp),Hero.abilities.ilike(tmp))
      ok1 = or_(TopPlayer.top_player_name.ilike(tmp),TopPlayer.skill_rank.ilike(tmp),TopPlayer.tier.ilike(tmp))
      ok2 = or_(Achievement.achievement_name.ilike(tmp),Achievement.description.ilike(tmp),Achievement.reward_name.ilike(tmp),Achievement.reward_type.ilike(tmp),Achievement.reward_quality.ilike(tmp))
      ok3 = or_(Event.event_name.ilike(tmp),Event.start_date.ilike(tmp),Event.end_date.ilike(tmp))
      ok4 = or_(Skin.skin_name.ilike(tmp),Skin.quality.ilike(tmp))
      ok5 = or_(Item.item_name.ilike(tmp),Item.item_type.ilike(tmp))
      if initial == True:
        hero_query = ok
        player_query = ok1
        achievement_query = ok2
        event_query = ok3
        skin_query = ok4
        item_query = ok5
      else:
        hero_query = or_(hero_query,ok)
        player_query = or_(player_query, ok1)
        achievement_query = or_(achievement_query,ok2)
        event_query = or_(event_query,ok3)
        skin_query = or_(skin_query, ok4)
        item_query = or_(item_query, ok5)
      initial = False

    # ok = or_(Hero.hero_name.ilike(filt),Hero.description.ilike(filt),Hero.role.ilike(filt),Hero.abilities.ilike(filt),Hero.ulti.ilike(filt))
    # ok2 = or_(ok,Hero.hero_name.ilike('%bas%'))
    hero_r = Hero.query.filter(hero_query)
    player_r = TopPlayer.query.filter(player_query)
    achievement_r = Achievement.query.filter(achievement_query)
    event_r = Event.query.filter(event_query)
    skin_r = Skin.query.filter(skin_query)
    item_r = Item.query.filter(item_query)
    

    search_hit = []
    pagination = None
    if(current_view == 'Hero'):
      pagination = hero_r.paginate(page = page, per_page = per_page)
      for h in hero_r:
        temp = ""
        for s in search_str.split(' '):
          if s.lower() in h.description.lower():
            temp= 'Description: ' + h.description
            break 
          elif s.lower() in h.abilities.lower():
            temp = 'Abilities: ' + h.abilities
            break
          elif s.lower() in h.role.lower():
            temp = 'Role: ' + h.role
            break
          elif s.lower() in h.hero_name.lower():
            temp = 'Name: ' + h.hero_name
            break 
        search_hit.append(temp)

    elif(current_view == 'Top Player'):
      pagination = player_r.paginate(page = page, per_page = per_page)
      for h in player_r:
        temp = ""
        for s in search_str.split(' '):
          if s.lower() in h.top_player_name.lower():
            temp=  'Nametag: ' + h.top_player_name 
          elif s.lower() in h.skill_rank.lower():
            temp =  'Skill: ' + h.abilities
          elif s.lower() in h.tier.lower():
            temp =  'Tier: ' + h.tier
        search_hit.append(temp)
    elif(current_view == 'Achievement'):
      pagination = achievement_r.paginate(page = page, per_page = per_page)
      for h in achievement_r:
        temp = ""
        for s in search_str.split(' '):
          if s.lower() in h.description.lower():
            temp= temp + 'Description: ' + h.description 
          elif s.lower() in h.reward_type.lower():
            temp = temp + 'Type: ' + h.reward_type
          elif s.lower() in h.achievement_name.lower():
            temp = temp + 'Name: ' + h.achievement_name
          elif s.lower() in h.reward_name.lower():
            temp = temp + 'Reward Name: ' + h.reward_name
          elif s.lower() in h.reward_quality.lower():
            temp =  'Reward Quality: ' + h.reward_quality
        search_hit.append(temp)
    elif(current_view == 'Event'):
      pagination = event_r.paginate(page = page, per_page = per_page)
      for h in event_r:
        temp = ""
        for s in search_str.split(' '):
          if s.lower() in h.event_name.lower():
            temp= temp + 'Name: ' + h.event_name 
          elif s.lower() in h.start_date.lower():
            temp = temp + 'Start: ' + h.start_date
          elif s.lower() in h.end_date.lower():
            temp = temp + 'End: ' + h.end_date
        search_hit.append(temp)
    elif(current_view == 'Skin'):
      pagination = skin_r.paginate(page = page, per_page = per_page)
      for h in skin_r:
        temp = ""
        for s in search_str.split(' '):
          if s.lower() in h.skin_name.lower():
            temp= temp + 'Name: ' + h.skin_name
          elif s.lower() in h.quality.lower():
            temp = temp + 'Type: ' + h.quality
        search_hit.append(temp)
    elif(current_view == 'Item'):
      pagination = item_r.paginate(page = page, per_page = per_page)
      for h in item_r:
        temp = ""
        for s in search_str.split(' '):
          if s.lower() in h.item_name.lower():
            temp= temp + 'Description: ' + h.item_name 
          elif s.lower() in h.item_type.lower():
            temp = temp + 'Type: ' + h.item_type
        search_hit.append(temp)

    s = []
    for se in search_hit:
      tmp = []
      for w in se.lower().split(' '):
        a = 1
        for st in search_str.lower().split(' '):
          if ':' in w:
            break
          if st in w:
            ind = w.find(st)
            tmp1 = [0,w[0:ind]]
            tmp.append(tmp1)
            tmp2 = [1,w[ind:ind+len(st)]]
            tmp.append(tmp2)
            tmp3 = [0,w[ind+len(st):]]
            tmp.append(tmp3)
            a = 0
            break
        if a == 1:
          tmp1 = [0,w]
          tmp.append(tmp1)
      s.append(tmp)


    set(hero_r)
    set(player_r)
    set(achievement_r)
    set(event_r)
    set(skin_r)
    set(item_r)
    hero_res = hero_r[per_page*(page-1) : per_page*page]
    player_res = player_r[per_page*(page-1) : per_page*page]
    achievement_res = achievement_r[per_page*(page-1) : per_page*page]
    event_res = event_r[per_page*(page-1) : per_page*page]
    skin_res = skin_r[per_page*(page-1) : per_page*page]
    item_res = item_r[per_page*(page-1) : per_page*page]

    return render_template('search.html', hero_res = hero_res, player_res = player_res, achievement_res = achievement_res, event_res = event_res, skin_res = skin_res, item_res = item_res, search_str = search_str, current_view = current_view, pagination = pagination, search_hit = s)
