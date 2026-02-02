l = input().split(' ')
hit = int(l[0])
heads = int(l[1])
regen_heads = int(l[2])

def battle(hit, heads, regen_heads):
    if heads <= hit:
        return '1'

    delta = hit - regen_heads
    if delta <= 0:
        return 'NO'

    return (heads-hit-1) // delta + 2


print(battle(hit, heads, regen_heads))