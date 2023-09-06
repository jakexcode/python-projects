def kangaroo(x1, v1, x2, v2):
    x1, v1, x2, v2 = 0, 3, 4, 2,
    # Write your code here
    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        if v2-v1 == 0:
            return 'NO'
        else:
            result = (x1-x2) % (v2-v1)
            if result == 0:
                return 'YES'
            else:
                return 'NO'
