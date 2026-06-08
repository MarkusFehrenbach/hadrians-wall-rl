import gymnasium as gym
from gymnasium import spaces
import numpy as np
from env.game_state import GameState
from env.actions import N_ACTIONS, N_OBSERVATIONS
from env.rules import MAX_ROUNDS, get_valid_actions, apply_action, validate_action, get_final_score

# For render()
from env.rules import NUM_PLAYER_CARDS, \
        NUM_COHORTS_BOXES, NUM_MINING_AND_FORESTING_BOXES, \
        NUM_WALL_GUARD_BOXES, NUM_CIPPI_BOXES, \
        NUM_WALL_AND_FORT_BOXES, NUM_TRAINING_GROUNDS_BOXES, \
        RESOURCE_PRODUCTION_BOXES, NUM_FORUM_BOXES, \
        ATTRIBUTE_POINTS_PER_TRACK, NUM_DISDAIN_BOXES, \
        NUM_CITIZEN_TRACK_BOXES, NUM_MARKET_BOXES

class HadriansWallEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(N_OBSERVATIONS, ),
            dtype=np.float32
        )

        self.action_space = spaces.Discrete(N_ACTIONS)

        self.state = None

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = GameState()
        obs = self.state.to_observation()
        return obs, {}
    
    def step(self, action):
        assert validate_action(self.state, action), "Action is not valid"
        apply_action(self.state, action)
        obs = self.state.to_observation()
        done = (self.state.current_round > MAX_ROUNDS)
        reward = (get_final_score(self.state) if done else 0)
        return obs, reward, done, False, {}

    def get_valid_actions(self):
        return get_valid_actions(self.state)
    
    def render(self):
        s = self.state

        # Count
        print(f"Round {s.current_round} | Action #{s.action_counter}")

        # Path cards
        print("Path cards: ", end="")
        print(" | ".join([s.all_player_cards[i]["name"] for i in range(NUM_PLAYER_CARDS) if s.player_card_is_path_card[i]]))
        print()
        print("----------------------------------------------------------------")

        # Resources
        print(f"Supply: {s.num_soldiers} | {s.num_builders} | {s.num_servants} | {s.num_civilians} | {s.num_resources}")

        # Scoring points
        self.render_boxes("Renown", s.renown_attribute_boxes, ATTRIBUTE_POINTS_PER_TRACK)
        self.render_boxes("Piety", s.piety_attribute_boxes, ATTRIBUTE_POINTS_PER_TRACK)
        self.render_boxes("Valour", s.valour_attribute_boxes, ATTRIBUTE_POINTS_PER_TRACK)
        self.render_boxes("Dicipline", s.dicipline_attribute_boxes, ATTRIBUTE_POINTS_PER_TRACK)
        print("Path cards" + " " * 10, end=" | ")
        print(f"{s.path_card_points}")
        print("Disdain" + " " * 12, end=" | ")
        print("[" + "o" * s.num_favours_used + "x" * (s.num_disdain - s.num_favours_used) + \
                "·" * (NUM_DISDAIN_BOXES - s.num_disdain) + "]")

        # Left sheet
        print()
        print("----------------------------------------------------------------")
        self.render_boxes("Cohorts", s.left_cohort_boxes, NUM_COHORTS_BOXES, end_line="")
        self.render_boxes("", s.center_cohort_boxes, NUM_COHORTS_BOXES, description_length=0, end_line="")
        self.render_boxes("", s.right_cohort_boxes, NUM_COHORTS_BOXES, description_length=0)
        self.render_boxes("Mining and Foresting", s.mining_and_foresting_boxes, NUM_MINING_AND_FORESTING_BOXES)
        self.render_boxes("Wall guard", s.wall_guard_boxes, NUM_WALL_GUARD_BOXES)
        self.render_boxes("Cippi", s.cippi_boxes, NUM_CIPPI_BOXES)
        self.render_boxes("Wall", s.wall_boxes, NUM_WALL_AND_FORT_BOXES)
        self.render_boxes("Fort", s.fort_boxes, NUM_WALL_AND_FORT_BOXES)
        print("Granaries" + " " * 11, end=" | ")
        print("[" + ("x" if s.small_granary_built else "·") + "|" + ("x" if s.large_granary_built else "·") + "]")
        self.render_round_boxes("Training grounds", s.training_grounds_rounds, NUM_TRAINING_GROUNDS_BOXES)
        self.render_boxes("Resource production", s.resource_production_boxes, RESOURCE_PRODUCTION_BOXES)
        print("Hotels" + " " * 14, end=" | ")
        print("[" + ("x" if s.small_hotel_built else "·") + "|" + ("x" if s.large_hotel_built else "·") + "]")
        print("Workshops" + " " * 11, end=" | ")
        print("[" + ("x" if s.small_workshop_built else "·") + "|" + ("x" if s.large_workshop_built else "·") + "]")
        print("Roads" + " " * 15, end=" | ")
        print("[" + ("x" if s.small_road_built else "·") + "|" + ("x" if s.large_road_built else "·") + "]")
        self.render_round_boxes("Forum", s.forum_rounds, NUM_FORUM_BOXES)
        print("Landmarks" + " " * 11, end=" | ")
        print("[" + ("x" if s.landmark_1_built else "·") + \
              "|" + ("x" if s.landmark_2_built else "·") + \
              "|" + ("x" if s.landmark_3_built else "·") + \
              "|" + ("x" if s.landmark_4_built else "·") + "]")
        print()
        print("----------------------------------------------------------------")
        
        # Right sheet
        self.render_boxes("Traders", s.traders_track_boxes, NUM_CITIZEN_TRACK_BOXES)
        self.render_boxes("Performers", s.performers_track_boxes, NUM_CITIZEN_TRACK_BOXES)
        self.render_boxes("Priests", s.priests_track_boxes, NUM_CITIZEN_TRACK_BOXES)
        self.render_boxes("Apparitores", s.apparitores_track_boxes, NUM_CITIZEN_TRACK_BOXES)
        self.render_boxes("Patricians", s.patricians_track_boxes, NUM_CITIZEN_TRACK_BOXES)
        print()
        print("----------------------------------------------------------------")

        print("Precincts" + " " * 11, end=" | ")
        print("[" + ("x" if s.small_precinct_built else "·") + \
              "|" + ("x" if s.medium_precinct_built else "·") + \
              "|" + ("x" if s.large_precinct_built else "·") + "]")
        print("Market" + " " * 14, end=" | ")
        print("[" + ("x" if s.market_built else "·") + "]")
        self.render_round_boxes("", s.market_goods_ids, NUM_MARKET_BOXES)
        

    def render_boxes(self, description, num_filled, max_boxes, description_length=20, filled_char='x', unfilled_char='·', end_line="\n"):
        if len(description) > 0:
            print(description, end="")
        if len(description) < description_length:
            print(" " * (description_length - len(description)), end="")
        print(" | ", end="")
        print("[" + (filled_char * num_filled) + (unfilled_char * (max_boxes - num_filled)) + "]", end=end_line)

    def render_round_boxes(self, description, rounds_list, max_boxes, description_length=20, unfilled_char='·', end_line="\n"):
        if len(description) > 0:
            print(description, end="")
        if len(description) < description_length:
            print(" " * (description_length - len(description)), end="")
        print(" | ", end="")
        print("[" + "|".join(str(r) if r is not None else unfilled_char for r in rounds_list), \
                end=("" if len(rounds_list) >= max_boxes else "|"))
        print("|".join(unfilled_char * (max(0, max_boxes - len(rounds_list)))) + "]", end=end_line)


    def close(self):
        pass