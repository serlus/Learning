def checkPalindrome(inputString):
    lista = [b for b in inputString]
    lista.reverse()
    contrario = ''.join(map(str, lista))
    if inputString == contrario:
        print(True)
    else:
        print(False)
   

if __name__ == "__main__":
    checkPalindrome('rata')

    checkPalindrome('asa')
