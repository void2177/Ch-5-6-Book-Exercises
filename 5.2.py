import time
now = time.time()

def dayssince():
    return int(now // 86400)

def time():
    subhour = now % 86400
    hours = int(subhour // 3600)
    minutes = int((subhour % 3600) // 60)
    seconds = int(subhour % 60)
    return hours, minutes, seconds
print(time())



