import random

if __name__ == '__main__':
    tamano_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? ')) # O(1)

    lista = [random.randint(0, 100) for i in range(tamano_lista)] 

    encontrado = False
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')