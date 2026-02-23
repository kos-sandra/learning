def mult(a,b):
    return a*b

def result_of_attempts(submitted_attempts, tests_points, extra_points):
    sum_points_for_attempts = []
    m = len(submitted_attempts)
    for i in range(m):
        points_for_attempt = map(mult, submitted_attempts[i], tests_points)
        sum_points_for_attempts.append(sum(points_for_attempt))

    for i in range(m):
        if all(x == 1 for x in submitted_attempts[i]):
            sum_points_for_attempts[i] += extra_points

    return sum_points_for_attempts


def score(sum_points_for_attempts):
    result = []
    curr_max = sum_points_for_attempts[0]
    for i in range(len(sum_points_for_attempts)):
        x = sum_points_for_attempts[i]
        if x > curr_max:
            curr_max = x
        else:
            x = curr_max
        result.append(x)

    return result



n = int(input())
tests_points = [int(x) for x in input().split()]
extra_points = int(input())
m = int(input())
submitted_attempts = []

for i in range(m):
    X = [int(x) for x in input().split()]
    submitted_attempts.append(X)

sum_points_for_attempts = result_of_attempts(submitted_attempts, tests_points, extra_points)

penalty = 0
for i in range(m):
    sum_points_for_attempts[i] -= penalty
    penalty += 2

result = score(sum_points_for_attempts)

for i in range(m):
    print(result[i])



