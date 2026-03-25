# #zadanie 1
# import random
# from operator import sub
#
# lista1 = list(range(1, 101))
# lista2 = [random.randint(1, 1000) for _ in range(100)]
# wynik = list(map(sub, lista2, lista1))
# print(wynik)
#
# #zadanie 2
# 
# import random
# import operator
# numbers = [random.randint(0, 10) for _ in range(10000)]
# less_than_3 = filter(lambda x: operator.lt(x, 3), numbers)
# even_and_less_than_3 = list(filter(lambda x: operator.eq(x % 2, 0), less_than_3))
#
# print(even_and_less_than_3)
#
# # zadanie 3
#
# from itertools import count
# numbers = []
#
# for n in count(start=100, step=5):
#     numbers.append(n)
#     if len(numbers) == 50:
#         break
#
# print(numbers)
#
# #zadanie 4
#
# from itertools import cycle
#
# def funcycle(n):
#     seq = "INFORMATYKA"
#     for ch, _ in zip(cycle(seq), range(n)):
#         print(ch)
#
# #zadanie 5
#
# from itertools import product
#
# A = [1, 2, 3]
# B = ['a', 'b', 'c']
# C = [True, False]
#
# cartesian_3d = list(product(A, B, C))
# print(cartesian_3d)
# #zadanie 6
# from itertools import combinations
# def podziel_grupe(studenci, n):
#     """
#     Funkcja dzieli grupę studentów na n-osobowe podgrupy
#     z wykorzystaniem iteratora kombinatorycznego.
#     """
#     return list(combinations(studenci, n))
# studenci = list(range(1, 11))
# podgrupy = podziel_grupe(studenci, 3)
#
# for g in podgrupy:
#     print(g)
#
# #zadanie 7
#
# from itertools import repeat
# def lokata(k, oprocentowanie, t):
#     mnoznik = 1 + oprocentowanie
#     kwota = k
#     for _ in repeat(None, t):   # iterator skończony — wykonuje się t razy
#         kwota *= mnoznik
#     return kwota
# k = 10000
# oprocentowanie = 0.0001
# t = 9
#
# wynik = lokata(k, oprocentowanie, t)
# print(f"Kwota po {t} miesiącach: {wynik:.2f} zł")
#
# #zadanie 8
#
# def gen_four(n):
#     value = 4
#     for _ in range(n):
#         yield value
#         value *= 2
#
# #zadanie 9
#
# import random
#
# def even_random_generator(n):
#     for _ in range(n):
#         yield random.randint(0, 50_000_000) * 2
# gen = even_random_generator(1000)
#
# for _ in range(5):
#     print(next(gen))
#
# #zadanie 10
#
# from itertools import accumulate, repeat
# def fib_generator(n):
#     start = (0, 1)
#     fib_pairs = accumulate(
#         repeat(None, n),
#         lambda acc, _: (acc[1], acc[0] + acc[1]),
#         initial=start
#     )
#
#     for a, _ in fib_pairs:
#         yield a
#
# n = 10
# gen = fib_generator(n)
# fib_n = None
# for _ in range(n):
#     fib_n = next(gen)
#
# print(f"{n}-ty element ciągu Fibonacciego to: {fib_n}")
#
# #zadanie 11
# import random
# import time
# import tracemalloc
# from multiprocessing import Pool
#
#
# N = 1_000_000
# L1 = [random.randint(0, 1000000) for _ in range(N)]
# L2 = [random.randint(0, 1000000) for _ in range(N)]
# L3 = [random.randint(0, 1000000) for _ in range(N)]
# DATA = L1 + L2 + L3
#
# def measure(func):
#     tracemalloc.start()
#     t0 = time.perf_counter()
#     result = func()
#     t1 = time.perf_counter()
#     mem = tracemalloc.get_traced_memory()[1]
#     tracemalloc.stop()
#     return t1 - t0, mem, result
#
# #a
# def imperative():
#     even = []
#     odd = []
#     for x in DATA:
#         if x % 2 == 0:
#             even.append(x)
#         else:
#             odd.append(x)
#     return even, odd
#
# #b
# def functional_simple():
#     def is_even(x): return x % 2 == 0
#     def is_odd(x): return x % 2 != 0
#     even = [x for x in DATA if is_even(x)]
#     odd = [x for x in DATA if is_odd(x)]
#     return even, odd
#
# #c
# def split_chunk(chunk):
#     return [x for x in chunk if x % 2 == 0], [x for x in chunk if x % 2 != 0]
#
# def functional_parallel():
#     chunks = [DATA[i:i+500000] for i in range(0, len(DATA), 500000)]
#     with Pool() as p:
#         results = p.map(split_chunk, chunks)
#     even = [x for ev, _ in results for x in ev]
#     odd = [x for _, od in results for x in od]
#     return even, odd
#
#
# #d
# def generator_based():
#     evens = (x for x in DATA if x % 2 == 0)
#     odds = (x for x in DATA if x % 2 != 0)
#     return list(evens), list(odds)
#
#
# #testy
# tests = {
#     "Imperatywny": imperative,
#     "Funkcyjny prosty": functional_simple,
#     "Funkcyjny równoległy": functional_parallel,
#     "Generatorowy": generator_based
# }
#
# for name, fn in tests.items():
#     t, mem, _ = measure(fn)
#     print(f"{name:25s}  czas: {t:.4f}s   pamięć: {mem/1024/1024:.2f} MB")
#

