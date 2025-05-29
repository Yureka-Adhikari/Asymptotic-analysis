def myfunction(n):
    for i in range(0,n+1):
        print("first loop")
    print("\nWith every 'n' the time taken and will be increased")
        
    j=1
    while j <= n+1:
        print("second loop")
        j = j*2
    print("\nWith every 'n' the time taken and will be increased but half of the first loop")
        
    for i in range(0,100):
        print("third loop")
    print("\nThis loop will always take 100 iterations regardless of 'n'")
        
myfunction(10)
myfunction(20)
