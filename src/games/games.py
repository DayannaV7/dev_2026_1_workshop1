import random

class Games:
    """
    Clase con la lógica de varios juegos clásicos.
    """

    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el GANADOR del juego Piedra, Papel o Tijera.

        Reglas:
          - Piedra  vence a Tijera  (la aplasta)
          - Tijera  vence a Papel   (lo corta)
          - Papel   vence a Piedra  (la envuelve)
          - Si ambos eligen lo mismo → empate

        ¿Cómo funciona?
          Guardamos un diccionario con la relación "X vence a Y":
            "piedra" vence a "tijera"
            "papel"  vence a "piedra"
            "tijera" vence a "papel"

          Luego revisamos si lo que eligió jugador1 vence a jugador2.

        Maneja mayúsculas y minúsculas (convierte todo a minúsculas).
        Si algún jugador elige algo inválido, retorna "invalid".

        Ejemplos:
            piedra_papel_tijera("piedra", "tijera") → "jugador1"
            piedra_papel_tijera("papel",  "piedra") → "jugador1"
            piedra_papel_tijera("piedra", "papel")  → "jugador2"
            piedra_papel_tijera("piedra", "piedra") → "empate"
            piedra_papel_tijera("PIEDRA", "tijera") → "jugador1"  (mayúsculas ok)
            piedra_papel_tijera("piedra", "xxx")    → "invalid"
        """
        j1 = jugador1.lower()
        j2 = jugador2.lower()

        opciones_validas = {"piedra", "papel", "tijera"}

        if j1 not in opciones_validas or j2 not in opciones_validas:
            return "invalid"

        if j1 == j2:
            return "empate"

        # Diccionario: cada opción sabe a quién vence
        quien_gana = {
            "piedra": "tijera",   # Piedra vence a Tijera
            "papel":  "piedra",   # Papel  vence a Piedra
            "tijera": "papel",    # Tijera vence a Papel
        }

        if quien_gana[j1] == j2:
            return "jugador1"
        else:
            return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Da una pista para el juego de adivinar un número.

        Compara el intento del jugador con el número secreto y responde:
          - "correcto"  → ¡acertó!
          - "muy alto"  → el intento es mayor que el secreto
          - "muy bajo"  → el intento es menor que el secreto

        Funciona con números negativos también.

        Ejemplos:
            adivinar_numero_pista(50, 50) → "correcto"
            adivinar_numero_pista(50, 75) → "muy alto"
            adivinar_numero_pista(50, 25) → "muy bajo"
            adivinar_numero_pista(-10,-5) → "muy alto"  (-5 > -10)
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        """
        Verifica el estado de un juego de TA TE TI (Tic-Tac-Toe).

        El tablero es una matriz 3×3 con:
          "X" → marca del jugador X
          "O" → marca del jugador O
          " " → casilla vacía

        ¿Cómo funciona?
          Revisamos las 8 posibles líneas ganadoras:
            - 3 filas horizontales
            - 3 columnas verticales
            - 2 diagonales

          Si alguna línea tiene 3 marcas iguales (y no son espacios) → hay ganador.
          Si no hay ganador:
            - Si hay algún espacio vacío → el juego "continua"
            - Si no hay espacios → "empate"

        Retorna:
            "X"       → ganó X
            "O"       → ganó O
            "empate"  → tablero lleno sin ganador
            "continua" → el juego sigue (hay espacios vacíos)

        Ejemplos:
            [["X","X","X"],["O","O"," "],[" "," "," "]] → "X"  (X ganó en fila 1)
            [["X","O","X"],["O","O","X"],["O","X","O"]] → "empate"
            [[" "," "," "],[" "," "," "],[" "," "," "]] → "continua"
        """
        # Las 8 líneas posibles (cada una como lista de coordenadas [fila][col])
        lineas_ganadoras = [
            [(0,0),(0,1),(0,2)],  # Fila 1
            [(1,0),(1,1),(1,2)],  # Fila 2
            [(2,0),(2,1),(2,2)],  # Fila 3
            [(0,0),(1,0),(2,0)],  # Columna 1
            [(0,1),(1,1),(2,1)],  # Columna 2
            [(0,2),(1,2),(2,2)],  # Columna 3
            [(0,0),(1,1),(2,2)],  # Diagonal ↘
            [(0,2),(1,1),(2,0)],  # Diagonal ↗
        ]

        # Revisar si alguna línea es ganadora
        for linea in lineas_ganadoras:
            valores = [tablero[fila][col] for fila, col in linea]
            # Si los tres son iguales y no son espacios vacíos → hay ganador
            if valores[0] != " " and valores[0] == valores[1] == valores[2]:
                return valores[0]  # Retorna "X" o "O"

        # No hay ganador. ¿Quedan espacios?
        hay_espacio = any(tablero[i][j] == " " for i in range(3) for j in range(3))
        if hay_espacio:
            return "continua"
        else:
            return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.

        ¿Qué es Mastermind?
          Es un juego donde un jugador crea una combinación secreta de colores
          y el otro debe adivinarla con pistas.

        ¿Cómo funciona?
          Usamos random.choice() para seleccionar un color al azar de la lista
          disponible, y lo hacemos 'longitud' veces.

          Los colores pueden repetirse (un mismo color puede aparecer varias veces).

        Ejemplos:
            generar_combinacion_mastermind(4, ["rojo","azul","verde"])
              → podría dar: ["rojo", "verde", "rojo", "azul"]  (aleatorio)

            generar_combinacion_mastermind(0, ["rojo","azul"]) → []
        """
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.

        Reglas de la torre:
          1. Solo puede moverse en línea recta (horizontal o vertical)
          2. NO puede moverse en diagonal
          3. NO puede saltar sobre otras piezas (si hay algo en el camino, se bloquea)
          4. No puede quedarse en el mismo lugar
          5. Debe mantenerse dentro del tablero (filas y columnas 0-7)

        El tablero es una cuadrícula 8×8:
          " " → casilla vacía
          Cualquier otra letra → hay una pieza allí

        ¿Cómo funciona?
          1. Verificar que todas las coordenadas estén en el rango 0-7
          2. Verificar que no sea el mismo lugar
          3. Verificar que sea movimiento recto (horizontal O vertical, no ambos)
          4. Verificar que no haya piezas en el camino

        Retorna True si el movimiento es válido, False si no.

        Ejemplos:
            validar_movimiento_torre_ajedrez(0,0, 0,7, tablero_vacio) → True  (fila completa)
            validar_movimiento_torre_ajedrez(0,0, 1,1, tablero_vacio) → False (diagonal)
            validar_movimiento_torre_ajedrez(4,4, 4,4, tablero_vacio) → False (mismo lugar)
            validar_movimiento_torre_ajedrez(0,0, 0,8, tablero_vacio) → False (fuera del tablero)
        """
        # 1. Verificar límites del tablero (debe estar entre 0 y 7)
        for coordenada in [desde_fila, desde_col, hasta_fila, hasta_col]:
            if coordenada < 0 or coordenada > 7:
                return False

        # 2. Verificar que no sea el mismo lugar
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        # 3. La torre solo se mueve en línea recta (NO diagonal)
        #    Si cambia tanto fila COMO columna al mismo tiempo, es diagonal
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        # 4. Verificar que no haya piezas en el camino
        if desde_fila == hasta_fila:
            # Movimiento HORIZONTAL: revisamos las columnas intermedias
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False  # Hay una pieza bloqueando
        else:
            # Movimiento VERTICAL: revisamos las filas intermedias
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False  # Hay una pieza bloqueando

        return True  # Movimiento válido