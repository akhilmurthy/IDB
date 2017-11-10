//Hero General

var data = JSON.parse(responseBody);
tests["verify hero_name"] = data[17].hero_name === "Tracer";

var data = JSON.parse(responseBody);
tests["verify hero_id"] = data[17].hero_id === 18;

var data = JSON.parse(responseBody);
tests["verify role"] = data[17].role === "offense";

//Hero Specific


var data = JSON.parse(responseBody);
tests["verify hero_name"] = data.hero_name === "Bastion";

var data = JSON.parse(responseBody);
tests["verify hero_id"] = data.hero_id === 2;

var data = JSON.parse(responseBody);
tests["verify role"] = data.role === "defense";




//TopPlayers Specific (7)

var data = JSON.parse(responseBody);
tests["verify player_name"] = data.top_player_name === "Josiah-11900";

var data = JSON.parse(responseBody);
tests["verify player_id"] = data.top_player_id === 7;

var data = JSON.parse(responseBody);
tests["verify player level"] = data.level === 591;

//TopPlayer General

var data = JSON.parse(responseBody);
tests["verify player_name"] = data[0].top_player_name === "Rexarthur-1739";

var data = JSON.parse(responseBody);
tests["verify player_id"] = data[0].top_player_id === 1;

var data = JSON.parse(responseBody);
tests["verify player level"] = data[0].level === 777;






//Achievements Specific (7)

var data = JSON.parse(responseBody);
tests["verify ach_name"] = data.achievement_name === "Slice and Dice";

var data = JSON.parse(responseBody);
tests["verify ach_id"] = data.achievement_id === 7;

var data = JSON.parse(responseBody);
tests["verify reward_name"] = data.reward_name === "Cute";

//TopPlayer General

var data = JSON.parse(responseBody);
tests["verify ach_name"] = data[0].achievement_name === "Level 10";

var data = JSON.parse(responseBody);
tests["verify ach_id"] = data[0].achievement_id === 1;

var data = JSON.parse(responseBody);
tests["verify reward_name"] = data[0].reward_name === "Forge Onward";


//Events Specific (2)

var data = JSON.parse(responseBody);
tests["verify event_name"] = data.event_name === "Halloween Terror";

var data = JSON.parse(responseBody);
tests["verify event_id"] = data.event_id === 2;

//Events General

var data = JSON.parse(responseBody);
tests["verify event_name"] = data[0].event_name === "Summer Games 2016";

var data = JSON.parse(responseBody);
tests["verify event_id"] = data[0].event_id === 1;



//Skins Specific (1224)

var data = JSON.parse(responseBody);
tests["verify skin_name"] = data.skins_name === "Citrine";

var data = JSON.parse(responseBody);
tests["verify skin_id"] = data.skins_id === 1224;

var data = JSON.parse(responseBody);
tests["verify skin_quality"] = data.quality === "rare";

//Skins General

var data = JSON.parse(responseBody);
tests["verify skin_name"] = data[0].skins_name === "Classic";

var data = JSON.parse(responseBody);
tests["verify skin_id"] = data[0].skins_id === 1223;

var data = JSON.parse(responseBody);
tests["verify skin_quality"] = data[0].quality === "common";




//Item Specific (6)

var data = JSON.parse(responseBody);
tests["verify item_name"] = data.item_name === "Dance";

var data = JSON.parse(responseBody);
tests["verify item_id"] = data.item_id === 6;

var data = JSON.parse(responseBody);
tests["verify item_type"] = data.item_type === "spray";

//Item General

var data = JSON.parse(responseBody);
tests["verify item_name"] = data[0].item_name === "Logo";

var data = JSON.parse(responseBody);
tests["verify item_id"] = data[0].item_id === 1;

var data = JSON.parse(responseBody);
tests["verify item_type"] = data[0].item_type === "spray";
