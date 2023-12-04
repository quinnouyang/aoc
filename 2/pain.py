RED = 12
GREEN = 13
BLUE = 14

with open("input.txt") as f:
    print(
        sum(
            int(split[1][:-1])
            for line in f
            if (split := line.split()) or True
            if not any(
                ("red" in color and n > RED)
                or ("green" in color and n > GREEN)
                or ("blue" in color and n > BLUE)
                for i in range(2, len(split) - 1, 2)
                if (color := split[i + 1]) and (n := int(split[i]))
            )
        )
    )
