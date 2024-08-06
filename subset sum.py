def subsetSum(n, W, weights):
    M = [[None] * (W + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][0] = []
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] > w:
                M[i][w] = M[i-1][w]
            else:
                if M[i-1][w] is not None:
                    M[i][w] = M[i-1][w]
                elif M[i-1][w - weights[i-1]] is not None:
                    M[i][w] = M[i-1][w - weights[i-1]] + [weights[i-1]]
                else:
                    M[i][w] = None
    return M[n][W]

n = int(input("Enter the number of elements: "))
weights = [int(input(f"Enter weight {i+1}: ")) for i in range(n)]
W = int(input("Enter the target sum: "))

subset = subsetSum(n, W, weights)
if subset is not None:
    print(f"A subset with sum {W} exists.")
    print("Weights contributing to the sum:", subset)
else:
    print(f"No subset with sum {W} exists.")
