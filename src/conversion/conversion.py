class Conversion:
    """
    Clase para convertir entre diferentes unidades y sistemas de representación.
    Incluye: temperaturas, distancias, binario, números romanos y código Morse.
    """

    # Tablas de referencia para Morse

    # Diccionario: letra/número a código Morse
    LETRA_A_MORSE = {
        'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',
        'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---',
        'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
        'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    }

    # Diccionario inverso: código Morse a letra/número
    # Se construye automáticamente a partir del diccionario anterior
    MORSE_A_LETRA = {codigo: letra for letra, codigo in LETRA_A_MORSE.items()}

    # Temperaturas

    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte grados Celsius a Fahrenheit.

        La fórmula es: F = (C × 9/5) + 32

        ¿Por qué esa fórmula?
          - Multiplicar por 9/5 ajusta la "escala" entre los dos sistemas
          - Sumar 32 desplaza el punto de inicio (0°C = 32°F)

        Ejemplos:
            celsius_a_fahrenheit(0)   → 32.0   (punto de congelación del agua)
            celsius_a_fahrenheit(100) → 212.0  (punto de ebullición del agua)
            celsius_a_fahrenheit(37)  → 98.6   (temperatura corporal normal)
        """
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit

    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte grados Fahrenheit a Celsius.

        La fórmula es: C = (F - 32) × 5/9

        Es la operación inversa de celsius_a_fahrenheit:
          - Primero restamos 32 para quitar el desplazamiento
          - Luego multiplicamos por 5/9 para ajustar la escala

        Ejemplos:
            fahrenheit_a_celsius(32)  → 0.0   (agua congelada)
            fahrenheit_a_celsius(212) → 100.0 (agua hirviendo)
            fahrenheit_a_celsius(-40) → -40.0 (único punto igual en ambas escalas)
        """
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

    # Distancias

    def metros_a_pies(self, metros):
        """
        Convierte metros a pies.

        1 metro = 3.28084 pies (factor de conversión estándar)

        Ejemplos:
            metros_a_pies(1)    → 3.28084
            metros_a_pies(0)    → 0
            metros_a_pies(1000) → 3280.84
        """
        pies = metros * 3.28084
        return pies

    def pies_a_metros(self, pies):
        """
        Convierte pies a metros.

        1 pie = 0.3048 metros (factor de conversión estándar)

        Ejemplos:
            pies_a_metros(1)       → 0.3048
            pies_a_metros(3.28084) → ~1.0
            pies_a_metros(1000)    → 304.8
        """
        metros = pies * 0.3048
        return metros

    # Sistema binario

    def decimal_a_binario(self, numero_decimal):
        """
        Convierte un número decimal (base 10) a su representación en binario (base 2).

        ¿Cómo funciona internamente?
          El binario solo usa dos dígitos: 0 y 1.
          Para convertir, dividimos el número entre 2 repetidamente y
          guardamos los restos. Esos restos leídos al revés forman el binario.

          Ejemplo con 10:
            10 ÷ 2 = 5, resto 0
             5 ÷ 2 = 2, resto 1
             2 ÷ 2 = 1, resto 0
             1 ÷ 2 = 0, resto 1
          Restos al revés: 1010 → eso es 10 en binario

          Python tiene bin() que hace esto automáticamente.
          bin(10) devuelve '0b1010', quitamos '0b' con [2:]

        Ejemplos:
            decimal_a_binario(0)   → "0"
            decimal_a_binario(2)   → "10"
            decimal_a_binario(10)  → "1010"
            decimal_a_binario(255) → "11111111"
        """
        binario = bin(numero_decimal)[2:]  # bin() devuelve "0b...", [2:] quita el "0b"
        return binario

    def binario_a_decimal(self, numero_binario):
        """
        Convierte un número en binario (string de 0s y 1s) a decimal.

        ¿Cómo funciona internamente?
          Cada dígito binario tiene un valor que es una potencia de 2,
          contando desde la derecha (posición 0, 1, 2, ...).

          Ejemplo con "1010":
            1 × 2³ = 8
            0 × 2² = 0
            1 × 2¹ = 2
            0 × 2⁰ = 0
            Total = 8 + 0 + 2 + 0 = 10

          Python tiene int(cadena, base) que hace esto directamente.

        Ejemplos:
            binario_a_decimal("0")        → 0
            binario_a_decimal("10")       → 2
            binario_a_decimal("1010")     → 10
            binario_a_decimal("11111111") → 255
        """
        decimal = int(numero_binario, 2)  # int(cadena, base) convierte la cadena en la base indicada
        return decimal

    # Números romanos

    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.

        ¿Cómo funciona?
          Los romanos usaban letras para representar valores:
            I=1, V=5, X=10, L=50, C=100, D=500, M=1000

          También hay formas especiales para evitar repetir 4 veces:
            IV=4, IX=9, XL=40, XC=90, CD=400, CM=900

          El algoritmo va de mayor a menor valor:
            - Si el número es ≥ al valor actual, añade el símbolo y resta ese valor
            - Repite hasta que el número sea 0

          Ejemplo con 1994:
            1994 ≥ 1000 → agrega M,  resta 1000 → queda 994
             994 ≥  900 → agrega CM, resta  900 → queda  94
              94 ≥   90 → agrega XC, resta   90 → queda   4
               4 ≥    4 → agrega IV, resta    4 → queda   0
            Resultado: MCMXCIV

        Ejemplos:
            decimal_a_romano(4)    → "IV"
            decimal_a_romano(9)    → "IX"
            decimal_a_romano(1994) → "MCMXCIV"
            decimal_a_romano(2023) → "MMXXIII"
        """
        # Lista de pares (valor, símbolo) ordenada de mayor a menor
        tabla_romanos = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100,  'C'), (90,  'XC'), (50,  'L'), (40,  'XL'),
            (10,   'X'), (9,   'IX'), (5,   'V'), (4,   'IV'),
            (1,    'I'),
        ]

        resultado = ''

        for valor, simbolo in tabla_romanos:
            # Mientras el número sea mayor o igual al valor actual,
            # añadimos el símbolo y restamos el valor
            while numero >= valor:
                resultado += simbolo
                numero -= valor

        return resultado

    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.

        ¿Cómo funciona?
          La regla clave es:
            - Si un símbolo es MENOR que el siguiente, se RESTA
            - Si un símbolo es MAYOR O IGUAL que el siguiente, se SUMA

          Ejemplo con "MCMXCIV":
            M  = 1000 → siguiente es C(100), M > C  → suma  1000 → total: 1000
            C  =  100 → siguiente es M(1000), C < M → resta  100 → total:  900
            M  = 1000 → siguiente es X(10),  M > X  → suma  1000 → total: 1900
            X  =   10 → siguiente es C(100), X < C  → resta   10 → total: 1890
            C  =  100 → siguiente es I(1),   C > I  → suma   100 → total: 1990
            I  =    1 → siguiente es V(5),   I < V  → resta    1 → total: 1989
            V  =    5 → es el último         V      → suma     5 → total: 1994

        Ejemplos:
            romano_a_decimal("IV")      → 4
            romano_a_decimal("IX")      → 9
            romano_a_decimal("MCMXCIV") → 1994
        """
        # Tabla de valores de cada letra romana
        valores = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0

        for i in range(len(romano)):
            valor_actual   = valores[romano[i]]

            # Si no es el último símbolo, miramos el siguiente
            if i + 1 < len(romano):
                valor_siguiente = valores[romano[i + 1]]

                if valor_actual < valor_siguiente:
                    # Caso de sustracción: ej. I antes de V → restar
                    total -= valor_actual
                else:
                    # Caso normal: sumar
                    total += valor_actual
            else:
                # Último símbolo: siempre suma
                total += valor_actual

        return total

    # Código Morse

    def texto_a_morse(self, texto):
        """
        Convierte texto normal a código Morse.

        ¿Cómo funciona?
          El código Morse representa cada letra y número con una combinación
          de puntos (.) y rayas (-). Cada símbolo se separa con un espacio.

          Pasos:
            1. Convertir el texto a mayúsculas (el Morse no distingue)
            2. Para cada letra/número, buscar su código en la tabla LETRA_A_MORSE
            3. Unir todos los códigos separados por espacios

          Ejemplo con "SOS":
            S → "..."
            O → "---"
            S → "..."
            Resultado: "... --- ..."

        Ejemplos:
            texto_a_morse("SOS")   → "... --- ..."
            texto_a_morse("HELLO") → ".... . .-.. .-.. ---"
            texto_a_morse("A1")    → ".- .----"
            texto_a_morse("")      → ""
        """
        if not texto:
            return ''

        # Convertimos a mayúsculas y buscamos cada caracter en la tabla
        codigos = []
        for caracter in texto.upper():
            if caracter in self.LETRA_A_MORSE:
                codigos.append(self.LETRA_A_MORSE[caracter])
            # Si el caracter no está en la tabla (ej. espacios), lo ignoramos

        return ' '.join(codigos)

    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto normal.

        ¿Cómo funciona?
          Separamos el código por espacios para obtener los símbolos individuales.
          Luego buscamos cada símbolo en la tabla inversa MORSE_A_LETRA.

          Maneja espacios dobles o múltiples (split() los ignora automáticamente).

          Ejemplo con "... --- ...":
            "..."  → S
            "---"  → O
            "..."  → S
            Resultado: "SOS"

        Ejemplos:
            morse_a_texto("... --- ...")        → "SOS"
            morse_a_texto(".... . .-.. .-.. ---") → "HELLO"
            morse_a_texto("...  ---  ...")      → "SOS"  (espacios dobles: ok)
            morse_a_texto("")                   → ""
        """
        if not morse:
            return ''

        # split() sin argumentos divide por cualquier cantidad de espacios
        simbolos = morse.split()

        letras = []
        for simbolo in simbolos:
            if simbolo in self.MORSE_A_LETRA:
                letras.append(self.MORSE_A_LETRA[simbolo])

        return ''.join(letras)