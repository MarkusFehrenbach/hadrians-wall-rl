from enum import IntEnum, auto


class GameStatus(IntEnum):
    STATUS_INIT = auto()
    STATUS_MAIN_LOOP = auto()
    STATUS_CHOOSE_PLAYER_CARD = auto()
    STATUS_ADVANCE_COHORT = auto()
    STATUS_USE_FAVOURS = auto()
    STATUS_CHOOSE_PIETY_OR_DISCIPLINE = auto()
    STATUS_CHOOSE_RENOWN_OR_VALOUR = auto()
    STATUS_CHOOSE_TWO_ATTRIBUTES = auto()
    STATUS_CHOOSE_ATTRIBUTE = auto()
    STATUS_SEND_SCOUT = auto()
