def generate_permutation(N):
    # The simplest permutation which satisfies the condition is the natural order
    return list(range(1, N + 1))

def main():
    data = input().split()
    
    T = int(data[0])
    test_cases = [int(data[i]) for i in range(1, T + 1)]
    
    results = []
    for N in test_cases:
        permutation = generate_permutation(N)
        results.append(" ".join(map(str, permutation)))
    
    # Print all results
    print("\n".join(results))

if __name__ == "__main__":
    main()
