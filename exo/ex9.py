def square_list()-> list:
    '''
    Entrée: /
    Sortie: une liste de nombres mis au carré

    Retourne une liste de nombres, chaque nombre étant passé au carré
    '''

    numbers = [1,2,3,4,5,6,7,8,9,10]
    squared_numbers = [number**2 for number in numbers]
    return squared_numbers


square_list()