for contador in range(1,11):
    #1. contador=1 1 % 2 == 0 --->si lo imprime
    #2. contador=2 1 % 2 == 0 --->no lo imprime
    #3. contador=3 1 % 3 == 0 --->si lo imprime
    #4. contador=4 1 % 4 == 0 --->no lo imprime
    if contador % 2 != 0:
        continue
    print(contador)