def steps_to_one(n):
    steps = 0

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        steps += 1

    return steps


print(steps_to_one(14))
