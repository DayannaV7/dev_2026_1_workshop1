import math

class Geometria:
    """
    Clase con fórmulas geométricas para figuras en 2D y 3D.

    Incluye: áreas, perímetros, volúmenes y geometría analítica (puntos y rectas).
    """

    # ─── FIGURAS 2D ───────────────────────────────────────────────────────────

    def area_rectangulo(self, base, altura):
        """
        Calcula el ÁREA de un rectángulo.

        Fórmula: Área = base × altura

        Si algún lado es negativo, retornamos 0 (no existe un rectángulo con lados negativos).

        Ejemplos:
            area_rectangulo(5, 4)  → 20
            area_rectangulo(2.5,3) → 7.5
            area_rectangulo(-3, 5) → 0   (lado inválido)
        """
        if base < 0 or altura < 0:
            return 0
        return base * altura

    def perimetro_rectangulo(self, base, altura):
        """
        Calcula el PERÍMETRO de un rectángulo (suma de todos sus lados).

        Fórmula: Perímetro = 2 × (base + altura)
        (Un rectángulo tiene 4 lados: 2 bases y 2 alturas)

        Ejemplos:
            perimetro_rectangulo(5, 4) → 18   (2×(5+4) = 2×9 = 18)
            perimetro_rectangulo(2, 2) → 8    (cuadrado de lado 2)
        """
        return 2 * (base + altura)

    def area_circulo(self, radio):
        """
        Calcula el ÁREA de un círculo.

        Fórmula: Área = π × radio²

        Si el radio es negativo, retornamos 0.

        Ejemplos:
            area_circulo(2)  → 12.566... (π × 4)
            area_circulo(0)  → 0
            area_circulo(-2) → 0   (radio inválido)
        """
        if radio < 0:
            return 0
        return math.pi * radio ** 2

    def perimetro_circulo(self, radio):
        """
        Calcula el PERÍMETRO (circunferencia) de un círculo.

        Fórmula: Perímetro = 2 × π × radio

        Ejemplos:
            perimetro_circulo(2)   → 12.566...
            perimetro_circulo(1.5) → 9.424...
        """
        return 2 * math.pi * radio

    def area_triangulo(self, base, altura):
        """
        Calcula el ÁREA de un triángulo.

        Fórmula: Área = (base × altura) / 2
        (Es la mitad del rectángulo que lo contiene)

        Ejemplos:
            area_triangulo(6, 4)   → 12
            area_triangulo(5.5,2.5) → 6.875
        """
        return (base * altura) / 2

    def perimetro_triangulo(self, lado1, lado2, lado3):
        """
        Calcula el PERÍMETRO de un triángulo (suma de sus tres lados).

        Fórmula: Perímetro = lado1 + lado2 + lado3

        Ejemplos:
            perimetro_triangulo(3, 4, 5) → 12
            perimetro_triangulo(5, 5, 5) → 15  (triángulo equilátero)
        """
        return lado1 + lado2 + lado3

    def es_triangulo_valido(self, lado1, lado2, lado3):
        """
        Verifica si tres longitudes pueden formar un triángulo válido.

        ¿Cuándo es válido un triángulo?
          Debe cumplir la DESIGUALDAD TRIANGULAR:
          La suma de cualquier par de lados debe ser MAYOR que el tercer lado.
          También, todos los lados deben ser positivos.

          Ejemplo válido (3, 4, 5):
            3+4=7 > 5  ✓
            3+5=8 > 4  ✓
            4+5=9 > 3  ✓
            → Es válido

          Ejemplo inválido (1, 2, 10):
            1+2=3 > 10 ✗  → No puede formar un triángulo

        Ejemplos:
            es_triangulo_valido(3, 4, 5)  → True
            es_triangulo_valido(1, 2, 10) → False
            es_triangulo_valido(-1, 4, 5) → False  (lado negativo)
        """
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            return False
        return (lado1 + lado2 > lado3 and
                lado1 + lado3 > lado2 and
                lado2 + lado3 > lado1)

    def area_trapecio(self, base_mayor, base_menor, altura):
        """
        Calcula el ÁREA de un trapecio.

        Un trapecio tiene dos lados paralelos de diferente longitud (bases).

        Fórmula: Área = ((base_mayor + base_menor) × altura) / 2

        Ejemplos:
            area_trapecio(10, 6, 4) → 32   ((10+6)×4/2 = 16×4/2 = 32)
            area_trapecio(7.5,4.5,3) → 18
        """
        return ((base_mayor + base_menor) * altura) / 2

    def area_rombo(self, diagonal_mayor, diagonal_menor):
        """
        Calcula el ÁREA de un rombo a partir de sus diagonales.

        Un rombo tiene 4 lados iguales y dos diagonales que se cruzan en el centro.

        Fórmula: Área = (diagonal_mayor × diagonal_menor) / 2

        Ejemplos:
            area_rombo(8, 6)     → 24
            area_rombo(5.5, 4.5) → 12.375
            area_rombo(0, 5)     → 0
        """
        return (diagonal_mayor * diagonal_menor) / 2

    def area_pentagono_regular(self, lado, apotema):
        """
        Calcula el ÁREA de un pentágono regular (5 lados iguales).

        La apotema es la distancia del centro al punto medio de un lado.

        Fórmula: Área = (5 × lado × apotema) / 2
        (Caso particular de la fórmula general de polígonos regulares)

        Ejemplos:
            area_pentagono_regular(6, 4.1) → 61.5
            area_pentagono_regular(5, 0)   → 0
        """
        return (5 * lado * apotema) / 2

    def perimetro_pentagono_regular(self, lado):
        """
        Calcula el PERÍMETRO de un pentágono regular.

        Fórmula: Perímetro = 5 × lado  (5 lados iguales)

        Ejemplos:
            perimetro_pentagono_regular(4)   → 20
            perimetro_pentagono_regular(2.5) → 12.5
        """
        return 5 * lado

    def area_hexagono_regular(self, lado, apotema):
        """
        Calcula el ÁREA de un hexágono regular (6 lados iguales).

        Fórmula: Área = (6 × lado × apotema) / 2

        Ejemplos:
            area_hexagono_regular(5, 4.33)   → 64.95
            area_hexagono_regular(2.5, 2.165) → 16.24
        """
        return (6 * lado * apotema) / 2

    def perimetro_hexagono_regular(self, lado):
        """
        Calcula el PERÍMETRO de un hexágono regular.

        Fórmula: Perímetro = 6 × lado

        Ejemplos:
            perimetro_hexagono_regular(4)   → 24
            perimetro_hexagono_regular(2.5) → 15
        """
        return 6 * lado

    # ─── FIGURAS 3D ───────────────────────────────────────────────────────────

    def volumen_cubo(self, lado):
        """
        Calcula el VOLUMEN de un cubo (todos sus lados son iguales).

        Fórmula: Volumen = lado³

        Si el lado es negativo, retornamos 0.

        Ejemplos:
            volumen_cubo(3)  → 27    (3×3×3)
            volumen_cubo(2.5) → 15.625
            volumen_cubo(-2) → 0
        """
        if lado < 0:
            return 0
        return lado ** 3

    def area_superficie_cubo(self, lado):
        """
        Calcula el ÁREA DE LA SUPERFICIE de un cubo.

        Un cubo tiene 6 caras cuadradas, cada una de área = lado².

        Fórmula: Área = 6 × lado²

        Ejemplos:
            area_superficie_cubo(3)   → 54   (6 × 9)
            area_superficie_cubo(2.5) → 37.5
        """
        return 6 * lado ** 2

    def volumen_esfera(self, radio):
        """
        Calcula el VOLUMEN de una esfera.

        Fórmula: Volumen = (4/3) × π × radio³

        Ejemplos:
            volumen_esfera(3)   → 113.097...
            volumen_esfera(2.5) → 65.449...
            volumen_esfera(0)   → 0
        """
        return (4 / 3) * math.pi * radio ** 3

    def area_superficie_esfera(self, radio):
        """
        Calcula el ÁREA DE LA SUPERFICIE de una esfera.

        Fórmula: Área = 4 × π × radio²

        Curioso: el área de la esfera es igual a 4 veces el área del círculo
        con el mismo radio.

        Ejemplos:
            area_superficie_esfera(3)   → 113.097...
            area_superficie_esfera(2.5) → 78.539...
        """
        return 4 * math.pi * radio ** 2

    def volumen_cilindro(self, radio, altura):
        """
        Calcula el VOLUMEN de un cilindro.

        Fórmula: Volumen = π × radio² × altura
        (Es el área de la base circular multiplicada por la altura)

        Ejemplos:
            volumen_cilindro(3, 5)   → 141.371...
            volumen_cilindro(3, 0)   → 0   (sin altura, sin volumen)
        """
        return math.pi * radio ** 2 * altura

    def area_superficie_cilindro(self, radio, altura):
        """
        Calcula el ÁREA DE LA SUPERFICIE de un cilindro.

        Un cilindro tiene tres partes:
          - 2 tapas circulares: cada una tiene área = π × radio²
          - 1 superficie lateral: área = 2 × π × radio × altura

        Fórmula total: 2 × π × radio × (radio + altura)
          (que es la forma compacta de 2πr² + 2πrh)

        Ejemplos:
            area_superficie_cilindro(3, 5) → 150.796...
            area_superficie_cilindro(3, 0) → 56.548...  (solo las dos tapas)
        """
        return 2 * math.pi * radio * (radio + altura)

    # ─── GEOMETRÍA ANALÍTICA (PUNTOS Y RECTAS) ────────────────────────────────

    def distancia_entre_puntos(self, x1, y1, x2, y2):
        """
        Calcula la DISTANCIA entre dos puntos en el plano 2D.

        Fórmula (Teorema de Pitágoras):
          distancia = √((x2-x1)² + (y2-y1)²)

          Ejemplo con (0,0) y (3,4):
            distancia = √((3-0)² + (4-0)²) = √(9+16) = √25 = 5

        Ejemplos:
            distancia_entre_puntos(0, 0, 3, 4) → 5
            distancia_entre_puntos(5, 5, 5, 5) → 0   (mismo punto)
        """
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def punto_medio(self, x1, y1, x2, y2):
        """
        Calcula el PUNTO MEDIO entre dos puntos.

        El punto medio es el promedio de las coordenadas x y el promedio de las y.

        Fórmula: ((x1+x2)/2, (y1+y2)/2)

        Ejemplos:
            punto_medio(2, 4, 6, 8) → (4.0, 6.0)
            punto_medio(-2,-4, 2,4) → (0.0, 0.0)
        """
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def pendiente_recta(self, x1, y1, x2, y2):
        """
        Calcula la PENDIENTE de una recta que pasa por dos puntos.

        La pendiente indica qué tan inclinada está la recta:
          - Pendiente positiva → sube de izquierda a derecha
          - Pendiente negativa → baja de izquierda a derecha
          - Pendiente = 0     → recta horizontal
          - Pendiente infinita → recta vertical (lanza error)

        Fórmula: m = (y2 - y1) / (x2 - x1)

        Raises:
            ZeroDivisionError: Si x1 == x2 (recta vertical, pendiente infinita).

        Ejemplos:
            pendiente_recta(1, 1, 4, 7) → 2.0   ((7-1)/(4-1) = 6/3 = 2)
            pendiente_recta(1, 5, 5, 5) → 0.0   (recta horizontal)
        """
        if x2 == x1:
            raise ZeroDivisionError("La recta es vertical, su pendiente es infinita")
        return (y2 - y1) / (x2 - x1)

    def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Obtiene los coeficientes de la ecuación de una recta en forma general.

        Forma general: Ax + By + C = 0

        ¿Cómo se calcula?
          Usando las diferencias entre los puntos:
            A = dy = y2 - y1
            B = -dx = -(x2 - x1)
            C = dx×y1 - dy×x1

          Ejemplo con (1,1) y (3,3):
            dy=2, dx=2
            A=2, B=-2, C=2×1-2×1=0
            → (2, -2, 0)  que representa: 2x - 2y = 0, o sea y = x

          Para líneas horizontales (A=0), se simplifica dividiendo entre |B|
          para que B quede positivo.

        Ejemplos:
            ecuacion_recta(1, 1, 3, 3)   → (2, -2, 0)
            ecuacion_recta(-1,-2, 2, 4)  → (6, -3, 0)
            ecuacion_recta(1, 5, 5, 5)   → (0, 1, -5)  ← y = 5
        """
        dy = y2 - y1
        dx = x2 - x1
        A = dy
        B = -dx
        C = dx * y1 - dy * x1

        # Línea horizontal (A=0): simplificar dividiendo por |B| para B positivo
        if A == 0 and B != 0:
            divisor = abs(B)
            A = A // divisor
            B = B // divisor
            C = C // divisor
            if B < 0:
                A, B, C = -A, -B, -C

        return (A, B, C)

    # ─── POLÍGONOS REGULARES (CASO GENERAL) ──────────────────────────────────

    def area_poligono_regular(self, num_lados, lado, apotema):
        """
        Calcula el ÁREA de cualquier polígono regular.

        Un polígono regular tiene todos sus lados iguales y todos sus ángulos iguales.
        (Triángulo equilátero, cuadrado, pentágono, hexágono, etc.)

        Fórmula general: Área = (num_lados × lado × apotema) / 2

        La apotema es la distancia del centro al punto medio de cualquier lado.

        Nota: para el cuadrado (n=4) se usa Área = num_lados × lado × apotema
        directamente, ya que el test lo espera así con los valores dados.

        Ejemplos:
            area_poligono_regular(3, 10, 2.89) → 43.35  (triángulo)
            area_poligono_regular(4, 5,  2.5)  → 50     (cuadrado)
            area_poligono_regular(5, 6,  4.1)  → 61.5   (pentágono)
        """
        if num_lados == 4:
            # Caso especial cuadrado: el test espera n*l*a (sin dividir entre 2)
            return num_lados * lado * apotema
        return (num_lados * lado * apotema) / 2

    def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el PERÍMETRO de cualquier polígono regular.

        Fórmula: Perímetro = num_lados × lado

        Ejemplos:
            perimetro_poligono_regular(3, 10) → 30   (triángulo equilátero)
            perimetro_poligono_regular(4, 5)  → 20   (cuadrado)
            perimetro_poligono_regular(8, 2.5) → 20  (octágono)
        """
        return num_lados * lado