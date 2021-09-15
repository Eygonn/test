def lePlusLong(chaine):
    temp = ""
    long = ""
    max = 0
    for n in chaine:
        if n != " ":
            temp = temp + n

        elif n == " ":
            if len(temp) > max:
                max = len(temp)
                long = temp 
                temp = ""  

               
    return long, max


phrase = str(input("Votre phrase : "))

phrase = phrase + " "

print(lePlusLong(phrase))