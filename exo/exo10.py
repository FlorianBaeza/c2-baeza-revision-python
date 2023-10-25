def tri_insertion(numbers: list)->list:
    '''
    Entrée: une liste de nombres à ordonner
    Sortie: la liste de nombres triée

    Cette fonction prend une liste de nombres et retourne la liste triée via un tri par insertion
    '''

    final_list = []
    index = -1

    for number in numbers:
        
        for i in range(len(final_list)):
            if number <= final_list[i]:
                index = i
                break

        if index == -1:
            final_list.append(number)
        else: 
            final_list.insert(index, number)
            index = -1

    return final_list


tri_insertion([10, 11, 2, 3, 8, 6])