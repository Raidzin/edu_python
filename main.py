import time
from random import randint

# t1 = time.time()
# time.sleep(4)
# t2 = time.time()

N = 2

# def decorator(func):
#     def wrapper():
#         return func()
#     return wrapper


# def time_of(a):
#     counter = 0
#     for _ in range(N):
#         time_1 = time.time()
#         a()
#         counter += time.time() - time_1
#     return counter / N

def time_of(func):
    def wrapper():
        summ = 0
        original = None
        for _ in range(N):
            time_1 = time.time()
            value = func()
            summ += time.time() - time_1
            if original is None:
                original = value
        print(summ / N)
        return original

    return wrapper


@time_of
def foo():
    r = randint(0, 5)
    time.sleep(r)
    return r

@time_of
def main():
    a = foo()
    print(a)


if __name__ == '__main__':
    main()
