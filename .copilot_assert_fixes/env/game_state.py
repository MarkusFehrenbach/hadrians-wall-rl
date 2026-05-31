import random

import numpy as np

from env.rules import *
import env.cards as cards
from env.enums import GameStatus

# --- Game state constants ---#
INVENTORY_NORM_FACTOR = 10

class GameState:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)

        # Internal state
        self.status = GameStatus.STATUS_INIT
        self.action_counter = 0

        # Cards
        self.all_fate_cards = cards.load_fate_cards()
        self.fate_card_pile = None
        self.current_fate_card_id = None
        self.left_fate_cards_remaining = NUM_LEFT_FATE_CARDS
        self.center_fate_cards_remaining = NUM_CENTER_FATE_CARDS
        self.right_fate_cards_remaining = NUM_RIGHT_FATE_CARDS
        self.reshuffle_fate_cards()
        self.all_player_cards = cards.load_player_cards()
        self.player_card_pile = None
        self.neighbor_card_pile = None

        # Game meta
        self.current_round = 0
        self.num_pict_attacks = 0
        self.left_cohort_incoming_disdain = 0
        self.num_left_cohort_favours = 0
        self.center_cohort_incoming_disdain = 0
        self.num_center_cohort_favours = 0
        self.right_cohort_incoming_disdain = 0
        self.num_right_cohort_favours = 0
        self.num_general_favours = 0
        self.num_soldiers = 0
        self.num_builders = 0
        self.num_servants = 0
        self.num_civilians = 0
        self.num_resources = 0
        self.num_disdain = 0
        self.num_favours_used = 0
        self.infrastructure_level = 0

        # Fate cards
        self.fate_card_revealed = [False] * NUM_TOTAL_FATE_CARDS

        # Player cards
        self.player_card_revealed = [False] * NUM_PLAYER_CARDS
        self.player_card_is_path_card = [False] * NUM_PLAYER_CARDS
        self.current_prospect_card_id = None
        self.left_player_card_id = None
        self.right_player_card_id = None

        # Neighbor cards
        self.neighbor_card_revealed = [False] * NUM_PLAYER_CARDS
        self.neighbor_prospect_card_1_id = None
        self.neighbor_prospect_card_2_id = None

        # Initial shuffle
        self.shuffle_players_cards()

        # Left sheet state
        self.left_cohort_boxes = 0
        self.center_cohort_boxes = 0
        self.right_cohort_boxes = 0
        self.mining_and_foresting_boxes = 0
        self.wall_guard_boxes = 0
        self.cippi_boxes = 0
        self.cippi_boxes_unlocked = 0
        self.wall_boxes = 0
        self.fort_boxes = 0
        self.wall_and_fort_boxes_unlocked = 0
        self.small_granary_unlocked = False
        self.small_granary_built = False
        self.large_granary_unlocked = False
        self.large_granary_built = False
        self.resource_production_boxes = 1
        self.training_grounds_boxes_available = NUM_TRAINING_GROUNDS_BOXES
        self.training_grounds_available = False
        self.training_grounds_rounds = []
        self.small_hotel_unlocked = False
        self.small_hotel_built = False
        self.large_hotel_unlocked = False
        self.large_hotel_built = False
        self.small_workshop_unlocked = False
        self.small_workshop_built = False
        self.large_workshop_unlocked = False
        self.large_workshop_built = False
        self.small_road_unlocked = False
        self.small_road_built = False
        self.large_road_unlocked = False
        self.large_road_built = False
        self.forum_boxes_available = NUM_FORUM_BOXES
        self.forum_available = False
        self.forum_rounds = []
        self.landmark_1_unlocked = False
        self.landmark_1_built = False
        self.landmark_2_unlocked = False
        self.landmark_2_built = False
        self.landmark_3_unlocked = False
        self.landmark_3_built = False
        self.landmark_4_unlocked = False
        self.landmark_4_built = False

        # Right sheet state
        # Traders
        self.traders_track_boxes = 0
        self.small_precinct_unlocked = False
        self.small_precinct_built = False
        self.medium_precinct_unlocked = False
        self.medium_precinct_built = False
        self.large_precinct_unlocked = False
        self.large_precinct_built = False
        self.market_unlocked = False
        self.market_built = False
        self.market_goods_ids = [None] * NUM_MARKET_BOXES
        self.market_boxes = [False] * NUM_MARKET_BOXES
        self.market_boxes_unlocked = 0

        # Performers
        self.performers_track_boxes = 0
        self.theater_unlocked = False
        self.theater_built = False
        self.theater_boxes = [False] * NUM_THEATER_BOXES
        self.theater_boxes_unlocked = 0
        self.theater_available = True
        self.theater_boxes_rounds = [None] * NUM_THEATER_BOXES
        self.colosseum_unlocked = False
        self.colosseum_built = False
        self.gladiator_boxes_unlocked = 0
        self.gladiator_1_strength = 0
        self.gladiator_1_damage = 0
        self.gladiator_1_can_battle = True
        self.gladiator_1_battle_rounds = []
        self.gladiator_2_strength = 0
        self.gladiator_2_damage = 0
        self.gladiator_2_can_battle = True
        self.gladiator_2_battle_rounds = []

        # Priests
        self.priests_track_boxes = 0
        self.small_garden_unlocked = False
        self.small_garden_built = False
        self.large_garden_unlocked = False
        self.large_garden_built = False
        self.small_temple_unlocked = False
        self.small_temple_built = False
        self.small_temple_boxes = 0
        self.medium_temple_unlocked = False
        self.medium_temple_built = False
        self.medium_temple_boxes = 0
        self.medium_temple_boxes_unlocked = 0
        self.large_temple_unlocked = False
        self.large_temple_built = False
        self.large_temple_boxes = 0
        self.large_temple_boxes_unlocked = 0

        # Apparitores
        self.apparitores_track_boxes = 0
        self.baths_unlocked = False
        self.baths_built = False
        self.baths_boxes = 0
        self.baths_boxes_unlocked = 0
        self.baths_boxes_available = MAX_NUM_BRIBES_PER_ROUND
        self.baths_rounds = []
        self.courthouse_unlocked = False
        self.courthouse_built = False
        self.courthouse_get_servant_boxes = 0
        self.courthouse_get_servant_unlocked = 0
        self.courthouse_get_servant_available = True
        self.courthouse_get_servant_rounds = []
        self.courthouse_builder_to_two_servants_boxes = 0
        self.courthouse_builder_to_two_servants_unlocked = 0
        self.courthouse_builder_to_two_servants_available = True
        self.courthouse_builder_to_two_servants_rounds = []
        self.courthouse_servant_to_builder_boxes = 0
        self.courthouse_servant_to_builder_unlocked = 0
        self.courthouse_servant_to_builder_available = True
        self.courthouse_servant_to_builder_rounds = []

        # Patricians
        self.patricians_track_boxes = 0
        self.diplomat_boxes_unlocked = 0
        self.diplomat_left_available = True
        self.diplomat_center_available = True
        self.diplomat_right_available = True
        self.scouts_boxes = 0
        self.scouts_boxes_unlocked = 0
        self.scouts_grid = [False] * (NUM_SCOUTS_GRID_ROWS * NUM_SCOUTS_GRID_COLS)
        self.chosen_scout_pattern = None

        # Scoring
        self.renown_attribute_boxes = 0
        self.piety_attribute_boxes = 0
        self.valour_attribute_boxes = 0
        self.dicipline_attribute_boxes = 0
        self.path_card_points = 0
        self.num_disdain_points = 0

        # Setup for first round
        start_new_round(self)

    def to_observation(self):
        ### Convert the game state to a normalized observation vector ###
        return np.array([
            # Game meta
            1 - self.current_round / MAX_ROUNDS,
            self.num_pict_attacks / MAX_PICT_ATTACKS,
            self.left_cohort_incoming_disdain / MAX_PICT_ATTACKS,
            self.num_left_cohort_favours / MAX_FAVOURS,
            self.center_cohort_incoming_disdain / MAX_PICT_ATTACKS,
            self.num_center_cohort_favours / MAX_FAVOURS,
            self.right_cohort_incoming_disdain / MAX_PICT_ATTACKS,
            self.num_right_cohort_favours / MAX_FAVOURS,
            self.num_general_favours / MAX_FAVOURS,
            self.left_fate_cards_remaining / NUM_LEFT_FATE_CARDS,
            self.center_fate_cards_remaining / NUM_CENTER_FATE_CARDS,
            self.right_fate_cards_remaining / NUM_RIGHT_FATE_CARDS,
            self.num_soldiers / INVENTORY_NORM_FACTOR,
            self.num_builders / INVENTORY_NORM_FACTOR,
            self.num_servants / INVENTORY_NORM_FACTOR,
            self.num_civilians / INVENTORY_NORM_FACTOR,
            self.num_resources / INVENTORY_NORM_FACTOR,
            self.num_disdain / NUM_DISDAIN_BOXES,
            self.num_favours_used / MAX_FAVOURS,
            self.infrastructure_level / MAX_INFRASTRUCTURE_LEVEL,

            # Fate cards
            *self.fate_card_revealed,

            # Player cards
            *self.player_card_revealed,
            *self.player_card_is_path_card,
            *[self.current_prospect_card_id == i for i in range(NUM_PLAYER_CARDS)],
            *[self.left_player_card_id == i for i in range(NUM_PLAYER_CARDS)],
            *[self.right_player_card_id == i for i in range(NUM_PLAYER_CARDS)],

            # neighbor cards
            *self.neighbor_card_revealed,
            *[self.neighbor_prospect_card_1_id == i or self.neighbor_prospect_card_2_id == i for i in range(NUM_PLAYER_CARDS)],

            # Left sheet state
            self.left_cohort_boxes / NUM_COHORTS_BOXES,
            self.center_cohort_boxes / NUM_COHORTS_BOXES,
            self.right_cohort_boxes / NUM_COHORTS_BOXES,
            self.mining_and_foresting_boxes / NUM_MINING_AND_FORESTING_BOXES,
            self.wall_guard_boxes / NUM_WALL_GUARD_BOXES,
            self.cippi_boxes / NUM_CIPPI_BOXES,
            self.cippi_boxes_unlocked / NUM_CIPPI_BOXES,
            self.wall_boxes / NUM_WALL_AND_FORT_BOXES,
            self.fort_boxes / NUM_WALL_AND_FORT_BOXES,
            self.wall_and_fort_boxes_unlocked / NUM_WALL_AND_FORT_BOXES,
            self.small_granary_unlocked,
            self.small_granary_built,
            self.large_granary_unlocked,
            self.large_granary_built,
            self.resource_production_boxes / RESOURCE_PRODUCTION_BOXES,
            self.training_grounds_boxes_available / NUM_TRAINING_GROUNDS_BOXES,
            self.training_grounds_available,
            self.small_hotel_unlocked,
            self.small_hotel_built,
            self.large_hotel_unlocked,
            self.large_hotel_built,
            self.small_workshop_unlocked,
            self.small_workshop_built,
            self.large_workshop_unlocked,
            self.large_workshop_built,
            self.small_road_unlocked,
            self.small_road_built,
            self.large_road_unlocked,
            self.large_road_built,
            self.forum_boxes_available / NUM_FORUM_BOXES,
            self.forum_available,
            self.landmark_1_unlocked,
            self.landmark_1_built,
            self.landmark_2_unlocked,
            self.landmark_2_built,
            self.landmark_3_unlocked,
            self.landmark_3_built,
            self.landmark_4_unlocked,
            self.landmark_4_built,

            # Right sheet state
            # Traders
            self.traders_track_boxes / NUM_CITIZEN_TRACK_BOXES,
            self.small_precinct_unlocked,
            self.small_precinct_built,
            self.medium_precinct_unlocked,
            self.medium_precinct_built,
            self.large_precinct_unlocked,
            self.large_precinct_built,
            self.market_unlocked,
            self.market_built,
            *[i+1 in self.market_goods_ids for i in range(6)],
            *self.market_boxes,
            self.market_boxes_unlocked / NUM_MARKET_BOXES,

            # Performers
            self.performers_track_boxes / NUM_CITIZEN_TRACK_BOXES,
            self.theater_unlocked,
            self.theater_built,
            *self.theater_boxes,
            self.theater_boxes_unlocked / NUM_THEATER_BOXES,
            self.theater_available,
            self.colosseum_unlocked,
            self.colosseum_built,
            self.gladiator_boxes_unlocked / NUM_GLADIATOR_BOXES,
            self.gladiator_1_strength / NUM_GLADIATOR_BOXES,
            self.gladiator_1_damage / NUM_GLADIATOR_BOXES,
            self.gladiator_1_can_battle,
            self.gladiator_2_strength / NUM_GLADIATOR_BOXES,
            self.gladiator_2_damage / NUM_GLADIATOR_BOXES,
            self.gladiator_2_can_battle,

            # Priests
            self.priests_track_boxes / NUM_CITIZEN_TRACK_BOXES,
            self.small_garden_unlocked,
            self.small_garden_built,
            self.large_garden_unlocked,
            self.large_garden_built,
            self.small_temple_unlocked,
            self.small_temple_built,
            self.small_temple_boxes / NUM_SMALL_TEMPLE_BOXES,
            self.medium_temple_unlocked,
            self.medium_temple_built,
            self.medium_temple_boxes / NUM_MEDIUM_TEMPLE_BOXES,
            self.medium_temple_boxes_unlocked / NUM_MEDIUM_TEMPLE_BOXES,
            self.large_temple_unlocked,
            self.large_temple_built,
            self.large_temple_boxes / NUM_LARGE_TEMPLE_BOXES,
            self.large_temple_boxes_unlocked / NUM_LARGE_TEMPLE_BOXES,

            # Apparitores
            self.apparitores_track_boxes / NUM_CITIZEN_TRACK_BOXES,
            self.baths_unlocked,
            self.baths_built,
            self.baths_boxes / NUM_BATHS_BOXES,
            self.baths_boxes_unlocked / NUM_BATHS_BOXES,
            self.baths_boxes_available / MAX_NUM_BRIBES_PER_ROUND,
            self.courthouse_unlocked,
            self.courthouse_built,
            self.courthouse_get_servant_boxes / MAX_NUM_COURTHOUSE_ACTIONS,
            self.courthouse_get_servant_unlocked / MAX_NUM_COURTHOUSE_ACTIONS,
            self.courthouse_get_servant_available,
            self.courthouse_builder_to_two_servants_boxes / MAX_NUM_COURTHOUSE_ACTIONS,
            self.courthouse_builder_to_two_servants_unlocked / MAX_NUM_COURTHOUSE_ACTIONS,
            self.courthouse_builder_to_two_servants_available,
            self.courthouse_servant_to_builder_boxes / MAX_NUM_COURTHOUSE_ACTIONS,
            self.courthouse_servant_to_builder_unlocked / MAX_NUM_COURTHOUSE_ACTIONS,
            self.courthouse_servant_to_builder_available,
            
            # Patricians
            self.patricians_track_boxes / NUM_CITIZEN_TRACK_BOXES,
            self.diplomat_boxes_unlocked / NUM_DIPLOTMAT_BOXES,
            self.diplomat_left_available,
            self.diplomat_center_available,
            self.diplomat_right_available,
            self.scouts_boxes / NUM_SCOUTS_BOXES,
            self.scouts_boxes_unlocked / NUM_SCOUTS_BOXES,
            *self.scouts_grid,

            # Scoring            
            self.renown_attribute_boxes / ATTRIBUTE_POINTS_PER_TRACK,
            self.piety_attribute_boxes / ATTRIBUTE_POINTS_PER_TRACK,
            self.valour_attribute_boxes / ATTRIBUTE_POINTS_PER_TRACK,
            self.dicipline_attribute_boxes / ATTRIBUTE_POINTS_PER_TRACK,
            self.path_card_points / ATTRIBUTE_POINTS_PER_TRACK,
            self.num_disdain_points / ATTRIBUTE_POINTS_PER_TRACK,
        ], dtype=np.float32)

    # Actions
    def add_good_to_market(self, goods_id, index):
        if 0 <= index < NUM_MARKET_BOXES:
            self.market_goods_ids[index] = goods_id
            self.market_boxes[index] = True

    def draw_fate_card(self):
        if len(self.fate_card_pile) == 0:
            self.reshuffle_fate_cards()
        self.current_fate_card_id = self.fate_card_pile.pop(0)["id"]
        self.fate_card_revealed[self.current_fate_card_id] = True
        pict_attack_direction = self.get_current_fate_card_pict_attack_direction()
        match pict_attack_direction:
            case 'left':
                self.left_fate_cards_remaining -= 1
            case 'center':
                self.center_fate_cards_remaining -= 1
            case 'right':
                self.right_fate_cards_remaining -= 1
            case _:
                raise ValueError(f"Unknown attack direction: {pict_attack_direction}")

    def draw_player_cards(self):
        assert len(self.player_card_pile) >= 2, "There have to be at least two player cards in the player card pile!"
        self.left_player_card_id = self.player_card_pile.pop(0)["id"]
        self.right_player_card_id = self.player_card_pile.pop(0)["id"]
        self.player_card_revealed[self.left_player_card_id] = True
        self.player_card_revealed[self.right_player_card_id] = True

    def draw_neighbor_cards(self):
        assert len(self.neighbor_card_pile) >= 2, "There have to be at least two player cards in the neighbor card pile!"
        self.neighbor_prospect_card_1_id = self.neighbor_card_pile.pop(0)["id"]
        self.neighbor_prospect_card_2_id = self.neighbor_card_pile.pop(0)["id"]
        self.neighbor_card_revealed[self.neighbor_prospect_card_1_id] = True
        self.neighbor_card_revealed[self.neighbor_prospect_card_2_id] = True

    def reshuffle_fate_cards(self):
        self.current_fate_card_id = None
        self.fate_card_revealed = [False] * NUM_TOTAL_FATE_CARDS
        self.left_fate_cards_remaining = NUM_LEFT_FATE_CARDS
        self.center_fate_cards_remaining = NUM_CENTER_FATE_CARDS
        self.right_fate_cards_remaining = NUM_RIGHT_FATE_CARDS
        self.fate_card_pile = self.all_fate_cards.copy()
        random.shuffle(self.fate_card_pile)

    def shuffle_players_cards(self):
        self.player_card_pile = self.all_player_cards.copy()
        self.neighbor_card_pile = self.all_player_cards.copy()
        random.shuffle(self.player_card_pile)
        random.shuffle(self.neighbor_card_pile)
        self.player_card_revealed = [False] * NUM_PLAYER_CARDS
        self.player_card_is_path_card = [False] * NUM_PLAYER_CARDS
        self.current_prospect_card_id = None
        self.left_player_card_id = None
        self.right_player_card_id = None
        self.neighbor_card_revealed = [False] * NUM_PLAYER_CARDS
        self.neighbor_prospect_card_1_id = None
        self.neighbor_prospect_card_2_id = None

    # Get information
    # General
    def get_current_fate_card(self):
        if self.current_fate_card_id is None:
            return None
        return self.all_fate_cards[self.current_fate_card_id]

    def get_current_prospect_card(self):
        return self.all_player_cards[self.current_prospect_card_id]

    def get_neighbor_prospect_card_1(self):
        if self.neighbor_prospect_card_1_id is None:
            return None
        return self.all_player_cards[self.neighbor_prospect_card_1_id]

    def get_neighbor_prospect_card_2(self):
        if self.neighbor_prospect_card_2_id is None:
            return None
        return self.all_player_cards[self.neighbor_prospect_card_2_id]

    # Fate card information
    def get_current_fate_card_goods_id(self):
        if self.current_fate_card_id is None:
            return None
        return self.get_current_fate_card()["goods_id"]

    def get_current_fate_card_num_soldiers(self):
        if self.current_fate_card_id is None:
            return None
        return self.get_current_fate_card()["num_soldiers"]

    def get_current_fate_card_num_builders(self):
        if self.current_fate_card_id is None:
            return None
        return self.get_current_fate_card()["num_builders"]

    def get_current_fate_card_num_servants(self):
        if self.current_fate_card_id is None:
            return None
        return self.get_current_fate_card()["num_servants"]

    def get_current_fate_card_num_civilians(self):
        if self.current_fate_card_id is None:
            return None
        return self.get_current_fate_card()["num_civilians"]

    def get_current_fate_card_num_resources(self):
        if self.current_fate_card_id is None:
            return None
        return self.get_current_fate_card()["num_resources"]

    def get_current_fate_card_pict_attack_direction(self):
        if self.current_fate_card_id is None:
            return None
        return self.get_current_fate_card()["pict_attack_direction"]

    # Player card information
    def get_current_prospect_card_goods_id(self):
        if self.current_prospect_card_id is None:
            return None
        return self.get_current_prospect_card()["goods_id"]

    def get_current_prospect_card_num_soldiers(self):
        if self.current_prospect_card_id is None:
            return None
        return self.get_current_prospect_card()["num_soldiers"]

    def get_current_prospect_card_num_builders(self):
        if self.current_prospect_card_id is None:
            return None
        return self.get_current_prospect_card()["num_builders"]

    def get_current_prospect_card_num_servants(self):
        if self.current_prospect_card_id is None:
            return None
        return self.get_current_prospect_card()["num_servants"]

    def get_current_prospect_card_num_civilians(self):
        if self.current_prospect_card_id is None:
            return None
        return self.get_current_prospect_card()["num_civilians"]

    def get_current_prospect_card_num_resources(self):
        if self.current_prospect_card_id is None:
            return None
        return self.get_current_prospect_card()["num_resources"]

    def get_current_prospect_card_scout_pattern_id(self):
        if self.current_prospect_card_id is None:
            return None
        return self.get_current_prospect_card()["scout_pattern_id"]

    # Pict attacks
    def get_sum_incoming_disdain(self):
        return self.left_cohort_incoming_disdain + \
            self.center_cohort_incoming_disdain + \
            self.right_cohort_incoming_disdain


    # Left sheet
    def get_final_disdain(self):
        return self.num_disdain - self.baths_boxes

    def get_num_cohorts_completed(self):
        return sum([
            self.left_cohort_boxes >= NUM_COHORTS_BOXES,
            self.center_cohort_boxes >= NUM_COHORTS_BOXES,
            self.right_cohort_boxes >= NUM_COHORTS_BOXES,
        ])

    def get_num_completed_citizen_tracks(self):
        return sum([
            self.traders_track_boxes >= NUM_CITIZEN_TRACK_BOXES,
            self.performers_track_boxes >= NUM_CITIZEN_TRACK_BOXES,
            self.priests_track_boxes >= NUM_CITIZEN_TRACK_BOXES,
            self.apparitores_track_boxes >= NUM_CITIZEN_TRACK_BOXES,
            self.patricians_track_boxes >= NUM_CITIZEN_TRACK_BOXES,
        ])

    def get_num_distinct_goods(self):
        return len(set([goods_id for goods_id in self.market_goods_ids if goods_id is not None]))

    def get_num_filled_temples(self):
        return sum([
            self.small_temple_boxes >= NUM_SMALL_TEMPLE_BOXES,
            self.medium_temple_boxes >= NUM_MEDIUM_TEMPLE_BOXES,
            self.large_temple_boxes >= NUM_LARGE_TEMPLE_BOXES,
        ])

    def get_num_landmarks_built(self):
        return sum([
            self.landmark_1_built,
            self.landmark_2_built,
            self.landmark_3_built,
            self.landmark_4_built
        ])

    def get_num_large_buildings_built(self):
        return sum([
            self.large_granary_built,
            self.large_hotel_built,
            self.large_workshop_built,
            self.large_road_built,
            self.large_precinct_built,
            self.large_garden_built,
            self.large_temple_built,
        ])

    def get_neighbor_prospect_card_1_goods_id(self):
        if self.neighbor_prospect_card_1_id is None:
            return None
        return self.all_player_cards[self.neighbor_prospect_card_1_id]["goods_id"]

    def get_neighbor_prospect_card_2_goods_id(self):
        if self.neighbor_prospect_card_2_id is None:
            return None
        return self.all_player_cards[self.neighbor_prospect_card_2_id]["goods_id"]

    # Right sheet
    # Traders
    def get_next_free_market_box(self):
        for i in range(self.market_boxes_unlocked):
            if not self.market_boxes[i]:
                return i
        return None

    def has_free_market_box(self):
        return self.get_next_free_market_box() is not None

    # Performers
    def get_current_fate_card_gladiator_damage(self):
        if self.current_fate_card_id is None:
            return None
        return self.get_current_fate_card()["gladiator_damage"]

    def get_total_gladiator_strength(self):
        return self.gladiator_1_strength + self.gladiator_2_strength

    def is_gladiator_1_alive(self):
        return self.gladiator_1_strength - self.gladiator_1_damage > 0

    def is_gladiator_2_alive(self):
        return self.gladiator_2_strength - self.gladiator_2_damage > 0

    # Priests
    def is_small_temple_filled(self):
        return self.small_temple_boxes >= NUM_SMALL_TEMPLE_BOXES

    def is_medium_temple_filled(self):
        return self.medium_temple_boxes >= NUM_MEDIUM_TEMPLE_BOXES

    def is_large_temple_filled(self):
        return self.large_temple_boxes >= NUM_LARGE_TEMPLE_BOXES

    # Patricians
    def has_diplomat_box_available(self):
        return self.get_num_diplomat_boxes_used() < self.diplomat_boxes_unlocked

    def get_num_diplomat_boxes_used(self):
        return (0 if self.diplomat_left_available else 1) + \
            (0 if self.diplomat_center_available else 1) + \
            (0 if self.diplomat_right_available else 1)

    def get_neighbor_prospect_card_1_scout_pattern_id(self):
        if self.neighbor_prospect_card_1_id is None:
            return None
        return self.get_neighbor_prospect_card_1()["scout_pattern_id"]

    def get_neighbor_prospect_card_2_scout_pattern_id(self):
        if self.neighbor_prospect_card_2_id is None:
            return None
        return self.get_neighbor_prospect_card_2()["scout_pattern_id"]

    def is_scout_grid_box_available(self, row, col):
        index = row * NUM_SCOUTS_GRID_COLS + col
        return not self.scouts_grid[index]

    def fill_scout_grid_box(self, row, col):
        index = row * NUM_SCOUTS_GRID_COLS + col
        self.scouts_grid[index] = True