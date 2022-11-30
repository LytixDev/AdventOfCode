def most_common_bit_is_one(arr, i):
    #ones = "".join("1" if i == "1" else "" for i in arr[i])
    #return len(ones)
    ones = 0
    for byte in arr:
        if byte[i] == "1":
            ones += 1

    return ones >= len(arr) / 2


def find_rating(bytes, most_common=True):
    nums = bytes
    for i, bit in enumerate(bytes):
        tmp = []
        for a in nums:
            if most_common:
                if most_common_bit_is_one(nums, i):
                    if a[i] == "1":
                        tmp.append(a)
                else:
                    if a[i] == "0":
                        tmp.append(a)
            else:
                if not most_common_bit_is_one(nums, i):
                    if a[i] == "1":
                        tmp.append(a)
                else:
                    if a[i] == "0":
                        tmp.append(a)
        
        nums = tmp
        if len(nums) == 1:
            break

    return nums[0]


bytes = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        bytes.append(line[:-1])



oxygen_nums = int(find_rating(bytes), 2)
scrubber_nums = int(find_rating(bytes, most_common=False), 2)
print(oxygen_nums * scrubber_nums)
