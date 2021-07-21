import pickle


def main():
    end_of_file = False
    input_file = open('mydata.dat', 'rb')

    while not end_of_file:
        try:
            person = pickle.load(input_file)

            display_data(person)
        except EOFError:
            end_of_file = True

    input_file.close()


def display_data(person):
    print('Игорь:', person['Игорь'])


main()
