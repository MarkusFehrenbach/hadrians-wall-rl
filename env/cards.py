"""Simple loader for JSON card data in env/data/"""
import json
from pathlib import Path
from typing import List, Dict

DATA_DIR = Path(__file__).parent / "data"
FATE_FILE = DATA_DIR / "fate_cards.json"
PLAYER_FILE = DATA_DIR / "player_cards.json"


def _load(path: Path) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_fate_cards() -> List[Dict]:
    """Return list of fate card dicts."""
    return _load(FATE_FILE)


def load_player_cards() -> List[Dict]:
    """Return list of player card dicts."""
    return _load(PLAYER_FILE)


__all__ = ["load_fate_cards", "load_player_cards"]


if __name__ == "__main__":
    print("fate:", len(load_fate_cards()))
    print("player:", len(load_player_cards()))
