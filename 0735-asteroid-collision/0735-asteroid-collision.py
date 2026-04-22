class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for a in asteroids:
            alive = True

            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                alive = False
                break

            if alive:
                stack.append(a)

        return stack