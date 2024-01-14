def removeDuplicates(nums):
    look_cur = 1
    edit_cur = 0 
    while look_cur < len(nums) - 1:
        if nums[look_cur] > nums[edit_cur]:
            print(nums)
            nums[edit_cur] = nums[look_cur]
            edit_cur += 1
            print(nums)
            print()
        look_cur += 1


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4] 
    removeDuplicates(nums)
    print(nums)