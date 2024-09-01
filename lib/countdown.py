# your code goes here!
def countdown(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        number -= 1
    print("HAPPY NEW YEAR!")


import time

def countdown_with_sleep(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        time.sleep(1)  # Pauses for 1 second
        number -= 1
    print("HAPPY NEW YEAR!")
