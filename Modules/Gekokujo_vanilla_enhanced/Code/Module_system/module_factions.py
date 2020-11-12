from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.05),("woku_pirates", -0.02),("shinano_rebels", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),
  ("culture_7",  "{!}culture_7", 0, 0.9, [], []),
  ("culture_8",  "{!}culture_8", 0, 0.9, [], []),
  ("culture_9",  "{!}culture_9", 0, 0.9, [], []),
  ("culture_10",  "{!}culture_10", 0, 0.9, [], []),
  ("culture_11",  "{!}culture_11", 0, 0.9, [], []),
  ("culture_12",  "{!}culture_12", 0, 0.9, [], []),
  ("culture_13",  "{!}culture_13", 0, 0.9, [], []),
  ("culture_14",  "{!}culture_14", 0, 0.9, [], []),
  ("culture_15",  "{!}culture_15", 0, 0.9, [], []),
  ("culture_16",  "{!}culture_16", 0, 0.9, [], []),
  ("culture_17",  "{!}culture_17", 0, 0.9, [], []),
  ("culture_18",  "{!}culture_18", 0, 0.9, [], []),
  ("culture_19",  "{!}culture_19", 0, 0.9, [], []),
  ("culture_20",  "{!}culture_20", 0, 0.9, [], []),
  ("culture_player",  "{!}culture_player", 0, 0.9, [], []),

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  ("kingdom_1",  "Uesugi Clan",		0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xff9900),
  ("kingdom_2",  "Date Clan",		0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x6599ff),
  ("kingdom_3",  "Oda Clan",		0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x631d77),
  ("kingdom_4",  "Mori Clan",		0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x028482),
  ("kingdom_5",  "Takeda Clan",  	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x005502),
  ("kingdom_6",  "Tokugawa Clan",  	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xffde00),
  ("kingdom_7",  "Miyoshi Clan",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xff3333),
  ("kingdom_8",  "Amako Clan",		0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x87dc00),
  ("kingdom_9",  "Otomo Clan",		0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x7c821e),
  ("kingdom_10",  "Nanbu Clan",		0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xa0a0a0), #from 0x808080
  ("kingdom_11",  "Asakura Clan",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x7a4012),
  ("kingdom_12",  "Chosokabe Clan",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x7a3e48),
  ("kingdom_13",  "Hojo Clan",		0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x93e2d5),
  ("kingdom_14",  "Mogami Clan",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xc3d938),
  ("kingdom_15",  "Shimazu Clan",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x800000),
  ("kingdom_16",  "Ryuzoji Clan",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x505050), #from 0x222222
  ("kingdom_17",  "Satake Clan",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xd8b98b),
  ("kingdom_18",  "Satomi Clan",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xc186c1),
  ("kingdom_19",  "Ukita Clan",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0x334db3), #from 0x000066
  ("kingdom_20",  "Ikko Ikki",	0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xf0f0f0), #from 0xeeeeee

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("shinano_rebels", -0.1),("deserters", -0.02),("woku_pirates", -0.05),("shinano_rebels", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("woku_pirates","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("shinano_rebel","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("shinano_rebels","{!}Shinano Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
]

##diplomacy start+ Define these for convenience
dplmc_factions_begin = 1 #As mentioned in the notes above, this is hardcoded and shouldn't be altered.  Deliberately excludes "no faction".
dplmc_non_generic_factions_begin = [x[0] for x in enumerate(factions) if x[1][0] == "merchants"][0] + 1
dplmc_factions_end   = len(factions)
##diplomacy end+

# modmerger_start version=201 type=4
try:
    component_name = "factions"
    var_set = { "factions":factions,"default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
