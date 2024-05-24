import random

def merge_sort(lista):
    if len(lista) > 1:
        #print('Esto es len(lista)', len(lista))
        medio = len(lista) // 2
        #print('Este es el medio', medio)
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print('izquierda', izquierda, '*' * 5, 'derecha', derecha)

        # Llamada recursiva en cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:   
                lista[k] = derecha[j]
                j += 1
            k += 1 

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierda {izquierda}, derecha {derecha}')
        print('Como va la lista ', lista)
        print('----' * 20)

    return lista
                    
if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)] 
    print(lista)
    print('-' * 20)

    lista_ordenada = merge_sort(lista)
    print('Lista ordenada', lista_ordenada)