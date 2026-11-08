class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), reverse = True)

        stack = []

        for pos, speed in pos_speed:
            time_taken = (target - pos) / speed

            if stack and time_taken <= stack[-1]:
                continue
            
            stack.append(time_taken)
        
        return len(stack)