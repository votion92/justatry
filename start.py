x = "yes"
y = "no"

print('''Tip:This program includes 
"sha256 encryption"
"base64 encryption"
"base64 decryption"
"QR code"''')

from hashlib import sha256
def encrypt(str):
    sh = sha256()
    sh.update(str.encode())
    return sh.hexdigest()

while True:
    requirement = input('''Do you intend to have a sha256 encryption?
    Please enter "yes" or "no":''')
    if requirement == x:
        CS = input("please enter your character string:")
        if __name__ == "__main__":
            result = encrypt(CS)
            print("code:",result)
    elif requirement == y:
        break
    else:
        print("Error:you can only enter \"yes\" or \"no\"!")

while True:
    requirement2 = input('''Do you intend to have a base64 encryption?
    Please enter \"yes\" or \"no\":''')
    if requirement2 == x:
        CS2 = input("please enter your character string:")

        import base64

        result2 = base64.b64encode(CS2.encode('utf-8'))
        print("code:"+str(result2,'utf-8'))
    elif requirement2 == y:
        break
    else:
        print("Error:you can only enter \"yes\" or \"no\"!")

while True:
    requirement3 = input('''Do you intend to have a base64 decryption?
    Please enter \"yes\" or \"no\":''')
    if requirement3 == x:
        CS3 = input("Please enter your cryptogram:")

        import base64

        try:
            result3 = base64.b64decode(CS3.encode('utf-8'))
            print("str:" + str(result3, 'utf-8'))
        except:
            print("Error:wrong from.")
    elif requirement3 == y:
        break
    else:
        print("Error:you can only enter \"yes\" or \"no\"!")

while True:
    requirement4 = input('''Do you intend to have a QR code?
    Please enter \"yes\" or \"no\":''')
    if requirement4 == x:
        CS4 = input("please enter your character string:")

        import qrcode

        img = qrcode.make(CS4)
        img.show()
    elif requirement4 == y:
        print("End")
        break
    else:
        print("Error:you can only enter \"yes\" or \"no\"!")

