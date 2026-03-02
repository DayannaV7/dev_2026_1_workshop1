class Logica:
    """
    Clase con las operaciones básicas de lógica booleana.

    La lógica booleana trabaja con valores de verdadero (True) y falso(False).
    Es la base de cómo funcionan los circuitos electrónicos y las condiciones
    en programación (if, while, etc.).
    """

    def AND(self, a, b):
        """
        Operación AND (Y): ambos deben ser True para que el resultado sea True.

        Tabla de verdad:
            True  AND True  → True   (ambos verdaderos → verdadero)
            True  AND False → False  (uno falso → falso)
            False AND True  → False
            False AND False → False

        Ejemplo del mundo real: una puerta se abre si tienes la llave AND el código correcto.
        """
        return a and b

    def OR(self, a, b):
        """
        Operación OR (O): basta con que uno sea True para que el resultado sea True.

        Tabla de verdad:
            True  OR True  → True   (al menos uno es verdadero)
            True  OR False → True
            False OR True  → True
            False OR False → False  (ninguno es verdadero → falso)

        Ejemplo del mundo real: pagas con efectivo OR con tarjeta.
        """
        return a or b

    def NOT(self, a):
        """
        Operación NOT (NO): invierte el valor. True se vuelve False y viceversa.

        Tabla de verdad:
            NOT True  → False
            NOT False → True

        Ejemplo del mundo real: si NO llueve, salgo a caminar.
        """
        return not a

    def XOR(self, a, b):
        """
        Operación XOR (O exclusivo): True solo cuando los valores son DIFERENTES.

        Tabla de verdad:
            True  XOR True  → False  (iguales → falso)
            True  XOR False → True   (diferentes → verdadero)
            False XOR True  → True
            False XOR False → False  (iguales → falso)

        Ejemplo del mundo real: una lámpara con dos interruptores,
        funciona cuando uno está arriba Y el otro abajo (posiciones diferentes).
        """
        return a ^ b

    def NAND(self, a, b):
        """
        Operación NAND (NO Y): es el opuesto de AND.
        Solo es False cuando AMBOS son True.

        Tabla de verdad:
            True  NAND True  → False  (inverso de AND)
            True  NAND False → True
            False NAND True  → True
            False NAND False → True

        Es equivalente a NOT(AND(a, b)).
        """
        return not (a and b)

    def NOR(self, a, b):
        """
        Operación NOR (NO O): es el opuesto de OR.
        Solo es True cuando AMBOS son False.

        Tabla de verdad:
            True  NOR True  → False
            True  NOR False → False
            False NOR True  → False
            False NOR False → True   (ninguno es verdadero → verdadero)

        Es equivalente a NOT(OR(a, b)).
        """
        return not (a or b)

    def XNOR(self, a, b):
        """
        Operación XNOR (NO O exclusivo): True cuando los valores son IGUALES.

        Tabla de verdad:
            True  XNOR True  → True   (iguales → verdadero)
            True  XNOR False → False
            False XNOR True  → False
            False XNOR False → True   (iguales → verdadero)

        Es el opuesto de XOR. También se llama "equivalencia lógica".
        """
        return not (a ^ b)

    def implicacion(self, a, b):
        """
        Implicación lógica (a → b): "Si a es verdad, entonces b también debe serlo."

        Tabla de verdad:
            True  → True  = True   (prometí y cumplí)
            True  → False = False  (prometí pero NO cumplí → esto es falso)
            False → True  = True   (no prometí nada, así que no puedo fallar)
            False → False = True   (no prometí nada, así que no puedo fallar)

        La única forma de que sea False es que 'a' sea True y 'b' sea False.
        (Prometí algo y no lo cumplí.)

        Fórmula equivalente: (NOT a) OR b
        """
        return (not a) or b

    def bi_implicacion(self, a, b):
        """
        Bi-implicación (a ↔ b): True solo cuando ambos valores son IGUALES.

        También llamada "doble implicación" o "si y solo si".
        Es como decir: "a implica b, Y b implica a".

        Tabla de verdad:
            True  ↔ True  = True   (ambos iguales)
            True  ↔ False = False  (diferentes)
            False ↔ True  = False  (diferentes)
            False ↔ False = True   (ambos iguales)

        Es idéntica a la operación XNOR.
        """
        return a == b