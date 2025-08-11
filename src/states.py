from typing import Literal, TypedDict

# Graph states
class OverallState(TypedDict):
    """Overall state of the game."""
    game_id: str
    room_id: str
    player_id: str
    player_nickname: str
    player_role: Literal["spymaster", "guesser"]
    team: Literal["red", "blue"]
    turn: Literal["red", "blue"]
    instruction: str
    instruction_number: int
    instruction_type: Literal["word", "number"]
    game_status: Literal["waiting", "playing", "finished"]