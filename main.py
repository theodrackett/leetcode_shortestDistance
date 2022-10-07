salary = [4000, 3000, 1000, 2000]


def average(salary):
    """
    :type low: int
    :type high: int
    :rtype: int
    """
    salary.sort()
    total = 0
    ctr = 0
    for item in range(1, len(salary)-1):
        total += salary[item]
        ctr += 1
        print(salary[item])

    avg = total / ctr
    print(avg)

def find_next(n):

    next_num = 0
    while n > 0:
        n, last_digit = divmod(n, 10)
        next_num += last_digit ** 2

    return next_num

def is_happy(n):
    happy_set = set()

    next_num = find_next(n)
    happy_set.add(next_num)
    looped = False

    while True:
        next_num = find_next(next_num)
        if next_num in happy_set:
            looped = True
            break
        if next_num == 1:
            return next_num
        happy_set.add(next_num)
    if looped:
        return 0

n = 9999
print(is_happy(n))
