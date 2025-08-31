from functools import reduce

cadena = "Hola Mundo 123!@#"

funciones = [
    lambda x: x.isalpha(),
    lambda x: x.isdigit(),
    lambda x: x != " " and not x.isalpha() and not x.isdigit(),
]

totales = []
for f in funciones:
    totales.append(reduce(lambda x, y: x + y, map(f, cadena)))

print(totales)




totales = [
    reduce(lambda x, y: x + y, map(lambda x: x.isalpha(), cadena)),
    reduce(lambda x, y: x + y, map(lambda x: x.isdigit(), cadena)),
    reduce(
        lambda x, y: x + y,
        map(lambda x: not x.isalpha() and not x.isdigit(), cadena),
    ),
]


# print(reduce(lambda x, y: str(x) + str(y), map(lambda x: x + 10, range(5))))


print(totales)
