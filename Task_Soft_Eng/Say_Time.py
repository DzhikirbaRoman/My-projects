from datetime import datetime

def time_now():
    my_time = datetime.now()
    print(my_time)

inp = input("Do you want to know time? If Yes - Write anything ; If Not - Press Enter \n")
if not inp:
    inp = input("You sure? If Yes - Write anything ; If Not - Press Enter \n")
if inp:
    time_now()