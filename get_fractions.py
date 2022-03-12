def get_fractions(valor: str) -> float:
    """Regresa el valor tipo float si es fraccionario retorna la division

    Parameters
    ----------
        valor: str :
            El valor que se va a convertir a float

    Returns
    -------
        returns:
            El valor en float

    """
    if "/" in valor:
        decimal = int(valor[0:1]) / int(valor[2:3])
        return decimal
    else:
        return float(valor)