def rotate(nums):
    new_nums = []
    for i in range(len(nums), 0, -1):
        new_nums.append(nums[i-1])
    return new_nums

def has23(nums):
    two = 0
    three = 0
    for value in nums:
        if value == 2:
            two += 1
        elif value == 3:
            three += 1
    return (two % 2 == 1 and three % 2 == 0)

def sum67(nums):
    sum = 0
    canCount = True
    for value in nums:
        if value == 6:
            canCount = False
        elif value == 7:
            canCount = True
        elif canCount:
            sum += value
        else:
            continue
    return (sum)

def love6(a,b):
    if (a == 6 or b == 6):
        return True
    elif a+b == 6:
        return True
    elif abs(a-b) == 6:
        return True
    else:
        return False

def make_chocolate(small, big, x):
    remain = x
    useSmall = 0
    for _ in range(big):
        remain -= 5
        if remain <= 0:
            return 0
    for _ in range(small):
        remain -= 1
        if remain < 0:
            return useSmall
        else:
            useSmall += 1
    return -1 if remain > 0 else useSmall   

print(rotate([11,23,55,18,29,77]))
print(has23([2,3,2,3,3,2,2,2,3,3,3]))
print(sum67([1,2,2,6,99,99,7]))
print(sum67([1,2,3]))
print(love6(1,6))
print(love6(6,9))
print(love6(1,5))
print(love6(1,7))
print(make_chocolate(4,1,9))
print(make_chocolate(4,1,10))
print(make_chocolate(4,1,7))
print(make_chocolate(4,2,9))
print(make_chocolate(4,2,11))