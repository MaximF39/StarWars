test1, res1 = [(1, 5)], 4
test2, res2 = [(1, 5), (6, 10)],  8
test3, res3 = [(1, 5), (1, 5)],  4
test4, res4 = [(1, 4), (7, 10), (3, 5)],  7

def f(test):
    return len({i for interval in test for i in range(*interval)})

# all_num = set()
# for tupl in test:
#     for i2 in range(*tupl):
#         all_num.add(i2)
# return len(all_num)


print(f(test1))
print(f(test2))
print(f(test3))
print(f(test4))
