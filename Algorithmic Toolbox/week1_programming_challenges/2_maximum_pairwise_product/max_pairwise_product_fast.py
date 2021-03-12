
def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = 0
    for i in range(n):
        if numbers[i] > numbers[index1]:
            index1 = i

    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for i in range(1, n):
        if i != index1 and numbers[i] > numbers[index2]:
            index2 = i

    return numbers[index1] * numbers[index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
