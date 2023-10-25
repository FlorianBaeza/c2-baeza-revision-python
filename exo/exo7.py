def words_in_file(file_read: str):
    '''
    Ecrit dans le fichier résultat le nombre de mots présents dans le fichier txt.
    '''

    words_number = 0
    with open(file_read, 'r') as f:
        for line in f:
            line.strip("\n")
            words = line.split()

            words_number += len(words)

        f.close()

    f2 = open('c2-baeza-result.txt', 'w')
    f2.write(str(words_number))
    f2.close()

words_in_file("exo/txt.txt")