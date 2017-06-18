from concurrent.futures import ThreadPoolExecutor
import random

import time

def task(n):
    time.sleep(5)
    return (4)

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(task, 1)

print(future.result())

# ex = futures.ThreadPoolExecutor(max_workers=1)
# print('main: starting')
#
# wait_for = [
# ex.submit(task, i)
# for i in range(0,1)
# ]
#
# for f in futures.as_completed(wait_for):
# print('main: result: {}'.format(f.result()))
