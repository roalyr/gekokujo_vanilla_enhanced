from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END
  ("manhunters","Ronin",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_ronin,9,40)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_northern_warlord,5,5)]),
  ("seto_pirates","Seto Pirates",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_seto_pirate,4,58)]),
  ("kanto_rebels","Kanto Rebels",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_kanto_rebel,4,58)]),
  ("northern_raiders","Ezo Warriors",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_northern_raider,4,58)]),
  ("shinano_rebels","Shinano Rebels",icon_axeman|carries_goods(2),0,fac_shinano_rebels,bandit_personality,[(trp_shinano_rebel,4,52)]),
  ("woku_pirates","Woku Pirates",icon_axeman|carries_goods(2),0,fac_woku_pirates,bandit_personality,[(trp_woku_pirate,4,60)]),
  ("kinai_rebels","Kinai Rebels",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_kinai_rebel,5,50)]),
  
  #gekokujo 3.0 new bandit types
  ("monk_rebels","Monk Rebels",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_monk_rebel,5,50)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_hired_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_hired_guard,5,11)]),
  ("runaway_serfs","Runaway Peasants",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("shinano_rebels", "Peasant Rebels", icon_peasant,0,fac_shinano_rebels,bandit_personality,[(trp_shinano_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_hired_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_hired_guard,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_uesugi_villager,7,14),(trp_gekokujo_uesugi_jizamurai,3,6)]), #10-20
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_uesugi_trained_spearman,3,5),(trp_gekokujo_uesugi_trained_skirmisher,2,4),(trp_gekokujo_uesugi_veteran_retainer,1,3),(trp_gekokujo_uesugi_mounted_retainer,1,2)]), #7-14
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_uesugi_veteran_skirmisher,3,6),(trp_gekokujo_uesugi_officer,2,4)]), #5-10

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_date_villager,7,14),(trp_gekokujo_date_jizamurai,3,6)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_date_trained_spearman,3,5),(trp_gekokujo_date_trained_skirmisher,2,4),(trp_gekokujo_date_veteran_retainer,1,3),(trp_gekokujo_date_mounted_retainer,1,2)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_date_veteran_spearman,3,6),(trp_gekokujo_date_officer,2,4)]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_oda_villager,7,14),(trp_gekokujo_oda_jizamurai,3,6)]),
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_oda_trained_spearman,3,5),(trp_gekokujo_oda_trained_skirmisher,2,4),(trp_gekokujo_oda_mounted_retainer,1,3),(trp_gekokujo_oda_samurai_gunner,1,2)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_oda_veteran_skirmisher,3,6),(trp_gekokujo_oda_mounted_officer,2,4)]),

  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_mori_villager,7,14),(trp_gekokujo_mori_jizamurai,3,6)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_mori_trained_spearman,3,5),(trp_gekokujo_mori_trained_skirmisher,2,4),(trp_gekokujo_mori_veteran_retainer,1,3),(trp_gekokujo_mori_mounted_retainer,1,2)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_mori_veteran_spearman,3,6),(trp_gekokujo_mori_officer,2,4)]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_takeda_villager,7,14),(trp_gekokujo_takeda_jizamurai,3,6)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_takeda_trained_spearman,3,5),(trp_gekokujo_takeda_trained_skirmisher,2,4),(trp_gekokujo_takeda_mounted_retainer,1,3),(trp_gekokujo_takeda_samurai_archer,1,2)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_takeda_veteran_spearman,3,6),(trp_gekokujo_takeda_mounted_officer,2,4)]),

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_tokugawa_villager,7,14),(trp_gekokujo_tokugawa_jizamurai,3,6)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_tokugawa_trained_spearman,3,5),(trp_gekokujo_tokugawa_trained_skirmisher,2,4),(trp_gekokujo_tokugawa_veteran_retainer,1,3),(trp_gekokujo_tokugawa_samurai_gunner,1,2)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_tokugawa_veteran_skirmisher,3,6),(trp_gekokujo_tokugawa_officer,2,4)]),

  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_miyoshi_villager,7,14),(trp_gekokujo_miyoshi_jizamurai,3,6)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_miyoshi_trained_spearman,3,5),(trp_gekokujo_miyoshi_trained_skirmisher,2,4),(trp_gekokujo_miyoshi_veteran_retainer,1,3),(trp_gekokujo_miyoshi_samurai_gunner,1,2)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_miyoshi_veteran_spearman,3,6),(trp_gekokujo_miyoshi_officer,2,4)]),

  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_amako_villager,7,14),(trp_gekokujo_amako_jizamurai,3,6)]),
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_amako_trained_spearman,3,5),(trp_gekokujo_amako_trained_skirmisher,2,4),(trp_gekokujo_amako_veteran_retainer,1,3),(trp_gekokujo_amako_mounted_retainer,1,2)]),
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_amako_veteran_skirmisher,3,6),(trp_gekokujo_amako_officer,2,4)]),

  ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_otomo_villager,7,14),(trp_gekokujo_otomo_jizamurai,3,6)]),
  ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_otomo_trained_spearman,3,5),(trp_gekokujo_otomo_trained_skirmisher,2,4),(trp_gekokujo_otomo_mounted_retainer,1,3),(trp_gekokujo_otomo_samurai_archer,1,2)]),
  ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_otomo_veteran_spearman,3,6),(trp_gekokujo_otomo_mounted_officer,2,4)]),

  ("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_nanbu_villager,7,14),(trp_gekokujo_nanbu_jizamurai,3,6)]),
  ("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_nanbu_trained_spearman,3,5),(trp_gekokujo_nanbu_trained_skirmisher,2,4),(trp_gekokujo_nanbu_mounted_retainer,1,3),(trp_gekokujo_nanbu_samurai_gunner,1,2)]),
  ("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_nanbu_veteran_skirmisher,3,6),(trp_gekokujo_nanbu_mounted_officer,2,4)]),

  ("kingdom_11_reinforcements_a", "{!}kingdom_11_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_asakura_villager,7,14),(trp_gekokujo_asakura_jizamurai,3,6)]),
  ("kingdom_11_reinforcements_b", "{!}kingdom_11_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_asakura_trained_spearman,3,5),(trp_gekokujo_asakura_trained_skirmisher,2,4),(trp_gekokujo_asakura_mounted_retainer,1,3),(trp_gekokujo_asakura_samurai_gunner,1,2)]),
  ("kingdom_11_reinforcements_c", "{!}kingdom_11_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_asakura_veteran_spearman,3,6),(trp_gekokujo_asakura_officer,2,4)]),

  ("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_chosokabe_villager,7,14),(trp_gekokujo_chosokabe_jizamurai,3,6)]),
  ("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_chosokabe_trained_spearman,3,5),(trp_gekokujo_chosokabe_trained_skirmisher,2,4),(trp_gekokujo_chosokabe_veteran_retainer,1,3),(trp_gekokujo_chosokabe_samurai_archer,1,2)]),
  ("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_chosokabe_veteran_skirmisher,3,6),(trp_gekokujo_chosokabe_officer,2,4)]),

  ("kingdom_13_reinforcements_a", "{!}kingdom_13_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_hojo_villager,7,14),(trp_gekokujo_hojo_jizamurai,3,6)]),
  ("kingdom_13_reinforcements_b", "{!}kingdom_13_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_hojo_trained_spearman,3,5),(trp_gekokujo_hojo_trained_skirmisher,2,4),(trp_gekokujo_hojo_mounted_retainer,1,3),(trp_gekokujo_hojo_samurai_archer,1,2)]),
  ("kingdom_13_reinforcements_c", "{!}kingdom_13_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_hojo_veteran_spearman,3,6),(trp_gekokujo_hojo_mounted_officer,2,4)]),

  ("kingdom_14_reinforcements_a", "{!}kingdom_14_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_mogami_villager,7,14),(trp_gekokujo_mogami_jizamurai,3,6)]),
  ("kingdom_14_reinforcements_b", "{!}kingdom_14_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_mogami_trained_spearman,3,5),(trp_gekokujo_mogami_trained_skirmisher,2,4),(trp_gekokujo_mogami_mounted_retainer,1,3),(trp_gekokujo_mogami_samurai_gunner,1,2)]),
  ("kingdom_14_reinforcements_c", "{!}kingdom_14_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_mogami_veteran_skirmisher,3,6),(trp_gekokujo_mogami_mounted_officer,2,4)]),

  ("kingdom_15_reinforcements_a", "{!}kingdom_15_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_shimazu_villager,7,14),(trp_gekokujo_shimazu_jizamurai,3,6)]),
  ("kingdom_15_reinforcements_b", "{!}kingdom_15_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_shimazu_trained_spearman,3,5),(trp_gekokujo_shimazu_trained_skirmisher,2,4),(trp_gekokujo_shimazu_veteran_retainer,1,3),(trp_gekokujo_shimazu_samurai_gunner,1,2)]),
  ("kingdom_15_reinforcements_c", "{!}kingdom_15_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_shimazu_veteran_spearman,3,6),(trp_gekokujo_shimazu_officer,2,4)]),

  ("kingdom_16_reinforcements_a", "{!}kingdom_16_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_ryuzoji_villager,7,14),(trp_gekokujo_ryuzoji_jizamurai,3,6)]),
  ("kingdom_16_reinforcements_b", "{!}kingdom_16_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_ryuzoji_trained_spearman,3,5),(trp_gekokujo_ryuzoji_trained_skirmisher,2,4),(trp_gekokujo_ryuzoji_veteran_retainer,1,3),(trp_gekokujo_ryuzoji_samurai_archer,1,2)]),
  ("kingdom_16_reinforcements_c", "{!}kingdom_16_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_ryuzoji_veteran_skirmisher,3,6),(trp_gekokujo_ryuzoji_officer,2,4)]),

  ("kingdom_17_reinforcements_a", "{!}kingdom_17_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_satake_villager,7,14),(trp_gekokujo_satake_jizamurai,3,6)]),
  ("kingdom_17_reinforcements_b", "{!}kingdom_17_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_satake_trained_spearman,3,5),(trp_gekokujo_satake_trained_skirmisher,2,4),(trp_gekokujo_satake_samurai_gunner,1,3),(trp_gekokujo_satake_samurai_archer,1,2)]),
  ("kingdom_17_reinforcements_c", "{!}kingdom_17_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_satake_veteran_spearman,3,6),(trp_gekokujo_satake_master_gunner,2,4)]),

  ("kingdom_18_reinforcements_a", "{!}kingdom_18_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_satomi_villager,7,14),(trp_gekokujo_satomi_jizamurai,3,6)]),
  ("kingdom_18_reinforcements_b", "{!}kingdom_18_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_satomi_trained_spearman,3,5),(trp_gekokujo_satomi_trained_skirmisher,2,4),(trp_gekokujo_satomi_veteran_retainer,1,3),(trp_gekokujo_satomi_mounted_retainer,1,2)]),
  ("kingdom_18_reinforcements_c", "{!}kingdom_18_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_satomi_veteran_skirmisher,3,6),(trp_gekokujo_satomi_officer,2,4)]),
  
  ("kingdom_19_reinforcements_a", "{!}kingdom_19_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_ukita_villager,7,14),(trp_gekokujo_ukita_jizamurai,3,6)]),
  ("kingdom_19_reinforcements_b", "{!}kingdom_19_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_ukita_trained_spearman,3,5),(trp_gekokujo_ukita_trained_skirmisher,2,4),(trp_gekokujo_ukita_veteran_retainer,1,3),(trp_gekokujo_ukita_samurai_gunner,1,2)]),
  ("kingdom_19_reinforcements_c", "{!}kingdom_19_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_ukita_veteran_spearman,3,6),(trp_gekokujo_ukita_officer,2,4)]),

  ("kingdom_20_reinforcements_a", "{!}kingdom_20_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_ikko_villager,6,12),(trp_gekokujo_ikko_monk,3,5),(trp_gekokujo_ikko_jizamurai,1,3)]),
  ("kingdom_20_reinforcements_b", "{!}kingdom_20_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_ikko_trained_spearman,1,3),(trp_gekokujo_ikko_trained_skirmisher,0,1),(trp_gekokujo_ikko_veteran_retainer,1,2),(trp_gekokujo_ikko_samurai_archer,0,1),(trp_gekokujo_ikko_yari_monk,3,4),(trp_gekokujo_ikko_marksman_monk,2,3)]),
  ("kingdom_20_reinforcements_c", "{!}kingdom_20_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_ikko_veteran_spearman,1,2),(trp_gekokujo_ikko_officer,1,3),(trp_gekokujo_ikko_elite_naginata_monk,3,5)]),

  #gekokujo 3.0 get rid of player culture start
  ##geokokujo player reinforcements
  #("kingdom_player_reinforcements_a", "{!}kingdom_player_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gekokujo_player_villager,5,10),(trp_gekokujo_player_jizamurai,2,4)]),
  #("kingdom_player_reinforcements_b", "{!}kingdom_player_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gekokujo_player_spearman,2,4),(trp_gekokujo_player_archer,1,2),(trp_gekokujo_player_retainer,1,2),(trp_gekokujo_player_skirmisher,1,2)]),
  #("kingdom_player_reinforcements_c", "{!}kingdom_player_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gekokujo_player_veteran_archer,2,3),(trp_gekokujo_player_mounted_officer,1,2)]),
  #gekokujo 3.0 get rid of player culture end
  
  ("seto_pirate_lair" ,"Pirate Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_seto_pirate,15,58)]),
  ("kanto_rebel_lair","Rebel Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_kanto_rebel,15,58)]),
  ("northern_raider_lair" ,"Raider Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_northern_raider,15,58)]),
  ("shinano_rebel_lair" ,"Rebel Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_shinano_rebel,15,58)]),
  ("woku_pirate_lair" ,"Pirate Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_woku_pirate,15,58)]),
  ("kinai_rebel_lair","Rebel Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_kinai_rebel,15,50)]),
  ("looter_lair","Kidnapper's Mansion",icon_mansion|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_generic_ashigaru,15,25)]),
  
  #gekokujo 3.0 new bandit types
  ("monk_rebel_lair","Rebel Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_monk_rebel,15,50)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_kinai_rebel,15,50)]),

  ("leaded_looters","Samurai Travelling Party",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_generic_ashigaru,3,3)]),

   ##diplomacy begin
  ("dplmc_spouse","Your Spouse",icon_woman|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_hired_guard,5,25)]),
#recruiter kit begin
   ("dplmc_recruiter","Recruiter",icon_gray_knight|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end
   
   # #gekokujo 3.0 zaitenko's reinforcement script
   # ("reinforcements","Reinforcements",icon_gray_knight|pf_show_faction,0,fac_commoners,soldier_personality,[]),
]
# modmerger_start version=201 type=2
try:
    component_name = "party_templates"
    var_set = { "party_templates" : party_templates }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
