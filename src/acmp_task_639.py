def read_block():
    result = []
    n = int(input())
    for i in range(n):
        k = input().split()
        k[0] = float(k[0])
        result.append(k)
    return result


def merge_blocks(all_participants, block):
    result = []
    a = all_participants
    b = block
    i, j = 0, 0
    while True:
        if i == len(a):
            return result + b[j:]
        if j == len(b):
            return result + a[i:]
        if a[i] >= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1


def print_participants(participants):
    print(len(participants))
    for x in participants:
        print(f"{x[0]:.2f}", x[1])


n = int(input())
all_participants = []

for i in range(n):
    block = read_block()
    all_participants = merge_blocks(all_participants, block)

print_participants(all_participants)

# n = int(input())
# total = 0
# participants = []
#
# for i in range(n):
#     nn = int(input())
#     total += nn
#     for j in range(nn):
#         k = input().split()
#         k[0] = float(k[0])
#         participants.append(k)
#
# result = sorted(participants, key=lambda x: x[0], reverse=True)
#
# print(total)
# for x in result:
#     print(f"{x[0]:.2f}", x[1])