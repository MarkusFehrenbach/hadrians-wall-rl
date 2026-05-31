from __future__ import annotations
from typing import Dict, TYPE_CHECKING
if TYPE_CHECKING:
    from .game_state import GameState

from . import actions
from .actions import N_ACTIONS
from .enums import GameStatus

# --- Game rule constants --- #
# Game meta
MAX_ROUNDS = 6
NUM_PICT_ATTACKS = [1, 2, 4, 6, 8, 10]
MAX_PICT_ATTACKS = NUM_PICT_ATTACKS[-1]
MAX_FAVOURS = 9

# Fate cards
NUM_LEFT_FATE_CARDS = 16
NUM_CENTER_FATE_CARDS = 16
NUM_RIGHT_FATE_CARDS = 16
NUM_TOTAL_FATE_CARDS = NUM_LEFT_FATE_CARDS + NUM_CENTER_FATE_CARDS + NUM_RIGHT_FATE_CARDS

# Player cards
NUM_PLAYER_CARDS = 12

# Left sheet state thresholds
COHORT_DICIPLINE_THRESHOLDS = [3, 6]
COHORT_VALOUR_THRESHOLDS = [5]
MINING_AND_FORESTING_THRESHOLDS = [2, 5, 8, 11, 14]
WALL_GUARD_SECTION_THRESHOLDS = [6, 12, 18]
WALL_GUARD_DICIPLINE_THRESHOLDS = [2, 5, 8, 11, 14, 17]
WALL_GUARD_COHORT_THRESHOLDS = [3, 6, 9, 12, 15, 18]
CIPPI_COHORT_THRESHOLDS = [3, 5, 7]
CIPPI_CIVILIAN_THRESHOLDS = [4]
CIPPI_RENOWN_THRESHOLDS = [6]
CIPPI_FORT_SECTION_THRESHOLDS = [1, 4, 7, 10, 13, 16, 20]
WALL_CITICIAN_THRESHOLDS = [1, 3, 5, 9, 13, 16, 19]
WALL_RENOWN_THRESHOLDS = [4, 8, 11, 15, 18]
WALL_COHORT_THRESHOLDS = [4, 7, 11, 14, 18, 21]
FORT_CITICIAN_THRESHOLDS = [4, 6, 8, 10, 12, 16, 18, 20]
FORT_DICIPLINE_THRESHOLDS = [7, 14, 21]
FORT_COHORT_THRESHOLDS = [14, 21]
FORT_INFRASTRUCTURE_THRESHOLDS = [1, 3, 5, 9, 11, 13, 15, 17]
WALL_AND_FORT_SECTION_THRESHOLDS = [7, 14, 21]
SMALL_GRANARY_INFRASTRUCTURE_THRESHOLD = 1
SMALL_GRANARY_FORT_AND_WALL_UNLOCK = WALL_AND_FORT_SECTION_THRESHOLDS[1]
LARGE_GRANARY_INFRASTRUCTURE_THRESHOLD = 5
LARGE_GRANARY_FORT_AND_WALL_UNLOCK = WALL_AND_FORT_SECTION_THRESHOLDS[2]
SMALL_HOTEL_INFRASTRUCTURE_THRESHOLD = 2
LARGE_HOTEL_INFRASTRUCTURE_THRESHOLD = 6
SMALL_WORKSHOP_INFRASTRUCTURE_THRESHOLD = 3
LARGE_WORKSHOP_INFRASTRUCTURE_THRESHOLD = 7
SMALL_ROAD_INFRASTRUCTURE_THRESHOLD = 4
LARGE_ROAD_INFRASTRUCTURE_THRESHOLD = 8
LANDMARK_ATTRIBUTE_POINTS_THRESHOLD = 15

# Left sheet state
NUM_COHORTS_BOXES = 6
NUM_MINING_AND_FORESTING_BOXES = 14
NUM_WALL_GUARD_BOXES = WALL_GUARD_SECTION_THRESHOLDS[2]
NUM_CIPPI_BOXES = 7
NUM_WALL_AND_FORT_BOXES = WALL_AND_FORT_SECTION_THRESHOLDS[2]
RESOURCE_PRODUCTION_BOXES = 9
NUM_TRAINING_GROUNDS_BOXES = 5
NUM_FORUM_BOXES = 4
ATTRIBUTE_POINTS_PER_TRACK = 25
NUM_DISDAIN_BOXES = 15
MAX_INFRASTRUCTURE_LEVEL = 8

# Right sheet state thresholds
# Traders
TRADERS_BUILDERS_THRESHOLDS = [3, 7]
TRADERS_SERVANTS_THRESHOLDS = [1]
TRADERS_RESOURCES_THRESHOLDS = [5, 9]
TRADERS_RENOWN_THRESHOLDS = [8]
TRADERS_SMALL_PRECINCT_THRESHOLD = 3
TRADERS_MEDIUM_PRECINCT_THRESHOLD = 6
TRADERS_LARGE_PRECINCT_THRESHOLD = 9
TRADERS_MARKET_THRESHOLD = 4
TRADERS_MARKET_THRESHOLDS = [4, 5, 5, 6, 6, 7, 8, 9]

# Performers
PERFORMERS_SOLDIERS_THRESHOLDS = [5]
PERFORMERS_BUILDERS_THRESHOLDS = [1, 9]
PERFORMERS_SERVANTS_THRESHOLDS = [3, 7]
PERFORMERS_RENOWN_THRESHOLDS = [8]
PERFORMERS_THEATER_THRESHOLD = 1
PERFORMERS_THEATER_ARRANGE_PERFORMANCE_THRESHOLDS = [1, 3, 5, 6, 8, 9]
PERFORMERS_COLOSSEUM_THRESHOLD = 3
PERFORMERS_COLOSSEUM_TRAINING_THRESHOLDS = [3, 4, 5, 6, 8, 9]

# Priests
PRIESTS_SERVANTS_THRESHOLDS = [1, 3, 5, 7, 9]
PRIESTS_PIETY_THRESHOLDS = [4, 6, 8]
PRIESTS_SMALL_GARDEN_THRESHOLD = 4
PRIESTS_LARGE_GARDEN_THRESHOLD = 7
PRIESTS_SMALL_TEMPLE_THRESHOLD = 1
PRIESTS_SMALL_TEMPLE_FILL_THRESHOLDS = [1]
PRIESTS_MEDIUM_TEMPLE_THRESHOLD = 3
PRIESTS_MEDIUM_TEMPLE_FILL_THRESHOLDS = [3, 5, 6]
PRIESTS_LARGE_TEMPLE_THRESHOLD = 6
PRIESTS_LARGE_TEMPLE_FILL_THRESHOLDS = [6, 8, 9]

# Apparitores
APPARITORES_SOLDIERS_THRESHOLDS = [3, 7]
APPARITORES_BUILDERS_THRESHOLDS = [1, 5, 9]
APPARITORES_DICIPLINE_THRESHOLDS = [4, 6, 8]
APPARITORES_BATHS_THRESHOLD = 3
APPARITORES_BATHS_BRIBE_THRESHOLDS = [3, 4, 5, 6, 7, 8]
APPARITORES_COURTHOUSE_THRESHOLD = 4
APPARITORES_COURTHOUSE_GET_SERVANT_THRESHOLDS = [4, 5, 6]
APPARITORES_COURTHOUSE_BUILDER_TO_TWO_SERVANTS_THRESHOLDS = [5, 6, 7]
APPARITORES_COURTHOUSE_SERVANT_TO_BUILDER_THRESHOLDS = [6, 7, 8]

# Patricians
PATRICIANS_SOLDIERS_THRESHOLDS = [3, 7]
PATRICIANS_RESOURCES_THRESHOLDS = [1, 5, 9]
PATRICIANS_RENOWN_THRESHOLDS = [4, 6, 8]
PATRICIANS_DIPLOMAT_THRESHOLDS = [1, 3, 6]
PATRICIANS_SCOUTS_THRESHOLDS = [2, 4, 5, 7, 9]

# Right sheet state
NUM_CITIZEN_TRACK_BOXES = 9

# Traders
NUM_MARKET_BOXES = 8
TRADERS_MARKET_SERVANT_BOX = 7
TRADERS_MARKET_BUILDER_BOX = 8

# Performers
NUM_THEATER_BOXES = 6
NUM_GLADIATOR_BOXES = 6

# Priests
NUM_SMALL_TEMPLE_BOXES = 1
NUM_MEDIUM_TEMPLE_BOXES = 3
NUM_LARGE_TEMPLE_BOXES = 3

# Apparitores
NUM_BATHS_BOXES = 6
MAX_NUM_BRIBES_PER_ROUND = 2
APPARITORES_BATHS_BRIBE_COSTS = [1, 1, 2, 2, 3, 3]
MAX_NUM_COURTHOUSE_ACTIONS = 3

# Patricians
NUM_DIPLOTMAT_BOXES = 3
NUM_SCOUTS_BOXES = 5
NUM_SCOUTS_GRID_ROWS = 4
NUM_SCOUTS_GRID_COLS = 5
PATRICIANS_SCOUTS_GRID_RESOURCES = [(0, 0), (0, 4), (3, 0), (3, 2), (3, 4),]
PATRICIANS_SCOUTS_GRID_SERVANTS = [(1, 1), (1, 3),]

# Scoring
ATTRIBUTE_CITIZEN_THRESHOLDS = [3, 6, 9, 12, 15, 19, 23]
RENOWN_ADD_PIETY_THRESHOLD = 17
RENOWN_ADD_VALOUR_THRESHOLD = 25
RENOWN_ADD_DICIPLINE_THRESHOLD = 21
PIETY_ADD_RENOWN_THRESHOLD = 17
PIETY_ADD_VALOUR_THRESHOLD = 21
PIETY_ADD_DICIPLINE_THRESHOLD = 25
VALOUR_ADD_RENOWN_THRESHOLD = 21
VALOUR_ADD_PIETY_THRESHOLD = 25
VALOUR_ADD_DICIPLINE_THRESHOLD = 17
DICIPLINE_ADD_RENOWN_THRESHOLD = 25
DICIPLINE_ADD_PIETY_THRESHOLD = 21
DICIPLINE_ADD_VALOUR_THRESHOLD = 17

# Cost dict
COSTS = {
    # Left sheet action costs
    actions.ACTION_ADVANCE_MINING_AND_FORESTING: {"servants": 1},
    actions.ACTION_ADVANCE_WALL_GUARD: {"solders": 1},
    actions.ACTION_ADVANCE_CIPPI: {"resources": 1},
    actions.ACTION_ADVANCE_WALL: {"resources": 1},
    actions.ACTION_ADVANCE_FORT_PAY_SOLDIER: {"solders": 1},
    actions.ACTION_ADVANCE_FORT_PAY_BUILDER: {"builders": 1},
    actions.ACTION_BUILD_SMALL_GRANARY: {"builders": 1, "servants": 1, "resources": 1},
    actions.ACTION_BUILD_LARGE_GRANARY: {"builders": 1, "servants": 1, "resources": 2},
    actions.ACTION_USE_TRAINING_GROUNDS: {"builders": 1},
    actions.ACTION_BUILD_SMALL_HOTEL: {"builders": 1, "servants": 1, "resources": 1},
    actions.ACTION_BUILD_LARGE_HOTEL: {"builders": 1, "servants": 1, "resources": 2},
    actions.ACTION_BUILD_SMALL_WORKSHOP: {"resources": 3},
    actions.ACTION_BUILD_LARGE_WORKSHOP: {"resources": 4},
    actions.ACTION_BUILD_SMALL_ROAD: {"builders": 1, "servants": 2, "resources": 1},
    actions.ACTION_BUILD_LARGE_ROAD: {"builders": 1, "servants": 2, "resources": 2},
    actions.ACTION_USE_FORUM_BUILDER_BUILDER_TO_SERVANT: {"builders": 2}, 
    actions.ACTION_USE_FORUM_BUILDER_BUILDER_TO_CIVILIAN: {"builders": 2},
    actions.ACTION_USE_FORUM_SERVANT_SERVANT_TO_BUILDER: {"servants": 2},
    actions.ACTION_USE_FORUM_SERVANT_SERVANT_TO_CIVILIAN: {"servants": 2},
    actions.ACTION_USE_FORUM_CIVILIAN_CIVILIAN_TO_BUILDER: {"civilians": 2},
    actions.ACTION_USE_FORUM_CIVILIAN_CIVILIAN_TO_SERVANT: {"civilians": 2},
    actions.ACTION_USE_FORUM_BUILDER_SERVANT_TO_CIVILIAN: {"builders": 1, "servants": 1},
    actions.ACTION_USE_FORUM_BUILDER_CIVILIAN_TO_SERVANT: {"builders": 1, "civilians": 1},
    actions.ACTION_USE_FORUM_SERVANT_CIVILIAN_TO_BUILDER: {"servants": 1, "civilians": 1},
    actions.ACTION_BUILD_LANDMARK_1: {"builders": 1, "resources": 2},
    actions.ACTION_BUILD_LANDMARK_2: {"builders": 1, "resources": 2},
    actions.ACTION_BUILD_LANDMARK_3: {"builders": 1, "resources": 2},
    actions.ACTION_BUILD_LANDMARK_4: {"builders": 1, "resources": 2},

    # Right sheet action costs
    # Traders
    actions.ACTION_ADVANCE_TRADERS_TRACK: {"civilians": 1},
    actions.ACTION_BUILD_SMALL_PRECINCT: {"servants": 1, "civilians": 1},
    actions.ACTION_BUILD_MEDIUM_PRECINCT: {"servants": 1, "civilians": 2},
    actions.ACTION_BUILD_LARGE_PRECINCT: {"servants": 1, "civilians": 3},
    actions.ACTION_BUILD_MARKET: {"builders": 1, "servants": 1, "resources": 2},
} | \
{a: {"resources": 1} for a in actions.ACTIONS_TRADERS_MARKET} | \
{
    # Performers
    actions.ACTION_ADVANCE_PERFORMERS_TRACK: {"civilians": 1},
    actions.ACTION_BUILD_THEATER: {"builders": 1, "servants": 1, "resources": 1},
    actions.ACTION_BUILD_COLOSSEUM: {"builders": 1, "servants": 2, "resources": 2},
    actions.ACTION_TRAIN_GLADIATOR_1_SERVANT: {"servants": 1},
    actions.ACTION_TRAIN_GLADIATOR_1_SERVANT_AND_FIGHT: {"servants": 1},
    actions.ACTION_TRAIN_GLADIATOR_1_CIVILIAN: {"civilians": 1},
    actions.ACTION_TRAIN_GLADIATOR_1_CIVILIAN_AND_FIGHT: {"civilians": 1},
    actions.ACTION_TRAIN_GLADIATOR_2_SERVANT: {"servants": 1},
    actions.ACTION_TRAIN_GLADIATOR_2_SERVANT_AND_FIGHT: {"servants": 1},
    actions.ACTION_TRAIN_GLADIATOR_2_CIVILIAN: {"civilians": 1},
    actions.ACTION_TRAIN_GLADIATOR_2_CIVILIAN_AND_FIGHT: {"civilians": 1},
} | \
{a: {"resources": 1} for a in actions.ACTIONS_PERFORMERS_THEATER} | \
{
    # Priests
    actions.ACTION_ADVANCE_PRIESTS_TRACK: {"civilians": 1},
    actions.ACTION_BUILD_SMALL_GARDEN: {"builders": 1, "servants": 1, "resources": 1},
    actions.ACTION_BUILD_LARGE_GARDEN: {"builders": 1, "servants": 1, "resources": 2},
    actions.ACTION_BUILD_SMALL_TEMPLE: {"builders": 1, "servants": 1, "resources": 1},
    actions.ACTION_BUILD_MEDIUM_TEMPLE: {"builders": 1, "servants": 1, "resources": 2},
    actions.ACTION_BUILD_LARGE_TEMPLE: {"builders": 2, "servants": 1, "resources": 2},
} | \
{a : {"soldiers": 1} for a in [actions.ACTION_FILL_SMALL_TEMPLE_SOLDIER, actions.ACTION_FILL_MEDIUM_TEMPLE_SOLDIER, actions.ACTION_FILL_LARGE_TEMPLE_SOLDIER]} | \
{a : {"builders": 1} for a in [actions.ACTION_FILL_SMALL_TEMPLE_BUILDER, actions.ACTION_FILL_MEDIUM_TEMPLE_BUILDER, actions.ACTION_FILL_LARGE_TEMPLE_BUILDER]} | \
{a : {"servants": 1} for a in [actions.ACTION_FILL_SMALL_TEMPLE_SERVANT, actions.ACTION_FILL_MEDIUM_TEMPLE_SERVANT, actions.ACTION_FILL_LARGE_TEMPLE_SERVANT]} | \
{a : {"civilians": 1} for a in [actions.ACTION_FILL_SMALL_TEMPLE_CIVILIAN, actions.ACTION_FILL_MEDIUM_TEMPLE_CIVILIAN, actions.ACTION_FILL_LARGE_TEMPLE_CIVILIAN]} | \
{
    # Apparitores
    actions.ACTION_ADVANCE_APPARITORES_TRACK: {"civilians": 1},
    actions.ACTION_BUILD_BATHS: {"builders": 2, "servants": 1, "resources": 2},
    actions.ACTION_PAY_BRIBE: {"resources": APPARITORES_BATHS_BRIBE_COSTS[0]},
    actions.ACTION_BUILD_COURTHOUSE: {"builders": 2, "servants": 1, "resources": 2},
    actions.ACTION_COURTHOUSE_BUILDER_TO_TWO_SERVANTS:{"builders": 1},
    actions.ACTION_COURTHOUSE_SERVANT_TO_BUILDER: {"servants": 1},

    # Patricians
    actions.ACTION_ADVANCE_PATRICIANS_TRACK: {"civilians": 1},
    actions.ACTION_SEND_LEFT_DIPLOMAT: {"soldiers": 1, "servants": 1, "resources": 2},
    actions.ACTION_SEND_CENTER_DIPLOMAT: {"soldiers": 1, "servants": 1, "resources": 2},
    actions.ACTION_SEND_RIGHT_DIPLOMAT: {"soldiers": 1, "servants": 1, "resources": 2},
    actions.ACTION_SEND_SCOUT_PROSPECT_CARD: {"soldiers": 1},
    actions.ACTION_SEND_SCOUT_NEIGHBOR_CARD_1: {"soldiers": 1},
    actions.ACTION_SEND_SCOUT_NEIGHBOR_CARD_2: {"soldiers": 1},
}

# --- Game rules flow functions --- #
def start_new_round(state: GameState):
    state.current_round += 1
    if state.current_round > MAX_ROUNDS:
        return
    _reset_resources(state)
    _reset_per_round_flags(state)
    state.num_pict_attacks = NUM_PICT_ATTACKS[state.current_round - 1]
    state.draw_fate_card()
    _add_resource_from_fate_card(state)
    _add_resource_from_left_sheet(state)
    state.draw_player_cards()
    if state.large_road_built:
        state.status = GameStatus.STATUS_CHOOSE_TWO_ATTRIBUTES
    elif state.small_road_built:
        state.status = GameStatus.STATUS_CHOOSE_ATTRIBUTE
    else:
        state.status = GameStatus.STATUS_CHOOSE_PLAYER_CARD

def _reset_per_round_flags(state: GameState):
    state.left_cohort_incoming_disdain = 0
    state.center_cohort_incoming_disdain = 0
    state.right_cohort_incoming_disdain = 0
    state.training_grounds_available = True
    state.forum_available = True
    state.theater_available = True
    state.gladiator_1_can_battle = True
    state.gladiator_2_can_battle = True
    state.baths_boxes_available = MAX_NUM_BRIBES_PER_ROUND
    state.courthouse_get_servant_available = True
    state.courthouse_builder_to_two_servants_available = True
    state.courthouse_servant_to_builder_available = True

def _start_pict_attack(state: GameState):
    assert(state.status == GameStatus.STATUS_MAIN_LOOP, "The game status is not correct")
    num_pict_attacks = NUM_PICT_ATTACKS[state.current_round - 1]
    num_pict_attacks_left = 0
    num_pict_attacks_center = 0
    num_pict_attacks_right = 0
    for _ in range(num_pict_attacks):
        state.draw_fate_card()
        pict_attack_direction = state.get_current_fate_card_pict_attack_direction()
        if pict_attack_direction == "left":
            num_pict_attacks_left += 1
        elif pict_attack_direction == "center":
            num_pict_attacks_center += 1
        elif pict_attack_direction == "right":
            num_pict_attacks_right += 1
        else:
            assert(False, f"Unknown pict attack direction {pict_attack_direction}")
    state.left_cohort_incoming_disdain = max(0, num_pict_attacks_left - state.left_cohort_boxes)
    state.center_cohort_incoming_disdain = max(0, num_pict_attacks_center - state.center_cohort_boxes)
    state.right_cohort_incoming_disdain = max(0, num_pict_attacks_right - state.right_cohort_boxes)
    if (state.left_cohort_incoming_disdain > 0 and (state.num_left_cohort_favours > 0 or state.num_general_favours > 0)) or \
            (state.center_cohort_incoming_disdain > 0 and (state.num_center_cohort_favours > 0 or state.num_general_favours > 0)) or \
            (state.right_cohort_incoming_disdain > 0 and (state.num_right_cohort_favours > 0 or state.num_general_favours > 0)):
        state.status == GameStatus.STATUS_USE_FAVOURS
    else:
        _end_round(state)  

def _end_round(state: GameState):
    state.num_disdain = min(state.num_disdain + state.get_sum_incoming_disdain(), NUM_DISDAIN_BOXES)
    start_new_round(state)

# --- Game rules apply action functions --- #
def apply_action(state: GameState, action):
    # Increase action counter
    state.action_counter += 1

    # Pay costs upfront. If action is free, this will just be a no-op.
    costs=COSTS.get(action, {})
    assert(_has_supplies(state, costs=costs), "Not enough supplies for this action")
    _pay_from_supply(state, costs=costs)

    # Take specified action
    match action:
        case action if action in actions.ACTIONS_CARD_ASSIGNMENT:
            _apply_card_assignment_action(state, action)
        case action if action in actions.ACTIONS_LEFT_SHEET:
            _apply_left_sheet_action(state, action)
        case action if action in actions.ACTIONS_RIGHT_SHEET:
            _apply_right_sheet_action(state, action)
        case action if action in actions.ACTIONS_FOLLOW_UP:
            _apply_follow_up_action(state, action)
        case actions.ACTION_END_ROUND:
            if state.status == GameStatus.STATUS_MAIN_LOOP:
                _start_pict_attack(state)
            elif state.status == GameStatus.STATUS_USE_FAVOURS:
                _end_round(state)
        case _:
            raise ValueError(f"Unknown action: {action}")    
    _update_path_cards_points(state)
    _update_disdain_malus_points(state)

def _apply_card_assignment_action(state: GameState, action):
    match action:
        case actions.ACTION_CARD_ASSIGNMENT_CHOOSE_LEFT_AS_PATH:
            _add_left_player_card_to_path(state)
        case actions.ACTION_CARD_ASSIGNMENT_CHOOSE_RIGHT_AS_PATH:
            _add_right_player_card_to_path(state)
        case _:
            raise ValueError(f"Unknown card assignment action: {action}")

def _apply_left_sheet_action(state: GameState, action):
    match action:
        case actions.ACTION_ADVANCE_COHORT_LEFT:
            _add_cohort_left(state)
        case actions.ACTION_ADVANCE_COHORT_CENTER:
            _add_cohort_center(state)
        case actions.ACTION_ADVANCE_COHORT_RIGHT:
            _add_cohort_right(state)
        case actions.ACTION_ADVANCE_MINING_AND_FORESTING:
            _advance_mining_and_foresting(state)
        case actions.ACTION_ADVANCE_WALL_GUARD:
            _advance_wall_guard(state)
        case actions.ACTION_ADVANCE_CIPPI:
            _advance_cippi(state)
        case actions.ACTION_ADVANCE_WALL:
            _advance_wall(state)
        case actions.ACTION_ADVANCE_FORT_PAY_SOLDIER:
            _advance_fort(state)
        case actions.ACTION_ADVANCE_FORT_PAY_BUILDER:
            _advance_fort(state)
        case actions.ACTION_BUILD_SMALL_GRANARY:
            _build_small_granary(state)
        case actions.ACTION_BUILD_LARGE_GRANARY:
            _build_large_granary(state)
        case actions.ACTION_USE_TRAINING_GROUNDS:
            _use_training_grounds(state)
        case actions.ACTION_BUILD_SMALL_HOTEL:
            _build_small_hotel(state)
        case actions.ACTION_BUILD_LARGE_HOTEL:
            _build_large_hotel(state)
        case actions.ACTION_BUILD_SMALL_WORKSHOP:
            _build_small_workshop(state)
        case actions.ACTION_BUILD_LARGE_WORKSHOP:
            _build_large_workshop(state)
        case actions.ACTION_BUILD_SMALL_ROAD:
            _build_small_road(state)
        case actions.ACTION_BUILD_LARGE_ROAD:
            _build_large_road(state)
        case actions.ACTION_USE_FORUM_BUILDER_BUILDER_TO_SERVANT:
            state.num_servants += 1
            _use_forum(state)
        case actions.ACTION_USE_FORUM_BUILDER_BUILDER_TO_CIVILIAN:
            state.num_civilians += 1
            _use_forum(state)
        case actions.ACTION_USE_FORUM_SERVANT_SERVANT_TO_BUILDER:
            state.num_builders += 1
            _use_forum(state)
        case actions.ACTION_USE_FORUM_SERVANT_SERVANT_TO_CIVILIAN:
            state.num_civilians += 1
            _use_forum(state)
        case actions.ACTION_USE_FORUM_CIVILIAN_CIVILIAN_TO_BUILDER:
            state.num_builders += 1
            _use_forum(state)
        case actions.ACTION_USE_FORUM_CIVILIAN_CIVILIAN_TO_SERVANT:
            state.num_servants += 1
            _use_forum(state)
        case actions.ACTION_USE_FORUM_BUILDER_SERVANT_TO_CIVILIAN:
            state.num_civilians += 1
            _use_forum(state)
        case actions.ACTION_USE_FORUM_BUILDER_CIVILIAN_TO_SERVANT:
            state.num_servants += 1
            _use_forum(state)
        case actions.ACTION_USE_FORUM_SERVANT_CIVILIAN_TO_BUILDER:
            state.num_builders += 1
            _use_forum(state)
        case actions.ACTION_BUILD_LANDMARK_1:
            _build_landmark_1(state)
        case actions.ACTION_BUILD_LANDMARK_2:
            _build_landmark_2(state)
        case actions.ACTION_BUILD_LANDMARK_3:
            _build_landmark_3(state)
        case actions.ACTION_BUILD_LANDMARK_4:
            _build_landmark_4(state)

def _apply_right_sheet_action(state: GameState, action):
    match action:
        case action if action in actions.ACTIONS_TRADERS:
            _apply_trader_action(state, action)
        case action if action in actions.ACTIONS_PERFORMERS:
            _apply_performer_action(state, action)
        case action if action in actions.ACTIONS_PRIESTS:
            _apply_priest_action(state, action)
        case action if action in actions.ACTIONS_APPARITORES:
            _apply_apparitore_action(state, action)
        case action if action in actions.ACTIONS_PATRICIANS:
            _apply_patrician_action(state, action)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_follow_up_action(state: GameState, action):
    match action:
        case actions.ACTION_ENFORCE_LEFT_COHORT:
            _enforce_left_cohort(state)
        case actions.ACTION_ENFORCE_CENTER_COHORT:
            _enforce_center_cohort(state)
        case actions.ACTION_ENFORCE_RIGHT_COHORT:
            _enforce_right_cohort(state)
        case actions.ACTION_RECEIVE_ATTRIBUTE_RENOWN:
            _add_renown_attribute_point(state)
            if state.status == GameStatus.STATUS_CHOOSE_TWO_ATTRIBUTES:
                state.status = GameStatus.STATUS_CHOOSE_ATTRIBUTE
            elif state.status == GameStatus.STATUS_CHOOSE_ATTRIBUTE:
                state.status = GameStatus.STATUS_CHOOSE_PLAYER_CARD
            else:
                state.status = GameStatus.STATUS_MAIN_LOOP
        case actions.ACTION_RECEIVE_ATTRIBUTE_PIETY:
            _add_piety_attribute_point(state)
            if state.status == GameStatus.STATUS_CHOOSE_TWO_ATTRIBUTES:
                state.status = GameStatus.STATUS_CHOOSE_ATTRIBUTE
            elif state.status == GameStatus.STATUS_CHOOSE_ATTRIBUTE:
                state.status = GameStatus.STATUS_CHOOSE_PLAYER_CARD
            else:
                state.status = GameStatus.STATUS_MAIN_LOOP
        case actions.ACTION_RECEIVE_ATTRIBUTE_VALOUR:
            _add_valour_attribute_point(state)
            if state.status == GameStatus.STATUS_CHOOSE_TWO_ATTRIBUTES:
                state.status = GameStatus.STATUS_CHOOSE_ATTRIBUTE
            elif state.status == GameStatus.STATUS_CHOOSE_ATTRIBUTE:
                state.status = GameStatus.STATUS_CHOOSE_PLAYER_CARD
            else:
                state.status = GameStatus.STATUS_MAIN_LOOP
        case actions.ACTION_RECEIVE_ATTRIBUTE_DICIPLINE:
            _add_dicipline_attribute_point(state)
            if state.status == GameStatus.STATUS_CHOOSE_TWO_ATTRIBUTES:
                state.status = GameStatus.STATUS_CHOOSE_ATTRIBUTE
            elif state.status == GameStatus.STATUS_CHOOSE_ATTRIBUTE:
                state.status = GameStatus.STATUS_CHOOSE_PLAYER_CARD
            else:
                state.status = GameStatus.STATUS_MAIN_LOOP
        case actions.ACTION_USE_LEFT_FAVOUR:
            _use_left_favour(state)
        case actions.ACTION_USE_CENTER_FAVOUR:
            _use_center_favour(state)
        case actions.ACTION_USE_RIGHT_FAVOUR:
            _use_right_favour(state)
        case actions.ACTION_USE_GENERAL_FAVOUR_LEFT:
            _use_general_favour_left(state)
        case actions.ACTION_USE_GENERAL_FAVOUR_CENTER:
            _use_general_favour_center(state)
        case actions.ACTION_USE_GENERAL_FAVOUR_RIGHT:
            _use_general_favour_right(state)
        case _:
            raise ValueError(f"Unknown follow-up action: {action}")

def _apply_trader_action(state: GameState, action):    
    match action:
        case actions.ACTION_ADVANCE_TRADERS_TRACK:
            _advance_traders_track(state)
        case actions.ACTION_BUILD_SMALL_PRECINCT:
            _build_small_precinct(state)
        case actions.ACTION_BUILD_MEDIUM_PRECINCT:
            _build_medium_precinct(state)
        case actions.ACTION_BUILD_LARGE_PRECINCT:
            _build_large_precinct(state)
        case actions.ACTION_BUILD_MARKET:
            _build_market(state)
        case actions.ACTION_BUY_GOODS_FATE_CARD:
            index = state.get_next_free_market_box()
            assert(index != TRADERS_MARKET_SERVANT_BOX - 1 and index != TRADERS_MARKET_BUILDER_BOX - 1, "Index of market box does not match the chosen action")
            state.draw_fate_card()
            goods_id = state.get_current_fate_card_goods_id()
            _buy_goods(state, goods_id)
        case actions.ACTION_BUY_GOODS_NEIGHBOR_CARD_1:
            index = state.get_next_free_market_box()
            assert(index != TRADERS_MARKET_SERVANT_BOX - 1 and index != TRADERS_MARKET_BUILDER_BOX - 1, "Index of market box does not match the chosen action")
            goods_id = state.get_neighbor_prospect_card_1_goods_id()
            assert(goods_id is not None, "Neighbor does not have a prospect card 1 to buy goods from")
            _buy_goods(state, goods_id)
        case actions.ACTION_BUY_GOODS_NEIGHBOR_CARD_2:
            index = state.get_next_free_market_box()
            assert(index != TRADERS_MARKET_SERVANT_BOX - 1 and index != TRADERS_MARKET_BUILDER_BOX - 1, "Index of market box does not match the chosen action")
            goods_id = state.get_neighbor_prospect_card_2_goods_id()
            assert(goods_id is not None, "Neighbor does not have a prospect card 2 to buy goods from")
            _buy_goods(state, goods_id)
        case action.ACTION_BUY_GOODS_7_FATE_CARD:
            state.draw_fate_card()
            goods_id = state.get_current_fate_card_goods_id()
            _buy_goods(state, goods_id, index=TRADERS_MARKET_SERVANT_BOX - 1)
        case action.ACTION_BUY_GOODS_7_NEIGHBOR_CARD_1:
            goods_id = state.get_neighbor_prospect_card_1_goods_id()
            assert(goods_id is not None, "Neighbor does not have a prospect card 1 to buy goods from")
            _buy_goods(state, goods_id, index=TRADERS_MARKET_SERVANT_BOX - 1)
        case action.ACTION_BUY_GOODS_7_NEIGHBOR_CARD_2:
            goods_id = state.get_neighbor_prospect_card_2_goods_id()
            assert(goods_id is not None, "Neighbor does not have a prospect card 2 to buy goods from")
            _buy_goods(state, goods_id, index=TRADERS_MARKET_SERVANT_BOX - 1)
        case action.ACTION_BUY_GOODS_8_FATE_CARD:
            state.draw_fate_card()
            goods_id = state.get_current_fate_card_goods_id()
            _buy_goods(state, goods_id, index=TRADERS_MARKET_BUILDER_BOX - 1)
        case action.ACTION_BUY_GOODS_8_NEIGHBOR_CARD_1:
            goods_id = state.get_neighbor_prospect_card_1_goods_id()
            assert(goods_id is not None, "Neighbor does not have a prospect card 1 to buy goods from")
            _buy_goods(state, goods_id, index=TRADERS_MARKET_BUILDER_BOX - 1)
        case action.ACTION_BUY_GOODS_8_NEIGHBOR_CARD_2:
            goods_id = state.get_neighbor_prospect_card_2_goods_id()
            assert(goods_id is not None, "Neighbor does not have a prospect card 2 to buy goods from")
            _buy_goods(state, goods_id, index=TRADERS_MARKET_BUILDER_BOX - 1)

def _apply_performer_action(state: GameState, action):
    match action:
        case actions.ACTION_ADVANCE_PERFORMERS_TRACK:
            _advance_performers_track(state)
        case actions.ACTION_BUILD_THEATER:
            _build_theater(state)
        case actions.ACTION_ARRANGE_PERFORMANCE_1:
            _arrange_performance_1(state)
        case actions.ACTION_ARRANGE_PERFORMANCE_2:
            _arrange_performance_2(state)
        case actions.ACTION_ARRANGE_PERFORMANCE_3:
            _arrange_performance_3(state)
        case actions.ACTION_ARRANGE_PERFORMANCE_4:
            _arrange_performance_4(state)
        case actions.ACTION_ARRANGE_PERFORMANCE_5:
            _arrange_performance_5(state)
        case actions.ACTION_ARRANGE_PERFORMANCE_6:
            _arrange_performance_6(state)
        case actions.ACTION_BUILD_COLOSSEUM:
            _build_colosseum(state)
        case action if action in [actions.ACTION_TRAIN_GLADIATOR_1_SERVANT, actions.ACTION_TRAIN_GLADIATOR_1_CIVILIAN]:
            _train_gladiator_1(state)
        case action if action in [actions.ACTION_TRAIN_GLADIATOR_1_SERVANT_AND_FIGHT, actions.ACTION_TRAIN_GLADIATOR_1_CIVILIAN_AND_FIGHT]:
            _train_gladiator_1(state)
            _fight_with_gladiator_1(state)
        case action if action in [actions.ACTION_TRAIN_GLADIATOR_2_SERVANT, actions.ACTION_TRAIN_GLADIATOR_2_CIVILIAN]:
            _train_gladiator_2(state)
        case action if action in [actions.ACTION_TRAIN_GLADIATOR_2_SERVANT_AND_FIGHT, actions.ACTION_TRAIN_GLADIATOR_2_CIVILIAN_AND_FIGHT]:
            _train_gladiator_2(state)
            _fight_with_gladiator_2(state)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_priest_action(state: GameState, action):
    match action:
        case actions.ACTION_ADVANCE_PRIESTS_TRACK:
            _advance_priests_track(state)
        case actions.ACTION_BUILD_SMALL_GARDEN:
            _build_small_garden(state)
        case actions.ACTION_BUILD_LARGE_GARDEN:
            _build_large_garden(state)
        case actions.ACTION_BUILD_SMALL_TEMPLE:
            _build_small_temple(state)
        case action if action in [
                actions.ACTION_FILL_SMALL_TEMPLE_SOLDIER,
                actions.ACTION_FILL_SMALL_TEMPLE_BUILDER,
                actions.ACTION_FILL_SMALL_TEMPLE_SERVANT,
                actions.ACTION_FILL_SMALL_TEMPLE_CIVILIAN,]:
            _fill_small_temple(state)
        case actions.ACTION_BUILD_MEDIUM_TEMPLE:
            _build_medium_temple(state)
        case action if action in [
                actions.ACTION_FILL_MEDIUM_TEMPLE_SOLDIER,
                actions.ACTION_FILL_MEDIUM_TEMPLE_BUILDER,
                actions.ACTION_FILL_MEDIUM_TEMPLE_SERVANT,
                actions.ACTION_FILL_MEDIUM_TEMPLE_CIVILIAN,]:
            _fill_medium_temple(state)
        case actions.ACTION_BUILD_LARGE_TEMPLE:
            _build_large_temple(state)#
        case action if action in [
                actions.ACTION_FILL_LARGE_TEMPLE_SOLDIER,
                actions.ACTION_FILL_LARGE_TEMPLE_BUILDER,
                actions.ACTION_FILL_LARGE_TEMPLE_SERVANT,
                actions.ACTION_FILL_LARGE_TEMPLE_CIVILIAN,]:
            _fill_large_temple(state)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_apparitore_action(state: GameState, action):
    match action:
        case actions.ACTION_ADVANCE_APPARITORES_TRACK:
            _advance_apparitores_track(state)
        case actions.ACTION_BUILD_BATHS:
            _build_baths(state)
        case actions.ACTION_PAY_BRIBE:
            _pay_bribe(state)
        case actions.ACTION_BUILD_COURTHOUSE:
            _build_courthouse(state)
        case actions.ACTION_COURTHOUSE_GET_SERVANT:
            _courthouse_get_servant(state)
        case actions.ACTION_COURTHOUSE_BUILDER_TO_TWO_SERVANTS:
            _courthouse_builder_to_two_servants(state)
        case actions.ACTION_COURTHOUSE_SERVANT_TO_BUILDER:
            _courthouse_servant_to_builder(state)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_patrician_action(state: GameState, action):
    match action:
        case actions.ACTION_ADVANCE_PATRICIANS_TRACK:
            _advance_patricians_track(state)
        case actions.ACTION_SEND_LEFT_DIPLOMAT:
            _send_left_diplomat(state)
        case actions.ACTION_SEND_CENTER_DIPLOMAT:
            _send_center_diplomat(state)
        case actions.ACTION_SEND_RIGHT_DIPLOMAT:
            _send_right_diplomat(state)
        case actions.ACTION_SEND_SCOUT_PROSPECT_CARD:
            _send_scout_prospect_card(state)
        case actions.ACTION_SEND_SCOUT_NEIGHBOR_CARD_1:
            _send_scout_neighbor_card_1(state)
        case actions.ACTION_SEND_SCOUT_NEIGHBOR_CARD_2:
            _send_scout_neighbor_card_2(state)
        case action if action in actions.ACTIONS_SCOUTS:
            _apply_scout_grid_pattern_action(state, action)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_scout_grid_pattern_action(state: GameState, action):
    match action:
        case actions.ACTION_SEND_SCOUT_GRID_1:
            _apply_scout_grid_pattern_1_action(state, action)
        case actions.ACTION_SEND_SCOUT_GRID_2:
            _apply_scout_grid_pattern_2_action(state, action)
        case actions.ACTION_SEND_SCOUT_GRID_3:
            _apply_scout_grid_pattern_3_action(state, action)
        case actions.ACTION_SEND_SCOUT_GRID_4:
            _apply_scout_grid_pattern_4_action(state, action)
        case actions.ACTION_SEND_SCOUT_GRID_5:
            _apply_scout_grid_pattern_5_action(state, action)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_scout_grid_pattern_1_action(state: GameState, action):
    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_0_0:
            _place_scout_grid_pattern_1(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_0_1:
            _place_scout_grid_pattern_1(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_0_2:
            _place_scout_grid_pattern_1(state, row=0, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_0_3:
            _place_scout_grid_pattern_1(state, row=0, col=3)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_1_0:
            _place_scout_grid_pattern_1(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_1_1:
            _place_scout_grid_pattern_1(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_1_2:
            _place_scout_grid_pattern_1(state, row=1, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_1_3:
            _place_scout_grid_pattern_1(state, row=1, col=3)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_2_0:
            _place_scout_grid_pattern_1(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_2_1:
            _place_scout_grid_pattern_1(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_2_2:
            _place_scout_grid_pattern_1(state, row=2, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_2_3:
            _place_scout_grid_pattern_1(state, row=2, col=3)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_scout_grid_pattern_2_action(state: GameState, action):
    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_0:
            _place_scout_grid_pattern_2(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_1:
            _place_scout_grid_pattern_2(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_1_0:
            _place_scout_grid_pattern_2(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_1_1:
            _place_scout_grid_pattern_2(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_2_0:
            _place_scout_grid_pattern_2(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_2_1:
            _place_scout_grid_pattern_2(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_3_0:
            _place_scout_grid_pattern_2(state, row=3, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_3_1:
            _place_scout_grid_pattern_2(state, row=3, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_0_90:
            _place_scout_grid_pattern_2(state, row=0, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_1_90:
            _place_scout_grid_pattern_2(state, row=0, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_2_90:
            _place_scout_grid_pattern_2(state, row=0, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_3_90:
            _place_scout_grid_pattern_2(state, row=0, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_4_90:
            _place_scout_grid_pattern_2(state, row=0, col=4, rotated=True)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_scout_grid_pattern_3_action(state: GameState, action):
    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_0:
            _place_scout_grid_pattern_3(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_1:
            _place_scout_grid_pattern_3(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_2:
            _place_scout_grid_pattern_3(state, row=0, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_0:
            _place_scout_grid_pattern_3(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_1:
            _place_scout_grid_pattern_3(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_2:
            _place_scout_grid_pattern_3(state, row=1, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_0:
            _place_scout_grid_pattern_3(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_1:
            _place_scout_grid_pattern_3(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_2:
            _place_scout_grid_pattern_3(state, row=2, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_0_M:
            _place_scout_grid_pattern_3(state, row=0, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_1_M:
            _place_scout_grid_pattern_3(state, row=0, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_2_M:
            _place_scout_grid_pattern_3(state, row=0, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_0_M:
            _place_scout_grid_pattern_3(state, row=1, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_1_M:
            _place_scout_grid_pattern_3(state, row=1, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_2_M:
            _place_scout_grid_pattern_3(state, row=1, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_0_M:
            _place_scout_grid_pattern_3(state, row=2, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_1_M:
            _place_scout_grid_pattern_3(state, row=2, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_2_M:
            _place_scout_grid_pattern_3(state, row=2, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_0_90:
            _place_scout_grid_pattern_3(state, row=0, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_1_90:
            _place_scout_grid_pattern_3(state, row=0, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_2_90:
            _place_scout_grid_pattern_3(state, row=0, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_3_90:
            _place_scout_grid_pattern_3(state, row=0, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_0_90:
            _place_scout_grid_pattern_3(state, row=1, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_1_90:
            _place_scout_grid_pattern_3(state, row=1, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_2_90:
            _place_scout_grid_pattern_3(state, row=1, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_3_90:
            _place_scout_grid_pattern_3(state, row=1, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_0_90_M:
            _place_scout_grid_pattern_3(state, row=0, col=0, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_1_90_M:
            _place_scout_grid_pattern_3(state, row=0, col=1, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_2_90_M:
            _place_scout_grid_pattern_3(state, row=0, col=2, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_3_90_M:
            _place_scout_grid_pattern_3(state, row=0, col=3, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_0_90_M:
            _place_scout_grid_pattern_3(state, row=1, col=0, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_1_90_M:
            _place_scout_grid_pattern_3(state, row=1, col=1, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_2_90_M:
            _place_scout_grid_pattern_3(state, row=1, col=2, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_3_90_M:
            _place_scout_grid_pattern_3(state, row=1, col=3, rotated=True, flipped=True)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_scout_grid_pattern_4_action(state: GameState, action):
    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_0:
            _place_scout_grid_pattern_4(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_1:
            _place_scout_grid_pattern_4(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_2:
            _place_scout_grid_pattern_4(state, row=0, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_0:
            _place_scout_grid_pattern_4(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_1:
            _place_scout_grid_pattern_4(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_2:
            _place_scout_grid_pattern_4(state, row=1, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_0:
            _place_scout_grid_pattern_4(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_1:
            _place_scout_grid_pattern_4(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_2:
            _place_scout_grid_pattern_4(state, row=2, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_0_M:
            _place_scout_grid_pattern_4(state, row=0, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_1_M:
            _place_scout_grid_pattern_4(state, row=0, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_2_M:
            _place_scout_grid_pattern_4(state, row=0, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_0_M:
            _place_scout_grid_pattern_4(state, row=1, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_1_M:
            _place_scout_grid_pattern_4(state, row=1, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_2_M:
            _place_scout_grid_pattern_4(state, row=1, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_0_M:
            _place_scout_grid_pattern_4(state, row=2, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_1_M:
            _place_scout_grid_pattern_4(state, row=2, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_2_M:
            _place_scout_grid_pattern_4(state, row=2, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_0_90:
            _place_scout_grid_pattern_4(state, row=0, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_1_90:
            _place_scout_grid_pattern_4(state, row=0, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_2_90:
            _place_scout_grid_pattern_4(state, row=0, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_3_90:
            _place_scout_grid_pattern_4(state, row=0, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_0_90:
            _place_scout_grid_pattern_4(state, row=1, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_1_90:
            _place_scout_grid_pattern_4(state, row=1, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_2_90:
            _place_scout_grid_pattern_4(state, row=1, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_3_90:
            _place_scout_grid_pattern_4(state, row=1, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_0_90_M:
            _place_scout_grid_pattern_4(state, row=0, col=0, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_1_90_M:
            _place_scout_grid_pattern_4(state, row=0, col=1, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_2_90_M:
            _place_scout_grid_pattern_4(state, row=0, col=2, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_3_90_M:
            _place_scout_grid_pattern_4(state, row=0, col=3, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_0_90_M:
            _place_scout_grid_pattern_4(state, row=1, col=0, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_1_90_M:
            _place_scout_grid_pattern_4(state, row=1, col=1, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_2_90_M:
            _place_scout_grid_pattern_4(state, row=1, col=2, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_3_90_M:
            _place_scout_grid_pattern_4(state, row=1, col=3, rotated=True, flipped=True)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _apply_scout_grid_pattern_5_action(state: GameState, action):
    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0:
            _place_scout_grid_pattern_5(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1:
            _place_scout_grid_pattern_5(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2:
            _place_scout_grid_pattern_5(state, row=0, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0:
            _place_scout_grid_pattern_5(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1:
            _place_scout_grid_pattern_5(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2:
            _place_scout_grid_pattern_5(state, row=1, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_0:
            _place_scout_grid_pattern_5(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_1:
            _place_scout_grid_pattern_5(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_2:
            _place_scout_grid_pattern_5(state, row=2, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_M:
            _place_scout_grid_pattern_5(state, row=0, col=0, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_M:
            _place_scout_grid_pattern_5(state, row=0, col=1, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_M:
            _place_scout_grid_pattern_5(state, row=0, col=2, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_M:
            _place_scout_grid_pattern_5(state, row=1, col=0, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_M:
            _place_scout_grid_pattern_5(state, row=1, col=1, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_M:
            _place_scout_grid_pattern_5(state, row=1, col=2, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_0_M:
            _place_scout_grid_pattern_5(state, row=2, col=0, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_1_M:
            _place_scout_grid_pattern_5(state, row=2, col=1, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_2_M:
            _place_scout_grid_pattern_5(state, row=2, col=2, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_180:
            _place_scout_grid_pattern_5(state, row=0, col=0, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_180:
            _place_scout_grid_pattern_5(state, row=0, col=1, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_180:
            _place_scout_grid_pattern_5(state, row=0, col=2, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_180:
            _place_scout_grid_pattern_5(state, row=1, col=0, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_180:
            _place_scout_grid_pattern_5(state, row=1, col=1, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_180:
            _place_scout_grid_pattern_5(state, row=1, col=2, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_0_180:
            _place_scout_grid_pattern_5(state, row=2, col=0, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_1_180:
            _place_scout_grid_pattern_5(state, row=2, col=1, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_2_180:
            _place_scout_grid_pattern_5(state, row=2, col=2, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_180_M:
            _place_scout_grid_pattern_5(state, row=0, col=0, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_180_M:
            _place_scout_grid_pattern_5(state, row=0, col=1, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_180_M:
            _place_scout_grid_pattern_5(state, row=0, col=2, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_180_M:
            _place_scout_grid_pattern_5(state, row=1, col=0, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_180_M:
            _place_scout_grid_pattern_5(state, row=1, col=1, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_180_M:
            _place_scout_grid_pattern_5(state, row=1, col=2, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_0_180_M:
            _place_scout_grid_pattern_5(state, row=2, col=0, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_1_180_M:
            _place_scout_grid_pattern_5(state, row=2, col=1, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_2_180_M:
            _place_scout_grid_pattern_5(state, row=2, col=2, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_90:
            _place_scout_grid_pattern_5(state, row=0, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_90:
            _place_scout_grid_pattern_5(state, row=0, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_90:
            _place_scout_grid_pattern_5(state, row=0, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_3_90:
            _place_scout_grid_pattern_5(state, row=0, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_90:
            _place_scout_grid_pattern_5(state, row=1, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_90:
            _place_scout_grid_pattern_5(state, row=1, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_90:
            _place_scout_grid_pattern_5(state, row=1, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_3_90:
            _place_scout_grid_pattern_5(state, row=1, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_90_M:
            _place_scout_grid_pattern_5(state, row=0, col=0, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_90_M:
            _place_scout_grid_pattern_5(state, row=0, col=1, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_90_M:
            _place_scout_grid_pattern_5(state, row=0, col=2, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_3_90_M:
            _place_scout_grid_pattern_5(state, row=0, col=3, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_90_M:
            _place_scout_grid_pattern_5(state, row=1, col=0, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_90_M:
            _place_scout_grid_pattern_5(state, row=1, col=1, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_90_M:
            _place_scout_grid_pattern_5(state, row=1, col=2, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_3_90_M:
            _place_scout_grid_pattern_5(state, row=1, col=3, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_270:
            _place_scout_grid_pattern_5(state, row=0, col=0, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_270:
            _place_scout_grid_pattern_5(state, row=0, col=1, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_270:
            _place_scout_grid_pattern_5(state, row=0, col=2, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_3_270:
            _place_scout_grid_pattern_5(state, row=0, col=3, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_270:
            _place_scout_grid_pattern_5(state, row=1, col=0, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_270:
            _place_scout_grid_pattern_5(state, row=1, col=1, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_270:
            _place_scout_grid_pattern_5(state, row=1, col=2, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_3_270:
            _place_scout_grid_pattern_5(state, row=1, col=3, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_270_M:
            _place_scout_grid_pattern_5(state, row=0, col=0, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_270_M:
            _place_scout_grid_pattern_5(state, row=0, col=1, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_270_M:
            _place_scout_grid_pattern_5(state, row=0, col=2, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_3_270_M:
            _place_scout_grid_pattern_5(state, row=0, col=3, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_270_M:
            _place_scout_grid_pattern_5(state, row=1, col=0, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_270_M:
            _place_scout_grid_pattern_5(state, row=1, col=1, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_270_M:
            _place_scout_grid_pattern_5(state, row=1, col=2, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_3_270_M:
            _place_scout_grid_pattern_5(state, row=1, col=3, rotated_reverse=True, flipped_vertical=True)
        case _:
            raise ValueError(f"Unknown action: {action}")


# --- Game rules action validation functions --- #
def get_valid_actions(state):
    return [validate_action(state, action) for action in range(N_ACTIONS)]

def validate_action(state: GameState, action) -> bool:
    if not _has_supplies(state, COSTS.get(action, {})):
        return False
    
    match action:
        # Pick player card for this round
        case action if action in actions.ACTIONS_CARD_ASSIGNMENT:
            return _validate_card_assignment_action(state, action)
        case action if action in actions.ACTIONS_LEFT_SHEET:
            _validate_left_sheet_action(state, action)
        case action if action in actions.ACTIONS_RIGHT_SHEET:
            _validate_right_sheet_action(state, action)
        case action if action in actions.ACTIONS_FOLLOW_UP:
            _validate_follow_up_action(state, action)
        case actions.ACTION_END_ROUND:
            return state.status in [GameStatus.STATUS_MAIN_LOOP, GameStatus.STATUS_USE_FAVOURS]
        case _:
            raise ValueError(f"Invalid action ID: {action}")
    return False

def _validate_card_assignment_action(state: GameState, action) -> bool:
    match action:
        # Pick player card for this round
        case actions.ACTION_CARD_ASSIGNMENT_CHOOSE_LEFT_AS_PATH:
            return state.status == GameStatus.STATUS_CHOOSE_PLAYER_CARD
        case actions.ACTION_CARD_ASSIGNMENT_CHOOSE_RIGHT_AS_PATH:
            return state.status == GameStatus.STATUS_CHOOSE_PLAYER_CARD
        case _:
            raise ValueError(f"Invalid action ID: {action}")
    return False

def _validate_left_sheet_action(state: GameState, action) -> bool:
    if action in actions.ACTIONS_ADVANCE_COHORT:
        return _validate_advance_cohort_action(state, action)

    if state.status != GameStatus.STATUS_MAIN_LOOP:
        return False

    match action:
        case actions.ACTION_ADVANCE_MINING_AND_FORESTING:
            return (state.mining_and_foresting_boxes < NUM_MINING_AND_FORESTING_BOXES)
        case actions.ACTION_ADVANCE_WALL_GUARD:
            return (state.wall_guard_boxes < NUM_WALL_AND_FORT_BOXES)
        case actions.ACTION_ADVANCE_CIPPI:
            return (state.cippi_boxes < state.cippi_boxes_unlocked)
        case actions.ACTION_ADVANCE_WALL:
            return (state.wall_guard_boxes < state.wall_and_fort_boxes_unlocked)
        case actions.ACTION_ADVANCE_FORT_PAY_SOLDIER | actions.ACTION_ADVANCE_FORT_PAY_BUILDER:
            return (state.fort_boxes < state.wall_and_fort_boxes_unlocked)
        case actions.ACTION_BUILD_SMALL_GRANARY:
            return state.small_granary_unlocked and not state.small_granary_built
        case actions.ACTION_BUILD_LARGE_GRANARY:
            return state.large_granary_unlocked and state.small_granary_built and not state.large_granary_built
        case actions.ACTION_USE_TRAINING_GROUNDS:
            return state.training_grounds_available and \
                (state.training_grounds_boxes_available > 0) and \
                (state.wall_guard_boxes < NUM_WALL_AND_FORT_BOXES)
        case actions.ACTION_BUILD_SMALL_HOTEL:
            return state.small_hotel_unlocked and not state.small_hotel_built
        case actions.ACTION_BUILD_LARGE_HOTEL:
            return state.large_hotel_unlocked and state.small_hotel_built and not state.large_hotel_built
        case actions.ACTION_BUILD_SMALL_WORKSHOP:
            return state.small_workshop_unlocked and not state.small_workshop_built
        case actions.ACTION_BUILD_LARGE_WORKSHOP:
            return state.large_workshop_unlocked and state.small_workshop_built and not state.large_workshop_built
        case actions.ACTION_BUILD_SMALL_ROAD:
            return state.small_road_unlocked and not state.small_road_built
        case actions.ACTION_BUILD_LARGE_ROAD:
            return state.large_road_unlocked and state.small_road_built and not state.large_road_built
        case actions.ACTION_USE_FORUM_BUILDER_BUILDER_TO_SERVANT | \
                actions.ACTION_USE_FORUM_BUILDER_BUILDER_TO_CIVILIAN | \
                actions.ACTION_USE_FORUM_SERVANT_SERVANT_TO_BUILDER | \
                actions.ACTION_USE_FORUM_SERVANT_SERVANT_TO_CIVILIAN | \
                actions.ACTION_USE_FORUM_CIVILIAN_CIVILIAN_TO_BUILDER | \
                actions.ACTION_USE_FORUM_CIVILIAN_CIVILIAN_TO_SERVANT | \
                actions.ACTION_USE_FORUM_BUILDER_SERVANT_TO_CIVILIAN | \
                actions.ACTION_USE_FORUM_BUILDER_CIVILIAN_TO_SERVANT | \
                actions.ACTION_USE_FORUM_SERVANT_CIVILIAN_TO_BUILDER:
            return state.forum_available and (state.forum_boxes_available > 0)
        case actions.ACTION_BUILD_LANDMARK_1:
            return state.landmark_1_unlocked and not state.landmark_1_built
        case actions.ACTION_BUILD_LANDMARK_2:
            return state.landmark_2_unlocked and not state.landmark_2_built
        case actions.ACTION_BUILD_LANDMARK_3:
            return state.landmark_3_unlocked and not state.landmark_3_built
        case actions.ACTION_BUILD_LANDMARK_4:
            return state.landmark_4_unlocked and not state.landmark_4_built
        case _:
            raise ValueError(f"Invalid action ID: {action}")
    return False

def _validate_advance_cohort_action(state: GameState, action) -> bool:
    if state.status != GameStatus.STATUS_ADVANCE_COHORT:
        return False

    match action:
        case actions.ACTION_ADVANCE_COHORT_LEFT:
            return (state.left_cohort_boxes < NUM_COHORTS_BOXES)
        case actions.ACTION_ADVANCE_COHORT_CENTER:
            return (state.center_cohort_boxes < NUM_COHORTS_BOXES)
        case actions.ACTION_ADVANCE_COHORT_RIGHT:
            return (state.right_cohort_boxes < NUM_COHORTS_BOXES)
        case _:
            raise ValueError(f"Invalid action ID: {action}")
    return False

def _validate_right_sheet_action(state: GameState, action):
    match action:
        case action if action in actions.ACTIONS_TRADERS:
            return _validate_trader_action(state, action)
        case action if action in actions.ACTIONS_PERFORMERS:
            return _validate_performer_action(state, action)
        case action if action in actions.ACTIONS_PRIESTS:
            return _validate_priest_action(state, action)
        case action if action in actions.ACTIONS_APPARITORES:
            return _validate_apparitore_action(state, action)
        case action if action in actions.ACTIONS_PATRICIANS:
            return _validate_patrician_action(state, action)
        case _:
            raise ValueError(f"Unknown action: {action}")
    return False

def _validate_follow_up_action(state: GameState, action):
    match action:
        case actions.ACTION_ENFORCE_LEFT_COHORT:
            return (state.status == GameStatus.STATUS_ADVANCE_COHORT) and \
                (state.left_cohort_boxes < NUM_COHORTS_BOXES)
        case actions.ACTION_ENFORCE_CENTER_COHORT:
            return (state.status == GameStatus.STATUS_ADVANCE_COHORT) and \
                (state.center_cohort_boxes < NUM_COHORTS_BOXES)
        case actions.ACTION_ENFORCE_RIGHT_COHORT:
            return (state.status == GameStatus.STATUS_ADVANCE_COHORT) and \
                (state.right_cohort_boxes < NUM_COHORTS_BOXES)
        case actions.ACTION_RECEIVE_ATTRIBUTE_RENOWN:
            return (state.status in [GameStatus.STATUS_CHOOSE_RENOWN_OR_VALOUR, \
                    GameStatus.STATUS_CHOOSE_TWO_ATTRIBUTES, \
                    GameStatus.STATUS_CHOOSE_ATTRIBUTE]) and \
                state.renown_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK
        case actions.ACTION_RECEIVE_ATTRIBUTE_PIETY:
            return (state.status in [GameStatus.STATUS_CHOOSE_PIETY_OR_DISCIPLINE, \
                    GameStatus.STATUS_CHOOSE_TWO_ATTRIBUTES, \
                    GameStatus.STATUS_CHOOSE_ATTRIBUTE]) and \
                state.piety_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK
        case actions.ACTION_RECEIVE_ATTRIBUTE_VALOUR:
            return (state.status in [GameStatus.STATUS_CHOOSE_RENOWN_OR_VALOUR, \
                    GameStatus.STATUS_CHOOSE_TWO_ATTRIBUTES, \
                    GameStatus.STATUS_CHOOSE_ATTRIBUTE]) and \
                state.valour_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK
        case actions.ACTION_RECEIVE_ATTRIBUTE_DISCIPLINE:
            return (state.status in [GameStatus.STATUS_CHOOSE_PIETY_OR_DISCIPLINE, \
                    GameStatus.STATUS_CHOOSE_TWO_ATTRIBUTES, \
                    GameStatus.STATUS_CHOOSE_ATTRIBUTE]) and \
                state.dicipline_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK
        case actions.ACTION_USE_LEFT_FAVOUR:
            return state.status == GameStatus.STATUS_USE_FAVOURS and \
                state.num_left_cohort_favours > 0 and \
                state.left_cohort_incoming_disdain >= 1
        case actions.ACTION_USE_CENTER_FAVOUR:
            return state.status == GameStatus.STATUS_USE_FAVOURS and \
                state.num_center_cohort_favours > 0 and \
                state.center_cohort_incoming_disdain >= 1
        case actions.ACTION_USE_RIGHT_FAVOUR:
            return state.status == GameStatus.STATUS_USE_FAVOURS and \
                state.num_right_cohort_favours > 0 and \
                state.right_cohort_incoming_disdain >= 1
        case actions.ACTION_USE_GENERAL_FAVOUR_LEFT:
            return state.status == GameStatus.STATUS_USE_FAVOURS and \
                state.num_general_favours > 0 and \
                state.left_cohort_incoming_disdain >= 1
        case actions.ACTION_USE_GENERAL_FAVOUR_CENTER:
            return state.status == GameStatus.STATUS_USE_FAVOURS and \
                state.num_general_favours > 0 and \
                state.center_cohort_incoming_disdain >= 1
        case actions.ACTION_USE_GENERAL_FAVOUR_RIGHT:
            return state.status == GameStatus.STATUS_USE_FAVOURS and \
                state.num_general_favours > 0 and \
                state.right_cohort_incoming_disdain >= 1
        case _:
            raise ValueError(f"Unknown action: {action}")
    return False

def _validate_trader_action(state: GameState, action) -> bool:
    if state.status != GameStatus.STATUS_MAIN_LOOP:
        return False
    
    match action:
        case actions.ACTION_ADVANCE_TRADERS_TRACK:
            return (state.traders_track_boxes < NUM_CITIZEN_TRACK_BOXES)
        case actions.ACTION_BUILD_SMALL_PRECINCT:
            return state.small_precinct_unlocked and not state.small_precinct_built
        case actions.ACTION_BUILD_MEDIUM_PRECINCT:
            return state.medium_precinct_unlocked and state.small_precinct_built and not state.medium_precinct_built
        case actions.ACTION_BUILD_LARGE_PRECINCT:
            return state.large_precinct_unlocked and state.medium_precinct_built and not state.large_precinct_built
        case actions.ACTION_BUILD_MARKET:
            return state.market_unlocked and not state.market_built
        case actions.ACTION_BUY_GOODS_FATE_CARD | actions.ACTION_BUY_GOODS_NEIGHBOR_CARD_1 | actions.ACTION_BUY_GOODS_NEIGHBOR_CARD_2:
            index = state.get_next_free_market_box()
            if not state.market_built or (index is None):
                return False
            return (index != TRADERS_MARKET_SERVANT_BOX - 1) and \
                (index != TRADERS_MARKET_BUILDER_BOX - 1)
        case actions.ACTION_BUY_GOODS_7_FATE_CARD | actions.ACTION_BUY_GOODS_7_NEIGHBOR_CARD_1 | actions.ACTION_BUY_GOODS_7_NEIGHBOR_CARD_2:
            return state.market_built and state.market_boxes_unlocked >= TRADERS_MARKET_SERVANT_BOX and not state.market_boxes[TRADERS_MARKET_SERVANT_BOX - 1]
        case actions.ACTION_BUY_GOODS_8_FATE_CARD | actions.ACTION_BUY_GOODS_8_NEIGHBOR_CARD_1 | actions.ACTION_BUY_GOODS_8_NEIGHBOR_CARD_2:
            return state.market_built and state.market_boxes_unlocked >= TRADERS_MARKET_BUILDER_BOX and not state.market_boxes[TRADERS_MARKET_BUILDER_BOX - 1]
        case _:
            raise ValueError(f"Unknown action: {action}")
    return False

def _validate_performer_action(state: GameState, action) -> bool:
    if state.status != GameStatus.STATUS_MAIN_LOOP:
        return False
    
    match action:
        case actions.ACTION_ADVANCE_PERFORMERS_TRACK:
            return (state.performers_track_boxes < NUM_CITIZEN_TRACK_BOXES)
        case actions.ACTION_BUILD_THEATER:
            return state.theater_unlocked and not state.theater_built
        case actions.ACTION_ARRANGE_PERFORMANCE_1:
            return state.theater_built and state.theater_boxes_unlocked >= 1 and not state.theater_boxes[0] and state.theater_available
        case actions.ACTION_ARRANGE_PERFORMANCE_2:
            return state.theater_built and state.theater_boxes_unlocked >= 2 and not state.theater_boxes[1] and state.theater_available
        case actions.ACTION_ARRANGE_PERFORMANCE_3:
            return state.theater_built and state.theater_boxes_unlocked >= 3 and not state.theater_boxes[2] and state.theater_available
        case actions.ACTION_ARRANGE_PERFORMANCE_4:
            return state.theater_built and state.theater_boxes_unlocked >= 4 and not state.theater_boxes[3] and state.theater_available
        case actions.ACTION_ARRANGE_PERFORMANCE_5:
            return state.theater_built and state.theater_boxes_unlocked >= 5 and not state.theater_boxes[4] and state.theater_available
        case actions.ACTION_ARRANGE_PERFORMANCE_6:
            return state.theater_built and state.theater_boxes_unlocked >= 6 and not state.theater_boxes[5] and state.theater_available
        case actions.ACTION_BUILD_COLOSSEUM:
            return state.colosseum_unlocked and not state.colosseum_built
        case actions.ACTION_TRAIN_GLADIATOR_1_SERVANT | actions.ACTION_TRAIN_GLADIATOR_1_CIVILIAN:
            return state.colosseum_built and \
                state.is_gladiator_1_alive() and \
                (state.gladiator_1_strength < state.gladiator_boxes_unlocked)
        case actions.ACTION_TRAIN_GLADIATOR_1_SERVANT_AND_FIGHT | actions.ACTION_TRAIN_GLADIATOR_1_CIVILIAN_AND_FIGHT:
            return state.colosseum_built and \
                state.is_gladiator_1_alive() and \
                state.gladiator_1_can_battle and \
                (state.gladiator_1_strength < state.gladiator_boxes_unlocked)
        case actions.ACTION_TRAIN_GLADIATOR_2_SERVANT | actions.ACTION_TRAIN_GLADIATOR_2_CIVILIAN:
            return state.colosseum_built and \
                state.is_gladiator_2_alive() and \
                (state.gladiator_2_strength < state.gladiator_boxes_unlocked)
        case actions.ACTION_TRAIN_GLADIATOR_2_SERVANT_AND_FIGHT | actions.ACTION_TRAIN_GLADIATOR_2_CIVILIAN_AND_FIGHT:
            return state.colosseum_built and \
                state.is_gladiator_2_alive() and \
                state.gladiator_2_can_battle and \
                (state.gladiator_2_strength < state.gladiator_boxes_unlocked)
        case _:
            raise ValueError(f"Unknown action: {action}")
    return False

def _validate_priest_action(state: GameState, action) -> bool:
    if state.status != GameStatus.STATUS_MAIN_LOOP:
        return False
    
    match action:
        case actions.ACTION_ADVANCE_PRIESTS_TRACK:
            return (state.priests_track_boxes < NUM_CITIZEN_TRACK_BOXES)
        case actions.ACTION_BUILD_SMALL_GARDEN:
            return state.small_garden_unlocked and not state.small_garden_built
        case actions.ACTION_BUILD_LARGE_GARDEN:
            return state.large_garden_unlocked and state.small_garden_built and not state.large_garden_built
        case actions.ACTION_BUILD_SMALL_TEMPLE:
            return state.small_temple_unlocked and not state.small_temple_built
        case actions.ACTION_FILL_SMALL_TEMPLE_SOLDIER | \
                actions.ACTION_FILL_SMALL_TEMPLE_BUILDER | \
                actions.ACTION_FILL_SMALL_TEMPLE_SERVANT | \
                actions.ACTION_FILL_SMALL_TEMPLE_CIVILIAN:
            return state.small_temple_built and not state.is_small_temple_filled()
        case actions.ACTION_BUILD_MEDIUM_TEMPLE:
            return state.medium_temple_unlocked and state.small_temple_built and not state.medium_temple_built
        case actions.ACTION_FILL_MEDIUM_TEMPLE_SOLDIER | \
                actions.ACTION_FILL_MEDIUM_TEMPLE_BUILDER | \
                actions.ACTION_FILL_MEDIUM_TEMPLE_SERVANT | \
                actions.ACTION_FILL_MEDIUM_TEMPLE_CIVILIAN:
            return state.medium_temple_built and \
                state.is_small_temple_filled() and \
                (state.medium_temple_boxes < state.medium_temple_boxes_unlocked)
        case actions.ACTION_BUILD_LARGE_TEMPLE:
            return state.large_temple_unlocked and state.medium_temple_built and not state.large_temple_built
        case actions.ACTION_FILL_LARGE_TEMPLE_SOLDIER | \
                actions.ACTION_FILL_LARGE_TEMPLE_BUILDER | \
                actions.ACTION_FILL_LARGE_TEMPLE_SERVANT | \
                actions.ACTION_FILL_LARGE_TEMPLE_CIVILIAN:
            return state.large_temple_built and \
                state.is_medium_temple_filled() and \
                (state.large_temple_boxes < state.large_temple_boxes_unlocked)
        case _:
            raise ValueError(f"Unknown action: {action}")
    return False

def _validate_apparitore_action(state: GameState, action) -> bool:
    if state.status != GameStatus.STATUS_MAIN_LOOP:
        return False
    
    match action:
        case actions.ACTION_ADVANCE_APPARITORES_TRACK:
            return (state.apparitores_track_boxes < NUM_CITIZEN_TRACK_BOXES)
        case actions.ACTION_BUILD_BATHS:
            return state.baths_unlocked and not state.baths_built
        case actions.ACTION_PAY_BRIBE:
            return state.baths_built and \
                (state.baths_boxes_available > 0) and \
                (state.baths_boxes < state.baths_boxes_unlocked)
        case actions.ACTION_BUILD_COURTHOUSE:
            return state.courthouse_unlocked and not state.courthouse_built
        case actions.ACTION_COURTHOUSE_GET_SERVANT:
            return state.courthouse_built and \
                state.courthouse_get_servant_available and \
                (state.courthouse_get_servant_boxes < state.courthouse_get_servant_unlocked)
        case actions.ACTION_COURTHOUSE_BUILDER_TO_TWO_SERVANTS:
            return state.courthouse_built and \
                state.courthouse_builder_to_two_servants_available and \
                (state.courthouse_builder_to_two_servants_boxes < state.courthouse_builder_to_two_servants_unlocked)
        case actions.ACTION_COURTHOUSE_SERVANT_TO_BUILDER:
            return state.courthouse_built and \
                state.courthouse_servant_to_builder_available and \
                (state.courthouse_servant_to_builder_boxes < state.courthouse_servant_to_builder_unlocked)
        case _:
            raise ValueError(f"Unknown action: {action}")
    return False

def _validate_patrician_action(state: GameState, action) -> bool:
    match action:
        case actions.ACTION_ADVANCE_PATRICIANS_TRACK:
            return (state.status == GameStatus.STATUS_MAIN_LOOP) and \
                (state.patricians_track_boxes < NUM_CITIZEN_TRACK_BOXES)
        case actions.ACTION_SEND_LEFT_DIPLOMAT:
            return (state.status == GameStatus.STATUS_MAIN_LOOP) and \
                state.diplomat_left_available and \
                state.has_diplomat_box_available()
        case actions.ACTION_SEND_CENTER_DIPLOMAT:
            return (state.status == GameStatus.STATUS_MAIN_LOOP) and \
                state.diplomat_center_available and \
                state.has_diplomat_box_available()
        case actions.ACTION_SEND_RIGHT_DIPLOMAT:
            return (state.status == GameStatus.STATUS_MAIN_LOOP) and \
                state.diplomat_right_available and \
                state.has_diplomat_box_available()
        case actions.ACTION_SEND_SCOUT_PROSPECT_CARD:
            if (state.status != GameStatus.STATUS_MAIN_LOOP) or \
                (state.scouts_boxes >= state.scouts_boxes_unlocked):
                return False
            pattern_id = state.get_current_prospect_card_scout_pattern_id()
            return _has_any_valid_scout_pattern_placement(pattern_id)
        case actions.ACTION_SEND_SCOUT_NEIGHBOR_CARD_1:
            if (state.status != GameStatus.STATUS_MAIN_LOOP) or \
                (state.scouts_boxes >= state.scouts_boxes_unlocked):
                return False
            pattern_id = state.get_neighbor_prospect_card_1_scout_pattern_id()
            return _has_any_valid_scout_pattern_placement(pattern_id)
        case actions.ACTION_SEND_SCOUT_NEIGHBOR_CARD_2:
            if (state.status != GameStatus.STATUS_MAIN_LOOP) or \
                (state.scouts_boxes >= state.scouts_boxes_unlocked):
                return False
            pattern_id = state.get_neighbor_prospect_card_2_scout_pattern_id()
            return _has_any_valid_scout_pattern_placement(pattern_id)
        case action if action in actions.ACTIONS_SCOUTS:
            return _validate_scout_grid_pattern_action(state, action)
        case _:
            raise ValueError(f"Unknown action: {action}")
    return False

def _validate_scout_grid_pattern_action(state: GameState, action) -> bool:
    if (state.status != GameStatus.STATUS_SEND_SCOUT):
        return False

    match action:
        case actions.ACTION_SEND_SCOUT_GRID_1:
            return _validate_scout_grid_pattern_1_action(state, action)
        case actions.ACTION_SEND_SCOUT_GRID_2:
            return _validate_scout_grid_pattern_2_action(state, action)
        case actions.ACTION_SEND_SCOUT_GRID_3:
            return _validate_scout_grid_pattern_3_action(state, action)
        case actions.ACTION_SEND_SCOUT_GRID_4:
            return _validate_scout_grid_pattern_4_action(state, action)
        case actions.ACTION_SEND_SCOUT_GRID_5:
            return _validate_scout_grid_pattern_5_action(state, action)
        case _:
            raise ValueError(f"Unknown action: {action}")
    return False

def _validate_scout_grid_pattern_1_action(state: GameState, action) -> bool:
    if state.chosen_scout_pattern != 1:
        return False

    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_0_0:
            return _is_valid_scout_pattern_placement_1(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_0_1:
            return _is_valid_scout_pattern_placement_1(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_0_2:
            return _is_valid_scout_pattern_placement_1(state, row=0, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_0_3:
            return _is_valid_scout_pattern_placement_1(state, row=0, col=3)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_1_0:
            return _is_valid_scout_pattern_placement_1(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_1_1:
            return _is_valid_scout_pattern_placement_1(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_1_2:
            return _is_valid_scout_pattern_placement_1(state, row=1, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_1_3:
            return _is_valid_scout_pattern_placement_1(state, row=1, col=3)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_2_0:
            return _is_valid_scout_pattern_placement_1(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_2_1:
            return _is_valid_scout_pattern_placement_1(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_2_2:
            return _is_valid_scout_pattern_placement_1(state, row=2, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_1_POSITION_2_3:
            return _is_valid_scout_pattern_placement_1(state, row=2, col=3)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _validate_scout_grid_pattern_2_action(state: GameState, action) -> bool:
    if state.chosen_scout_pattern != 2:
        return False

    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_0:
            return _is_valid_scout_pattern_placement_2(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_1:
            return _is_valid_scout_pattern_placement_2(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_1_0:
            return _is_valid_scout_pattern_placement_2(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_1_1:
            return _is_valid_scout_pattern_placement_2(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_2_0:
            return _is_valid_scout_pattern_placement_2(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_2_1:
            return _is_valid_scout_pattern_placement_2(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_3_0:
            return _is_valid_scout_pattern_placement_2(state, row=3, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_3_1:
            return _is_valid_scout_pattern_placement_2(state, row=3, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_0_90:
            return _is_valid_scout_pattern_placement_2(state, row=0, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_1_90:
            return _is_valid_scout_pattern_placement_2(state, row=0, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_2_90:
            return _is_valid_scout_pattern_placement_2(state, row=0, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_3_90:
            return _is_valid_scout_pattern_placement_2(state, row=0, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_2_POSITION_0_4_90:
            return _is_valid_scout_pattern_placement_2(state, row=0, col=4, rotated=True)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _validate_scout_grid_pattern_3_action(state: GameState, action) -> bool:
    if state.chosen_scout_pattern != 3:
        return False

    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_0:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_1:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_2:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_0:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_1:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_2:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_0:
            return _is_valid_scout_pattern_placement_3(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_1:
            return _is_valid_scout_pattern_placement_3(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_2:
            return _is_valid_scout_pattern_placement_3(state, row=2, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_0_M:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_1_M:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_2_M:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_0_M:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_1_M:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_2_M:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_0_M:
            return _is_valid_scout_pattern_placement_3(state, row=2, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_1_M:
            return _is_valid_scout_pattern_placement_3(state, row=2, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_2_2_M:
            return _is_valid_scout_pattern_placement_3(state, row=2, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_0_90:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_1_90:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_2_90:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_3_90:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_0_90:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_1_90:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_2_90:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_3_90:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_0_90_M:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=0, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_1_90_M:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=1, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_2_90_M:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=2, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_0_3_90_M:
            return _is_valid_scout_pattern_placement_3(state, row=0, col=3, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_0_90_M:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=0, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_1_90_M:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=1, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_2_90_M:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=2, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_3_POSITION_1_3_90_M:
            return _is_valid_scout_pattern_placement_3(state, row=1, col=3, rotated=True, flipped=True)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _validate_scout_grid_pattern_4_action(state: GameState, action) -> bool:
    if state.chosen_scout_pattern != 4:
        return False
    
    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_0:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_1:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_2:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_0:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_1:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_2:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_0:
            return _is_valid_scout_pattern_placement_4(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_1:
            return _is_valid_scout_pattern_placement_4(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_2:
            return _is_valid_scout_pattern_placement_4(state, row=2, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_0_M:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_1_M:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_2_M:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_0_M:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_1_M:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_2_M:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_0_M:
            return _is_valid_scout_pattern_placement_4(state, row=2, col=0, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_1_M:
            return _is_valid_scout_pattern_placement_4(state, row=2, col=1, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_2_2_M:
            return _is_valid_scout_pattern_placement_4(state, row=2, col=2, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_0_90:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_1_90:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_2_90:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_3_90:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_0_90:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_1_90:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_2_90:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_3_90:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_0_90_M:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=0, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_1_90_M:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=1, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_2_90_M:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=2, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_0_3_90_M:
            return _is_valid_scout_pattern_placement_4(state, row=0, col=3, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_0_90_M:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=0, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_1_90_M:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=1, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_2_90_M:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=2, rotated=True, flipped=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_4_POSITION_1_3_90_M:
            return _is_valid_scout_pattern_placement_4(state, row=1, col=3, rotated=True, flipped=True)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _validate_scout_grid_pattern_5_action(state: GameState, action) -> bool:
    if state.chosen_scout_pattern != 5:
        return False
    
    match action:
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_0:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=0)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_1:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=1)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_2:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=2)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=0, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=1, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=2, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=0, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=1, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=2, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_0_M:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=0, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_1_M:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=1, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_2_M:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=2, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_180:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=0, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_180:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=1, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_180:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=2, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_180:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=0, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_180:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=1, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_180:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=2, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_0_180:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=0, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_1_180:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=1, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_2_180:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=2, flipped_horizontal=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_180_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=0, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_180_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=1, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_180_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=2, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_180_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=0, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_180_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=1, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_180_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=2, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_0_180_M:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=0, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_1_180_M:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=1, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_2_2_180_M:
            return _is_valid_scout_pattern_placement_5(state, row=2, col=2, flipped_horizontal=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_90:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_90:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_90:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_3_90:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_90:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=0, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_90:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=1, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_90:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=2, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_3_90:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=3, rotated=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_90_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=0, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_90_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=1, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_90_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=2, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_3_90_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=3, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_90_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=0, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_90_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=1, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_90_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=2, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_3_90_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=3, rotated=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_270:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=0, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_270:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=1, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_270:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=2, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_3_270:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=3, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_270:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=0, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_270:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=1, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_270:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=2, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_3_270:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=3, rotated_reverse=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_0_270_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=0, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_1_270_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=1, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_2_270_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=2, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_0_3_270_M:
            return _is_valid_scout_pattern_placement_5(state, row=0, col=3, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_0_270_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=0, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_1_270_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=1, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_2_270_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=2, rotated_reverse=True, flipped_vertical=True)
        case actions.ACTION_PLACE_SCOUT_PATTERN_5_POSITION_1_3_270_M:
            return _is_valid_scout_pattern_placement_5(state, row=1, col=3, rotated_reverse=True, flipped_vertical=True)
        case _:
            raise ValueError(f"Unknown action: {action}")

def _has_any_valid_scout_pattern_placement(pattern_id) -> bool:
    match pattern_id:
        case 1:
            return _has_any_valid_scout_pattern_placement_1()
        case 2:
            return _has_any_valid_scout_pattern_placement_2()
        case 3:
            return _has_any_valid_scout_pattern_placement_3()
        case 4:
            return _has_any_valid_scout_pattern_placement_4()
        case 5:
            return _has_any_valid_scout_pattern_placement_5()
        case _:
            raise ValueError(f"Unknown scout pattern: {pattern_id}")
        
def _has_any_valid_scout_pattern_placement_1() -> bool:
    return any([_validate_scout_grid_pattern_1_action(a) for a in actions.ACTIONS_SCOUTS_PATTERN_1])

def _has_any_valid_scout_pattern_placement_2() -> bool:
    return any([_validate_scout_grid_pattern_2_action(a) for a in actions.ACTIONS_SCOUTS_PATTERN_2])

def _has_any_valid_scout_pattern_placement_3() -> bool:
    return any([_validate_scout_grid_pattern_3_action(a) for a in actions.ACTIONS_SCOUTS_PATTERN_3])

def _has_any_valid_scout_pattern_placement_4() -> bool:
    return any([_validate_scout_grid_pattern_4_action(a) for a in actions.ACTIONS_SCOUTS_PATTERN_4])

def _has_any_valid_scout_pattern_placement_5() -> bool:
    return any([_validate_scout_grid_pattern_5_action(a) for a in actions.ACTIONS_SCOUTS_PATTERN_5])


# Supply management
def _has_supplies(state, costs: Dict[str, int]) -> bool:
    return (state.num_soldiers >= costs.get("soldiers", 0)) and \
            (state.num_builders >= costs.get("builders", 0)) and \
            (state.num_servants >= costs.get("servants", 0)) and \
            (state.num_civilians >= costs.get("civilians", 0)) and \
            (state.num_resources >= costs.get("resources", 0))

def _pay_from_supply(state, costs: Dict[str, int]):
    if costs.get("soldiers", 0) > 0:
        assert(state.num_soldiers >= costs["soldiers"], "Not enough soldiers to pay the cost")
        state.num_soldiers -= costs["soldiers"]
    if costs.get("builders", 0) > 0:
        assert(state.num_builders >= costs["builders"], "Not enough builders to pay the cost")
        state.num_builders -= costs["builders"]
    if costs.get("civilians", 0) > 0:
        assert(state.num_civilians >= costs["civilians"], "Not enough civilians to pay the cost")
        state.num_civilians -= costs["civilians"]
    if costs.get("servants", 0) > 0:
        assert(state.num_servants >= costs["servants"], "Not enough servants to pay the cost")
        state.num_servants -= costs["servants"]
    if costs.get("resources", 0) > 0:
        assert(state.num_resources >= costs["resources"], "Not enough resources to pay the cost")
        state.num_resources -= costs["resources"]

def _add_resource_production_box(state: GameState):
    assert(state.resource_production_boxes < RESOURCE_PRODUCTION_BOXES, "All resource production boxes are already filled")
    state.resource_production_boxes += 1

def _reset_resources(state: GameState):
    state.num_soldiers = 0
    state.num_builders = 0
    state.num_servants = 0
    state.num_civilians = 0
    state.num_resources = 0

def _add_resource_from_fate_card(state: GameState):
    state.num_soldiers += state.get_current_fate_card_num_soldiers()
    state.num_builders += state.get_current_fate_card_num_builders()
    state.num_servants += state.get_current_fate_card_num_servants()
    state.num_civilians += state.get_current_fate_card_num_civilians()
    state.num_resources += state.get_current_fate_card_num_resources()

def _add_resources_from_prospect_card(state: GameState):
    state.num_soldiers += state.get_current_prospect_card_num_soldiers()
    state.num_builders += state.get_current_prospect_card_num_builders()
    state.num_servants += state.get_current_prospect_card_num_servants()
    state.num_civilians += state.get_current_prospect_card_num_civilians()
    state.num_resources += state.get_current_prospect_card_num_resources()

def _add_resource_from_left_sheet(state: GameState):
    state.num_resources += state.resource_production_boxes
    if state.large_hotel_built:
        state.num_civilians += 2
    elif state.small_hotel_built:
        state.num_civilians += 1
    if state.large_workshop_built:
        state.num_builders += 2
    elif state.small_workshop_built:
        state.num_builders += 1


# Choose player cards for path and prospect
def _add_left_player_card_to_path(state: GameState):
    assert(state.status == GameStatus.STATUS_CHOOSE_PLAYER_CARD, "The game status is not correct")
    assert(state.left_player_card_id is not None, "There has to be one left card to choose from")
    assert(state.right_player_card_id is not None, "There has to be one right card to choose from")
    state.player_card_is_path_card[state.left_player_card_id] = True
    state.current_prospect_card_id = state.right_player_card_id
    state.draw_neighbor_cards()
    _add_resources_from_prospect_card(state)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _add_right_player_card_to_path(state: GameState):
    assert(state.status == GameStatus.STATUS_CHOOSE_PLAYER_CARD, "The game status is not correct")
    assert(state.left_player_card_id is not None, "There has to be one left card to choose from")
    assert(state.right_player_card_id is not None, "There has to be one right card to choose from")
    state.player_card_is_path_card[state.right_player_card_id] = True
    state.current_prospect_card_id = state.left_player_card_id
    state.draw_neighbor_cards()
    _add_resources_from_prospect_card(state)
    state.status = GameStatus.STATUS_MAIN_LOOP


# Cohorts
def _add_cohort_left(state: GameState):
    assert(state.status == GameStatus.STATUS_ADVANCE_COHORT, "The game status is not correct")
    assert(state.left_cohort_boxes < NUM_COHORTS_BOXES, "All left cohort boxes are already filled")
    state.left_cohort_boxes += 1
    if state.left_cohort_boxes in COHORT_DICIPLINE_THRESHOLDS:
        _add_dicipline_attribute_point(state)
    if state.left_cohort_boxes in COHORT_VALOUR_THRESHOLDS:
        _add_valour_attribute_point(state)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _add_cohort_center(state: GameState):
    assert(state.status == GameStatus.STATUS_ADVANCE_COHORT, "The game status is not correct")
    assert(state.center_cohort_boxes < NUM_COHORTS_BOXES, "All center cohort boxes are already filled")
    state.center_cohort_boxes += 1
    if state.center_cohort_boxes in COHORT_DICIPLINE_THRESHOLDS:
        _add_dicipline_attribute_point(state)
    if state.center_cohort_boxes in COHORT_VALOUR_THRESHOLDS:
        _add_valour_attribute_point(state)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _add_cohort_right(state: GameState):
    assert(state.status == GameStatus.STATUS_ADVANCE_COHORT, "The game status is not correct")
    assert(state.right_cohort_boxes < NUM_COHORTS_BOXES, "All right cohort boxes are already filled")
    state.right_cohort_boxes += 1
    if state.right_cohort_boxes in COHORT_DICIPLINE_THRESHOLDS:
        _add_dicipline_attribute_point(state)
    if state.right_cohort_boxes in COHORT_VALOUR_THRESHOLDS:
        _add_valour_attribute_point(state)
    state.status = GameStatus.STATUS_MAIN_LOOP


# Left sheet
def _advance_mining_and_foresting(state: GameState):
    assert(state.mining_and_foresting_boxes < NUM_MINING_AND_FORESTING_BOXES, "All mining and foresting boxes are already filled")
    state.mining_and_foresting_boxes += 1
    if state.mining_and_foresting_boxes in MINING_AND_FORESTING_THRESHOLDS:
        state.num_resources += 1
        _add_resource_production_box(state)

def _advance_wall_guard(state: GameState):
    assert(state.wall_guard_boxes < NUM_WALL_GUARD_BOXES, "All wall guard boxes are already filled")
    state.wall_guard_boxes += 1
    if state.wall_guard_boxes in WALL_GUARD_DICIPLINE_THRESHOLDS:
        _add_dicipline_attribute_point(state)
    elif state.wall_guard_boxes in WALL_GUARD_COHORT_THRESHOLDS:
        state.status = GameStatus.STATUS_ADVANCE_COHORT

def _advance_cippi(state: GameState):
    assert(state.cippi_boxes < NUM_CIPPI_BOXES, "All cippi boxes are already filled")
    assert(state.cippi_boxes < state.cippi_boxes_unlocked, "The next cippi box is not unlocked yet")
    state.cippi_boxes += 1
    if state.cippi_boxes in CIPPI_COHORT_THRESHOLDS:
        state.status = GameStatus.STATUS_ADVANCE_COHORT
    elif state.cippi_boxes in CIPPI_CIVILIAN_THRESHOLDS:
        state.num_civilians += 1
    elif state.cippi_boxes in CIPPI_RENOWN_THRESHOLDS:
        _add_renown_attribute_point(state)

def _advance_wall(state: GameState):
    assert(state.wall_boxes < NUM_WALL_AND_FORT_BOXES, "All wall and fort boxes are already filled")
    assert(state.wall_boxes < state.wall_and_fort_boxes_unlocked, "The next wall box is not unlocked yet")
    state.wall_boxes += 1
    if state.wall_boxes in WALL_CITICIAN_THRESHOLDS:
        state.num_civilians += 1
    else:
        if state.wall_boxes in WALL_RENOWN_THRESHOLDS:
            _add_renown_attribute_point(state)
        if state.wall_boxes in WALL_COHORT_THRESHOLDS:
            state.status = GameStatus.STATUS_ADVANCE_COHORT

def _advance_fort(state: GameState):
    assert(state.fort_boxes < NUM_WALL_AND_FORT_BOXES, "All wall and fort boxes are already filled")
    assert(state.fort_boxes < state.wall_and_fort_boxes_unlocked, "The next fort box is not unlocked yet")
    state.fort_boxes += 1
    if state.fort_boxes in CIPPI_FORT_SECTION_THRESHOLDS:
        state.cippi_boxes_unlocked += 1
    
    if state.fort_boxes in FORT_INFRASTRUCTURE_THRESHOLDS:
        assert(state.infrastructure_level < MAX_INFRASTRUCTURE_LEVEL, "Infrastructure level is already at maximum")
        state.infrastructure_level += 1
        state.small_granary_unlocked = state.small_granary_unlocked or (state.infrastructure_level >= SMALL_GRANARY_INFRASTRUCTURE_THRESHOLD)
        state.large_granary_unlocked = state.large_granary_unlocked or (state.infrastructure_level >= LARGE_GRANARY_INFRASTRUCTURE_THRESHOLD)
        state.small_hotel_unlocked = state.small_hotel_unlocked or (state.infrastructure_level >= SMALL_HOTEL_INFRASTRUCTURE_THRESHOLD)
        state.large_hotel_unlocked = state.large_hotel_unlocked or (state.infrastructure_level >= LARGE_HOTEL_INFRASTRUCTURE_THRESHOLD)
        state.small_workshop_unlocked = state.small_workshop_unlocked or (state.infrastructure_level >= SMALL_WORKSHOP_INFRASTRUCTURE_THRESHOLD)
        state.large_workshop_unlocked = state.large_workshop_unlocked or (state.infrastructure_level >= LARGE_WORKSHOP_INFRASTRUCTURE_THRESHOLD)
        state.small_road_unlocked = state.small_road_unlocked or (state.infrastructure_level >= SMALL_ROAD_INFRASTRUCTURE_THRESHOLD)
        state.large_road_unlocked = state.large_road_unlocked or (state.infrastructure_level >= LARGE_ROAD_INFRASTRUCTURE_THRESHOLD)
    elif state.fort_boxes in FORT_CITICIAN_THRESHOLDS:
        state.num_civilians += 1
    else:
        if state.fort_boxes in FORT_DICIPLINE_THRESHOLDS:
            _add_dicipline_attribute_point(state)
        if state.fort_boxes in FORT_COHORT_THRESHOLDS:
            state.status = GameStatus.STATUS_ADVANCE_COHORT

def _build_small_granary(state: GameState):
    assert(state.small_granary_unlocked, "Small granary action is not unlocked yet")
    assert(state.infrastructure_level >= SMALL_GRANARY_INFRASTRUCTURE_THRESHOLD, "Infrastructure level is not high enough to build the small granary")
    assert(state.small_granary_built == False, "Small granary is already built")
    state.small_granary_built = True
    state.fort_and_wall_boxes_unlocked = max(state.fort_and_wall_boxes_unlocked, SMALL_GRANARY_FORT_AND_WALL_UNLOCK)

def _build_large_granary(state: GameState):
    assert(state.large_granary_unlocked, "Large granary action is not unlocked yet")
    assert(state.infrastructure_level >= LARGE_GRANARY_INFRASTRUCTURE_THRESHOLD, "Infrastructure level is not high enough to build the large granary")
    assert(state.small_granary_built == True, "Small granary must be built before building the large granary")
    assert(state.large_granary_built == False, "Large granary is already built")
    state.large_granary_built = True
    state.fort_and_wall_boxes_unlocked = max(state.fort_and_wall_boxes_unlocked, LARGE_GRANARY_FORT_AND_WALL_UNLOCK)
    _add_renown_attribute_point(state)

def _use_training_grounds(state: GameState):
    assert(state.training_grounds_available, "Training grounds action is not available")
    assert(state.training_grounds_boxes < NUM_TRAINING_GROUNDS_BOXES, "All training grounds boxes are already filled")
    state.training_grounds_boxes += 1
    state.training_grounds_available = False
    state.training_grounds_rounds.append(state.current_round)
    _advance_wall_guard(state)

def _build_small_hotel(state: GameState):
    assert(state.small_hotel_unlocked, "Small hotel action is not unlocked yet")
    assert(state.infrastructure_level >= SMALL_HOTEL_INFRASTRUCTURE_THRESHOLD, "Infrastructure level is not high enough to build the small hotel")
    assert(state.small_hotel_built == False, "Small hotel is already built")
    state.small_hotel_built = True
    state.num_civilians += 1

def _build_large_hotel(state: GameState):
    assert(state.large_hotel_unlocked, "Large hotel action is not unlocked yet")
    assert(state.infrastructure_level >= LARGE_HOTEL_INFRASTRUCTURE_THRESHOLD, "Infrastructure level is not high enough to build the large hotel")
    assert(state.small_hotel_built == True, "Small hotel must be built before building the large hotel")
    assert(state.large_hotel_built == False, "Large hotel is already built")
    state.large_hotel_built = True
    state.num_civilians += 1
    _add_renown_attribute_point(state)

def _build_small_workshop(state: GameState):
    assert(state.small_workshop_unlocked, "Small workshop action is not unlocked yet")
    assert(state.infrastructure_level >= SMALL_WORKSHOP_INFRASTRUCTURE_THRESHOLD, "Infrastructure level is not high enough to build the small workshop")
    assert(state.small_workshop_built == False, "Small workshop is already built")
    state.small_workshop_built = True
    state.num_builders += 1

def _build_large_workshop(state: GameState):
    assert(state.large_workshop_unlocked, "Large workshop action is not unlocked yet")
    assert(state.infrastructure_level >= LARGE_WORKSHOP_INFRASTRUCTURE_THRESHOLD, "Infrastructure level is not high enough to build the large workshop")
    assert(state.small_workshop_built == True, "Small workshop must be built before building the large workshop")
    assert(state.large_workshop_built == False, "Large workshop is already built")
    state.large_workshop_built = True
    state.num_builders += 1
    _add_renown_attribute_point(state)

def _build_small_road(state: GameState):
    assert(state.small_road_unlocked, "Small road action is not unlocked yet")
    assert(state.infrastructure_level >= SMALL_ROAD_INFRASTRUCTURE_THRESHOLD, "Infrastructure level is not high enough to build the small road")
    assert(state.small_road_built == False, "Small road is already built")
    state.small_road_built = True
    if (state.piety_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK) or \
            (state.dicipline_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK):
        state.status = GameStatus.STATUS_CHOOSE_PIETY_OR_DISCIPLINE

def _build_large_road(state: GameState):
    assert(state.large_road_unlocked, "Large road action is not unlocked yet")
    assert(state.infrastructure_level >= LARGE_ROAD_INFRASTRUCTURE_THRESHOLD, "Infrastructure level is not high enough to build the large road")
    assert(state.small_road_built == True, "Small road must be built before building the large road")
    assert(state.large_road_built == False, "Large road is already built")
    state.large_road_built = True
    if (state.renown_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK) or \
            (state.valour_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK):
        state.status = GameStatus.STATUS_CHOOSE_RENOWN_OR_VALOUR

def _use_forum(state: GameState):
    assert(state.forum_available, "Forum action is not available")
    assert(state.forum_boxes < NUM_FORUM_BOXES, "All forum boxes are already filled")
    state.forum_boxes += 1
    state.forum_available = False
    state.forum_rounds.append(state.current_round)

def _build_landmark_1(state: GameState):
    assert(state.landmark_1_unlocked, "Landmark 1 action is not unlocked yet")
    assert(state.num_renown_attribute_boxes >= LANDMARK_ATTRIBUTE_POINTS_THRESHOLD, "Not enough renown attribute points to build landmark 1")
    assert(state.landmark_1_built == False, "Landmark 1 is already built")
    state.landmark_1_built = True
    _add_valour_attribute_point(state, num_points=2)

def _build_landmark_2(state: GameState):
    assert(state.landmark_2_unlocked, "Landmark 2 action is not unlocked yet")
    assert(state.num_piety_attribute_boxes >= LANDMARK_ATTRIBUTE_POINTS_THRESHOLD, "Not enough piety attribute points to build landmark 2")
    assert(state.landmark_2_built == False, "Landmark 2 is already built")
    state.landmark_2_built = True
    _add_dicipline_attribute_point(state, num_points=2)

def _build_landmark_3(state: GameState):
    assert(state.landmark_3_unlocked, "Landmark 3 action is not unlocked yet")
    assert(state.num_valour_attribute_boxes >= LANDMARK_ATTRIBUTE_POINTS_THRESHOLD, "Not enough valour attribute points to build landmark 3")
    assert(state.landmark_3_built == False, "Landmark 3 is already built")
    state.landmark_3_built = True
    _add_piety_attribute_point(state, num_points=2)

def _build_landmark_4(state: GameState):
    assert(state.landmark_4_unlocked, "Landmark 4 action is not unlocked yet")
    assert(state.num_dicipline_attribute_boxes >= LANDMARK_ATTRIBUTE_POINTS_THRESHOLD, "Not enough dicipline attribute points to build landmark 4")
    assert(state.landmark_4_built == False, "Landmark 4 is already built")
    state.landmark_4_built = True
    _add_renown_attribute_point(state, num_points=2)


# Right sheet
# Traders
def _advance_traders_track(state: GameState):
    assert(state.traders_track_boxes < NUM_CITIZEN_TRACK_BOXES, "All traders track boxes are already filled")
    state.traders_track_boxes += 1

    state.small_precinct_unlocked = state.small_precinct_unlocked or (state.traders_track_boxes >= TRADERS_SMALL_PRECINCT_THRESHOLD)
    state.medium_precinct_unlocked = state.medium_precinct_unlocked or (state.traders_track_boxes >= TRADERS_MEDIUM_PRECINCT_THRESHOLD)
    state.large_precinct_unlocked = state.large_precinct_unlocked or (state.traders_track_boxes >= TRADERS_LARGE_PRECINCT_THRESHOLD)
    state.market_unlocked = state.market_unlocked or (state.traders_track_boxes >= TRADERS_MARKET_THRESHOLD)
    state.market_boxes_unlocked = sum(1 for threshold in TRADERS_MARKET_THRESHOLDS if state.traders_track_boxes >= threshold)

    if state.traders_track_boxes in TRADERS_BUILDERS_THRESHOLDS:
        state.num_builders += 1
    elif state.traders_track_boxes in TRADERS_SERVANTS_THRESHOLDS:
        state.num_servants += 1
    elif state.traders_track_boxes in TRADERS_RESOURCES_THRESHOLDS:
        state.num_resources += 1
    elif state.traders_track_boxes in TRADERS_RENOWN_THRESHOLDS:
        _add_renown_attribute_point(state)    

def _build_small_precinct(state: GameState):
    assert(state.small_precinct_unlocked, "Small precinct action is not unlocked yet")
    assert(state.traders_track_boxes >= TRADERS_SMALL_PRECINCT_THRESHOLD, "Traders track is not high enough to build the small precinct")
    assert(state.small_precinct_built == False, "Small precinct is already built")
    state.small_precinct_built = True
    state.num_resources += 1
    _add_resource_production_box(state)
    _add_piety_attribute_point(state)

def _build_medium_precinct(state: GameState):
    assert(state.medium_precinct_unlocked, "Medium precinct action is not unlocked yet")
    assert(state.traders_track_boxes >= TRADERS_MEDIUM_PRECINCT_THRESHOLD, "Traders track is not high enough to build the medium precinct")
    assert(state.small_precinct_built == True, "Small precinct must be built before building the medium precinct")
    assert(state.medium_precinct_built == False, "Medium precinct is already built")
    state.medium_precinct_built = True
    state.num_resources += 1
    _add_resource_production_box(state)
    _add_dicipline_attribute_point(state)

def _build_large_precinct(state: GameState):
    assert(state.large_precinct_unlocked, "Large precinct action is not unlocked yet")
    assert(state.traders_track_boxes >= TRADERS_LARGE_PRECINCT_THRESHOLD, "Traders track is not high enough to build the large precinct")
    assert(state.small_precinct_built == True, "Small precinct must be built before building the large precinct")
    assert(state.medium_precinct_built == True, "Medium precinct must be built before building the large precinct")
    assert(state.large_precinct_built == False, "Large precinct is already built")
    state.large_precinct_built = True
    state.num_resources += 1
    _add_resource_production_box(state)
    _add_renown_attribute_point(state)

def _build_market(state: GameState):
    assert(state.market_unlocked, "Market action is not unlocked yet")
    assert(state.traders_track_boxes >= TRADERS_MARKET_THRESHOLD, "Traders track is not high enough to build the market")
    assert(state.market_built == False, "Market is already built")
    state.market_built = True
    _add_renown_attribute_point(state)

def _buy_goods(state, goods_id, index=None):
    assert(state.market_built, "Market is not built yet")
    assert(state.has_free_market_box(), "No free market boxes available to buy goods")
    assert(index is None or (0 <= index < state.market_boxes_unlocked), "Market box index out of bounds")
    assert(index is None or (state.market_boxes[index] == False), "Market box is not free")

    num_distinct_goods_before = state.get_num_distinct_goods()
    if index is None:
        index = state.get_next_free_market_box()
    state.add_good_to_market(goods_id, index)
    num_distinct_goods_after = state.get_num_distinct_goods()
    if num_distinct_goods_after > num_distinct_goods_before:
        if num_distinct_goods_after <= 3:
            _add_renown_attribute_point(state)
        elif num_distinct_goods_after <= 5:
            _add_renown_attribute_point(state, num_points=2)
        elif num_distinct_goods_after == 6:
            _add_renown_attribute_point(state, num_points=3)
    if index == TRADERS_MARKET_SERVANT_BOX - 1:
        state.num_servants += 1
    elif index == TRADERS_MARKET_BUILDER_BOX - 1:
        state.num_builders += 1

# Performers
def _advance_performers_track(state: GameState):
    assert(state.performers_track_boxes < NUM_CITIZEN_TRACK_BOXES, "All performers track boxes are already filled")
    state.performers_track_boxes += 1

    state.theater_unlocked = state.theater_unlocked or (state.performers_track_boxes >= PERFORMERS_THEATER_THRESHOLD)
    state.theater_boxes_unlocked = sum(1 for threshold in PERFORMERS_THEATER_ARRANGE_PERFORMANCE_THRESHOLDS if state.performers_track_boxes >= threshold)
    state.colosseum_unlocked = state.colosseum_unlocked or (state.performers_track_boxes >= PERFORMERS_COLOSSEUM_THRESHOLD)
    state.gladiator_boxes_unlocked = sum(1 for threshold in PERFORMERS_COLOSSEUM_TRAINING_THRESHOLDS if state.performers_track_boxes >= threshold)
    
    if state.performers_track_boxes in PERFORMERS_SOLDIERS_THRESHOLDS:
        state.num_soldiers += 1
    elif state.performers_track_boxes in PERFORMERS_BUILDERS_THRESHOLDS:
        state.num_builders += 1
    elif state.performers_track_boxes in PERFORMERS_SERVANTS_THRESHOLDS:
        state.num_servants += 1
    elif state.performers_track_boxes in PERFORMERS_RENOWN_THRESHOLDS:
        _add_renown_attribute_point(state)

def _build_theater(state: GameState):
    assert(state.theater_unlocked, "Theater action is not unlocked yet")
    assert(state.performers_track_boxes >= PERFORMERS_THEATER_THRESHOLD, "Performers track is not high enough to build the theater")
    assert(state.theater_built == False, "Theater is already built")
    state.theater_built = True
    _add_renown_attribute_point(state)

def _arrange_performance_1(state: GameState):
    assert(state.theater_boxes_unlocked[0] == True, "Theater box has not been unlocked yet")
    assert(state.performers_track_boxes >= PERFORMERS_THEATER_ARRANGE_PERFORMANCE_THRESHOLDS[0], f"Performers track is not high enough to arrange performance 1")
    assert(state.theater_built, "Theater is not built yet")
    assert(state.theater_available, "Theater is not available this round")
    assert(state.theater_boxes[0] == False, f"Theater performance 1 is already used")

    state.theater_boxes[0] = True
    state.theater_available = False
    state.theater_boxes_rounds[0] = state.current_round
    _advance_traders_track(state)

def _arrange_performance_2(state: GameState):
    assert(state.theater_boxes_unlocked[1] == True, "Theater box has not been unlocked yet")
    assert(state.performers_track_boxes >= PERFORMERS_THEATER_ARRANGE_PERFORMANCE_THRESHOLDS[1], f"Performers track is not high enough to arrange performance 2")
    assert(state.theater_built, "Theater is not built yet")
    assert(state.theater_available, "Theater is not available this round")
    assert(state.theater_boxes[1] == False, f"Theater performance 2 is already used")

    state.theater_boxes[1] = True
    state.theater_available = False
    state.theater_boxes_rounds[1] = state.current_round
    state.num_soldiers += 1
    _add_dicipline_attribute_point(state)

def _arrange_performance_3(state: GameState):
    assert(state.theater_boxes_unlocked[2] == True, "Theater box has not been unlocked yet")
    assert(state.performers_track_boxes >= PERFORMERS_THEATER_ARRANGE_PERFORMANCE_THRESHOLDS[2], f"Performers track is not high enough to arrange performance 3")
    assert(state.theater_built, "Theater is not built yet")
    assert(state.theater_available, "Theater is not available this round")
    assert(state.theater_boxes[2] == False, f"Theater performance 3 is already used")

    state.theater_boxes[2] = True
    state.theater_available = False
    state.theater_boxes_rounds[2] = state.current_round
    state.num_servants += 1
    _add_piety_attribute_point(state)

def _arrange_performance_4(state: GameState):
    assert(state.theater_boxes_unlocked[3] == True, "Theater box has not been unlocked yet")
    assert(state.performers_track_boxes >= PERFORMERS_THEATER_ARRANGE_PERFORMANCE_THRESHOLDS[3], f"Performers track is not high enough to arrange performance 4")
    assert(state.theater_built, "Theater is not built yet")
    assert(state.theater_available, "Theater is not available this round")
    assert(state.theater_boxes[3] == False, f"Theater performance 4 is already used")

    state.theater_boxes[3] = True
    state.theater_available = False
    state.theater_boxes_rounds[3] = state.current_round
    _add_dicipline_attribute_point(state)
    _advance_apparitores_track(state)

def _arrange_performance_5(state: GameState):
    assert(state.theater_boxes_unlocked[4] == True, "Theater box has not been unlocked yet")
    assert(state.performers_track_boxes >= PERFORMERS_THEATER_ARRANGE_PERFORMANCE_THRESHOLDS[4], f"Performers track is not high enough to arrange performance 5")
    assert(state.theater_built, "Theater is not built yet")
    assert(state.theater_available, "Theater is not available this round")
    assert(state.theater_boxes[4] == False, f"Theater performance 5 is already used")

    state.theater_boxes[4] = True
    state.theater_available = False
    state.theater_boxes_rounds[4] = state.current_round
    _add_piety_attribute_point(state)
    _advance_priests_track(state)

def _arrange_performance_6(state: GameState):
    assert(state.theater_boxes_unlocked[5] == True, "Theater box has not been unlocked yet")
    assert(state.performers_track_boxes >= PERFORMERS_THEATER_ARRANGE_PERFORMANCE_THRESHOLDS[5], f"Performers track is not high enough to arrange performance 6")
    assert(state.theater_built, "Theater is not built yet")
    assert(state.theater_available, "Theater is not available this round")
    assert(state.theater_boxes[5] == False, f"Theater performance 6 is already used")

    state.theater_boxes[5] = True
    state.theater_available = False
    state.theater_boxes_rounds[5] = state.current_round
    _add_renown_attribute_point(state)
    _advance_patricians_track(state)

def _build_colosseum(state: GameState):
    assert(state.colosseum_unlocked, "Colosseum action is not unlocked yet")
    assert(state.performers_track_boxes >= PERFORMERS_COLOSSEUM_THRESHOLD, "Performers track is not high enough to build the colosseum")
    assert(state.colosseum_built == False, "Colosseum is already built")
    state.colosseum_built = True
    _add_renown_attribute_point(state)

def _train_gladiator_1(state: GameState):
    assert(state.colosseum_built, "The colosseum has not been built yet but is required for this action")
    assert(state.is_gladiator_1_alive(), "Gladiator 1 is not alive and cannot be trained")
    assert(state.performers_track_boxes >= PERFORMERS_COLOSSEUM_TRAINING_THRESHOLDS[state.gladiator_1_strength], \
           f"Performers track is not high enough to train gladiator 1")
    assert(state.gladiator_boxes_unlocked > state.gladiator_1_strength, \
           f"Gladiator 1 strength is too high to train (current strength: {state.gladiator_1_strength}, gladiator boxes unlocked: {state.gladiator_boxes_unlocked})")
    assert(state.gladiator_1_strength < NUM_GLADIATOR_BOXES, "Gladiator 1 is already at maximum strength")
    state.gladiator_1_strength += 1

def _train_gladiator_2(state: GameState):
    assert(state.colosseum_built, "The colosseum has not been built yet but is required for this action")
    assert(state.is_gladiator_2_alive(), "Gladiator 2 is not alive and cannot be trained")
    assert(state.performers_track_boxes >= PERFORMERS_COLOSSEUM_TRAINING_THRESHOLDS[NUM_GLADIATOR_BOXES + state.gladiator_2_strength], \
           f"Performers track is not high enough to train gladiator 2")
    assert(state.gladiator_boxes_unlocked > NUM_GLADIATOR_BOXES + state.gladiator_2_strength, \
           f"Gladiator 2 strength is too high to train (current strength: {state.gladiator_2_strength}, gladiator boxes unlocked: {state.gladiator_boxes_unlocked})")
    assert(state.gladiator_2_strength < NUM_GLADIATOR_BOXES, "Gladiator 2 is already at maximum strength")
    state.gladiator_2_strength += 1

def _fight_with_gladiator_1(state: GameState):
    assert(state.colosseum_built, "The colosseum has not been built yet but is required for this action")
    assert(state.is_gladiator_1_alive(), "Gladiator 1 is not alive and cannot fight")
    assert(state.gladiator_1_can_battle == True, "Gladiator 1 has already battled this round")
    
    state.draw_fate_card()
    gladiator_damage = state.get_current_fate_card_gladiator_damage()
    state.gladiator_1_damage += gladiator_damage
    state.gladiator_1_can_battle = False
    state.gladiator_1_battle_rounds.append(state.current_round)
    if state.is_gladiator_1_alive():
        match state.gladiator_1_strength:
            case 2 | 3:
                _add_renown_attribute_point(state)
            case 4 | 5:
                _add_renown_attribute_point(state, num_points=2)
            case 6:
                state.num_resources += 1
                _add_renown_attribute_point(state, num_points=2)
    else:
        match state.gladiator_1_strength:
            case 1 | 2:
                _add_piety_attribute_point(state, num_points=2)
            case 3 | 4:
                _add_piety_attribute_point(state)

def _fight_with_gladiator_2(state: GameState):
    assert(state.colosseum_built, "The colosseum has not been built yet but is required for this action")
    assert(state.is_gladiator_2_alive(), "Gladiator 2 is not alive and cannot fight")
    assert(state.gladiator_2_can_battle == True, "Gladiator 2 has already battled this round")
    
    state.draw_fate_card()
    gladiator_damage = state.get_current_fate_card_gladiator_damage()
    state.gladiator_2_damage += gladiator_damage
    state.gladiator_2_can_battle = False
    state.gladiator_2_battle_rounds.append(state.current_round)
    if state.is_gladiator_2_alive():
        match state.gladiator_2_strength:
            case 2 | 3:
                _add_renown_attribute_point(state)
            case 4 | 5:
                _add_renown_attribute_point(state, num_points=2)
            case 6:
                state.num_resources += 1
                _add_renown_attribute_point(state, num_points=2)
    else:
        match state.gladiator_2_strength:
            case 1 | 2:
                _add_piety_attribute_point(state, num_points=2)
            case 3 | 4:
                _add_piety_attribute_point(state)

# Priests
def _advance_priests_track(state: GameState):
    assert(state.priests_track_boxes < NUM_CITIZEN_TRACK_BOXES, "All priests track boxes are already filled")
    state.priests_track_boxes += 1

    state.small_garden_unlocked = state.small_garden_unlocked or (state.priests_track_boxes >= PRIESTS_SMALL_GARDEN_THRESHOLD)
    state.large_garden_unlocked = state.large_garden_unlocked or (state.priests_track_boxes >= PRIESTS_LARGE_GARDEN_THRESHOLD)
    state.small_temple_unlocked = state.small_temple_unlocked or (state.priests_track_boxes >= PRIESTS_SMALL_TEMPLE_THRESHOLD)
    state.small_temple_boxes_unlocked = sum(1 for threshold in PRIESTS_SMALL_TEMPLE_FILL_THRESHOLDS if state.priests_track_boxes >= threshold)
    state.medium_temple_unlocked = state.medium_temple_unlocked or (state.priests_track_boxes >= PRIESTS_MEDIUM_TEMPLE_THRESHOLD)
    state.medium_temple_boxes_unlocked = sum(1 for threshold in PRIESTS_MEDIUM_TEMPLE_FILL_THRESHOLDS if state.priests_track_boxes >= threshold)
    state.large_temple_unlocked = state.large_temple_unlocked or (state.priests_track_boxes >= PRIESTS_LARGE_TEMPLE_THRESHOLD)
    state.large_temple_boxes_unlocked = sum(1 for threshold in PRIESTS_LARGE_TEMPLE_FILL_THRESHOLDS if state.priests_track_boxes >= threshold)

    if state.priests_track_boxes in PRIESTS_SERVANTS_THRESHOLDS:
        state.num_servants += 1
    elif state.priests_track_boxes in PRIESTS_PIETY_THRESHOLDS:
        _add_piety_attribute_point(state)

def _build_small_garden(state: GameState):
    assert(state.small_garden_unlocked, "Small garden action is not unlocked yet")
    assert(state.priests_track_boxes >= PRIESTS_SMALL_GARDEN_THRESHOLD, "Priests track is not high enough to build the small garden")
    assert(state.small_garden_built == False, "Small garden is already built")
    state.small_garden_built = True
    _add_piety_attribute_point(state)
    _advance_traders_track(state)
    _advance_performers_track(state)
    _advance_priests_track(state)

def _build_large_garden(state: GameState):
    assert(state.large_garden_unlocked, "Large garden action is not unlocked yet")
    assert(state.priests_track_boxes >= PRIESTS_LARGE_GARDEN_THRESHOLD, "Priests track is not high enough to build the large garden")
    assert(state.small_garden_built == True, "Small garden must be built before building the large garden")
    assert(state.large_garden_built == False, "Large garden is already built")
    state.large_garden_built = True
    _add_piety_attribute_point(state)
    _advance_traders_track(state)
    _advance_performers_track(state)
    _advance_priests_track(state)
    _advance_apparitores_track(state)
    _advance_patricians_track(state)

def _build_small_temple(state: GameState):
    assert(state.small_temple_unlocked, "Small temple action is not unlocked yet")
    assert(state.priests_track_boxes >= PRIESTS_SMALL_TEMPLE_THRESHOLD, "Priests track is not high enough to build the small temple")
    assert(state.small_temple_built == False, "Small temple is already built")
    state.small_temple_built = True
    _add_piety_attribute_point(state)

def _fill_small_temple(state: GameState):
    assert(state.small_temple_built, "Small temple must be built before filling it")
    assert(state.priests_track_boxes >= PRIESTS_SMALL_TEMPLE_FILL_THRESHOLDS[state.small_temple_boxes], \
           "Priests track is not high enough to fill the small temple")
    assert(state.is_small_temple_filled() == False, "All small temple boxes are already filled")
    state.small_temple_boxes += 1
    _add_piety_attribute_point(state)
    if state.is_small_temple_filled():
        state.num_general_favours += 1

def _build_medium_temple(state: GameState):
    assert(state.medium_temple_unlocked, "Medium temple action is not unlocked yet")
    assert(state.priests_track_boxes >= PRIESTS_MEDIUM_TEMPLE_THRESHOLD, "Priests track is not high enough to build the medium temple")
    assert(state.small_temple_built == True, "Small temple must be built before building the medium temple")
    assert(state.medium_temple_built == False, "Medium temple is already built")
    state.medium_temple_built = True
    _add_piety_attribute_point(state)

def _fill_medium_temple(state: GameState):
    assert(state.medium_temple_built, "Medium temple must be built before filling it")
    assert(state.priests_track_boxes >= PRIESTS_MEDIUM_TEMPLE_FILL_THRESHOLDS[state.medium_temple_boxes], \
           "Priests track is not high enough to fill the medium temple")
    assert(state.is_small_temple_filled(), "All small temple boxes must be filled")
    assert(state.is_medium_temple_filled() == False, "All medium temple boxes are already filled")
    state.medium_temple_boxes += 1
    _add_piety_attribute_point(state)
    if state.is_medium_temple_filled():
        state.num_general_favours += 1

def _build_large_temple(state: GameState):
    assert(state.large_temple_unlocked, "Large temple action is not unlocked yet")
    assert(state.priests_track_boxes >= PRIESTS_LARGE_TEMPLE_THRESHOLD, "Priests track is not high enough to build the large temple")
    assert(state.small_temple_built == True, "Small temple must be built before building the large temple")
    assert(state.medium_temple_built == True, "Medium temple must be built before building the large temple")
    assert(state.large_temple_built == False, "Large temple is already built")
    state.large_temple_built = True
    _add_piety_attribute_point(state)

def _fill_large_temple(state: GameState):
    assert(state.large_temple_built, "Large temple must be built before filling it")
    assert(state.priests_track_boxes >= PRIESTS_LARGE_TEMPLE_FILL_THRESHOLDS[state.large_temple_boxes], \
           "Priests track is not high enough to fill the large temple")
    assert(state.is_large_temple_filled() == False, "All large temple boxes are already filled")
    state.large_temple_boxes += 1
    _add_piety_attribute_point(state)
    if state.is_large_temple_filled():
        state.num_general_favours += 1

# Apparitores
def _advance_apparitores_track(state: GameState):
    assert(state.apparitores_track_boxes < NUM_CITIZEN_TRACK_BOXES, "All apparitores track boxes are already filled")
    state.apparitores_track_boxes += 1

    state.baths_unlocked = state.baths_unlocked or (state.apparitores_track_boxes >= APPARITORES_BATHS_THRESHOLD)
    state.baths_boxes_unlocked = sum(1 for threshold in APPARITORES_BATHS_BRIBE_THRESHOLDS if state.apparitores_track_boxes >= threshold)
    state.courthouse_unlocked = state.courthouse_unlocked or (state.apparitores_track_boxes >= APPARITORES_COURTHOUSE_THRESHOLD)
    state.courthouse_get_servant_unlocked = sum(1 for threshold in APPARITORES_COURTHOUSE_GET_SERVANT_THRESHOLDS if state.apparitores_track_boxes >= threshold)
    state.courthouse_builder_to_two_servants_unlocked = sum(1 for threshold in APPARITORES_COURTHOUSE_BUILDER_TO_TWO_SERVANTS_THRESHOLDS if state.apparitores_track_boxes >= threshold)
    state.courthouse_servant_to_builder_unlocked = sum(1 for threshold in APPARITORES_COURTHOUSE_SERVANT_TO_BUILDER_THRESHOLDS if state.apparitores_track_boxes >= threshold)

    if state.apparitores_track_boxes in APPARITORES_SOLDIERS_THRESHOLDS:
        state.num_soldiers += 1
    elif state.apparitores_track_boxes in APPARITORES_BUILDERS_THRESHOLDS:
        state.num_builders += 1
    elif state.apparitores_track_boxes in APPARITORES_DICIPLINE_THRESHOLDS:
        _add_dicipline_attribute_point(state)

def _build_baths(state: GameState):
    assert(state.baths_unlocked, "Baths action is not unlocked yet")
    assert(state.apparitores_track_boxes >= APPARITORES_BATHS_THRESHOLD, "Apparitores track is not high enough to build the baths")
    assert(state.baths_built == False, "Baths is already built")
    state.baths_built = True
    _add_renown_attribute_point(state)

def _pay_bribe(state: GameState):
    assert(state.baths_built, "Baths must be built before bribing it")
    assert(state.baths_boxes < NUM_BATHS_BOXES, "All baths bribe boxes are already filled")
    assert(state.apparitores_track_boxes >= APPARITORES_BATHS_BRIBE_THRESHOLDS[state.baths_boxes], \
           "Apparitores track is not high enough to bribe in the baths")
    assert(state.get_final_disdain() > 0, "Not enough disdain to pay a bribe in the baths")
    state.baths_boxes += 1
    state.baths_rounds.append(state.current_round)
    COSTS[actions.ACTION_PAY_BRIBE] = {"resources": APPARITORES_BATHS_BRIBE_COSTS[state.baths_boxes]}

def _build_courthouse(state: GameState):
    assert(state.courthouse_unlocked, "Courthouse action is not unlocked yet")
    assert(state.apparitores_track_boxes >= APPARITORES_COURTHOUSE_THRESHOLD, "Apparitores track is not high enough to build the courthouse")
    assert(state.courthouse_built == False, "Courthouse is already built")
    state.courthouse_built = True
    _add_renown_attribute_point(state)

def _courthouse_get_servant(state: GameState):
    assert(state.courthouse_built, "Courthouse must be built before getting a servant from it")
    assert(not state.courthouse_get_servant_available, "Courthouse get servant action is not available")
    assert(state.courthouse_get_servant_boxes < MAX_NUM_COURTHOUSE_ACTIONS, "All courthouse get servant boxes are already used")
    assert(state.courthouse_get_servant_boxes < state.courthouse_get_servant_unlocked, "Not enough courthouse get servant boxes are unlocked yet")
    assert(state.apparitores_track_boxes >= APPARITORES_COURTHOUSE_GET_SERVANT_THRESHOLDS[state.courthouse_get_servant_boxes], \
           "Apparitores track is not high enough to get a servant from the courthouse")
    state.courthouse_get_servant_available = False
    state.num_servants += 1
    state.courthouse_get_servant_boxes += 1
    state.courthouse_get_servant_rounds.append(state.current_round)

def _courthouse_builder_to_two_servants(state: GameState):
    assert(state.courthouse_built, "Courthouse must be built before converting a builder to two servants")
    assert(not state.courthouse_builder_to_two_servants_available, "Courthouse builder to two servants action is not available")
    assert(state.courthouse_builder_to_two_servants_boxes < MAX_NUM_COURTHOUSE_ACTIONS, "All courthouse builder to two servants boxes are already used") 
    assert(state.courthouse_builder_to_two_servants_boxes < state.courthouse_builder_to_two_servants_unlocked, \
           "Not enough courthouse builder to two servants boxes are unlocked yet")
    assert(state.apparitores_track_boxes >= APPARITORES_COURTHOUSE_BUILDER_TO_TWO_SERVANTS_THRESHOLDS[state.courthouse_builder_to_two_servants_boxes], \
           "Apparitores track is not high enough to convert a builder to two servants in the courthouse")
    state.courthouse_builder_to_two_servants_available = False
    state.num_servants += 2
    state.courthouse_builder_to_two_servants_boxes += 1
    state.courthouse_builder_to_two_servants_rounds.append(state.current_round)

def _courthouse_servant_to_builder(state: GameState):
    assert(state.courthouse_built, "Courthouse must be built before converting a servant to a builder")
    assert(not state.courthouse_servant_to_builder_available, "Courthouse servant to builder action is not available")
    assert(state.courthouse_servant_to_builder_boxes < MAX_NUM_COURTHOUSE_ACTIONS, "All courthouse servant to builder boxes are already used")
    assert(state.courthouse_servant_to_builder_boxes < state.courthouse_servant_to_builder_unlocked, \
           "Not enough courthouse servant to builder boxes are unlocked yet")
    assert(state.apparitores_track_boxes >= APPARITORES_COURTHOUSE_SERVANT_TO_BUILDER_THRESHOLDS[state.courthouse_servant_to_builder_boxes], \
           "Apparitores track is not high enough to convert a servant to a builder in the courthouse")
    assert(state.num_servants >= 1, "Not enough servants to convert to a builder in the courthouse")
    state.courthouse_servant_to_builder_available = False
    state.num_builders += 1
    state.courthouse_servant_to_builder_boxes += 1
    state.courthouse_servant_to_builder_rounds.append(state.current_round)


# Patricians
def _advance_patricians_track(state: GameState):
    assert(state.patricians_track_boxes < NUM_CITIZEN_TRACK_BOXES, "All patricians track boxes are already filled")
    state.patricians_track_boxes += 1

    state.diplomat_boxes_unlocked = sum(1 for threshold in PATRICIANS_DIPLOMAT_THRESHOLDS if state.patricians_track_boxes >= threshold)
    state.scouts_boxes_unlocked = sum(1 for threshold in PATRICIANS_SCOUTS_THRESHOLDS if state.patricians_track_boxes >= threshold)

    if state.patricians_track_boxes in PATRICIANS_SOLDIERS_THRESHOLDS:
        state.num_soldiers += 1
    elif state.patricians_track_boxes in PATRICIANS_RESOURCES_THRESHOLDS:
        state.num_resources += 1
    elif state.patricians_track_boxes in PATRICIANS_RENOWN_THRESHOLDS:
        _add_renown_attribute_point(state)

def _send_left_diplomat(state: GameState):
    assert(state.has_diplomat_box_available(), "No diplomat boxes available to send a diplomat")
    assert(state.patricians_track_boxes >= PATRICIANS_DIPLOMAT_THRESHOLDS[state.get_num_diplomat_boxes_available()], "Patricians track is not high enough to send a diplomat to the left cohort")
    assert(state.diplomat_left_available == True, "Left diplomat action is not available")
    state.diplomat_left_available = False
    _add_valour_attribute_point(state)
    state.num_left_cohort_favours = 2

def _send_center_diplomat(state: GameState):
    assert(state.has_diplomat_box_available(), "No diplomat boxes available to send a diplomat")
    assert(state.patricians_track_boxes >= PATRICIANS_DIPLOMAT_THRESHOLDS[state.get_num_diplomat_boxes_available()], "Patricians track is not high enough to send a diplomat to the left cohort")
    assert(state.diplomat_center_available == True, "Center diplomat action his not available")
    state.diplomat_center_available = False
    _add_valour_attribute_point(state)
    state.num_center_cohort_favours = 2

def _send_right_diplomat(state: GameState):
    assert(state.has_diplomat_box_available(), "No diplomat boxes available to send a diplomat")
    assert(state.patricians_track_boxes >= PATRICIANS_DIPLOMAT_THRESHOLDS[state.get_num_diplomat_boxes_available()], "Patricians track is not high enough to send a diplomat to the left cohort")
    assert(state.diplomat_right_available == True, "Right diplomat action has is not available")
    state.diplomat_right_available = False
    _add_valour_attribute_point(state)
    state.num_right_cohort_favours = 2

def _send_scout_prospect_card(state: GameState):
    assert(state.patricians_track_boxes >= PATRICIANS_SCOUTS_THRESHOLDS[state.scouts_boxes], "Patricians track is not high enough to send a scout")
    assert(state.scouts_boxes < NUM_SCOUTS_BOXES, "All scouts boxes are already used")
    assert(state.scouts_boxes == state.scouts_boxes_unlocked, "Next scout box is not unlocked yet")
    state.scouts_boxes += 1
    state.chosen_scout_pattern = state.get_current_prospect_card_scout_pattern_id()
    state.status = GameStatus.STATUS_SEND_SCOUT

def _send_scout_neighbor_card_1(state: GameState):
    assert(state.patricians_track_boxes >= PATRICIANS_SCOUTS_THRESHOLDS[state.scouts_boxes], "Patricians track is not high enough to send a scout")
    assert(state.scouts_boxes < NUM_SCOUTS_BOXES, "All scouts boxes are already used")
    assert(state.scouts_boxes == state.scouts_boxes_unlocked, "Next scout box is not unlocked yet")
    state.scouts_boxes += 1
    state.chosen_scout_pattern = state.get_neighbor_prospect_card_1_scout_pattern_id()
    state.status = GameStatus.STATUS_SEND_SCOUT

def _send_scout_neighbor_card_2(state: GameState):
    assert(state.patricians_track_boxes >= PATRICIANS_SCOUTS_THRESHOLDS[state.scouts_boxes], "Patricians track is not high enough to send a scout")
    assert(state.scouts_boxes < NUM_SCOUTS_BOXES, "All scouts boxes are already used")
    assert(state.scouts_boxes == state.scouts_boxes_unlocked, "Next scout box is not unlocked yet")
    state.scouts_boxes += 1
    state.chosen_scout_pattern = state.get_neighbor_prospect_card_2_scout_pattern_id()
    state.status = GameStatus.STATUS_SEND_SCOUT

def _place_scout_grid_pattern_1(state: GameState, row, col):
    # Pattern:
    # [X][X]
    # [X][X]
    assert(state.status == GameStatus.STATUS_SEND_SCOUT, "Not currently sending a scout")
    assert(state.chosen_scout_pattern == 1, "Chosen scout pattern does not match the pattern required for this action")
    _fill_scout_box(state, row, col)
    _fill_scout_box(state, row, col + 1)
    _fill_scout_box(state, row + 1, col)
    _fill_scout_box(state, row + 1, col + 1)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _place_scout_grid_pattern_2(state: GameState, row, col, rotated=False):
    # Pattern:
    # [X][X][X][X]
    assert(state.status == GameStatus.STATUS_SEND_SCOUT, "Not currently sending a scout")
    assert(state.chosen_scout_pattern == 2, "Chosen scout pattern does not match the pattern required for this action")
    if rotated:
        _fill_scout_box(state, row, col)
        _fill_scout_box(state, row + 1, col)
        _fill_scout_box(state, row + 2, col)
        _fill_scout_box(state, row + 3, col)
    else:
        _fill_scout_box(state, row, col)
        _fill_scout_box(state, row, col + 1)
        _fill_scout_box(state, row, col + 2)
        _fill_scout_box(state, row, col + 3)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _place_scout_grid_pattern_3(state: GameState, row, col, rotated=False, flipped=False):
    # Pattern:
    # [X][X]
    #    [X][X]
    assert(state.status == GameStatus.STATUS_SEND_SCOUT, "Not currently sending a scout")
    assert(state.chosen_scout_pattern == 3, "Chosen scout pattern does not match the pattern required for this action")
    if rotated:
        if flipped:
            _fill_scout_box(state, row, col)
            _fill_scout_box(state, row + 1, col)
            _fill_scout_box(state, row + 1, col + 1)
            _fill_scout_box(state, row + 2, col + 1)
        else:
            _fill_scout_box(state, row, col + 1)
            _fill_scout_box(state, row + 1, col)
            _fill_scout_box(state, row + 1, col + 1)
            _fill_scout_box(state, row + 2, col)
    else:
        if flipped:
            _fill_scout_box(state, row, col + 1)
            _fill_scout_box(state, row, col + 2)
            _fill_scout_box(state, row + 1, col)
            _fill_scout_box(state, row + 1, col + 1)
        else:
            _fill_scout_box(state, row, col)
            _fill_scout_box(state, row, col + 1)
            _fill_scout_box(state, row + 1, col + 1)
            _fill_scout_box(state, row + 1, col + 2)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _place_scout_grid_pattern_4(state: GameState, row, col, rotated=False, flipped=False):
    # Pattern:
    # [X][X][X]
    #    [X]
    assert(state.status == GameStatus.STATUS_SEND_SCOUT, "Not currently sending a scout")
    assert(state.chosen_scout_pattern == 4, "Chosen scout pattern does not match the pattern required for this action")
    if rotated:
        if flipped:
            _fill_scout_box(state, row, col)
            _fill_scout_box(state, row + 1, col)
            _fill_scout_box(state, row + 1, col + 1)
            _fill_scout_box(state, row + 2, col)
        else:
            _fill_scout_box(state, row, col + 1)
            _fill_scout_box(state, row + 1, col)
            _fill_scout_box(state, row + 1, col + 1)
            _fill_scout_box(state, row + 2, col + 1)
    else:
        if flipped:
            _fill_scout_box(state, row, col + 1)
            _fill_scout_box(state, row + 1, col)
            _fill_scout_box(state, row + 1, col + 1)
            _fill_scout_box(state, row + 1, col + 2)
        else:
            _fill_scout_box(state, row, col)
            _fill_scout_box(state, row, col + 1)
            _fill_scout_box(state, row, col + 2)
            _fill_scout_box(state, row + 1, col + 1)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _place_scout_grid_pattern_5(state: GameState, row, col, rotated=False, rotated_reverse=False, flipped_horizontal=False, flipped_vertical=False):
    # Pattern:
    # [X][X][X]
    # [X]
    assert(state.status == GameStatus.STATUS_SEND_SCOUT, "Not currently sending a scout")
    assert(state.chosen_scout_pattern == 5, "Chosen scout pattern does not match the pattern required for this action")
    assert(not (rotated and rotated_reverse), "Scout pattern cannot be both rotated and rotated in reverse")

    if rotated:
        if flipped_vertical:
            if flipped_horizontal:
                _fill_scout_box(state, row, col)
                _fill_scout_box(state, row + 1, col)
                _fill_scout_box(state, row + 2, col)
                _fill_scout_box(state, row + 2, col + 1)
            else:
                _fill_scout_box(state, row, col)
                _fill_scout_box(state, row , col + 1)
                _fill_scout_box(state, row + 1, col)
                _fill_scout_box(state, row + 2, col)
        else:
            if flipped_horizontal:
                _fill_scout_box(state, row, col + 1)
                _fill_scout_box(state, row + 1, col + 1)
                _fill_scout_box(state, row + 2, col)
                _fill_scout_box(state, row + 2, col + 1)
            else:
                _fill_scout_box(state, row, col)
                _fill_scout_box(state, row, col + 1)
                _fill_scout_box(state, row + 1, col + 1)
                _fill_scout_box(state, row + 2, col + 1)
    elif rotated_reverse:
        if flipped_vertical:
            if flipped_horizontal:
                _fill_scout_box(state, row, col)
                _fill_scout_box(state, row, col + 1)
                _fill_scout_box(state, row + 1, col + 1)
                _fill_scout_box(state, row + 2, col + 1)
            else:
                _fill_scout_box(state, row, col + 1)
                _fill_scout_box(state, row + 1, col + 1)
                _fill_scout_box(state, row + 2, col)
                _fill_scout_box(state, row + 2, col + 1)
        else:
            if flipped_horizontal:
                _fill_scout_box(state, row, col)
                _fill_scout_box(state, row, col + 1)
                _fill_scout_box(state, row + 1, col)
                _fill_scout_box(state, row + 2, col)
            else:
                _fill_scout_box(state, row, col)
                _fill_scout_box(state, row + 1, col)
                _fill_scout_box(state, row + 2, col)
                _fill_scout_box(state, row + 2, col + 1)
    else:
        if flipped_vertical:
            if flipped_horizontal:
                _fill_scout_box(state, row, col + 2)
                _fill_scout_box(state, row + 1, col)
                _fill_scout_box(state, row + 1, col + 1)
                _fill_scout_box(state, row + 1, col + 2)
            else:
                _fill_scout_box(state, row, col)
                _fill_scout_box(state, row, col + 1)
                _fill_scout_box(state, row, col + 2)
                _fill_scout_box(state, row + 1, col + 2)
        else:
            if flipped_horizontal:
                _fill_scout_box(state, row, col)
                _fill_scout_box(state, row + 1, col )
                _fill_scout_box(state, row + 1, col + 1)
                _fill_scout_box(state, row + 1, col + 2)
            else:
                _fill_scout_box(state, row, col)
                _fill_scout_box(state, row, col + 1)
                _fill_scout_box(state, row, col + 2)
                _fill_scout_box(state, row + 1, col)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _fill_scout_box(state: GameState, row, col):
    assert(0 <= row < NUM_SCOUTS_GRID_ROWS and 0 <= col < NUM_SCOUTS_GRID_COLS, "Scout grid box position out of bounds")
    assert(state.is_scout_grid_box_available(row, col), f"Scout grid box ({row}, {col}) is not available")

    state.fill_scout_grid_box(row, col)
    if (row, col) in PATRICIANS_SCOUTS_GRID_RESOURCES:
        state.num_resources += 1
    elif (row, col) in PATRICIANS_SCOUTS_GRID_SERVANTS:
        state.num_servants += 1

def _is_valid_scout_pattern_placement_1(state: GameState, row, col) -> bool:
    # Pattern:
    # [X][X]
    # [X][X]
    return state.is_scout_grid_box_available(row, col) and \
        state.is_scout_grid_box_available(row, col + 1) and \
        state.is_scout_grid_box_available(row + 1, col) and \
        state.is_scout_grid_box_available(row + 1, col + 1)

def _is_valid_scout_pattern_placement_2(state: GameState, row, col, rotated=False) -> bool:
    # Pattern:
    # [X][X][X][X]
    if rotated:
        return state.is_scout_grid_box_available(row, col) and \
            state.is_scout_grid_box_available(row + 1, col) and \
            state.is_scout_grid_box_available(row + 2, col) and \
            state.is_scout_grid_box_available(row + 3, col)
    else:
        return state.is_scout_grid_box_available(row, col) and \
            state.is_scout_grid_box_available(row, col + 1) and \
            state.is_scout_grid_box_available(row, col + 2) and \
            state.is_scout_grid_box_available(row, col + 3)

def _is_valid_scout_pattern_placement_3(state: GameState, row, col, rotated=False, flipped=False) -> bool:
    # Pattern:
    # [X][X]
    #    [X][X]
    if rotated:
        if flipped:
            return state.is_scout_grid_box_available(row, col) and \
                state.is_scout_grid_box_available(row + 1, col) and \
                state.is_scout_grid_box_available(row + 1, col + 1) and \
                state.is_scout_grid_box_available(row + 2, col + 1)
        else:
            return state.is_scout_grid_box_available(row, col + 1) and \
                state.is_scout_grid_box_available(row + 1, col) and \
                state.is_scout_grid_box_available(row + 1, col + 1) and \
                state.is_scout_grid_box_available(row + 2, col)
    else:
        if flipped:
            return state.is_scout_grid_box_available(row, col + 1) and \
                state.is_scout_grid_box_available(row, col + 2) and \
                state.is_scout_grid_box_available(row + 1, col) and \
                state.is_scout_grid_box_available(row + 1, col + 1)
        else:
            return state.is_scout_grid_box_available(row, col) and \
                state.is_scout_grid_box_available(row, col + 1) and \
                state.is_scout_grid_box_available(row + 1, col + 1) and \
                state.is_scout_grid_box_available(row + 1, col + 2)

def _is_valid_scout_pattern_placement_4(state: GameState, row, col, rotated=False, flipped=False) -> bool:
    # Pattern:
    # [X][X][X]
    #    [X]
    if rotated:
        if flipped:
            return state.is_scout_grid_box_available(row, col) and \
                state.is_scout_grid_box_available(row + 1, col) and \
                state.is_scout_grid_box_available(row + 1, col + 1) and \
                state.is_scout_grid_box_available(row + 2, col)
        else:
            return state.is_scout_grid_box_available(row, col + 1) and \
                state.is_scout_grid_box_available(row + 1, col) and \
                state.is_scout_grid_box_available(row + 1, col + 1) and \
                state.is_scout_grid_box_available(row + 2, col + 1)
    else:
        if flipped:
            return state.is_scout_grid_box_available(row, col + 1) and \
                state.is_scout_grid_box_available(row + 1, col) and \
                state.is_scout_grid_box_available(row + 1, col + 1) and \
                state.is_scout_grid_box_available(row + 1, col + 2)
        else:
            return state.is_scout_grid_box_available(row, col) and \
                state.is_scout_grid_box_available(row, col + 1) and \
                state.is_scout_grid_box_available(row, col + 2) and \
                state.is_scout_grid_box_available(row + 1, col + 1)

def _is_valid_scout_pattern_placement_5(state: GameState, row, col, rotated=False, rotated_reverse=False, flipped_horizontal=False, flipped_vertical=False) -> bool:
    # Pattern:
    # [X][X][X]
    # [X]

    if rotated:
        if flipped_vertical:
            if flipped_horizontal:
                return state.is_scout_grid_box_available(row, col) and \
                    state.is_scout_grid_box_available(row + 1, col) and \
                    state.is_scout_grid_box_available(row + 2, col) and \
                    state.is_scout_grid_box_available(row + 2, col + 1)
            else:
                return state.is_scout_grid_box_available(row, col) and \
                    state.is_scout_grid_box_available(row , col + 1) and \
                    state.is_scout_grid_box_available(row + 1, col) and \
                    state.is_scout_grid_box_available(row + 2, col)
        else:
            if flipped_horizontal:
                return state.is_scout_grid_box_available(row, col + 1) and \
                    state.is_scout_grid_box_available(row + 1, col + 1) and \
                    state.is_scout_grid_box_available(row + 2, col) and \
                    state.is_scout_grid_box_available(row + 2, col + 1)
            else:
                return state.is_scout_grid_box_available(row, col) and \
                    state.is_scout_grid_box_available(row, col + 1) and \
                    state.is_scout_grid_box_available(row + 1, col + 1) and \
                    state.is_scout_grid_box_available(row + 2, col + 1)
    elif rotated_reverse:
        if flipped_vertical:
            if flipped_horizontal:
                return state.is_scout_grid_box_available(row, col) and \
                    state.is_scout_grid_box_available(row, col + 1) and \
                    state.is_scout_grid_box_available(row + 1, col + 1) and \
                    state.is_scout_grid_box_available(row + 2, col + 1)
            else:
                return state.is_scout_grid_box_available(row, col + 1) and \
                    state.is_scout_grid_box_available(row + 1, col + 1) and \
                    state.is_scout_grid_box_available(row + 2, col) and \
                    state.is_scout_grid_box_available(row + 2, col + 1)
        else:
            if flipped_horizontal:
                return state.is_scout_grid_box_available(row, col) and \
                    state.is_scout_grid_box_available(row, col + 1) and \
                    state.is_scout_grid_box_available(row + 1, col) and \
                    state.is_scout_grid_box_available(row + 2, col)
            else:
                return state.is_scout_grid_box_available(row, col) and \
                    state.is_scout_grid_box_available(row + 1, col) and \
                    state.is_scout_grid_box_available(row + 2, col) and \
                    state.is_scout_grid_box_available(row + 2, col + 1)
    else:
        if flipped_vertical:
            if flipped_horizontal:
                return state.is_scout_grid_box_available(row, col + 2) and \
                    state.is_scout_grid_box_available(row + 1, col) and \
                    state.is_scout_grid_box_available(row + 1, col + 1) and \
                    state.is_scout_grid_box_available(row + 1, col + 2)
            else:
                return state.is_scout_grid_box_available(row, col) and \
                    state.is_scout_grid_box_available(row, col + 1) and \
                    state.is_scout_grid_box_available(row, col + 2) and \
                    state.is_scout_grid_box_available(row + 1, col + 2)
        else:
            if flipped_horizontal:
                return state.is_scout_grid_box_available(row, col) and \
                    state.is_scout_grid_box_available(row + 1, col ) and \
                    state.is_scout_grid_box_available(row + 1, col + 1) and \
                    state.is_scout_grid_box_available(row + 1, col + 2)
            else:
                return state.is_scout_grid_box_available(row, col) and \
                    state.is_scout_grid_box_available(row, col + 1) and \
                    state.is_scout_grid_box_available(row, col + 2) and \
                    state.is_scout_grid_box_available(row + 1, col)

# Follow-up actions
def _enforce_left_cohort(state: GameState):
    assert(state.status == GameStatus.STATE_ADVANCE_COHORT, "Game does not have the correct status to perform this action")
    assert(state.left_cohort_boxes < NUM_COHORTS_BOXES, "All left cohort boxes are already filled, cannot enforce the left cohort")
    state.left_cohort_boxes += 1
    if state.left_cohort_boxes in COHORT_DICIPLINE_THRESHOLDS:
        _add_dicipline_attribute_point(state)
    elif state.left_cohort_boxes in COHORT_VALOUR_THRESHOLDS:
        _add_valour_attribute_point(state)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _enforce_center_cohort(state: GameState):
    assert(state.status == GameStatus.STATE_ADVANCE_COHORT, "Game does not have the correct status to perform this action")
    assert(state.center_cohort_boxes < NUM_COHORTS_BOXES, "All center cohort boxes are already filled, cannot enforce the center cohort")
    state.center_cohort_boxes += 1
    if state.center_cohort_boxes in COHORT_DICIPLINE_THRESHOLDS:
        _add_dicipline_attribute_point(state)
    elif state.center_cohort_boxes in COHORT_VALOUR_THRESHOLDS:
        _add_valour_attribute_point(state)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _enforce_right_cohort(state: GameState):
    assert(state.status == GameStatus.STATE_ADVANCE_COHORT, "Game does not have the correct status to perform this action")
    assert(state.right_cohort_boxes < NUM_COHORTS_BOXES, "All right cohort boxes are already filled, cannot enforce the right cohort")
    state.right_cohort_boxes += 1
    if state.right_cohort_boxes in COHORT_DICIPLINE_THRESHOLDS:
        _add_dicipline_attribute_point(state)
    elif state.right_cohort_boxes in COHORT_VALOUR_THRESHOLDS:
        _add_valour_attribute_point(state)
    state.status = GameStatus.STATUS_MAIN_LOOP

def _use_left_favour(state: GameState):
    assert(state.status == GameStatus.STATUS_USE_FAVOURS, "Game does not have the correct status to perform this action")
    assert(state.num_left_cohort_favours > 0, "No left cohort favours available to use")
    assert(state.left_cohort_incoming_disdain >= 1, "Left cohort does not have enough incoming disdain to use a favour")
    state.num_left_cohort_favours -= 1
    state.num_favours_used += 1
    state.left_cohort_incoming_disdain -= 1
    if state.get_sum_incoming_disdain() <= 0:
        _end_round(state)

def _use_center_favour(state: GameState):
    assert(state.status == GameStatus.STATUS_USE_FAVOURS, "Game does not have the correct status to perform this action")
    assert(state.num_center_cohort_favours > 0, "No center cohort favours available to use")
    assert(state.center_cohort_incoming_disdain >= 1, "Center cohort does not have enough incoming disdain to use a favour")
    state.num_center_cohort_favours -= 1
    state.num_favours_used += 1
    state.center_cohort_incoming_disdain -= 1
    if state.get_sum_incoming_disdain() <= 0:
        _end_round(state)

def _use_right_favour(state: GameState):
    assert(state.status == GameStatus.STATUS_USE_FAVOURS, "Game does not have the correct status to perform this action")
    assert(state.num_right_cohort_favours > 0, "No right cohort favours available to use")
    assert(state.right_cohort_incoming_disdain >= 1, "Right cohort does not have enough incoming disdain to use a favour")
    state.num_right_cohort_favours -= 1
    state.num_favours_used += 1
    state.right_cohort_incoming_disdain -= 1
    if state.get_sum_incoming_disdain() <= 0:
        _end_round(state)

def _use_general_favour_left(state: GameState):
    assert(state.status == GameStatus.STATUS_USE_FAVOURS, "Game does not have the correct status to perform this action")
    assert(state.num_general_favours > 0, "No general favours available to use")
    assert(state.left_cohort_incoming_disdain >= 1, "Left cohort does not have enough incoming disdain to use a favour")
    state.num_general_favours -= 1
    state.num_favours_used += 1
    state.left_cohort_incoming_disdain -= 1
    if state.get_sum_incoming_disdain() <= 0:
        _end_round(state)

def _use_general_favour_center(state: GameState):
    assert(state.status == GameStatus.STATUS_USE_FAVOURS, "Game does not have the correct status to perform this action")
    assert(state.num_general_favours > 0, "No general favours available to use")
    assert(state.center_cohort_incoming_disdain >= 1, "Center cohort does not have enough incoming disdain to use a favour")
    state.num_general_favours -= 1
    state.num_favours_used += 1
    state.center_cohort_incoming_disdain -= 1
    if state.get_sum_incoming_disdain() <= 0:
        _end_round(state)

def _use_general_favour_right(state: GameState):
    assert(state.status == GameStatus.STATUS_USE_FAVOURS, "Game does not have the correct status to perform this action")
    assert(state.num_general_favours > 0, "No general favours available to use")
    assert(state.right_cohort_incoming_disdain >= 1, "Right cohort does not have enough incoming disdain to use a favour")
    state.num_general_favours -= 1
    state.num_favours_used += 1
    state.right_cohort_incoming_disdain -= 1
    if state.get_sum_incoming_disdain() <= 0:
        _end_round(state)


# Add scoring points
def _add_renown_attribute_point(state, num_points=1):
    for _ in range(num_points):
        if state.renown_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK:
            state.renown_attribute_boxes += 1
            if state.renown_attribute_boxes >= LANDMARK_ATTRIBUTE_POINTS_THRESHOLD:
                state.landmark_1_unlocked = True
            if state.renown_attribute_boxes in ATTRIBUTE_CITIZEN_THRESHOLDS:
                state.num_civilians += 1
            elif state.renown_attribute_boxes == RENOWN_ADD_PIETY_THRESHOLD:
                _add_piety_attribute_point(state)
            elif state.renown_attribute_boxes == RENOWN_ADD_VALOUR_THRESHOLD:
                _add_valour_attribute_point(state)
            elif state.renown_attribute_boxes == RENOWN_ADD_DICIPLINE_THRESHOLD:
                _add_dicipline_attribute_point(state)

def _add_piety_attribute_point(state, num_points=1):
    for _ in range(num_points):
        if state.piety_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK:
            state.piety_attribute_boxes += 1
            if state.piety_attribute_boxes >= LANDMARK_ATTRIBUTE_POINTS_THRESHOLD:
                state.landmark_2_unlocked = True
            if state.piety_attribute_boxes in ATTRIBUTE_CITIZEN_THRESHOLDS:
                state.num_servants += 1
            elif state.piety_attribute_boxes == PIETY_ADD_RENOWN_THRESHOLD:
                _add_renown_attribute_point(state)
            elif state.piety_attribute_boxes == PIETY_ADD_VALOUR_THRESHOLD:
                _add_valour_attribute_point(state)
            elif state.piety_attribute_boxes == PIETY_ADD_DICIPLINE_THRESHOLD:
                _add_dicipline_attribute_point(state)

def _add_valour_attribute_point(state, num_points=1):
    for _ in range(num_points):
        if state.valour_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK:
            state.valour_attribute_boxes += 1
            if state.valour_attribute_boxes >= LANDMARK_ATTRIBUTE_POINTS_THRESHOLD:
                state.landmark_3_unlocked = True
            if state.valour_attribute_boxes in ATTRIBUTE_CITIZEN_THRESHOLDS:
                state.num_soldiers += 1
            elif state.valour_attribute_boxes == VALOUR_ADD_RENOWN_THRESHOLD:
                _add_renown_attribute_point(state)
            elif state.valour_attribute_boxes == VALOUR_ADD_PIETY_THRESHOLD:
                _add_piety_attribute_point(state)
            elif state.valour_attribute_boxes == VALOUR_ADD_DICIPLINE_THRESHOLD:
                _add_dicipline_attribute_point(state)

def _add_dicipline_attribute_point(state, num_points=1):
    for _ in range(num_points):
        if state.dicipline_attribute_boxes < ATTRIBUTE_POINTS_PER_TRACK:
            state.dicipline_attribute_boxes += 1
            if state.dicipline_attribute_boxes >= LANDMARK_ATTRIBUTE_POINTS_THRESHOLD:
                state.landmark_4_unlocked = True
            if state.dicipline_attribute_boxes in ATTRIBUTE_CITIZEN_THRESHOLDS:
                state.num_builders += 1
            elif state.dicipline_attribute_boxes == DICIPLINE_ADD_RENOWN_THRESHOLD:
                _add_renown_attribute_point(state)
            elif state.dicipline_attribute_boxes == DICIPLINE_ADD_PIETY_THRESHOLD:
                _add_piety_attribute_point(state)
            elif state.dicipline_attribute_boxes == DICIPLINE_ADD_VALOUR_THRESHOLD:
                _add_valour_attribute_point(state)

def _update_path_cards_points(state: GameState):
    count = 0
    # Player Card 1: Architect
    if (state.player_card_is_path_card[0]):
        num_landmarks_built = state.get_num_landmarks_built()
        count += min(num_landmarks_built, 3)
    # Player Card 2: Aristocrat
    if (state.player_card_is_path_card[1]):
        final_disdain = state.get_final_disdain()
        if final_disdain <= 0:
            count += 3
        elif final_disdain <= 2:
            count += 2
        elif final_disdain <= 4:
            count += 1
    # Player Card 3: Defender
    if (state.player_card_is_path_card[2]):
        if state.wall_boxes >= WALL_AND_FORT_SECTION_THRESHOLDS[2]:
            count += 3
        elif state.wall_boxes >= WALL_AND_FORT_SECTION_THRESHOLDS[1]:
            count += 2
        elif state.wall_boxes >= WALL_AND_FORT_SECTION_THRESHOLDS[0]:
            count += 1
    # Player Card 4: Engineer
    if (state.player_card_is_path_card[3]):
        num_large_buildings = state.get_num_large_buildings_built()
        if num_large_buildings >= 6:
            count += 3
        elif num_large_buildings >= 4:
            count += 2
        elif num_large_buildings >= 2:
            count += 1
    # Player Card 5: Fighter
    if (state.player_card_is_path_card[4]):
        count += state.get_num_cohorts_completed()
    # Player Card 6: Resource production
    if (state.player_card_is_path_card[5]):
        count += int(state.resource_production_boxes / 3)
    # Player Card 7: Merchant
    if (state.player_card_is_path_card[6]):
        count += max(int(sum(1 for box in state.market_boxes if box) / 2 - 1), 0)
    # Player Card 8: Planner
    if (state.player_card_is_path_card[7]):
        num_completed_citician_tracks = state.get_num_completed_citizen_tracks()
        if num_completed_citician_tracks >= 5:
            count += 3
        elif num_completed_citician_tracks >= 4:
            count += 2
        elif num_completed_citician_tracks >= 2:
            count += 1
    # Player Card 9: Pontiff
    if (state.player_card_is_path_card[8]):
        num_filled_temples = state.get_num_filled_temples()
        count += num_filled_temples
    # Player Card 10: Ranger
    if (state.player_card_is_path_card[9]):
        count += int((state.scouts_boxes + 1) / 2)
    # Player Card 11: Trainer
    if (state.player_card_is_path_card[10]):
        total_gladiator_strength = state.get_total_gladiator_strength()
        count += int(total_gladiator_strength / 4)
    # Player Card 12: Vanguard
    if (state.player_card_is_path_card[11]):
        if state.wall_guard_boxes >= WALL_GUARD_SECTION_THRESHOLDS[2]:
            count += 3
        elif state.wall_guard_boxes >= WALL_GUARD_SECTION_THRESHOLDS[1]:
            count += 2
        elif state.wall_guard_boxes >= WALL_GUARD_SECTION_THRESHOLDS[0]:
            count += 1

    state.path_card_points = count

def _update_disdain_malus_points(state: GameState):
    final_disdain = state.get_final_disdain()
    if final_disdain <= 0:
        state.num_disdain_points = 0
    elif final_disdain <= 5:
        state.num_disdain_points = -2 * final_disdain + 1
    elif final_disdain <= 8:
        state.num_disdain_points = -3 * final_disdain + 6
    else:
        state.num_disdain_points = -22

def get_final_score(state) -> int:
    return state.renown_attribute_boxes \
        + state.piety_attribute_boxes \
        + state.valour_attribute_boxes \
        + state.dicipline_attribute_boxes \
        + state.path_card_points \
        + state.num_disdain_points