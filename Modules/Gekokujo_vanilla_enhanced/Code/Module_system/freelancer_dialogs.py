# Freelancer (1.3) by Taragoth
# Released 11 July 2011
# Edits by Caba'drin 14 Dec 2011
# Mod-Merger'd by Windyplains, Monnikje and Caba'drin

# -*- coding: cp1254 -*-
from header_common import *
from header_dialogs import *
from header_operations import *
from module_constants import *



####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

#+freelancer start
lord_talk_addon = [
# dialog_ask_enlistment

    [anyone|plyr,"lord_talk", [
		#gekokujo 3.0 freelancer prison dialogue fix start
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"), #this shouldn't happen in prison
		(neg|eq, "$talk_context", tc_hero_freed), #this also shouldn't happen immediately after the prison break
		#gekokujo 3.0 freelancer prison dialogue fix end
		(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
		(store_mul, ":samurai_potential", "$g_talk_troop_effective_relation", 5),
		(val_add, ":samurai_potential", ":renown"),
		
		(eq, "$freelancer_state", 0),
		(ge, "$g_talk_troop_faction_relation", 0),
		#(neq, "$players_kingdom", "$g_talk_troop_faction"),
		(eq, "$players_kingdom", 0),
		(try_begin),
			(ge, ":samurai_potential", 75),
			(str_store_string, s7, "@a samurai"),
		(else_try),
			(str_store_string, s7, "@an ashigaru"),
		(try_end),
		],
	"My lord, please employ me in your army as {s7} retainer!", "lord_request_enlistment",[]],
	
	#gekokujo 3.0 monk enlistment start
    [anyone|plyr,"lord_talk", [
		#gekokujo 3.0 freelancer prison dialogue fix start
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"), #this shouldn't happen in prison
		(neg|eq, "$talk_context", tc_hero_freed), #this also shouldn't happen immediately after the prison break
		#gekokujo 3.0 freelancer prison dialogue fix end
		(eq, "$freelancer_state", 0),
		(ge, "$g_talk_troop_faction_relation", 0),
		(eq, "$g_talk_troop_faction", "fac_kingdom_20"),
		(eq, "$players_kingdom", 0),
		],
	"My lord, please allow me to accompany your army as a lay monk!", "lord_request_enlistment_monk",[]],
	#gekokujo 3.0 monk enlistment end
		
#	#gekokujo 3.0 early try with returning to service
#		[anyone|plyr,"lord_talk",[
#		(eq, "$g_talk_troop", "$enlisted_lord"),
#		(eq, "$freelancer_state", 3),
#		(ge, "$g_talk_troop_faction_relation", 0),
#		(neq, "$players_kingdom", "$g_talk_troop_faction"),
#		(eq, "$players_kingdom", 0),
#		],
#		"My lord, I have returned to you after our defeat in battle.", "return_from_defeat",[]],	
	
	#Gekokujo 3.0 transfer to samurai status
	[anyone|plyr,"lord_talk", [
		#gekokujo 3.0 freelancer prison dialogue fix start
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"), #this shouldn't happen in prison
		(neg|eq, "$talk_context", tc_hero_freed), #this also shouldn't happen immediately after the prison break
		#gekokujo 3.0 freelancer prison dialogue fix end
		(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
		(store_mul, ":samurai_potential", "$g_talk_troop_effective_relation", 5),
		(val_add, ":samurai_potential", ":renown"),
		
		(eq, "$g_talk_troop", "$enlisted_lord"),
		(neq, "$freelancer_state", 0),
		(ge, "$g_talk_troop_faction_relation", 0),
		(neq, "$players_kingdom", "$g_talk_troop_faction"),
		(eq, "$players_kingdom", 0),
		
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"), #this shouldn't happen in prison
		(neg|eq, "$talk_context", tc_hero_freed), #this also shouldn't happen immediately after the prison break
		
		(neg|is_between, "$player_cur_troop", samurai_troops_begin, samurai_troops_end),
		(ge, ":samurai_potential", 75), #player meets minimum requirements
		],
	"My lord, I humbly request a promotion to samurai as befitting my status.", "lord_request_promotion",[]],
	
	# dialog_advise_retirement
    [anyone|plyr,"lord_talk", [
		#gekokujo 3.0 freelancer prison dialogue fix start
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"), #this shouldn't happen in prison
		(neg|eq, "$talk_context", tc_hero_freed), #this also shouldn't happen immediately after the prison break
		#gekokujo 3.0 freelancer prison dialogue fix end
        (eq, "$g_talk_troop", "$enlisted_lord"),
		(neq, "$freelancer_state", 0),
        (ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
				
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"), #this shouldn't happen in prison
		(neg|eq, "$talk_context", tc_hero_freed), #this also shouldn't happen immediately after the prison break
        ],
    "My lord, I humbly request that you release me from service.", "lord_request_retire",[]],
	
	#dialog_ask_leave
    [anyone|plyr,"lord_talk",[
		#gekokujo 3.0 freelancer prison dialogue fix start
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"), #this shouldn't happen in prison
		(neg|eq, "$talk_context", tc_hero_freed), #this also shouldn't happen immediately after the prison break
		#gekokujo 3.0 freelancer prison dialogue fix end
		(eq, "$g_talk_troop", "$enlisted_lord"),
		(eq, "$freelancer_state", 1),
        (ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
        ],
        "My lord, I would like to request some personal leave.", "lord_request_vacation",[]],  
		
	#dialog_ask_return_from_leave
		[anyone|plyr,"lord_talk",[
		#gekokujo 3.0 freelancer prison dialogue fix start
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"), #this shouldn't happen in prison
		(neg|eq, "$talk_context", tc_hero_freed), #this also shouldn't happen immediately after the prison break
		#gekokujo 3.0 freelancer prison dialogue fix end
		(eq, "$g_talk_troop", "$enlisted_lord"),
		(eq, "$freelancer_state", 2),
        (ge, "$g_talk_troop_faction_relation", 0),
        (neq, "$players_kingdom", "$g_talk_troop_faction"),
        (eq, "$players_kingdom", 0),
        ],
        "My lord, I am ready to return under your banner.", "ask_return_from_leave",[]],	
]
		
dialogs	= [   
# dialog_accept_enlistment

    [anyone,"lord_request_enlistment",
    [
        (ge, "$g_talk_troop_relation", 0),
		
		(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
		(store_mul, ":samurai_potential", "$g_talk_troop_effective_relation", 5),
		(val_add, ":samurai_potential", ":renown"),
		
		(try_begin),
			(neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_freelancer_troop, 0),
			(faction_get_slot, reg1, "$g_talk_troop_faction", slot_faction_freelancer_troop),
			(neg|is_between, reg1, monk_troops_begin, monk_troops_end),
		(else_try),
			#(neg|troop_slot_ge, "trp_player", slot_troop_renown, 75),
			(lt, ":samurai_potential", 75),
			(faction_get_slot, reg1, "$g_talk_troop_faction", slot_faction_tier_0_troop),
		(else_try),
			(try_begin),
				(eq, "$g_talk_troop_faction", "fac_kingdom_20"),
				(assign, reg1, "trp_gekokujo_ikko_jizamurai"),
			(else_try),
				(faction_get_slot, reg1, "$g_talk_troop_faction", slot_faction_tier_1_troop),
			(try_end),
		(try_end),
		
		(try_begin),
			(is_between, reg1, samurai_troops_begin, samurai_troops_end),
			(assign, ":pay_multiplier", 20), #samurai get paid more
		(else_try),
			(assign, ":pay_multiplier", 10), #ashigaru get paid less
		(try_end),
		
		(str_store_troop_name, s1, reg1),
		(store_character_level, reg1, reg1),
		(val_mul, reg1, ":pay_multiplier"),
		(str_store_string, s2, "str_reg1_denars"),
    ], "I have room in my household for a {man/woman} like yourself, {playername}. I can take you on as a {s1}, with a stipend of {s2} per week. And food, of course.  Plenty of room for promotion and you'll be equipped as befits your rank. You'll have your take of what you can scavange in battle, too.  What do you say?", "lord_request_enlistment_confirm", []],
		
    [anyone|plyr,"lord_request_enlistment_confirm", [],
    "I humbly accept, my lord!", "close_window",
	[
		(party_clear, "p_freelancer_party_backup"),
		(call_script, "script_dismiss_companions"), #gekokujo 3.0 dismiss companions at enlistment
		(call_script, "script_party_copy", "p_freelancer_party_backup", "p_main_party"),
		(remove_member_from_party, "trp_player","p_freelancer_party_backup"),
		
		#if they used to be a monk they're not anymore
		(faction_get_slot, ":faction_troop", "$g_talk_troop_faction", slot_faction_freelancer_troop),
		(try_begin),
			(is_between, ":faction_troop", monk_troops_begin, monk_troops_end),
			(faction_set_slot, "$g_talk_troop_faction", slot_faction_freelancer_troop, 0),
		(try_end),
		
        (call_script, "script_event_player_enlists"),
		(assign, "$g_infinite_camping", 1),
		(rest_for_hours_interactive, 24 * 365, 5, 1),
		(eq,"$talk_context",tc_party_encounter),
		(assign, "$g_leave_encounter", 1),
		(assign, "$time_in_service", 0), #gekokujo 3.0 initialize/reset the time in service counter on enlistment
	]],

	[anyone|plyr,"lord_request_enlistment_confirm",[],
    "On second thought my lord, I might try my luck alone a bit longer. My thanks.", "lord_pretalk",[]],
	
	#gekokujo 3.0 monk enlistment start
    [anyone,"lord_request_enlistment_monk",
    [
        (ge, "$g_talk_troop_relation", 0),
		
		(faction_get_slot, reg1, "fac_kingdom_20", slot_faction_freelancer_troop),
		(try_begin),
			(neg|is_between, reg1, monk_troops_begin, monk_troops_end),
			(assign, reg1, "trp_gekokujo_ikko_monk"),
		(try_end),
		
		(str_store_troop_name, s1, reg1),
    ], "I have room in my army for a {man/woman} like yourself, {playername}. I can take you on as a {s1} with free food and lodging, but as a monk you are obviously not paid.  Plenty of room for promotion, however, and you'll be equipped as befits your rank.  What do you say?", "lord_request_enlistment_confirm_monk", []],
		
    [anyone|plyr,"lord_request_enlistment_confirm_monk", [],
    "I humbly accept, my lord!", "close_window",
	[
	    (party_clear, "p_freelancer_party_backup"),
		(call_script, "script_dismiss_companions"), #gekokujo 3.0 dismiss companions at enlistment
		(call_script, "script_party_copy", "p_freelancer_party_backup", "p_main_party"),
		(remove_member_from_party, "trp_player","p_freelancer_party_backup"),
		
		#let's sidestep the samurai/ashigaru thing
		(faction_get_slot, ":faction_troop", "fac_kingdom_20", slot_faction_freelancer_troop),
		(try_begin),
			(neg|is_between, ":faction_troop", monk_troops_begin, monk_troops_end),
			(faction_set_slot, "fac_kingdom_20", slot_faction_freelancer_troop, "trp_gekokujo_ikko_monk"),
		(try_end),
		
        (call_script, "script_event_player_enlists"),
		(assign, "$g_infinite_camping", 1),
        (rest_for_hours_interactive, 24 * 365, 5, 1),
		(eq,"$talk_context",tc_party_encounter),
		(assign, "$g_leave_encounter", 1),
	]],

	[anyone|plyr,"lord_request_enlistment_confirm_monk",[],
    "On second thought my lord, I might try my luck alone a bit longer. My thanks.", "lord_pretalk",[]],
	#gekokujo 3.0 monk enlistment end
	
# dialog_reject_enlistment

    [anyone,"lord_request_enlistment", [(lt, "$g_talk_troop_relation", 0)],
    "I do not trust you enough to allow you to serve for me.", "lord_pretalk",[]],

# gekokujo 3.0 accept promotion

    [anyone,"lord_request_promotion",
    [
		(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
		(store_mul, ":samurai_potential", "$g_talk_troop_effective_relation", 5),
		(val_add, ":samurai_potential", ":renown"),
		
		(ge, ":samurai_potential", 75), #player meets minimum requirements
        (ge, "$g_talk_troop_relation", 0),
		
		(try_begin),
			(eq, "$g_talk_troop_faction", "fac_kingdom_20"),
			(assign, reg1, "trp_gekokujo_ikko_jizamurai"),
		(else_try),
			(faction_get_slot, reg1, "$g_talk_troop_faction", slot_faction_tier_1_troop),
		(try_end),
		
		(str_store_troop_name, s1, reg1),
		(store_character_level, reg1, reg1),
		(val_mul, reg1, 20),		
		(str_store_string, s2, "str_reg1_denars"),
    ], "You have the potential for leadership, {playername}. I can move you up to {s1}, with a new stipend of {s2} per week and a room in my mansion rather than the barracks. Your equipment will also be upgraded accordingly.", "lord_request_promotion_confirm", []],
		
    [anyone|plyr,"lord_request_promotion_confirm", [],
    "I humbly accept, my lord!", "close_window",
	[
		#change rank
		(call_script, "script_freelancer_unequip_troop", "$player_cur_troop"),
		
		(try_begin),
			(eq, "$g_talk_troop_faction", "fac_kingdom_20"),
			(assign, "$player_cur_troop", "trp_gekokujo_ikko_jizamurai"),			
		(else_try),
			(faction_get_slot, "$player_cur_troop", "$g_talk_troop_faction", slot_faction_tier_1_troop),
		(try_end),
		
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(faction_set_slot, ":commander_faction", slot_faction_freelancer_troop, "$player_cur_troop"),
		(call_script, "script_freelancer_equip_troop", "$player_cur_troop"),
		(str_store_troop_name, s5, "$player_cur_troop"),
		(str_store_string, s5, "@Current rank: {s5}"),
		(add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, s5, 1),
		
		#reset xp
        (troop_get_xp, ":xp", "trp_player"),
		(troop_set_slot, "trp_player", slot_troop_freelancer_start_xp, ":xp"),
		
		#half-assed version start
		##from the retirement script
		#(call_script, "script_event_player_discharge"),
		#(call_script, "script_party_restore"),
		#
		##from the enlistment script
	    #(party_clear, "p_freelancer_party_backup"),
		#(call_script, "script_party_copy", "p_freelancer_party_backup", "p_main_party"),
		#(remove_member_from_party, "trp_player","p_freelancer_party_backup"),
        #(call_script, "script_event_player_enlists"),
		#(assign, "$g_infinite_camping", 1),
        #(rest_for_hours_interactive, 24 * 365, 5, 1),
		#(eq,"$talk_context",tc_party_encounter),
		#(assign, "$g_leave_encounter", 1),
		#half-assed version end
		(change_screen_map),
	]],

	[anyone|plyr,"lord_request_promotion_confirm",[],
    "On second thought my lord, I am happy where I am. Thank you.", "lord_pretalk",[]],

# gekokujo 3.0 reject promotion

    [anyone,"lord_request_promotion", [(lt, "$g_talk_troop_relation", 0)],
    "I do not trust you enough to bring you closer to my inner circle.", "lord_pretalk",[]],

# dialog_lord_accept_retire 

    [anyone,"lord_request_retire",
    [		
		(try_begin),
			(ge, "$g_talk_troop_effective_relation", 10),
			(str_store_string, s11, "@I am sad to see you go. The equipment I loaned you -- please keep it and stay safe out there."),
		(else_try),
			(str_store_string, s11, "@You are relieved of duty."),
		(try_end),
		
		(try_begin),
			(gt, "$time_in_service", 0),
			(assign, reg1, 10),
			(val_mul, reg1, "$time_in_service"),
			(str_store_string, s13, "str_reg1_denars"),
			(try_begin),
				(ge, "$g_talk_troop_effective_relation", 10),
				(str_store_string, s12, "@For your time in my service, I also bid you farewell with {s13}."),		
			(else_try),
				(str_store_string, s12, "@For your time in my service, I grant you {s13}."),		
			(try_end),
		(else_try),
			(str_store_string, s12, "@You weren't with me very long, were you?"),
		(try_end),
    ],
    "Very well, {playername}. {s11} {s12}", "lord_pretalk",[
	
	(assign, ":retirement_bonus", 10),
	(assign, ":retirement_xp", 100),
	(val_mul, ":retirement_bonus", "$time_in_service"),
	(val_mul, ":retirement_xp", "$time_in_service"),
	(quest_set_slot, "qst_freelancer_enlisted", slot_quest_gold_reward, ":retirement_bonus"),
	(quest_set_slot, "qst_freelancer_enlisted", slot_quest_xp_reward, ":retirement_xp"),
	
	(call_script, "script_event_player_discharge"),
	(call_script, "script_party_restore"),
	
	(assign, "$time_in_service", 0), #reset the clock so you can't just quit and rejoin and so on in the same scene
	(change_screen_map),
	],
	],	
	
#dialog_accept_leave  
    [anyone,"lord_request_vacation",
        [
        (ge, "$g_talk_troop_relation", 0),
		],
            "Very well {playername}. You shall take some time off from duty. Return in two weeks.", "lord_pretalk",[
		(call_script, "script_event_player_vacation"),
       	(call_script, "script_party_restore"),
		(change_screen_map),
		],
		],
					

				
	
#dialog_accept_ask_return_from_leave
        [anyone,"ask_return_from_leave",
        [
        (ge, "$g_talk_troop_relation", 0),
		],
        "Welcome back {playername}. Your gashira has missed you I daresay, Now return to your post.", "lord_pretalk",[
		(call_script, "script_dismiss_companions"), #gekokujo 3.0 dismiss companions at enlistment
        (call_script, "script_party_copy", "p_freelancer_party_backup", "p_main_party"),
		(remove_member_from_party, "trp_player","p_freelancer_party_backup"),
		(call_script, "script_event_player_returns_vacation"),
		(change_screen_map),
		],
		],	
#+freelancer end

#gekokujo 3.0 return to lord after defeat start (early attempt)
#		[anyone,"return_from_defeat",
#		[
#		(ge, "$g_talk_troop_relation", 0),
#		],
#		"{playername}, you survived! And to return after what happened? You are what all samurai should aspire to.", "lord_pretalk",[
#		(call_script, "script_party_copy", "p_freelancer_party_backup", "p_main_party"),
#		(remove_member_from_party, "trp_player","p_freelancer_party_backup"),
#
#		(call_script, "script_freelancer_equip_troop", "$player_cur_troop"),
#
#		(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", 10),
#		(call_script, "script_change_troop_renown", "trp_player", 10),
#		(call_script, "script_change_player_honor", 10),
#
#		(call_script, "script_event_player_returns_defeat"),
#		(change_screen_map),
#		],
#		],	
#gekokujo 3.0 return to lord after defeat end
]

from util_common import *
from util_wrappers import *

def dialogs_addendum(orig_dialogs):
	try:
		dialog = FindDialog(orig_dialogs, anyone|plyr, "lord_talk", "lord_request_mission_ask")
		codeblock = dialog.GetConditionBlock()
		codeblock.InsertBefore(0, not_enlisted)
		dialog = FindDialog(orig_dialogs, anyone|plyr, "lord_talk", "lord_ask_enter_service", "I have come")
		codeblock = dialog.GetConditionBlock()
		codeblock.InsertBefore(0, not_enlisted)
		dialog = FindDialog(orig_dialogs, anyone|plyr, "lord_talk", "lord_ask_enter_service", "I wish to become")
		codeblock = dialog.GetConditionBlock()
		codeblock.InsertBefore(0, not_enlisted)
	except:
		import sys
		print "Injecton 1 failed:", sys.exc_info()[1]
		raise

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
		var_name_1 = "dialogs"
		orig_dialogs = var_set[var_name_1]
		orig_dialogs.extend(dialogs)
		pos = FindDialog_i(orig_dialogs, anyone|plyr, "lord_talk", "lord_leave_prison")
		OpBlockWrapper(orig_dialogs).InsertBefore(pos, lord_talk_addon)
		##ORIG_DIALOGS is a list, can use OpBlockWrapper and other list operations.
		
		dialogs_addendum(orig_dialogs) #other dialog additions
		
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)