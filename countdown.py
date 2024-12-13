import time

my_time = int(input("Enter the Time⌛ in seconds:"))

for x in range (0, my_time):
    #for x in range (my_time,0,-1) to reverse pr use revresed keyword
    seconds= x % 60
    print(type(seconds))

    minutes = int(x / 60) % 60

    hours = int(x /24) %60

    print(f"{hours:02}:{minutes:02}: {seconds:02}")

time.sleep(1)
print("Time's UP!")