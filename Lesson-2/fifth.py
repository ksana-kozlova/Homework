# Написать программу, которая принимает от пользователя имя и пароль. Сравнивает пароль с заданным в коде.
#	В случае совпадения печатает в консоль "Password for user: <Имя пользователя> is correct"
#	Если пароль не совпадает, то печатает в консоль
#	"Password for user: <Имя пользователя> is incorrect"
#	"Please try again..."
#	И снова запрашивает пароль (не завершается).


def fifth(dictionary):
    flag = 1
    name = input()
    while (flag):
        password = input()
        if password == dictionary[name]:
            print("Password for user:", name, " is correct ")
            flag = 0
        else:
            print("Password for user:", name, "is incorrect")
            print("Please try again...")


name_pass = {"Max": "M1234", "Alex": "A1234", "Mikle": "M2345", "Ann": "A2345"}
fifth(name_pass)
