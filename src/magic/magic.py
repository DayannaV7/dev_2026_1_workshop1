class Magic:
    """
    Clase con algoritmos matemáticos mágicos, secuencias especiales,
    números con propiedades únicas y operaciones numéricas clásicas.
    """

    def fibonacci(self, n):
        """
        Calcula el N-ésimo número de la secuencia fibonacci.

        ¿Qué es Fibonacci?
          Es una secuencia donde cada número es la suma de los dos anteriores:
          0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

          fibonacci(0) = 0
          fibonacci(1) = 1
          fibonacci(2) = 1  (0+1)
          fibonacci(3) = 2  (1+1)
          fibonacci(4) = 3  (1+2)
          fibonacci(10) = 55

        ¿Cómo funciona el algoritmo?
          Usamos dos variables 'a' y 'b' que van avanzando:
            Inicio: a=0, b=1
            Paso 1: a=1, b=1  (a toma el valor de b, b es a+b anterior)
            Paso 2: a=1, b=2
            Paso 3: a=2, b=3
            ...y así n veces. Al final, 'b' es el resultado.

        Casos especiales:
            fibonacci(-1) → None  (no existe posición negativa)
        """
        if n < 0:
            return None
        if n == 0:
            return 0

        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b  # Avanzar: a toma b, b toma a+b (simultáneo)
        return b

    def secuencia_fibonacci(self, n):
        """
        Genera los primeros N números de la secuencia de Fibonacci como lista.

        Ejemplo con n=5:
          [0, 1, 1, 2, 3]

        Casos especiales:
            secuencia_fibonacci(0) → []
            secuencia_fibonacci(1) → [0]
            secuencia_fibonacci(2) → [0, 1]
        """
        if n == 0:
            return []

        secuencia = [0]   # Siempre empieza con 0
        a, b = 0, 1

        for _ in range(n - 1):
            a, b = b, a + b
            secuencia.append(a)

        return secuencia

    def es_primo(self, n):
        """
        Verifica si un número es primo.

        ¿Qué es un número primo?
          Un número primo es aquel que solo puede dividirse exactamente
          entre 1 y entre sí mismo.

          Ejemplos primos: 2, 3, 5, 7, 11, 13, 17, 19, 23...
          No primos: 4 (÷2), 6 (÷2,3), 9 (÷3), 15 (÷3,5)...

        ¿Cómo funciona el algoritmo?
          Solo necesitamos probar divisores hasta la raíz cuadrada del número.
          ¿Por qué? Porque si un número tiene un divisor mayor que su raíz cuadrada,
          también tiene uno menor. Así ahorramos muchas comprobaciones.

          Ejemplo con 17:
            √17 ≈ 4.1 → probamos 2, 3, 4
            17 ÷ 2 = 8.5  (no divide exacto)
            17 ÷ 3 = 5.67 (no divide exacto)
            17 ÷ 4 = 4.25 (no divide exacto)
            Ninguno divide → 17 es primo

          Ejemplo con 15:
            √15 ≈ 3.9 → probamos 2, 3
            15 ÷ 3 = 5 exacto → 15 no es primo

        Casos especiales:
            es_primo(1)  → False  (el 1 no se considera primo por definición)
            es_primo(-5) → False  (negativos no son primos)
        """
        if n < 2:
            return False

        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                return False  # Encontramos un divisor → no es primo

        return True  # Ningún divisor encontrado → es primo

    def generar_primos(self, n):
        """
        Genera una lista de todos los números primos desde 2 hasta N (inclusive).

        Simplemente usamos es_primo() para verificar cada número en el rango.

        Ejemplos:
            generar_primos(10) → [2, 3, 5, 7]
            generar_primos(20) → [2, 3, 5, 7, 11, 13, 17, 19]
            generar_primos(1)  → []  (no hay primos menores o iguales a 1)
        """
        return [numero for numero in range(2, n + 1) if self.es_primo(numero)]

    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto.

        ¿Qué es un número perfecto?
          Un número es perfecto si la suma de todos sus divisores propios
          (todos excepto él mismo) es igual al número.

          Ejemplo con 6:
            Divisores propios de 6: 1, 2, 3
            Suma: 1 + 2 + 3 = 6  ← ¡igual al número! → es perfecto

          Ejemplo con 28:
            Divisores propios de 28: 1, 2, 4, 7, 14
            Suma: 1+2+4+7+14 = 28 → es perfecto

          Ejemplo con 10:
            Divisores propios de 10: 1, 2, 5
            Suma: 1+2+5 = 8 ≠ 10 → no es perfecto

        Casos especiales:
            es_numero_perfecto(0) → False
            es_numero_perfecto(1) → False
        """
        if n < 2:
            return False

        # Encontrar todos los divisores propios (excluyendo el número mismo)
        divisores = [i for i in range(1, n) if n % i == 0]
        return sum(divisores) == n

    def triangulo_pascal(self, filas):
        """
        Genera el triángulo de pascal con el número de filas indicado.

        ¿Qué es el triángulo de Pascal?
          Es un triángulo de números donde:
            - Los bordes siempre son 1
            - Cada número interior es la SUMA de los dos números de encima

          Ejemplo con 5 filas:
                  [1]
                [1, 1]
              [1, 2, 1]
            [1, 3, 3, 1]
          [1, 4, 6, 4, 1]

        ¿Cómo funciona?
          Para construir cada fila:
            1. Empieza y termina con 1
            2. Cada elemento interno [j] = fila_anterior[j-1] + fila_anterior[j]

        Curiosidades:
          - Cada fila son los coeficientes binomiales
          - La suma de cada fila es una potencia de 2: 1, 2, 4, 8, 16...
        """
        triangulo = []

        for i in range(filas):
            fila = [1] * (i + 1)  # Empezar con todos unos

            # Calcular los elementos internos (índices 1 hasta i-1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]

            triangulo.append(fila)

        return triangulo

    def factorial(self, n):
        """
        Calcula el FACTORIAL de un número (escrito como n!).

        ¿Qué es el factorial?
          Es la multiplicación de todos los enteros positivos desde 1 hasta n.

          5! = 5 × 4 × 3 × 2 × 1 = 120
          3! = 3 × 2 × 1 = 6
          0! = 1  (por definición matemática)
          1! = 1

        ¿Para qué se usa?
          Combinatoria (cuántas formas hay de ordenar elementos),
          probabilidad, series matemáticas, etc.

        Casos especiales:
            factorial(-1) → None  (no existe factorial de negativos)
        """
        if n < 0:
            return None

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i  # resultado = resultado × i

        return resultado

    def mcd(self, a, b):
        """
        Calcula el Máximo Común Divisor (MCD) usando el algoritmo de Euclides.

        ¿Qué es el MCD?
          El número más grande que divide exactamente a ambos números.

          mcd(48, 18) = 6  porque 6 es el mayor que divide a 48 y a 18

        ¿Cómo funciona el algoritmo de Euclides?
          Se basa en este principio: mcd(a, b) = mcd(b, a % b)
          Y se repite hasta que b sea 0. Entonces a es el MCD.

          Ejemplo con mcd(48, 18):
            48, 18 → 18, 48%18=12
            18, 12 → 12, 18%12=6
            12,  6 → 6,  12%6=0
            b=0 → el MCD es 6

        Casos especiales:
            mcd(0, 5) → 5  (el MCD de 0 y cualquier número es ese número)
        """
        while b != 0:
            a, b = b, a % b  # a toma el valor de b, b toma el resto de a÷b
        return a

    def mcm(self, a, b):
        """
        Calcula el Mínimo Común Múltiplo (MCM).

        ¿Qué es el MCM?
          El número más pequeño que es divisible exactamente por ambos números.

          mcm(4, 6) = 12  porque 12 es el menor que divide a 4 y a 6

        ¿Cómo funciona?
          Usando la relación: MCM(a, b) = |a × b| / MCD(a, b)

          Ejemplo con mcm(4, 6):
            MCD(4, 6) = 2
            MCM = (4 × 6) / 2 = 24 / 2 = 12

        Casos especiales:
            mcm(5, 0) → 0  (el MCM con 0 es 0 por convención)
        """
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.

        ¿Cómo funciona?
          Convertimos el número a string para poder recorrer cada dígito,
          luego convertimos cada dígito de vuelta a entero y los sumamos.

          Ejemplo con 123:
            "123" → '1', '2', '3' → 1, 2, 3 → 1+2+3 = 6

        Ejemplos:
            suma_digitos(123)  → 6
            suma_digitos(9999) → 36
            suma_digitos(0)    → 0
            suma_digitos(7)    → 7
        """
        return sum(int(digito) for digito in str(abs(n)))

    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de armstorng (también llamado número narcisista).

        ¿Qué es un número de Armstrong?
          Un número es de Armstrong si la suma de cada uno de sus dígitos
          elevado a la potencia del total de dígitos es igual al número mismo.

          Ejemplo con 153 (3 dígitos):
            1³ + 5³ + 3³ = 1 + 125 + 27 = 153  ✓ → Es Armstrong

          Ejemplo con 370 (3 dígitos):
            3³ + 7³ + 0³ = 27 + 343 + 0 = 370  ✓ → Es Armstrong

          Ejemplo con 123 (3 dígitos):
            1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123  → No es Armstrong

        Ejemplos:
            es_numero_armstrong(153) → True
            es_numero_armstrong(370) → True
            es_numero_armstrong(371) → True
            es_numero_armstrong(123) → False
        """
        digitos = str(n)
        cantidad_digitos = len(digitos)
        suma = sum(int(d) ** cantidad_digitos for d in digitos)
        return suma == n

    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico.

        ¿Qué es un cuadrado mágico?
          Una cuadrícula de números donde la suma de cada fila, cada columna
          y las dos diagonales da el mismo resultado (llamado "suma mágica").

          Ejemplo de cuadrado mágico 3×3 (suma mágica = 15):
            2  7  6
            9  5  1
            4  3  8
            Filas:      2+7+6=15, 9+5+1=15, 4+3+8=15  ✓
            Columnas:   2+9+4=15, 7+5+3=15, 6+1+8=15  ✓
            Diagonal ↘: 2+5+8=15  ✓
            Diagonal ↗: 6+5+4=15  ✓

        ¿Cómo funciona?
          1. Calculamos la suma mágica (usamos la primera fila como referencia)
          2. Verificamos que todas las filas sumen lo mismo
          3. Verificamos que todas las columnas sumen lo mismo
          4. Verificamos las dos diagonales

        Casos especiales:
            es_cuadrado_magico([[5]]) → True  (1×1 siempre es mágico)
        """
        n = len(matriz)
        if n == 0:
            return False

        suma_magica = sum(matriz[0])  # Referencia: suma de la primera fila

        # Verificar todas las filas
        for fila in matriz:
            if sum(fila) != suma_magica:
                return False

        # Verificar todas las columnas
        for j in range(n):
            suma_columna = sum(matriz[i][j] for i in range(n))
            if suma_columna != suma_magica:
                return False

        # Verificar diagonal principal (↘): posiciones (0,0), (1,1), (2,2)...
        if sum(matriz[i][i] for i in range(n)) != suma_magica:
            return False

        # Verificar diagonal secundaria (↗): posiciones (0,n-1), (1,n-2)...
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_magica:
            return False

        return True