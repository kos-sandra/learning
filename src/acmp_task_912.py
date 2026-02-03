def most_popular_color(counts):
    count_maxes = 0
    res = 0
    max_value = max(counts.values())

    for key in counts:
        if counts[key] == max_value:
            if count_maxes == 1:
                return 0
            count_maxes += 1
            res = key
    return res

n = int(input())
counts = {}

for x in input().split():
    if x not in counts:
        counts[x] = 0
    counts[x] += 1

print(most_popular_color(counts))


