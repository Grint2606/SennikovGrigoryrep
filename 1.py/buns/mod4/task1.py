def checkТumbers(nums):
    if all(x == nums[0] for x in nums):
        return "Все числа равны"
    elif len(set(nums)) == len(nums):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"
