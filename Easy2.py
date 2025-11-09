def solve(string):
    s = 0
    for i in string:
        if i.lower() in 'aeiou':
            s+=1
    return s


print(solve('aeiou'))
print(solve('bcdfghjklmnpqrstvwxyz'))
print(solve("PYTHON"))