elves = {}
i = 0

with open("day1_input.txt", "r") as f:
    for line in f:
        cal = line.strip("\n")
        if cal:
            elves[i] = elves.get(i, 0) + int(cal)
        else:
            i += 1

sorted_values = sorted(list(elves.values()))
last_three = sorted_values[-3:]

print(last_three)
print(sum(last_three))
