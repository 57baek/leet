# %%

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for ast in asteroids:

            while stack and stack[-1] > 0 and ast < 0:

                if abs(ast) > stack[-1]:
                    stack.pop()

                elif abs(ast) == stack[-1]:
                    stack.pop()
                    break

                else:
                    break

            else:
                stack.append(ast)

        return stack


# %%
asteroids = [-5, -2, 2, 5]
sol = Solution()
print(sol.asteroidCollision(asteroids))


# %%


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # Initialize an empty stack to keep track of surviving asteroids
        stack = []

        # Loop through each asteroid in the input list
        for asteroid in asteroids:

            # While there are asteroids in the stack, and the current asteroid is moving left (< 0),
            # and the last asteroid in the stack is moving right (> 0), a collision may happen
            # When a negative asteroid (moving left) encounters positive asteroids (moving right), the while loop will continue processing collisions until stopped
            while stack and asteroid < 0 and stack[-1] > 0:

                # If the current asteroid is larger (in absolute value) than the last one in the stack,
                # the last asteroid in the stack is destroyed, so pop it
                # this process will continue until below break is activated
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()

                # If both asteroids are of equal size, both are destroyed, so pop the stack,
                # and stop further processing of the current asteroid
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    break  # Exit the while loop, as the current asteroid no longer exists

                # If the last asteroid in the stack is larger, the current asteroid is destroyed,
                # so break out of the while loop without appending the current asteroid
                else:
                    break

            # If no collision happens or the current asteroid survives, add it to the stack
            # [-2,2] then nothing will happen
            else:
                stack.append(asteroid)

        # After processing all asteroids, return the stack containing the surviving asteroids
        return stack
