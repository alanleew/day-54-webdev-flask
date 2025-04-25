import time
current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970

# Write your code below 👇

def speed_calc_decorator(input_func):
    def return_func():
        start_time = time.time()
        input_func()
        end_time = time.time()
        time_diff = end_time - start_time
        return time_diff
    return return_func


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

speed_calc_decorator(fast_function)