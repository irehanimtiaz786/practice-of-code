while True:
    print("\n1. Display numbers from 1 to N")
    print("2. Display even numbers between 1 and N")
    print("3. Display multiplication table of a number")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == '1':
        n = int(input("Enter the value of N: "))
        for i in range(1, n + 1):
            print(i, end=" ")
        print()
        
    elif choice == '2':
        n = int(input("Enter the value of N: "))
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()
        
    elif choice == '3':
        num = int(input("Enter the number for the multiplication table: "))
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)
            
    elif choice == '4':
        break
        
    else:
        print("Invalid choice!")