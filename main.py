import random


def main():
    print("Welcome to the Coin Flip Simulator! This program is designed to help you determine the number of coin flips required to achieve a specific number of consecutive heads or tails. Whether you're curious about probability or just want to satisfy your curiosity, this simulator will provide you with the answer you seek. Get ready to explore the fascinating world of coin flips and uncover the mystery behind consecutive outcomes. Let's dive in and discover how many flips it takes to reach your desired sequence!\n")
    userinput = (input("What is the desired consecutive integer that your desire (has to be less than 25): "))
    while (secondary_check(userinput)):
        userinput = input("That is an invalid number. Please enter an integer: ")
    print("\n")
    compute(userinput)


def primary_check(user_input):
    if user_input.isdigit():
        return True
    return False

def secondary_check(user_input):
    if primary_check(user_input):
        integer_input = int(user_input)
        if integer_input <= 25:
            return False
    return True

def compute(user_input):
    int_user_input=int(user_input)
    max_head = 0
    max_tail = 0
    total_toss = 0
    head = 0
    tail = 0

    while not(max_head == int_user_input or max_tail== int_user_input):
        total_toss = total_toss + 1
        random_number = random.choice([1, 2])
        print(random_number, end="")
        if random_number == 1:
            head += 1
            if head > max_head:
                max_head = head
            tail = 0
        elif random_number == 2:
            if tail > max_tail:
                max_tail = tail
            head = 0

    print("\n")
    if max_head == int_user_input:
        print(f'After {total_toss} there was {user_input} consecutive heads')
    else:
        print(f'After {total_toss} there was {user_input} consecutive tails')


if __name__ == '__main__':
    main()


