import time

def Agenda():
    dictionary = {

        "daniel": {
            "name": "Daniel de Souza Alves",
            "age": 19,
            "cell": 19981524545,
            "email": "daniel@gmail.com"
        },

        "bedon": {
            "name": "Igor Bedon de Sousa",
            "age": 19,
            "cell": 19981527845,
            "email": "bedon@gmail.com"
        },

        "favaro": {
            "name": "Vitoria Espindola Favaro",
            "age": 18,
            "cell": 19981525545,
            "email": "favaro@gmail.com"
        },

        "vinicius": {
            "name": "Vinicius Teixeira de Toledo Lira",
            "age": 19,
            "cell": 19981566645,
            "email": "vinicius@gmail.com"
        },

        "davi": {
            "name": "Davi Fernando Lima de Andrade",
            "age": 17,
            "cell": 19981524545,
            "email": "davi@gmail.com"
        }

    }
    return dictionary
def Call():

    list_people = ["Daniel", "Bedon", "Favaro", "Vinicius", "Davi"]
    print("Your contact list:", *list_people)

    while True:
        choice_mode = input("Do you want to Call, Register or Remove someone from the list?")
        match choice_mode.lower():
            case "call":
                while True:
                    try:
                        choice = input("Who you want to call?").lower()
                        dictionary = Agenda()
                        print(dictionary[choice])
                        confirm = input("Call? (yes / no)")
                        match confirm.lower():
                            case "yes":
                                print("Calling")
                                for i in range(5):
                                    print(".", end="")
                                    time.sleep(1)
                                print("\nAlo?")

                            case "no":
                                continue
                        break
                    except:
                        print("Error")
                        continue
            case "register":
                print("Your contact list:", *list_people)
                while True:
                    try:
                        remove = input("Who do want to register in the list?")
                        dictionaty = Agenda()
                        dictionaty.pop(remove)
                        print("Now your list is: ")
                        for keys in dictionaty:
                            print(keys)

                        print("\nYou remove", remove)
                        break
                    except:
                        print("errei")
                        break
                break
            case "remove":
                print("Your contact list:", *list_people)
                while True:
                    try:
                        remove = input("Who do want to remove from the list?")
                        dictionaty = Agenda()
                        dictionaty.pop(remove)
                        print("Now your list is: ")

                        for keys in dictionaty:
                            print(keys)

                        print("\nYou remove", remove)
                        break
                    except:
                        print("errei")
                        break
                break


if __name__ == "__main__":
    Call()