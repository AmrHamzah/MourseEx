Morsedictonary =  {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',
    'e': '.',     'f': '..-.',  'g': '--.',   'h': '....',
    'i': '..',    'j': '.---',  'k': '-.-',   'l': '.-..',
    'm': '--',    'n': '-.',    'o': '---',   'p': '.--.',
    'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',
    'y': '-.--',  'z': '--..', " ": " ","  ":"  ", "   ":"   "
}

def translatefunc(userinput):
    result=[]
    for x in userinput:
       result.append(Morsedictonary[x])
    return result
Runing = 1 
while Runing : 
    print("------------------")
    userinput = str(input("enter the value that u r goin to translate q to leave ")).lower()
    if userinput == "q":
        Runing = 0
    elif all(c.isalpha() or c == " " for c in userinput):
        value = translatefunc(userinput)
        for val in value:
            print(val, end=" ")
        print()
    else:
        print("Please inter an valid value")
