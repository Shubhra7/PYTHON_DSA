# 10
# 7
# Sample Output 1:
# 55
# 13


def matrix_multiply(A, B):
    """Multiplies two 2x2 matrices A and B."""
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def matrix_power(matrix, n):
    """Computes matrix^n using binary exponentiation."""
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = matrix

    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        n //= 2

    return result

def nth_fibonacci(n):
    """Returns the n-th Fibonacci number."""
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Transformation matrix for Fibonacci
    transformation_matrix = [[1, 1], [1, 0]]

    # Calculate transformation_matrix^(n-1)
    result_matrix = matrix_power(transformation_matrix, n - 1)

    # The top left cell of the result matrix is F(n)
    return result_matrix[0][0]

# Example usage:
# n = 10  # 55 # Change this value to compute different Fibonacci numbers
n = 7 # 13 # Change this value to compute different Fibonacci numbers
print(f"The {n}-th Fibonacci number is: {nth_fibonacci(n)}")  
