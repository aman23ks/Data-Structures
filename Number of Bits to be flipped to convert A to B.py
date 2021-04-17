class Solution:
    # Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self, a, b):
        # Your code here

        count = 0

        n = a ^ b

        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1  # Right Shift

        return count
