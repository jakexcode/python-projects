s = ["aabbbaa", "aaabccaattt"]
t = ["aaabbba", "aaabaadssss"]


def equivalent_test(list1, list2):
    conditions = []
    for i in range(len(list1)):
        values = {}
        for j in range(len(list1[i])):
            if list1[i][j] not in values:
                values[list1[i][j]] = 1
            else:
                values[list1[i][j]] += 1

        for j in range(len(list2[i])):
            if list2[i][j] not in values:
                values[list2[i][j]] = -1
            else:
                values[list2[i][j]] -= 1
    for o in values:
        if values[o] < -3 or values[o] > 3:
            conditions.append("NO")
    conditions.append("YES")
    return conditions


print(equivalent_test(s, t))


def getidealNumbers(low: int, high: int):
    ideal_numbers = []
    for i in range(low, high+1):
        if i % 3 == 0 and i % 5 == 0:
            ideal_numbers.append(i)
    return len(ideal_numbers)


print(getidealNumbers(3, 80))

# low and high

# find number between divisible by 3 and 5

# return how many numbers there are

# 3^X 5^y
