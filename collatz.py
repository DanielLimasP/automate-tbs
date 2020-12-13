# Collat'z sequence: Automate the boring stuff
def collatz_sequence(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            print(n//2)
            return collatz_sequence(n//2)
        else:
            print(3 * n + 1)
            return collatz_sequence(3 * n + 1)

if __name__ == "__main__":
    loop_control = True

    while loop_control:
        user_input = input("Please enter a number: ")
        collatz_sequence(int(user_input))