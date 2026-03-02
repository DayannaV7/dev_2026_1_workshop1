import math
from collections import Counter

class Stats:
    """
    Clase con las operaciones estadísticas básicas.

    La estadística nos ayuda a resumir y entender conjuntos de datos numéricos.
    Ejemplo: saber si los estudiantes aprobaron en promedio, qué nota fue
    la más común, o qué tan dispersas están las calificaciones.
    """

    def promedio(self, numeros):
        """
        Calcula el promedio (media aritmética) de una lista de números.

        ¿Qué es el promedio?
          Es el valor "central" que representa a todo el grupo.
          Se calcula sumando todos los valores y dividiendo entre la cantidad.

          Ejemplo con [1, 2, 3, 4, 5]:
            Suma = 1+2+3+4+5 = 15
            Cantidad = 5
            Promedio = 15 / 5 = 3.0

        Casos especiales:
            promedio([]) → 0  (lista vacía, no hay nada que promediar)
            promedio([42]) → 42.0  (un solo elemento, él mismo es el promedio)
        """
        if not numeros:
            return 0

        suma = sum(numeros)
        cantidad = len(numeros)
        return suma / cantidad

    def mediana(self, numeros):
        """
        Calcula la mediana: el valor que está justo en el centro de la lista ordenada.

        ¿Para qué sirve?
          A diferencia del promedio, la mediana no se ve afectada por valores
          extremos. Por ejemplo, si 4 personas ganan $1000 y 1 gana $1.000.000,
          el promedio sería muy alto, pero la mediana mostraría $1000.

        ¿Cómo se calcula?
          1. Ordenar la lista de menor a mayor
          2. Si la cantidad es impar → tomar el elemento del medio
          3. Si la cantidad es par  → promediar los dos elementos del medio

          Ejemplo impar [1, 3, 5, 7, 9] (5 elementos):
            Ordenada: [1, 3, 5, 7, 9]
            Posición central: índice 2 → valor 5
            Mediana = 5.0

          Ejemplo par [1, 2, 3, 4] (4 elementos):
            Ordenada: [1, 2, 3, 4]
            Dos centrales: índices 1 y 2 → valores 2 y 3
            Mediana = (2+3)/2 = 2.5

        Casos especiales:
            mediana([]) → 0
        """
        if not numeros:
            return 0

        ordenada = sorted(numeros)   # Ordenar de menor a mayor
        n = len(ordenada)
        mitad = n // 2              # División entera: posición central

        if n % 2 == 0:
            # Cantidad par: promediar los dos del centro
            return (ordenada[mitad - 1] + ordenada[mitad]) / 2
        else:
            # Cantidad impar: tomar el elemento central
            return float(ordenada[mitad])

    def moda(self, numeros):
        """
        Encuentra la Moda: el valor que aparece con más frecuencia.

        ¿Para qué sirve?
          Útil cuando queremos saber "qué es lo más común". Por ejemplo,
          la talla de ropa más vendida, el producto más pedido, etc.

        ¿Cómo se calcula?
          Contamos cuántas veces aparece cada valor, y retornamos el más repetido.
          Si hay empate, retornamos el primero que apareció en la lista original.

          Ejemplo con [1, 2, 2, 3, 3, 3]:
            1 aparece 1 vez
            2 aparece 2 veces
            3 aparece 3 veces  ← la más frecuente
            Moda = 3

          Ejemplo con empate [1, 1, 2, 2, 3]:
            1 aparece 2 veces
            2 aparece 2 veces  ← empate, pero 1 apareció primero en la lista
            Moda = 1

        Casos especiales:
            moda([]) → None  (no hay moda si la lista está vacía)
        """
        if not numeros:
            return None

        # Counter crea un diccionario con la frecuencia de cada elemento
        frecuencias = Counter(numeros)
        frecuencia_maxima = max(frecuencias.values())

        # Recorremos la lista ORIGINAL para respetar el orden de aparición
        for elemento in numeros:
            if frecuencias[elemento] == frecuencia_maxima:
                return elemento

    def varianza(self, numeros):
        """
        Calcula la varianza: qué tan dispersos están los datos respecto al promedio.

        ¿Para qué sirve?
          Nos dice si los datos están "juntos" o "esparcidos".
          Varianza cercana a 0 → todos los valores son similares entre sí.
          Varianza grande → los valores están muy dispersos.

        ¿Cómo se calcula?
          1. Calcular el promedio
          2. Para cada número, calcular la diferencia con el promedio
          3. Elevar esa diferencia al cuadrado (para que no haya negativos)
          4. Promediar todas esas diferencias al cuadrado

          Ejemplo con [1, 2, 3, 4, 5]:
            Promedio = 3
            Diferencias al cuadrado: (1-3)²=4, (2-3)²=1, (3-3)²=0, (4-3)²=1, (5-3)²=4
            Varianza = (4+1+0+1+4) / 5 = 10/5 = 2.0

        Casos especiales:
            varianza([]) → 0
            varianza([42]) → 0.0  (un solo elemento, no hay dispersión)
        """
        if not numeros:
            return 0
        if len(numeros) == 1:
            return 0.0

        promedio = self.promedio(numeros)
        diferencias_cuadradas = [(x - promedio) ** 2 for x in numeros]
        return sum(diferencias_cuadradas) / len(numeros)

    def desviacion_estandar(self, numeros):
        """
        Calcula la desviacion estándar: dispersión en las mismas unidades que los datos.

        ¿Qué diferencia tiene con la varianza?
          La varianza tiene unidades al cuadrado (difícil de interpretar).
          La desviación estándar es la raíz cuadrada de la varianza,
          así queda en las mismas unidades que los datos originales.

          Ejemplo: si medimos estaturas en metros y la varianza es 0.04 m²,
          la desviación estándar es √0.04 = 0.2 metros.

          Ejemplo con [1, 2, 3, 4, 5]:
            Varianza = 2.0
            Desviación estándar = √2.0 ≈ 1.4142

        ¿Cómo se interpreta?
          Si la desviación es pequeña → los datos están cerca del promedio.
          Si es grande → los datos están muy dispersos.

        Casos especiales:
            desviacion_estandar([]) → 0
        """
        if not numeros:
            return 0

        return math.sqrt(self.varianza(numeros))

    def rango(self, numeros):
        """
        Calcula el rango: la diferencia entre el valor máximo y el mínimo.

        ¿Para qué sirve?
          Es la medida de dispersión más simple. Nos dice cuánto "abarca" el conjunto.

          Ejemplo con [1, 5, 3, 9, 2]:
            Máximo = 9
            Mínimo = 1
            Rango = 9 - 1 = 8

          Ejemplo con [7, 7, 7, 7]:
            Máximo = 7, Mínimo = 7
            Rango = 0  (todos iguales, no hay dispersión)

        Limitación: el rango solo considera dos valores (el mayor y el menor),
        ignorando todo lo que hay en medio.

        Casos especiales:
            rango([]) → 0
            rango([42]) → 0  (un solo elemento, no hay rango)
        """
        if not numeros:
            return 0

        return max(numeros) - min(numeros)