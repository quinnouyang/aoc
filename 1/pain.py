with open("input.txt") as f:
    print(
        sum(
            int(
                f"{next(ch for ch in line if ch.isnumeric())}{next(ch for ch in line[::-1] if ch.isnumeric())}"
            )
            for line in f
        )
    )

DIGITS = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)

with open("input.txt") as f:
    print(
        sum(
            10
            * min(
                next((i, int(ch)) for i, ch in enumerate(line) if ch.isnumeric()),
                min(
                    (
                        (j, i)
                        for (i, d) in enumerate(DIGITS)
                        if (j := line.find(d)) != -1
                    ),
                    default=(9999, -1),
                ),
            )[1]
            + max(
                next(
                    (len(line) - i - 1, int(ch))
                    for i, ch in enumerate(line[::-1])
                    if ch.isnumeric()
                ),
                max(
                    (
                        (j, i)
                        for (i, d) in enumerate(DIGITS)
                        if (j := line.rfind(d)) != -1
                    ),
                    default=(-1, -1),
                ),
            )[1]
            for line in f
        )
    )
