def square_list(numbers: list)-> list:
    '''
    Entrée: une liste de nombres
    Sortie: la liste des nombres mis au carré

    Retourne la liste de nombres reçue en entrée, chaque nombre étant passé au carré
    '''

    squared_numbers = [number**2 for number in numbers]
    return squared_numbers


square_list([5,1,2,9,4,3])