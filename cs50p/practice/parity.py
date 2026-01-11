def main():
    x = int(input("enter x: "))
    
    if is_equal(x):
        print("Even")
    else:
        print("Odd")



def is_equal(n):
    return n % 2 == 0

main()

