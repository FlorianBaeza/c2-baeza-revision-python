def best_grade(grades: dict)-> str:
    '''
    Entrée : grades, un dictionnaire contenant les noms des élèves et les notes associées
    Sortie : le nom d'un élève

    Retourne le nom de l'élève ayant obtenu la meilleure note
    '''

    maxGrade = -1
    bestStudent = ""

    for name, grade in grades.items():
        if grade > maxGrade:
            maxGrade = grade
            bestStudent = name
    
    return bestStudent


best_grade({'eleve1': 10, 'eleve2': 3, 'eleve3': 17, 'eleve4': 17, 'eleve5': 9})