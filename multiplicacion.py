# Función de multiplicar para la calculadora 

def multiplica(a: str, b: str) -> float:
    """
    Multiplica 2 numeros
    
    Parameters
    ----------
        a: str :
            El numero a
        b: str :
            El numero b

    Returns
    -------
        float:
            Retorna la multilplicaion de los numeros
    """

    multiplicando = get_fractions(a)
    multiplicador = get_fractions(b)
    
    return multiplicando * multiplicador
