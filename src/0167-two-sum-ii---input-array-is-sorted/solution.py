class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer, first, last = float("-inf"), 0, len(numbers) - 1
        while answer != target:
            answer = numbers[first] + numbers[last]
            if answer == target:
                return [first + 1, last + 1]
            elif answer > target:
                last -= 1
            else:
                first += 1
