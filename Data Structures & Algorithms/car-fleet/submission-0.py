class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, speed in cars:
            time_taken = (target - pos) / speed

            if not stack or time_taken > stack[-1]:
                stack.append(time_taken)

        return len(stack)

        