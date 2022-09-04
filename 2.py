# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

X = input("Введите X: ")
Y = input("Введите Y: ")
z = input("Введите Z: ")
print(not (X or Y or Z) == (not X and not Y and not Z))