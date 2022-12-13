from betterlib import threader
import random

def return_random():
    return random.randint(0, 100)

threads = threader.Threader(return_random, numThreads=10)

print("Threads are alive:", threads.isAlive())
print("Joining threads...")
print("Returned data:", threads.joinAndReturn())