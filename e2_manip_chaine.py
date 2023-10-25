def count_word(sentence: str) -> int :
    '''
    Entrée : sentence, une phrase (string)
    Sortie : nombre de mots (nombre)

    Cette fonction prend en entrée une phrase et compte le nombre de mot à l'intérieur
    '''

    return len(sentence.split(" "))

# =========================================================

sentence = str(input("Veuillez saisir une phrase : "))

# affichage en masjucule
print(sentence.upper())

# affichage en minuscule
print(sentence.lower())

# nombre de mots
print(count_word(sentence))