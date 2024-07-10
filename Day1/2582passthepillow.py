def PassThePillow(n, time):
    stand, flag = 1, 1
    while time:
        time -= 1
        if flag:
            stand += 1
            if stand == n:
                flag = not flag
        else:
            stand -= 1
            if stand == 1:
                flag = not flag
    return stand

n = 4
time = 5

output = PassThePillow(n, time)
print(output)