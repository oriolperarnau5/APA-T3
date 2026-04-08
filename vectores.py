"""
APA-T3: Multiplicación de vectores y ortogonalidad

Nombre y apellidos: ORIOL PERARNAU
"""

from numbers import Real
import doctest


class Vector:
    """
    Clase que representa un vector.

    Ejemplos:

    >>> v1 = Vector([1, 2, 3])
    >>> v2 = Vector([4, 5, 6])

    >>> v1 * 2
    Vector([2, 4, 6])

    >>> v1 * v2
    Vector([4, 10, 18])

    >>> 2 * v1
    Vector([2, 4, 6])

    >>> v1 @ v2
    32

    >>> v1 = Vector([2, 1, 2])
    >>> v2 = Vector([0.5, 1, 0.5])

    >>> v1 // v2
    Vector([1.0, 2.0, 1.0])

    >>> v1 % v2
    Vector([1.0, -1.0, 1.0])

    >>> v1 // v2 + v1 % v2
    Vector([2.0, 1.0, 2.0])
    """

    def __init__(self, componentes):
        self.componentes = list(componentes)

    def __repr__(self):
        return f"Vector({self.componentes})"

    def __len__(self):
        return len(self.componentes)

    def __iter__(self):
        return iter(self.componentes)

    def __eq__(self, otro):
        if not isinstance(otro, Vector):
            return False
        return self.componentes == otro.componentes

    def __add__(self, otro):
        if not isinstance(otro, Vector):
            raise TypeError("Solo se pueden sumar vectores.")
        if len(self) != len(otro):
            raise ValueError("Dimensiones distintas.")
        return Vector([a + b for a, b in zip(self, otro)])

    def __sub__(self, otro):
        if not isinstance(otro, Vector):
            raise TypeError("Solo se pueden restar vectores.")
        if len(self) != len(otro):
            raise ValueError("Dimensiones distintas.")
        return Vector([a - b for a, b in zip(self, otro)])

    # -------------------------
    # MULTIPLICACIÓN (*)
    # -------------------------
    def __mul__(self, otro):
        if isinstance(otro, Real):
            return Vector([x * otro for x in self])

        if isinstance(otro, Vector):
            if len(self) != len(otro):
                raise ValueError("Dimensiones distintas.")
            return Vector([a * b for a, b in zip(self, otro)])

        raise TypeError("Operación no válida.")

    def __rmul__(self, otro):
        return self * otro

    # -------------------------
    # PRODUCTO ESCALAR (@)
    # -------------------------
    def __matmul__(self, otro):
        if not isinstance(otro, Vector):
            raise TypeError("Debe ser un vector.")
        if len(self) != len(otro):
            raise ValueError("Dimensiones distintas.")
        return sum(a * b for a, b in zip(self, otro))

    # -------------------------
    # COMPONENTE PARALELA (//)
    # -------------------------
    def __floordiv__(self, otro):
        if not isinstance(otro, Vector):
            raise TypeError("Debe ser un vector.")
        if len(self) != len(otro):
            raise ValueError("Dimensiones distintas.")

        norma2 = otro @ otro
        if norma2 == 0:
            raise ValueError("Vector nulo.")

        factor = (self @ otro) / norma2
        return factor * otro

    # -------------------------
    # COMPONENTE PERPENDICULAR (%)
    # -------------------------
    def __mod__(self, otro):
        return self - (self // otro)


# Ejecutar doctests
if __name__ == "__main__":
    doctest.testmod(verbose=True)