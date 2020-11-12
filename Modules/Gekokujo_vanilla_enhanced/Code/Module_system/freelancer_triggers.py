# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

from header_common import *
from header_operations import *
from header_triggers import *

from module_constants import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################


triggers = [
#+freelancer start

#  CHECKS IF "$enlisted_party" IS DEFEATED

    (0.0, 0, 0, [
        (this_or_next|eq, "$freelancer_state", 2), #gekokujo 3.0 freelancer vacation fix -- let's piggyback on the defeat trigger
        (eq, "$freelancer_state", 1),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),
    ],
    [
		#gekokujo 3.0 remove old defeat consequences start
        #(assign, "$freelancer_state", 0),
        #(call_script, "script_freelancer_detach_party"),
		
		##to prevent companions from being lost forever
		#(call_script, "script_party_restore"), 
		#(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        #(try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
		#	(party_stack_get_troop_id, ":return_troop", "p_main_party", ":cur_stack"),
		#	(neg|troop_is_hero, ":return_troop"),
		#	(party_stack_get_size, ":stack_size", "p_main_party", ":cur_stack"),
		#	(party_remove_members, "p_main_party", ":return_troop", ":stack_size"),
		#(try_end),

        ##removes faction relation given at enlist
		#(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        #(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
        #    (neq, ":commander_faction", ":cur_faction"),
		#	(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
        #    (call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
        #(try_end),
		
		##gekokujo changes
		##(troop_set_slot, "trp_player", slot_troop_banner_scene_prop, 0), #get rid of lord's banner (this is from 2.0)
		#(troop_set_slot, "trp_player", slot_troop_banner_scene_prop, "$freelancer_original_banner"), #get rid of lord's banner (this is the 3.0 version)
		
		#(display_message, "@With your commander's defeat, you have been released from service."), #should probably be a notification menu as well
		#(call_script, "script_end_quest", "qst_freelancer_enlisted"),
		#gekokujo 3.0 remove old defeat consequences end
		
		(try_begin),
			#gekokujo 3.0 freelancer vacation fix start
			#lets kick you out of the army if you're on vacation when your lord is beaten
			#you shouldn't be rewarded if you weren't fighting for him in the end
			(eq, "$freelancer_state", 2),
			(troop_set_slot, "trp_player", slot_troop_banner_scene_prop, "$freelancer_original_banner"),
			(display_message, "@With your commander's defeat, you have been released from service."),
			(call_script, "script_end_quest", "qst_freelancer_vacation"),
			#gekokujo 3.0 freelancer vacation fix end
		(else_try),
			(eq, "$freelancer_state", 1),
			#gekokujo 3.0 freelancer rejoin quest start
			#getting defeated is now like being forced to take leave
			#you have a chance to return to your lord and continue your service (with a reward of xp, honor, and renown, as well as a relations boost with your lord)
		
			(troop_set_slot, "trp_player", slot_troop_current_mission, plyr_mission_vacation), ###move to quests, not missions
			(troop_set_slot, "trp_player", slot_troop_days_on_mission, 14),
	
			#removes faction relation given at enlist
			(store_troop_faction, ":commander_faction", "$enlisted_lord"),
			(try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
				(neq, ":commander_faction", ":cur_faction"),
				(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
				(call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
			(try_end),

			(assign, "$freelancer_state", 3), #new state: scattered after defeat
			(call_script, "script_freelancer_detach_party"),
			(rest_for_hours, 0,0,0),
			(display_message, "@With your lord's defeat, your army has been scattered to the winds!"), 	

			(str_store_troop_name_link, s13, "$enlisted_lord"),
			(str_store_faction_name_link, s14, ":commander_faction"),
			(quest_set_slot, "qst_freelancer_captured", slot_quest_target_party, "$enlisted_party"),
			(quest_set_slot, "qst_freelancer_captured", slot_quest_importance, 0),
			(quest_set_slot, "qst_freelancer_captured", slot_quest_xp_reward, 100),
			(quest_set_slot, "qst_freelancer_captured",	slot_quest_expiration_days, 14),
			(setup_quest_text, "qst_freelancer_captured"),
			(str_clear, s2), #description. necessary?
			(call_script, "script_start_quest", "qst_freelancer_captured", "$enlisted_lord"),		
		
			(call_script, "script_freelancer_unequip_troop", "$player_cur_troop"), #your assigned items are lost, but you hopefully have a stash of loot
			(call_script, "script_add_notification_menu", "mnu_gekokujo_notification_defeated", 0, 0),
			#gekokujo 3.0 freelancer rejoin quest end

			(assign, "$g_encountered_party", "$g_enemy_party"),
			(jump_to_menu, "mnu_captivity_start_wilderness"),
		(try_end),
    ]),

 #  CHECKS IF "$enlisted_party" HAS JOINED BATTLE

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
		
		#collected nearby enemies->detach (post-battle)
		(try_begin), 
			(party_slot_ge, "p_freelancer_party_backup", slot_party_last_in_combat, 1),
			(map_free),
			(party_set_slot, "p_freelancer_party_backup", slot_party_last_in_combat, 0),
			(party_get_num_attached_parties, ":num_attached", "p_main_party"),
			(try_for_range_backwards, ":i", 0, ":num_attached"),
				(party_get_attached_party_with_rank, ":party", "p_main_party", ":i"),
				(party_detach, ":party"),
			(try_end),
		(try_end),
		
		#Is currently in battle
        (party_get_battle_opponent, ":commander_enemy", "$enlisted_party"),
        (gt, ":commander_enemy", 0),
		
		#checks that the player's health is high enough to join battle
        (store_troop_health, ":player_health", "trp_player"),
        (ge, ":player_health", 50),
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
    ]),

#  CHECKS IF PLAYER WON THE REVOLT

    (1.0, 0, 0, [
        (eq, "$freelancer_state", 0),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),

		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":commander_faction"),
        (lt, ":relation", 0),

        (party_get_attached_party_with_rank, ":attached_party", "p_main_party", 0),
        (eq, "p_temp_party_2", ":attached_party"),
    ],
    [
        (assign, "$enlisted_party", -1),
        (party_detach, "p_temp_party_2"),
        (store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
        (store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
        (store_add, ":chance", ":cur_persuasion", ":cur_leadership"),
        (val_add, ":chance", 10),
        (store_random_in_range, ":prisoner_state", 0, ":chance"),

        (try_begin),
            (is_between, ":prisoner_state", 0, 5),
            (call_script, "script_party_calculate_strength", "p_main_party", 0),
            (assign, ":main_strength", reg0),
            (call_script, "script_party_calculate_strength", "p_temp_party_2", 0),
            (assign, ":temp_strength", reg0),
            (ge, ":temp_strength", ":main_strength"),

            (party_get_num_prisoner_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_prisoner_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_prisoner_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_remove_prisoners, "p_temp_party_2", ":cur_troops", ":cur_size"),
            (try_end),

            (tutorial_box, "@The released prisoners were not be trusted and they are preparing to attack you!", "@Warning!"),
            (start_encounter, "p_temp_party_2"),
            (change_screen_map),
        (else_try),
            (is_between, ":prisoner_state", 5, 10),
            (tutorial_box, "@The released prisoners scattered as soon as the battle finished. You will not be seeing them again.", "@Notice!"),
            (party_clear, "p_temp_party_2"),
        (else_try),
            (tutorial_box, "@The released prisoners have remained loyal and will join your party", "@Notice!"),
            (party_get_num_companion_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_add_members, "p_main_party", ":cur_troops", ":cur_size"),
            (try_end),
            (party_clear, "p_temp_party_2"),
        (try_end),
    ]),

# IF LEFT MOUSE CLICK GO TO SOLDIER'S MENU

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (key_clicked, key_left_mouse_button),

        (set_fixed_point_multiplier, 1000),
        (mouse_get_position, pos0),
        (position_get_y, ":y", pos0),
        (gt, ":y", 50), #allows the camp, reports, quests, etc. buttons to be clicked
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
        (rest_for_hours_interactive, 9999, 4, 0),
    ]),

(24.0, 0, 0, [
        (eq, "$freelancer_state", 2),
    ],
    [
		(troop_get_slot, ":days_left", "trp_player", slot_troop_days_on_mission),
		(try_begin),
		  (gt, ":days_left", 5),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try),		  
		  (is_between, ":days_left", 1, 5),
		  (assign, reg0, ":days_left"),
		  (display_message, "@You have {reg0} days left till you are declared as a deserter!"),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try), #declare deserter
		  (eq, ":days_left", 0),
		  (call_script, "script_event_player_deserts"),
          (display_message, "@You have now been declared as a deserter!"),
		(try_end),  
    ]),

#gekokujo 3.0 choosing not to return to your lord after defeat start
(24.0, 0, 0, [
        (eq, "$freelancer_state", 3),
    ],
    [
		(troop_get_slot, ":days_left", "trp_player", slot_troop_days_on_mission),
		(try_begin),
		  (gt, ":days_left", 5),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try),		  
		  (is_between, ":days_left", 1, 5),
		  (assign, reg0, ":days_left"),
		  (display_message, "@You have {reg0} days left to return to your lord for a reward."),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try), #declare deserter
		  (eq, ":days_left", 0),
		  (call_script, "script_event_player_retires_defeat"),
          (display_message, "@You have decided not to return to your lord."),
		(try_end),  
    ]),
#gekokujo 3.0 choosing not to return to your lord after defeat end

#+freelancer end
]


# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "triggers"
        orig_triggers = var_set[var_name_1]
        orig_triggers.extend(triggers)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)