# Take an integer input from the user
n = int(input("Enter any number: "))

# Set a flag to keep checking for the previous prime number
previous = True

# Run the loop until the previous prime number is found
while previous:
    # Decrement the number by 1 to check the previous number
    n = n - 1

    # Initialize a variable to count if the number is not prime
    fact = 0

    # Loop from 2 to n-1 to check for any divisors of n
    for i in range(2, n):
        # If n is divisible by i, it is not a prime number
        if n % i == 0:
            fact += 1  # Increase fact to indicate it's not prime
            break       # No need to check further, break out of the loop

    # If fact is still 0, it means the number is prime
    if fact == 0:
        print(f"Previous prime is {n}")
        previous = False  # Exit the while loop
