'''
Las tuplas son Inmutables
'''

tupla=("uno", "dos", "tres")
print(tupla)

tuplasVariosDatos = (12, True, 23.5, "El gato", 12+2j)
print(tuplasVariosDatos)

tuplasConTuplas = (1, 2, 3, 4, (1, 2, 3))
print(tuplasConTuplas)
print(tuplasVariosDatos[3])
print(tuplasVariosDatos[-2])
print(tuplasVariosDatos[0:2])

a, b, c = tupla
print(a)
print(b)
print(c)

tuplasNueva = tupla+tuplasVariosDatos
print(tuplasNueva)

