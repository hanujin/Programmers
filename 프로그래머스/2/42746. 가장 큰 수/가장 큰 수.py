def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=lambda x: x*3, reverse=True)
        
    return ''.join(nums) if nums[0]!= "0" else "0"