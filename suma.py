def suma(sumando_a, sumando_b):
  """
  Regresa el valor tipo float de una suma de dos variables
    Parameters
    ----------
        valor: str :
            El valor que se va a convertir a float
    Returns
    -------
        returns:
            El valor en float
"""
  sumando_a = get_fractions(sumando_a)
  sumando_b = get_fractions(sumando_b)
  return sumando_a + sumando_b