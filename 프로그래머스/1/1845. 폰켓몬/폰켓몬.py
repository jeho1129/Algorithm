def solution(nums):
    answer = len(nums) // 2
    nums = set(nums)
    answer = min(len(nums), answer)
    return answer