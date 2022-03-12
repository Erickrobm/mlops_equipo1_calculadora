def division(a, b):
    """

    Parameters
    ----------
    a : int, float, string.
    Primer valor definido para la operación.
        
    b : int, float, string.
    Segundo valor definido para la operación.
        

    Returns
    -------
    Valor obtenido por la división de los parámetros.

    """
    dividendo = float(a)
    divisor = float(b)
    try:
      return dividendo / divisor
    except ZeroDivisionError: 
      return "Division entre cero"
