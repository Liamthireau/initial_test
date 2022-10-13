import time

a = ""
name = input("Indiquez votre prénom : ")
getHours = time.strftime('%H', time.localtime())

if 0 < int(getHours) < 17:
    a = str("\nBonjour " + name + ",")
    print(a)
else:
    a = str("\nBonsoir " + name + ",")
    print(a)


def check_palindrome(v):
    reverse = v[::-1]

    if v == reverse:
        return True
    return False


while True:

    var = input("Entrez une valeur : ")

    if check_palindrome(var):
        print("\nBien dit "+name+"!")
        print("### Au revoir ###")
        quit()
    else:
        print("\nCeci n'est pas un palindrome. Veuillez réessayer.")
