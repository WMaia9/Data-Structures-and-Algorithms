import random
import sys
import os

# aceita o número de testes como um comando de parametro linha
tests = int(sys.argv[1])
# aceita os parametros para os teste como um parametro de comando linha
n = int(sys.argv[2])

for i in range(tests):
    print('Test #' + str(i))
    # executa o gerador gen.py com um parametro n e seed i
    os.system('PY Stress2.py ' + str(n) + ' ' + str(i) + ' > input.txt')
    # executa a solução modelo model.py
    os.system('PY max_pairwise_product.py <input.txt >model.txt')
    # executa a solução principal
    os.system('PY max_pairwise_product_fast.py <input.txt >main.txt')

    # lê a saida da solução modelo:
    with open('model.txt') as f:
        model = f.read()
    print('Model: ', model)
    # leia a saida da solução principal:
    with open('main.txt') as f:
        main = f.read()
    print('Main: ', main)
    if model != main:
        break
