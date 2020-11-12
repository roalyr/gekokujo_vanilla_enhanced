from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
  ("bogus", "cant_find_this.ogg", 0, 0),
  ("captured", "capture.ogg", mtf_persist_until_finished, 0),
  ("defeated_by_neutral", "defeated_by_neutral.ogg",mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_2", "defeated_by_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("defeated_by_neutral_3", "defeated_by_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_killed, 0),
  ("empty_village", "empty_village.ogg", mtf_persist_until_finished, 0),
  ("encounter_hostile_nords", "encounter_hostile_nords.ogg", mtf_persist_until_finished|mtf_sit_encounter_hostile, 0),
  ("escape", "escape.ogg", mtf_persist_until_finished, 0),

  ("victorious_evil", "victorious_evil.ogg", mtf_persist_until_finished, 0),
  ("victorious_neutral_1", "victorious_neutral_1.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_2", "victorious_neutral_2.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_neutral_3", "victorious_neutral_3.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("victorious_swadian", "victorious_swadian.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir", "victorious_vaegir.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
  ("victorious_vaegir_2", "victorious_vaegir_2.ogg", mtf_persist_until_finished|mtf_culture_2|mtf_sit_victorious, 0),
    
  ("wedding", "wedding.ogg", mtf_persist_until_finished, 0),

  ("coronation", "coronation.ogg", mtf_persist_until_finished, 0),

  #gekokujo main menu
  #don't use this anymore, replace with 'ambushed 4'
  #("gekokujo_menu", "gekokujo_menu.mp3", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),
  ("gekokujo_menu", "kagurazaka_genjiro_menu.mp3", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),
  
  #------
  
  #gekokujo ambushed
  ("gekokujo_ambushed_1", "korogi_ambushed_1.mp3", mtf_module_track|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight),
  ("gekokujo_ambushed_2", "korogi_ambushed_2.mp3", mtf_module_track|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight),
  ("gekokujo_ambushed_3", "hmix_ambushed.mp3", mtf_module_track|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight),
  ("gekokujo_ambushed_4", "rathmor_ishiyama_honganji.ogg", mtf_module_track|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight),
  #ishiyama_honganji was meant for, well, the ikko ikki, but there are no culture flags past 6
  
  #gekokujo bandits
  ("gekokujo_bandit_1", "khamukkamu_bandit_1.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_travel, 0),
  ("gekokujo_bandit_2", "khamukkamu_bandit_2.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_travel, 0),
  
  #gekokujo siege battle
  ("gekokujo_siege_1", "khamukkamu_siege_1.mp3", mtf_module_track|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  ("gekokujo_siege_2", "khamukkamu_siege_2.mp3", mtf_module_track|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  ("gekokujo_siege_3", "khamukkamu_siege_3.mp3", mtf_module_track|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  ("gekokujo_siege_4", "shw_siege.mp3", mtf_module_track|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  
  #gekokujo field battle
  ("gekokujo_fight_1", "rathmor_battle_2.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("gekokujo_fight_2", "rathmor_battle_3.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("gekokujo_fight_3", "teohui_battle.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("gekokujo_fight_4", "shw_battle_1.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("gekokujo_fight_5", "shw_battle_2.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("gekokujo_fight_6", "shw_battle_3.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  ("gekokujo_fight_7", "hmix_battle.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
  
  ("gekokujo_fight_tokugawa", "rathmor_tokugawa.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_culture_6, 0),
  
  #------
  
  #gekokujo infiltration
  ("gekokujo_infiltration_1", "korogi_infiltration.mp3", mtf_module_track|mtf_sit_town_infiltrate, 0),
  ("gekokujo_infiltration_2", "hmix_infiltration.mp3", mtf_module_track|mtf_sit_town_infiltrate, 0),
  
  #------
  
  #gekokujo night travel
  ("gekokujo_night_1", "koya_takashi_night.mp3", mtf_module_track|mtf_sit_night, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  ("gekokujo_night_2", "kuusuke_night.mp3", mtf_module_track|mtf_sit_night, mtf_sit_town|mtf_sit_tavern|mtf_sit_travel),
  
  #gekokujo day travel
  ("gekokujo_travel_1", "rathmor_travel_1.ogg", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("gekokujo_travel_2", "rathmor_travel_2.ogg", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("gekokujo_travel_3", "rathmor_travel_3.mp3", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("gekokujo_travel_4", "ilodolly_travel.mp3", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  ("gekokujo_travel_5", "hmix_travel.mp3", mtf_module_track|mtf_sit_travel, mtf_sit_town|mtf_sit_night|mtf_sit_tavern),
  
  #gekokujo towns
  ("gekokujo_town_1", "khamukkamu_town_1.mp3", mtf_module_track|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("gekokujo_town_2", "tam_town.mp3", mtf_module_track|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("gekokujo_town_3", "ug_town.mp3", mtf_module_track|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("gekokujo_town_4", "kuusuke_town.mp3", mtf_module_track|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("gekokujo_town_5", "shw_town_1.mp3", mtf_module_track|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("gekokujo_town_6", "shw_town_2.mp3", mtf_module_track|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("gekokujo_town_7", "shw_town_3.mp3", mtf_module_track|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  ("gekokujo_town_8", "hmix_town.mp3", mtf_module_track|mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
  
  #------
  
  #gekokujo tournaments
  ("gekokujo_arena", "alaki_arena.mp3", mtf_module_track|mtf_sit_arena, 0),
  
  #gekokujo taverns/feasts
  ("gekokujo_tavern_1", "moetic_justice_tavern.mp3", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0),
  ("gekokujo_tavern_2", "rauyo_tsuyoshi_tavern_1.mp3", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0),
  ("gekokujo_tavern_3", "rauyo_tsuyoshi_tavern_2.mp3", mtf_module_track|mtf_sit_tavern|mtf_sit_feast, 0),

  
]
# modmerger_start version=201 type=4
try:
    component_name = "music"
    var_set = { "tracks":tracks, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
