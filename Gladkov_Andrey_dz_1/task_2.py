# 2 задание
def sum_list_1(dataset: list) -> int:
    sum_1 = 0
    for num in dataset:
        sum = 0
        num_saved = num
        while (num != 0):
            sum = sum + num % 10
            num = num // 10
        if sum % 7 == 0:
            sum_1 = sum_1 + num_saved

    return sum_1


def sum_list_2(dataset: list) -> int:
    for i in range(len(dataset)):
        dataset[1] += 17
    return sum_list_1(dataset)




my_list = list(range(1, 1001, 2))
for i in range(len(my_list)):
    my_list[1] = my_list[1] ** 3

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
