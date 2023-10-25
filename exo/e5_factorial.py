def factorial(n: int)-> int:
    '''
    Entrée: n, un entier
    Sortie: un entier

    Fonction récursive calculant la factorielle d'un nombre
    '''

    if (n == 1 or n == 0):
        return 1
    
    return n * factorial(n-1)


factorial(5)