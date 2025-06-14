import time

wait_time = 1
max_attempt = 5
attempts = 0

while attempts < max_attempt:
    print("Number of attempt: ", (attempts+1), " - wait for ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1 