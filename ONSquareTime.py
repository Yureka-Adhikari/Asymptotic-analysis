def ONSquareTime(n):
    iteration = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end=" ")
            iteration += 1
        print(" ")
    print(f"\nWhen n is {n}, Iterations = {iteration}")
    
ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)

print("\nWith every 'n' the time will be n^2")
print("O(n^2)")