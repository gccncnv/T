def solve(string):
    res = ""
    for i in string:
        if i != " ":
            res += i
    return res.lower() == res[::-1].lower()


print(solve('abcba'))
print(solve('PYTHON'))
print(solve('ABA'))
print(solve("nurses run"))