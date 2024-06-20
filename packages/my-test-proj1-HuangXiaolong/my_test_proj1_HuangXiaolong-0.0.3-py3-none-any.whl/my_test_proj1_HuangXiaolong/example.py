import time
from tqdm import tqdm

def plus(a, b):
    return a + b

def progress():
    for i in tqdm(range(1000)):
        time.sleep(.001)