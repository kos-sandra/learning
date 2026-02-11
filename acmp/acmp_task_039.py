def find_index_max(lst):
    index_mmx = 0
    for i in range(len(lst)):
        if lst[i] >= lst[index_mmx]:
            index_mmx = i
    return index_mmx


def strategy_max_and_next_max(rates):
    total = 0
    while len(rates) > 0:
        hair_len = find_index_max(rates) + 1
        max_rate = rates[hair_len - 1]
        total += max_rate * hair_len
        rates = rates[hair_len:]
    return total


n = int(input())
rates = [int(x) for x in input().split()]
print(strategy_max_and_next_max(rates))
