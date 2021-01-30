import time
try:
    print("Let's set a countdown! Integers only!")
    timer_count = int(input("Countdown (In seconds): "))
    while timer_count > 0:
        print(timer_count)
        timer_count -= 1
        time.sleep(1)
    print("0\nTime's Up!")
except ValueError:
    print("That's not an integer!")