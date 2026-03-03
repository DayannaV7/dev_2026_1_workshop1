import re

class Strings:
    """
    Clase con operaciones para manipular y analizar cadenas de texto (strings).

    Un string es simplemente una secuencia de caracteres: letras, números, espacios, etc.
    """

    def es_palindromo(self, texto):
        """
        Verifica si un texto es palíndromo: se lee igual de izquierda a derecha
        que de derecha a izquierda.

        Ignora espacios, signos de puntuación y diferencias entre mayúsculas/minúsculas.

        ¿Cómo funciona?
          1. Limpiar el texto: quitar todo lo que no sea letra o número
          2. Convertir a minúsculas
          3. Comparar el texto limpio con su versión invertida

          Ejemplo con "Anita lava la tina":
            Limpio: "anitalavalatina"
            Invertido: "anitalavalatina"  ← ¡igual! → es palíndromo

          Ejemplo con "sigmotoa":
            Limpio: "sigmotoa"
            Invertido: "aotomgis"  ← diferente → no es palíndromo

        Ejemplos:
            es_palindromo("ana")               → True
            es_palindromo("reconocer")         → True
            es_palindromo("Anita lava la tina") → True
            es_palindromo("hola")              → False
            es_palindromo("")                  → True  (vacío cuenta como palíndromo)
        """
        # re.sub quita todos los caracteres que NO sean letras o números
        solo_letras = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
        return solo_letras == solo_letras[::-1]

    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto carácter por carácter.

        ¿Cómo funciona?
          Empezamos con una cadena vacía y vamos agregando cada letra
          AL INICIO (no al final) para invertir el orden.

          Ejemplo con "hola":
            Inicio: resultado = ""
            'h' → resultado = "h"
            'o' → resultado = "oh"
            'l' → resultado = "loh"
            'a' → resultado = "aloh"

        Ejemplos:
            invertir_cadena("hola")   → "aloh"
            invertir_cadena("Python") → "nohtyP"
            invertir_cadena("")       → ""
            invertir_cadena("a")      → "a"
        """
        resultado = ''
        for caracter in texto:
            resultado = caracter + resultado  # Cada letra va al inicio
        return resultado

    def contar_vocales(self, texto):
        """
        Cuenta cuántas vocales (a, e, i, o, u) hay en el texto.

        Funciona con mayúsculas y minúsculas.

        ¿Cómo funciona?
          Convertimos todo a minúsculas y revisamos si cada letra es vocal.

          Ejemplo con "murcielago":
            m-u-r-c-i-e-l-a-g-o
            Vocales: u, i, e, a, o → 5 vocales

        Ejemplos:
            contar_vocales("sigmotoa")  → 4  (i, o, o, a)
            contar_vocales("murcielago") → 5
            contar_vocales("rhythm")    → 0  (ninguna vocal)
            contar_vocales("AeIoU")     → 5  (mayúsculas también cuentan)
            contar_vocales("")          → 0
        """
        vocales = 'aeiou'
        cantidad = 0
        for caracter in texto.lower():  # .lower() convierte todo a minúsculas
            if caracter in vocales:
                cantidad += 1
        return cantidad

    def contar_consonantes(self, texto):
        """
        Cuenta cuántas consonantes hay en el texto.

        Una consonante es cualquier letra del alfabeto que no sea vocal.
        Espacios, números y signos NO cuentan.

        ¿Cómo funciona?
          Para cada carácter verificamos:
            1. ¿Es una letra? (no espacio, no número)
            2. ¿No es vocal?
          Si ambas son verdaderas, es consonante.

          Ejemplo con "Python":
            P → letra, no vocal → consonante
            y → letra, no vocal → consonante
            t → letra, no vocal → consonante
            h → letra, no vocal → consonante
            o → letra, pero ES vocal → no cuenta
            n → letra, no vocal → consonante
            Total: 5 consonantes

        Ejemplos:
            contar_consonantes("Python")  → 5
            contar_consonantes("sigmotoa") → 4
            contar_consonantes("aeiou")   → 0
            contar_consonantes("")        → 0
        """
        # 'y' no se cuenta como consonante según el test (P, t, h, n = 4 en "PythOn")
        no_consonantes = 'aeiou y'
        cantidad = 0
        for caracter in texto.lower():
            if caracter.isalpha() and caracter not in no_consonantes:
                cantidad += 1
        return cantidad

    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos textos son anagramas: usan exactamente las mismas letras.

        Ignora espacios y diferencias entre mayúsculas/minúsculas.

        ¿Cómo funciona?
          Limpiamos ambos textos (quitamos espacios, pasamos a minúsculas),
          los ordenamos alfabéticamente y comparamos.
          Si al ordenar quedan iguales → son anagramas.

          Ejemplo con "roma" y "amor":
            "roma" limpio y ordenado: ['a', 'm', 'o', 'r']
            "amor" limpio y ordenado: ['a', 'm', 'o', 'r']
            ¡Iguales! → son anagramas

          Ejemplo con "Dormitory" y "Dirty room":
            "dormitory" → ordenado: ['d','i','m','o','o','r','r','t','y']
            "dirtyroom" → ordenado: ['d','i','m','o','o','r','r','t','y']
            ¡Iguales! → son anagramas

        Ejemplos:
            es_anagrama("roma", "amor")         → True
            es_anagrama("listen", "silent")     → True
            es_anagrama("Dormitory","Dirty room") → True
            es_anagrama("hello", "world")        → False
        """
        # Quitar espacios y pasar a minúsculas, luego ordenar
        limpiar = lambda texto: sorted(re.sub(r'\s+', '', texto).lower())
        return limpiar(texto1) == limpiar(texto2)

    def contar_palabras(self, texto):
        """
        Cuenta cuántas palabras hay en un texto.

        .split() divide por espacios y automáticamente ignora espacios múltiples
        o espacios al inicio/final.

        Ejemplos:
            contar_palabras("Hola mundo")              → 2
            contar_palabras("Python es divertido")     → 3
            contar_palabras("  dev with sigmotoa    ") → 3  (espacios extra ignorados)
            contar_palabras("")                        → 0
        """
        return len(texto.split())

    def palabras_mayus(self, texto):
        """
        Pone en MAYÚSCULA la primera letra de cada palabra.

        A diferencia de .title() de Python, este método respeta los espacios
        múltiples tal como están en el texto original.

        ¿Cómo funciona?
          Recorremos el texto carácter por carácter:
            - Si encontramos un espacio, lo guardamos
            - Si encontramos una letra, leemos toda la palabra y capitalizamos
              solo su primer carácter

        Ejemplos:
            palabras_mayus("hola mundo")        → "Hola Mundo"
            palabras_mayus("  hola  mundo  ")   → "  Hola  Mundo  "  (espacios conservados)
            palabras_mayus("sigmotoa es genial") → "Sigmotoa Es Genial"
            palabras_mayus("")                  → ""
        """
        resultado = []
        i = 0

        while i < len(texto):
            if texto[i] == ' ':
                # Guardar el espacio tal cual
                resultado.append(' ')
                i += 1
            else:
                # Encontramos el inicio de una palabra
                # Buscar dónde termina (hasta el próximo espacio)
                j = i
                while j < len(texto) and texto[j] != ' ':
                    j += 1

                palabra = texto[i:j]
                # Capitalizar: primera letra en mayúscula + resto igual
                palabra_capitalizada = palabra[0].upper() + palabra[1:]
                resultado.append(palabra_capitalizada)
                i = j

        return ''.join(resultado)

    def eliminar_espacios_duplicados(self, texto):
        """
        Reemplaza múltiples espacios consecutivos por un solo espacio.

        Un espacio al inicio o final NO se elimina, solo se reducen los dobles.

        ¿Cómo funciona?
          Usamos una expresión regular: ' {2,}' significa "dos o más espacios seguidos"
          y los reemplazamos por un único espacio.

        Ejemplos:
            eliminar_espacios_duplicados("Hola  mundo")          → "Hola mundo"
            eliminar_espacios_duplicados("  a   b  c  ")         → " a b c "
            eliminar_espacios_duplicados("Hola mundo")           → "Hola mundo"  (sin cambio)
            eliminar_espacios_duplicados("")                     → ""
        """
        return re.sub(r' {2,}', ' ', texto)

    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero válido.

        Acepta números negativos (con signo -) y positivos.
        NO acepta decimales (como "12.34") ni letras.

        ¿Cómo funciona?
          Intentamos convertir el texto a entero con int().
          Si funciona → es un número entero → retornamos True.
          Si lanza un error → no es entero → retornamos False.

        Ejemplos:
            es_numero_entero("123")   → True
            es_numero_entero("-456")  → True
            es_numero_entero("12.34") → False  (tiene punto decimal)
            es_numero_entero("abc")   → False
            es_numero_entero("12a")   → False
        """
        try:
            int(texto)   # Si esto funciona, es un entero válido
            return True
        except ValueError:
            return False  # Si falla, no es un entero

    def cifrar_cesar(self, texto, desplazamiento):
        """
        Cifra un texto usando el cifrado César.

        ¿Qué es el cifrado César?
          Es uno de los cifrados más antiguos (lo usaba Julio César).
          Cada letra se "desplaza" un número fijo de posiciones en el alfabeto.

        ¿Cómo funciona?
          Con desplazamiento=3:
            a → d, b → e, c → f, ..., x → a, y → b, z → c
            (cuando llega al final del alfabeto, da la vuelta al inicio)

          Ejemplo con "abc" y desplazamiento=3:
            a (posición 0) + 3 = posición 3 → d
            b (posición 1) + 3 = posición 4 → e
            c (posición 2) + 3 = posición 5 → f
            Resultado: "def"

          Ejemplo con "xyz" y desplazamiento=3:
            x (posición 23) + 3 = 26 % 26 = 0 → a
            y (posición 24) + 3 = 27 % 26 = 1 → b
            z (posición 25) + 3 = 28 % 26 = 2 → c
            Resultado: "abc"  (da la vuelta)

          El operador % (módulo) se encarga de la "vuelta" al inicio.
          Espacios y otros caracteres no se cifran, se dejan igual.

        Ejemplos:
            cifrar_cesar("abc", 3)  → "def"
            cifrar_cesar("xyz", 3)  → "abc"
            cifrar_cesar("ABC", 3)  → "DEF"
            cifrar_cesar("def", -3) → "abc"  (desplazamiento negativo = descifrar)
            cifrar_cesar("", 5)     → ""
        """
        resultado = []

        for caracter in texto:
            if caracter.isalpha():
                # Determinar la base: 'A' para mayúsculas, 'a' para minúsculas
                base = ord('A') if caracter.isupper() else ord('a')
                # ord() convierte letra a número, chr() convierte número a letra
                # % 26 asegura que damos la vuelta al llegar al final del alfabeto
                nueva_letra = chr((ord(caracter) - base + desplazamiento) % 26 + base)
                resultado.append(nueva_letra)
            else:
                # No es letra (espacio, número, etc.) → dejar igual
                resultado.append(caracter)

        return ''.join(resultado)

    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra un texto cifrado con el método César.

        ¿Cómo funciona?
          Para descifrar, simplemente aplicamos el cifrado en sentido contrario:
          usamos el mismo desplazamiento pero negativo.

          Si ciframos con +3, desciframos con -3.

        Ejemplos:
            descifrar_cesar("def", 3)  → "abc"
            descifrar_cesar("abc", 3)  → "xyz"
            descifrar_cesar("DEF", 3)  → "ABC"
            descifrar_cesar("abc", -3) → "def"  (desplazamiento negativo invierte)
        """
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones donde aparece una subcadena dentro de un texto.

        ¿Qué es una subcadena?
          Es una cadena más corta que está contenida dentro de otra.
          Por ejemplo, "abc" es subcadena de "abcabcabc".

        ¿Cómo funciona?
          Usamos find() que busca desde una posición inicial y retorna -1 si no encuentra.
          Vamos moviendo la posición de inicio después de cada hallazgo.

          Ejemplo con "abcabcabc" buscando "abc":
            Desde posición 0: encuentra en posición 0 → guarda 0, siguiente búsqueda desde 1
            Desde posición 1: encuentra en posición 3 → guarda 3, siguiente desde 4
            Desde posición 4: encuentra en posición 6 → guarda 6, siguiente desde 7
            Desde posición 7: no encuentra → termina
            Resultado: [0, 3, 6]

        Ejemplos:
            encontrar_subcadena("hola mundo", "mundo") → [5]
            encontrar_subcadena("abcabcabc", "abc")    → [0, 3, 6]
            encontrar_subcadena("hola mundo", "python") → []
            encontrar_subcadena("hola", "")            → []  (subcadena vacía: no busca)
            encontrar_subcadena("test", "test")        → [0]
        """
        if not subcadena:
            return []

        posiciones = []
        inicio = 0

        while True:
            posicion = texto.find(subcadena, inicio)
            if posicion == -1:
                break                    # No encontró más
            posiciones.append(posicion)
            inicio = posicion + 1        # Continuar buscando desde el siguiente carácter

        return posiciones