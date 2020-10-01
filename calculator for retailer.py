if __name__ == '__main__':
    print("PRESS 's' to get the sum of all value entered.\n")
    sum = 0
    while True:
        num = input("\nEnter the price of item : ").capitalize()
        if num == "s":
            print(f"Total amount to be paid is {sum} \n\t Thankyou for shopping")
            break
        else:
             sum += int(num)
             print(f"The total of Order : {sum}")
