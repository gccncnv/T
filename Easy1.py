def solve(arr):
    s = 0
    for i in arr:
        if i%2 == 0:
            s += i
    return s

print(solve([1,2,3,4,5,6]))