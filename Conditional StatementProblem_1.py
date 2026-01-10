'''Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number). Note: Return "Even" if the number is even; otherwise, return "Odd".
Examples
Input: x = 4 Output: Even'''
def check_even_odd(x: int) -> str:
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
print(check_even_odd(4))  # Output: Even
print(check_even_odd(7))  # Output: Odd
