def map_him_to_rps(string: str) -> str:
    mapping = {"A": "rock", "B": "paper", "C": "scissors"}
    return mapping.get(string)


def map_me_to_rps(string: str) -> str:
    mapping = {"X": "rock", "Y": "paper", "Z": "scissors"}
    return mapping.get(string)


def map_points(string: str) -> int:
    mapping = {"rock": 1, "paper": 2, "scissors": 3}
    return mapping.get(string)


def compute_win_score(me: str, him: str) -> int:
    beat_map = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if me == him:
        return 3
    elif beat_map.get(me) == him:
        return 6
    return 0


def compute_my_points(me: str, him: str) -> int:
    me = map_me_to_rps(me)
    him = map_him_to_rps(him)
    return compute_win_score(me, him) + map_points(me)


score = 0
with open("day2_input.txt") as f:
    for line in f:
        him, me = line.strip("\n").split(" ")
        print(him, me)
        print(compute_my_points(me, him))
        score += compute_my_points(me, him)
print(score)
