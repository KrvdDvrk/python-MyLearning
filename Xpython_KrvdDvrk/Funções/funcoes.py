"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2)
"""

# Solid - Single Responsibility

def f(x): # assinatura
    result = 5 * (x / 2)
    ...
    return result

def double(x):
    return x * 2

valor = double(f(10))

print(valor)
print(valor == 50)

###
# Procedimentos / Procedures

def print_in_upper(text):
    # "Procedure with no explicit return"
    print(text.upper())
    # implicit return None

print_in_upper("dvrk")

# Fórmula de Heron's

def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5 # marh.sqrt(area)

def heron2(params):
    return heron(*params)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37)
]

# 1º Do
"""for t in triangulos:
    # formanormal: area = heron(t[0], t[1], t[2])
    # formasimples:
    area = heron(*t)
    print(f"A area do triangulo é: {area}")
"""

# 2º Do
print(list(map(heron2, triangulos)))

for t in triangulos:
    area = heron2(t)
    print(f"A area do triangulo é: {area}")

### Anatomia da função

def nome_da_funcao():
    print("Hello funcao")
    return 1

result = nome_da_funcao()
print(result)

### Para vizualizar melhor sua função use:
# " https://pythontutor.com/visualize.html#mode=edit "
