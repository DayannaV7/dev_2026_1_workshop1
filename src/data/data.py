class Data:
    """
    Clase con operaciones sobre estructuras de datos: listas, matrices y estructuras
    clásicas como pilas y colas.
    """

    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos de una lista.

        ¿Cómo funciona?
          Recorremos la lista desde el ÚLTIMO elemento hasta el primero
          y vamos agregando cada uno a una nueva lista.

          Ejemplo con [1, 2, 3, 4, 5]:
            Recorremos índices: 4, 3, 2, 1, 0
            Tomamos: 5, 4, 3, 2, 1
            Resultado: [5, 4, 3, 2, 1]

        Ejemplos:
            invertir_lista([1, 2, 3, 4, 5]) → [5, 4, 3, 2, 1]
            invertir_lista([])              → []
            invertir_lista([42])            → [42]
            invertir_lista(["a","b","c"])   → ["c","b","a"]
        """
        resultado = []
        for i in range(len(lista) - 1, -1, -1):  # Desde el último al primero
            resultado.append(lista[i])
        return resultado

    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y retorna su POSICIÓN (índice).

        ¿Cómo funciona?
          Recorremos la lista uno por uno. En cuanto encontramos el elemento,
          retornamos su posición. Si llegamos al final sin encontrarlo, retornamos -1.
          (El -1 es la convención para indicar "no encontrado".)

        Ejemplos:
            buscar_elemento([10,20,30,40,50], 30) → 2   (posición 2)
            buscar_elemento([10,20,30,40,50], 60) → -1  (no está)
            buscar_elemento([10,20,30,20,50], 20) → 1   (primera ocurrencia)
            buscar_elemento([], 42)               → -1
        """
        for posicion, item in enumerate(lista):
            if item == elemento:
                return posicion
        return -1  # No se encontró

    def eliminar_duplicados(self, lista):
        """
        Elimina los elementos repetidos de una lista, conservando el ORDEN original.

        ¿Cómo funciona?
          Llevamos un registro de lo que ya vimos. Para cada elemento:
            - Si ya lo vimos → lo ignoramos
            - Si es nuevo → lo guardamos en el resultado y en el registro

          DETALLE IMPORTANTE: distingue entre 1 (entero) y True (booleano),
          aunque en Python 1 == True. Lo hacemos guardando también el tipo.

          Ejemplo con [1, "a", 1, "a", True]:
            1 (int) → nuevo → guardar
            "a"     → nuevo → guardar
            1 (int) → ya está → ignorar
            "a"     → ya está → ignorar
            True (bool) → aunque True==1, el TIPO es diferente → guardar
            Resultado: [1, "a", True]

        Ejemplos:
            eliminar_duplicados([1,2,2,3,4,4,5])   → [1,2,3,4,5]
            eliminar_duplicados([1,"a",1,"a",True]) → [1,"a",True]
            eliminar_duplicados([])                 → []
        """
        vistos = []     # Registro de (valor, tipo) para detectar duplicados
        resultado = []

        for elemento in lista:
            clave = (elemento, type(elemento))  # Combinamos valor y tipo
            if clave not in vistos:
                vistos.append(clave)
                resultado.append(elemento)

        return resultado

    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.

        ¿Cómo funciona? (Algoritmo de mezcla / merge)
          Tenemos dos "punteros" (i y j) que apuntan al inicio de cada lista.
          En cada paso, comparamos los dos elementos actuales y tomamos el menor.
          Cuando una lista se agota, añadimos el resto de la otra.

          Ejemplo con [1,3,5] y [2,4,6]:
            i=0,j=0: compara 1 vs 2 → toma 1 (de lista1), i=1
            i=1,j=0: compara 3 vs 2 → toma 2 (de lista2), j=1
            i=1,j=1: compara 3 vs 4 → toma 3, i=2
            i=2,j=1: compara 5 vs 4 → toma 4, j=2
            i=2,j=2: compara 5 vs 6 → toma 5, i=3
            lista1 agotada → añadir resto de lista2: [6]
            Resultado: [1,2,3,4,5,6]

        Ejemplos:
            merge_ordenado([1,3,5], [2,4,6])   → [1,2,3,4,5,6]
            merge_ordenado([], [1,2,3])         → [1,2,3]
            merge_ordenado([1,2,3], [1,3,5])   → [1,1,2,3,3,5]
        """
        resultado = []
        i, j = 0, 0

        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        # Añadir los elementos restantes (solo una de las dos tendrá)
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])

        return resultado

    def rotar_lista(self, lista, k):
        """
        Rota los elementos de la lista K posiciones hacia la derecha.

        ¿Qué significa rotar?
          Los últimos K elementos "se mueven" al inicio de la lista.

          Ejemplo con [1,2,3,4,5] rotando 2 posiciones:
            Los últimos 2 elementos son [4, 5]
            El resto es [1, 2, 3]
            Resultado: [4, 5, 1, 2, 3]

        ¿Qué pasa si k > longitud?
          Usamos k % longitud para evitar rotaciones redundantes.
          Rotar 5 posiciones una lista de 3 es igual a rotar 2 (5 % 3 = 2).

        Ejemplos:
            rotar_lista([1,2,3,4,5], 2) → [4,5,1,2,3]
            rotar_lista([1,2,3], 5)     → [2,3,1]   (5%3=2)
            rotar_lista([1,2,3], 0)     → [1,2,3]   (sin cambio)
            rotar_lista([], 3)          → []
        """
        if not lista:
            return []

        k = k % len(lista)  # Evitar rotaciones mayores que la longitud

        if k == 0:
            return lista[:]  # Copia sin cambios

        # Los últimos k elementos van primero, luego el resto
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número que FALTA en una secuencia del 1 al N.

        ¿Cómo funciona?
          Si tenemos los números del 1 al N sin duplicados y falta uno,
          podemos calcularlo con una fórmula matemática.

          La suma de 1+2+3+...+N = N×(N+1)/2  (fórmula de Gauss)

          Si sabemos la suma esperada y la suma real, la diferencia es el faltante.

          Ejemplo con [1, 2, 4, 5] (falta el 3, hay 4 elementos así que N=5):
            Suma esperada del 1 al 5: 5×6/2 = 15
            Suma real: 1+2+4+5 = 12
            Faltante: 15 - 12 = 3  ✓

        Ejemplos:
            encuentra_numero_faltante([1,2,4,5])        → 3
            encuentra_numero_faltante([2,3,4,5])        → 1
            encuentra_numero_faltante([1,2,3,4])        → 5
            encuentra_numero_faltante([1,2,3,4,5,6,8,9,10]) → 7
        """
        n = len(lista) + 1           # El total de números que debería haber
        suma_esperada = n * (n + 1) // 2
        suma_real = sum(lista)
        return suma_esperada - suma_real

    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si todos los elementos de conjunto1 están en conjunto2.

        ¿Qué es un subconjunto?
          A es subconjunto de B si TODOS los elementos de A están en B.
          El conjunto vacío es subconjunto de cualquier conjunto.

          Ejemplo: [1,2] es subconjunto de [1,2,3,4] porque 1 y 2 están en [1,2,3,4]
          Ejemplo: [1,5] NO es subconjunto de [1,2,3,4] porque 5 no está

        Ejemplos:
            es_subconjunto([1,2],   [1,2,3,4]) → True
            es_subconjunto([1,5],   [1,2,3,4]) → False
            es_subconjunto([1,2,3], [1,2,3])   → True   (un conjunto es subconjunto de sí mismo)
            es_subconjunto([],      [1,2,3])   → True   (el vacío siempre es subconjunto)
        """
        return all(elemento in conjunto2 for elemento in conjunto1)

    def implementar_pila(self):
        """
        Implementa una pila (Stack).

        ¿Qué es una pila?
          Es una estructura de datos LIFO: Last In, First Out.
          (Último en entrar, primero en salir)

          Piensa en una pila de platos: siempre sacas el de ARRIBA (el último que pusiste).

          Operaciones:
            push(x)  → agrega x encima de la pila
            pop()    → saca y retorna el elemento de arriba
            peek()   → mira el elemento de arriba SIN sacarlo
            is_empty() → True si la pila está vacía

          Ejemplo de uso:
            pila = implementar_pila()
            pila["push"](1)   → pila: [1]
            pila["push"](2)   → pila: [1, 2]
            pila["peek"]()    → 2  (mira sin sacar)
            pila["pop"]()     → 2  (saca), pila: [1]
            pila["pop"]()     → 1  (saca), pila: []
            pila["is_empty"]() → True

        Returns:
            dict: Diccionario con las funciones push, pop, peek e is_empty
        """
        datos = []  # Lista interna que guarda los elementos

        return {
            "push":     lambda x: datos.append(x),       # Agregar al final (arriba)
            "pop":      lambda: datos.pop(),              # Sacar del final (arriba)
            "peek":     lambda: datos[-1],                # Ver el último sin sacar
            "is_empty": lambda: len(datos) == 0,          # ¿Está vacía?
        }

    def implementar_cola(self):
        """
        Implementa una cola(Queue).

        ¿Qué es una cola?
          Es una estructura de datos FIFO: First In, First Out.
          (Primero en entrar, primero en salir)

          Como una fila de personas: el primero que llega es el primero en ser atendido.

          Operaciones:
            enqueue(x) → agrega x al FINAL de la cola
            dequeue()  → saca y retorna el elemento del INICIO
            peek()     → mira el elemento del inicio SIN sacarlo
            is_empty() → True si la cola está vacía

          Ejemplo de uso:
            cola = implementar_cola()
            cola["enqueue"](1)    → cola: [1]
            cola["enqueue"](2)    → cola: [1, 2]
            cola["peek"]()        → 1  (el primero)
            cola["dequeue"]()     → 1  (sale el primero), cola: [2]
            cola["dequeue"]()     → 2  (sale el siguiente), cola: []
            cola["is_empty"]()    → True

        Returns:
            dict: Diccionario con las funciones enqueue, dequeue, peek e is_empty
        """
        datos = []  # Lista interna que guarda los elementos

        return {
            "enqueue":  lambda x: datos.append(x),        # Agregar al final
            "dequeue":  lambda: datos.pop(0),             # Sacar del inicio (posición 0)
            "peek":     lambda: datos[0],                  # Ver el primero sin sacar
            "is_empty": lambda: len(datos) == 0,           # ¿Está vacía?
        }

    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz: intercambia filas por columnas.

        ¿Qué es la transpuesta?
          Si la matriz original tiene el elemento M[fila][columna],
          la transpuesta tiene ese elemento en T[columna][fila].
          En otras palabras, las filas se convierten en columnas y viceversa.

          Ejemplo con matriz 2×3:
            Original:     Transpuesta:
            1  2  3         1  4
            4  5  6    →    2  5
                            3  6
          (2 filas, 3 columnas) → (3 filas, 2 columnas)

        Casos especiales:
            matriz_transpuesta([]) → []
            matriz_transpuesta([[5]]) → [[5]]  (1×1 no cambia)
        """
        if not matriz:
            return []

        filas_original = len(matriz)
        columnas_original = len(matriz[0])

        # La transpuesta tiene las dimensiones invertidas
        transpuesta = [
            [matriz[fila][columna] for fila in range(filas_original)]
            for columna in range(columnas_original)
        ]

        return transpuesta