pasword = "1235"

crypto = {
    "1": "h",
    "2": "9",
    "3": "r",
    "4": "g",
    "5": "o"
}

while True:
    a = input(">>>")
    if a != pasword:
        print("Пароль был введён не верно")
        pasword = "8899"
    else:
        print("Пароль был ввдён верно")
        try:
            with open("test.txt", "r") as file:
                string_for_crypt = file.read()

            string_crypt = ""

            for n in string_for_crypt:
                if n != "\n":
                    string_crypt += crypto[n]

            with open("test.txt", "w") as file:
                file.write(string_crypt)
            print("Файл успешно расшифрован")
        except:
            print("Что-то пошло не так")