beat_map = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
beat_by_map = {v: k for k, v in beat_map.items()}


def map_him_to_rps(string: str) -> str:
    mapping = {"A": "rock", "B": "paper", "C": "scissors"}
    return mapping.get(string)


def get_my_input(him: str, result: str) -> str:
    if result == "Y":
        return him
    if result == "X":
        return beat_map.get(him)
    else:
        return beat_by_map.get(him)


def map_points(string: str) -> int:
    mapping = {"rock": 1, "paper": 2, "scissors": 3}
    return mapping.get(string)


def compute_win_score(me: str, him: str) -> int:

    if me == him:
        return 3
    elif beat_map.get(me) == him:
        return 6
    return 0


def compute_my_points(me: str, him: str) -> int:
    return compute_win_score(me, him) + map_points(me)


score = 0
with open("day2_input.txt") as f:
    for line in f:
        him, result = line.strip("\n").split(" ")
        print(him, result)
        him = map_him_to_rps(him)
        me = get_my_input(him, result)
        print(compute_my_points(me, him))
        score += compute_my_points(me, him)
        print()
print(score)
