from datetime import datetime

def logger(func):
    def wrapped_func(*args, **kwargs):
        if args[0] == 0:
            print("invalid number")
            return None
        print(args, kwargs)
        return func(*args, **kwargs)

    return wrapped_func

@logger
def pow2(num):      # wrapped : pow2
    return num ** 2

@logger
def is_even(num):   # wrapped : is_even
    return num % 2 == 0

#========================================
def log_time(func):

    def wrap_function(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60

        print(f"Elapse time {hours} : {minutes} : {seconds}")
        return result

    return wrap_function