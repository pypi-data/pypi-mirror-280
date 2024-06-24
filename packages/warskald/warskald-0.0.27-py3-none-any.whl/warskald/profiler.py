from time import time
from typing import Callable

def profile(funct: Callable, *args) -> None:
    start = time() * 1000
    funct(*args)
    end = time() * 1000
    total = round(end - start, 2)
    print(f'Execution time: {total}ms')