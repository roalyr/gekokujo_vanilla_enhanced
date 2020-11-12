from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(110, -130),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(120,-120),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(120,-120),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120,-120),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(209,242),[]),

  ("town_1","Edo", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116, -134.5),[],195),
  ("town_2","Mito", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(152, -98),[],90),
  ("town_3","Choshi", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160, -130),[],120),
  ("town_4","Kyoto", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82, -171),[],240),
  ("town_5","Sakai", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104, -195),[],60),
  ("town_6","Tsu", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42, -184),[],75),
  ("town_7","Himeji", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132, -177.5),[],165),
  ("town_8","Kanazawa", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.2, -82.8),[],195),
  ("town_9","Kiyosu", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28, -167),[],285),
  ("town_10","Niigata", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.3, -26.3),[],30),
  ("town_11","Kofu", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.3, -134.5),[],240),
  ("town_12","Kasugayama", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.9, -59.2),[],255),
  ("town_13","Hiroshima", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-246, -204),[],165),
  ("town_14","Okayama", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-168, -188),[],12),
  ("town_15","Sendai", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(173.4, -12.4),[],75),
  ("town_16","Yonezawa", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130.1, -14),[],270),
  ("town_17","Kubota", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.2, 65.1),[],60),
  ("town_18","Hirosaki", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154.5, 118.5),[],360),
  ("town_19","Hakata", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-337, -233),[],255),
  ("town_20","Kagoshima", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-337.6, -338),[],225),
  ("town_21","Nagasaki", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-369, -279),[],270),
  ("town_22","Matsuyama", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.5, -230.9),[],240),
  
  #gekokujo new town ids
  ("town_23","Odawara", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89, -157),[],225),
  ("town_24","Nara", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.5, -187.4),[],120),
  ("town_25","Hamamatsu", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24, -179),[],120),
  ("town_26","Imahama", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72, -146),[],315),
  ("town_27","Yamaguchi", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-290.4, -212.8),[],225),
  ("town_28","Izumo", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-232, -150),[],30),
  ("town_29","Funai", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-276.5, -260.5),[],270),
  ("town_30","Kumamoto", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-336.2, -276.6),[],150),
  ("town_31","Kochi", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-192, -240),[],135),
  
  #gekokujo new towns, 2nd addition
  ("town_32","Tottori", icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.7, -138.4),[],255),

  
#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1","Kanayama Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98, -104.8),[],330),
  ("castle_2","Utsunomiya Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130, -77.8),[],285),
  ("castle_3","Takasaki Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(78.9, -99.3),[],105),
  ("castle_4","Sakasai Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117, -100.7),[],345),
  ("castle_5","Kururi Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(131.2, -155.8),[],135),
  ("castle_6","Sumoto Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128, -202),[],285),
  ("castle_7","Obama Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-99, -141.6),[],345),
  ("castle_8","Kannonji Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65, -168.1),[],0),
  ("castle_9","Tanabe Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100, -230.9),[],300),
  ("castle_10","Ichijodani Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58, -123),[],105),
  ("castle_11","Sasayama Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.4, -171),[],165),
  ("castle_12","Tamaru Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32, -197),[],135),
  ("castle_13","Yoshida Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1.8, -179.5),[],150),
  ("castle_14","Toyama Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11, -85),[],75),
  ("castle_15","Sakado Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.7, -69.5),[],135),
  ("castle_16","Komaki Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26, -153),[],315),
  ("castle_17","Iida Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.3, -128),[],0),
  ("castle_18","Shibata Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.4, -8.9),[],120),
  ("castle_19","Kaizu Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.9, -96.8),[],300),
  ("castle_20","Takatenjin Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.1, -181.4),[],75),
  ("castle_21","Ueda Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39, -114),[],30),
  ("castle_22","Gifu Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33, -140),[],300),
  ("castle_23","Gassantoda Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-216.1, -152.4),[],120),
  ("castle_24","Yoshiwara Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61, -161),[],255),
  ("castle_25","Hamada Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-254.2, -172.3),[],345),
  ("castle_26","Hagi Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-294.3, -195.9),[],285),
  ("castle_27","Mihara Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214, -202.1),[],225),
  ("castle_28","Tsuyama Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155, -159.5),[],135),
  ("castle_29","Kushizaki Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-316, -214),[],360),
  ("castle_30","Hachinohe Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(197.9, 112.5),[],255),
  ("castle_31","Morioka Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(182.7, 69.2),[],255),
  ("castle_32","Ichinoseki Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(179.5, 33.3),[],135),
  ("castle_33","Yamagata Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.6, 12.7),[],45),
  ("castle_34","Shirakawa Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.6, -52),[],150),
  ("castle_35","Tsuruoka Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.9, 31.2),[],330),
  ("castle_36","Iwaki Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(181.5, -47.9),[],150),
  ("castle_37","Yokote Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.7, 51.8),[],180),
  ("castle_38","Hirado Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-372, -242.5),[],315),
  ("castle_39","Kokura Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-317, -224),[],75),
  ("castle_40","Nobeoka Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-283.6, -297.1),[],180),
  ("castle_41","Miyazaki Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-293.1, -317.8),[],300),
  ("castle_42","Aso Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-311, -277),[],60),
  ("castle_43","Sashiki Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-350, -296),[],15),
  ("castle_44","Yanagawa Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-340.6, -255.5),[],330),
  ("castle_45","Uwajima Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-240, -265),[],120),
  ("castle_46","Nakamura Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-220.8, -269.4),[],60),
  ("castle_47","Tokushima Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140, -219),[],180),
  ("castle_48","Takamatsu Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-166.9, -200),[],315),
  
  #gekokujo new castle ids
  ("castle_49","Kawagoe Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.3, -125),[],120),
  ("castle_50","Konodai Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.2, -132.2),[],90),
  ("castle_51","Akashi Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123, -186),[],225),
  ("castle_52","Fukuchiyama Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-121, -151),[],225),
  ("castle_53","Sunpu Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43, -166),[],300),
  ("castle_54","Okazaki Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10, -173),[],210),
  ("castle_55","Nagashino Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.5, -160),[],150),
  ("castle_56","Iwamura Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0, -145),[],0),
  ("castle_57","Takane Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27, -137),[],180),
  ("castle_58","Ashigara Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74, -149),[],360),
  ("castle_59","Matsukura Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16, -67),[],60),
  ("castle_60","Shobara Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195, -170),[],180),
  ("castle_61","Takahashi Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-190, -190),[],120),
  ("castle_62","Kurokawa Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115, -40),[],210),
  ("castle_63","Hitachi Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167, -73),[],135),
  ("castle_64","Kashima Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-363 , -257),[],285),
  ("castle_65","Hitoyoshi Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-327, -312),[],30),
  ("castle_66","Nakatsu Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-286, -242),[],240),
  ("castle_67","Muroto Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159, -250),[],60),
  ("castle_68","Kawanoe Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-186, -216),[],180),
  
  #gekokujo new castles, 2nd addition
  ("castle_69","Otari Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.5, -86.9),[],30),
  ("castle_70","Iiyama Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46, -85),[],240),
  ("castle_71","Iwakura Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160, -220),[],60),
  ("castle_72","Nagashima Fortress", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41, -170),[],180),
  
  #gekokujo new castles, 3rd addition
  ("castle_73","Katsuyama Castle", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138, 176),[],180),
  ("castle_74","Ishiyama Fortress", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.5, -188),[],60),
  ("castle_75","Jogu-ji Fortress", icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2, -167),[],30),

#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  ("village_1","Yamakita", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.5, -150),[],345),
  ("village_2","Ichikawa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(122.1, -131.3),[],120),
  ("village_3","Kiyose", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(111, -126),[],315),
  ("village_4","Kamakura", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101, -155),[],90),
  ("village_5","Miura", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.5, -159.5),[],150),
  ("village_6","Naka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(153.8, -93.2),[],300),
  ("village_7","Kasumigaura", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(142.5, -107.6),[],360),
  ("village_8","Katori", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(146.6, -126.8),[],195),
  ("village_9","Asahi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(153.8, -134.1),[],0),
  ("village_10","Kanayama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101, -107.8),[],300),
  ("village_11","Utsunomiya", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(125.8, -80.1),[],255),
  ("village_12","Maebashi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(81, -103.5),[],30),
  ("village_13","Sakasai", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(114.8, -98.5),[],0),
  ("village_14","Kimitsu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.1, -156.9),[],285),
  ("village_15","Ibaraki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.8, -178.3),[],135),
  ("village_16","Kamigyo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.5, -166),[],315),
  ("village_17","Kameoka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-88.8, -169),[],210),
  ("village_18","Kishiwada", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109, -201),[],90),
  ("village_19","Wakayama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.3, -218.3),[],315),
  ("village_20","Kobe", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112, -185),[],240),
  ("village_21","Misaki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-119, -208.5),[],90),
  ("village_22","Matsusaka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42, -194),[],180),
  ("village_23","Uji", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30, -201),[],0),
  ("village_24","Aioi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-140, -178),[],45),
  ("village_25","Kasai", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-128.9, -169.2),[],60),
  ("village_26","Sumoto", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129, -206),[],60),
  ("village_27","Obama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98, -139.4),[],0),
  ("village_28","Azuchi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.5, -165),[],195),
  ("village_29","Tanabe", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.1, -229.8),[],270),
  ("village_30","Kohoku", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63, -140.6),[],330),
  ("village_31","Sasayama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-115.3, -173.9),[],285),
  ("village_32","Kameyama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49, -174),[],285),
  ("village_33","Daishoji", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50, -96),[],315),
  ("village_34","Yoshizaki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.5, -102.5),[],30),
  ("village_35","Kahoku", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.2, -74.7),[],270),
  ("village_36","Miyukizuka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.5, -91.1),[],0),
  ("village_37","Kuwana", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36, -166),[],255),
  ("village_38","Chita", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23, -169.2),[],165),
  ("village_39","Arako", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31, -163),[],150),
  #gekokujo 3.0 make kasugayama larger and richer than niigata
  #("village_40","Uchino", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.2, -25.2),[],135),
  ("village_40","Yoita", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61, -59),[],135),
  ("village_41","Tsubame", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69, -40.3),[],195),
  ("village_42","Agano", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.3, -24.3),[],300),
  ("village_43","Hokuto", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.8, -128.9),[],90),
  ("village_44","Chuo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56, -140.3),[],360),
  ("village_45","Kashiwazaki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.3, -55.9),[],45),
  ("village_46","Myoko", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(37.9, -72.4),[],270),
  ("village_47","Toyohashi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.3, -177.4),[],0),
  ("village_48","Imizu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15, -80),[],15),
  ("village_49","Uedanosho", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(59.7, -66),[],195),
  ("village_50","Kitanosho", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63, -117),[],45),
  ("village_51","Iida", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.4, -134.1),[],285),
  ("village_52","Shibata", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.4, -11.9),[],315),
  ("village_53","Katsurao", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34, -99.7),[],225),
  ("village_54","Kakegawa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34, -178.4),[],330),
  ("village_55","Suwa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36, -118),[],105),
  ("village_56","Sekigahara", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45, -148),[],315),
  ("village_57","Iwakuni", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-257, -215),[],105),
  ("village_58","Akitakata", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-233.6, -181.5),[],135),
  ("village_59","Takehara", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231, -206),[],165),
  ("village_60","Kurashiki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-175.1, -189.6),[],195),
  ("village_61","Setouchi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155, -182.5),[],165),
  ("village_62","Kasaoka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-181.3, -191.7),[],195),
  ("village_63","Gassantoda", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213.1, -153.4),[],60),
  #("village_64","Tottori", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165.8, -141.5),[],255),
  ("village_64","Yoshiwara", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64, -163),[],255),
  ("village_65","Hamada", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-260.4, -174.3),[],105),
  ("village_66","Hagi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-291.2, -194.9),[],120),
  ("village_67","Mihara", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.2, -202.1),[],120),
  ("village_68","Tsuyama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-148, -159),[],315),
  ("village_69","Shimonseki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-316, -217),[],105),
  ("village_70","Iwanuma", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(174.3, -25),[],285),
  ("village_71","Matsushima", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(185.9, 5.5),[],120),
  ("village_72","Osaki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(172.3, 4.8),[],285),
  ("village_73","Fukushima", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(156, -25),[],300),
  ("village_74","Nagai", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120, -12),[],15),
  ("village_75","Nanyo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140, -8),[],90),
  #gekokujo 3.0 make yonezawa poorer, kofu richer
  #("village_76","Kaminoyama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.4, 2.7),[],135),
  ("village_76","Tsuru", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.5, -135),[],135),
  ("village_77","Katagami", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(128, 76),[],30),
  ("village_78","Noshiro", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(131, 96),[],165),
  ("village_79","Utou", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(161, 128),[],15),
  ("village_80","Hirakawa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.6, 133),[],120),
  ("village_81","Hachinohe", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(205.2, 113.4),[],150),
  ("village_82","Morioka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(182.7, 62),[],75),
  ("village_83","Ichinoseki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(180.4, 39.3),[],210),
  ("village_84","Yamagata", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150, 8),[],360),
  ("village_85","Shirakawa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.4, -55.1),[],180),
  ("village_86","Tsuruoka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(118, 31),[],180),
  ("village_87","Iwaki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(180.5, -53.1),[],255),
  ("village_88","Yokote", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(146.6, 46.7),[],0),
  ("village_89","Fukuoka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-334, -229),[],60),
  ("village_90","Itoshima", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-348, -237),[],75),
  ("village_91","Chikushino", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-333.4, -240.1),[],360),
  ("village_92","Ibusuki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-338.3, -355.7),[],60),
  ("village_93","Kirishima", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-326.1, -329.6),[],135),
  ("village_94","Kanoya", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-321, -353.6),[],195),
  ("village_95","Sasebo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-367.5, -267.9),[],90),
  ("village_96","Shimabara", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-353, -279),[],360),
  ("village_97","Hirado", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-373.5, -240),[],45),
  ("village_98","Kitakyushu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-313, -222),[],300),
  ("village_99","Nobeoka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-285.6, -300.1),[],330),
  ("village_100","Miyazaki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-296, -321),[],360),
  ("village_101","Aso", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-312, -282),[],165),
  ("village_102","Sashiki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-347.9, -294.1),[],120),
  ("village_103","Yanagawa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-344.7, -252.6),[],270),
  ("village_104","Saijo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206, -222),[],0),
  ("village_105","Toon", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230, -236),[],270),
  ("village_106","Gunchuu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212, -236),[],225),
  ("village_107","Uwajima", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-238, -267),[],15),
  ("village_108","Nakamura", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.8, -271.4),[],135),
  ("village_109","Anan", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137, -227),[],105),
  ("village_110","Takamatsu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.7, -202),[],0),
  
  #gekokujo new village ids
  ("village_111","Kawaguchi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117, -120),[],330),
  ("village_112","Shiki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.5, -121.5),[],270),
  ("village_113","Ikoma", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85, -189),[],165),
  ("village_114","Asuka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76, -196),[],135),
  ("village_115","Gojo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78, -202),[],300),
  ("village_116","Maisaka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19, -179),[],90),
  ("village_117","Kosai", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14, -177),[],345),
  ("village_118","Mikatagahara", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25, -173),[],345),
  ("village_119","Kunitomo", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69, -152),[],165),
  ("village_120","Nagakute", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21, -158),[],270),
  ("village_121","Ube", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-300, -219),[],60),
  ("village_122","Hofu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-285, -217),[],60),
  ("village_123","Tokuyama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-273, -222),[],75),
  ("village_124","Mihonoseki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-208, -136.3),[],45),
  #("village_125","Kurayoshi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180, -142),[],225),
  ("village_125","Yonago", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-204, -143),[],225),
  ("village_126","Unnan", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-228, -155),[],105),
  ("village_127","Usuki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-269, -257),[],360),
  ("village_128","Yufu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-285.3, -262.3),[],315),
  ("village_129","Taketa", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-289.2, -277.9),[],330),
  ("village_130","Tamana", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-341, -269),[],255),
  ("village_131","Yatsushiro", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-344, -287),[],225),
  ("village_132","Kikuchi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-326, -270),[],315),
  ("village_133","Nankoku", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-186, -239),[],45),
  ("village_134","Aki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-173, -244),[],135),
  ("village_135","Susaki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205, -252),[],120),
  ("village_136","Kawagoe", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.3, -126.5),[],165),
  ("village_137","Konodai", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130.7, -134.2),[],45),
  ("village_138","Akashi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120, -187),[],360),
  ("village_139","Fukuchiyama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123, -146),[],300),
  ("village_140","Sunpu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47, -167),[],330),
  ("village_141","Okazaki", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7, -174),[],195),
  ("village_142","Nagashino", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15, -157),[],15),
  ("village_143","Akechi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6, -149),[],255),
  ("village_144","Takane", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25, -144),[],135),
  ("village_145","Ashigara", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79, -147.5),[],30),
  ("village_146","Matsukura", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20, -65),[],15),
  ("village_147","Shobara", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202, -174),[],255),
  ("village_148","Takahashi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195, -193),[],255),
  ("village_149","Aizu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110, -37),[],150),
  ("village_150","Hitachi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(170, -69),[],180),
  ("village_151","Kashima", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-361, -255.5),[],300),
  ("village_152","Hitoyoshi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-330, -317),[],105),
  ("village_153","Nakatsu", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-293, -241),[],165),
  ("village_154","Muroto", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161, -248),[],315),
  ("village_155","Kawanoe", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-190, -217),[],315),
  
  #gekokujo new village, 2nd addition
  ("village_156","Mikata", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-145, -137),[],315),
  ("village_157","Kurayoshi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180, -142),[],165),
  ("village_158","Otari", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30, -92),[],105),
  ("village_159","Iiyama", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50, -80),[],300),
  ("village_160","Iwakura", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165, -221),[],180),
  ("village_161","Nagashima", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40, -167),[],150),
  
  #gekokujo new villages, 3rd addition
  ("village_162","Usukeshi", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(166, 174),[],150),
  ("village_163","Osaka", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.5, -189.5),[],150),
  ("village_164","Azukikaza", icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5, -165),[],150),

  #gekokujo 3.0 microfactions! start
  #gekokujo 3.0 forts
  ("fort_1","Sado",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48, -14.5),[],165),
  ("fort_2","Tsushima",icon_mansion|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-370, -210),[],75),
  ("fort_3","Kokawa-dera",icon_temple|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104, -215),[],225),
  ("fort_4","Mii-dera",icon_temple|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81, -161),[],300),
  ("fort_5","Niputay",icon_village_snow_a|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(218, 244),[],120),
  ("fort_6","Otasut",icon_village_snow_a|pf_is_static|pf_always_visible|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(280, 234),[],165),
  #gekokujo 3.0 microfactions! end
  
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(224, 341),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(324, 275),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132, 209),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(293, 229),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(356,245),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139, -119),[]), #Kanto

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81, -196),[], 100), #Kinai
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75, -60),[], 100), #Echigo
  ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(206, 32),[], 100), #Tohoku
  ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24, -50),[], 100), #Noto
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-298, -337),[], 100), #Kyushu


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(181.85, 42.95),[], -95),
  ("Bridge_2","{!}2",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(185.75, 14.25),[], 100),
  ("Bridge_3","{!}3",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(158.77, -126.94),[], 170),
  ("Bridge_4","{!}4",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.74, -101.6),[], -26),
  ("Bridge_5","{!}5",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.99, -130.38),[], 105),
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.22, -139.37),[], -51),
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.25, -160.9),[], -80),
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.69, -146.31),[], 23),
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.8, -139.72),[], -80),
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.12, -69.66),[], 48),
  ("Bridge_11","{!}11",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.57, -34.2),[], 104),
  ("Bridge_12","{!}12",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.6, -144.3),[], 40),
  ("Bridge_13","{!}13",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.22, -148.98),[], 54),
  ("Bridge_14","{!}14",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.55, -174.85),[], -12),
  ("Bridge_15","{!}15",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.63, -187.13),[], -9),
  ("Bridge_16","{!}16",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-250.65, -204.1),[], 106),
  ("Bridge_17","{!}17",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-344, -249.95),[], 14),
  ("Bridge_18","{!}18",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.3, -164.5),[], 92),
  ("Bridge_19","{!}19",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(128.4, -97.7),[], 85),
  ("Bridge_20","{!}20",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.9, 34),[], -12),
  ("Bridge_21","{!}21",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(147.9, 9.85),[], 81),
  ("Bridge_22","{!}22",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.7, -177.7),[], 58),
  ("Bridge_23","{!}23",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(134.92, 24.13),[], 144.5),
  ("Bridge_24","{!}24",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.39, -3.28),[], 51),
  ("Bridge_25","{!}25",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(213.41, 248.12),[], 17),
  ("Bridge_26","{!}26",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(227.13, 268.15),[], 16.5),
  ("Bridge_27","{!}27",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(279.93, 238.84),[], 173),
  ("Bridge_28","{!}28",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(296.57, 229.89),[], 146),
  ("Bridge_29","{!}29",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(300.29, 244.64),[], 32),
  ("Bridge_30","{!}30",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(236.63, 279.84),[], 36),
   
  ("Bridge_31","{!}31",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-150.78, -222.07),[],19),
  ("Bridge_32","{!}32",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-227.41, -235.3),[],136),
  ("Bridge_33","{!}33",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-335.27, -279.12),[],12),
  ("Bridge_34","{!}34",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-352.43, -320.01),[],176), 
  ("Bridge_35","{!}35",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-314.5, -327.05),[],88), 
  ("Bridge_36","{!}36",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-298.02, -319.25),[],215), 
  ("Bridge_37","{!}37",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-277.73, -265.14),[],79), 
  ("Bridge_38","{!}38",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-248.89, -170.96),[],20), 
  ("Bridge_39","{!}39",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-292.55, -213.38),[],93), 
  ("Bridge_40","{!}40",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155.61, 119.6),[],149), 
  ("Bridge_41","{!}41",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130, 94.74),[],146), 
  ("Bridge_42","{!}42",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.65, 67.69),[],156), 
  ("Bridge_43","{!}43",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(164.97, -15.02),[],161), 
  ("Bridge_44","{!}44",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.91, -28.06),[],148), 
  ("Bridge_45","{!}45",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154.15, -119.04),[],87), 

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(34, -114),[(trp_looter,15,0)]), #not enabled
  ("seto_pirate_spawn_point"  ,"Kyushu",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-215, -209),[(trp_looter,15,0)]),
  ("kanto_rebel_spawn_point"   ,"the Kanto",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(117, -110),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("shinano_rebel_spawn_point"  ,"Shinano",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(32, -95.9),[(trp_looter,15,0)]),
  ("woku_pirate_spawn_point","the Seto Inland Sea",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-361, -291),[(trp_looter,15,0)]),
  ("kinai_rebel_spawn_point"   ,"the Kinai",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-90, -186),[(trp_looter,15,0)]),
  #gekokujo 3.0 new bandit types -- enable sea_raider_spawn_point_2 as monk rebel spawn point
  ("monk_rebel_spawn_point"   ,"the Tokaido",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-7, -165),[(trp_looter,15,0)]),
  ("northern_raider_spawn_point"  ,"Ezo",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(130, 210),[(trp_looter,15,0)]),
  
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(120, -120),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(120, -120),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(120, -120),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(120, -120),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(120, -120),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(120, -120),[(trp_looter,15,0)]),
  ]
  
# modmerger_start version=201 type=2
try:
    component_name = "parties"
    var_set = { "parties" : parties }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
