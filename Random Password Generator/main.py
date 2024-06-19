import random
import string

if __name__=="__main__":
    u=string.ascii_uppercase
    #print(u)
    l=string.ascii_lowercase
    #print(l)
    d=string.digits
    #print(d)
    p=string.punctuation
    #print(p)

    while True :
        print("Enter Password Length : ")
        len = input()
        try :
            len=int(len)
        except:
            print("Please Enter Length in Digits Only")
            continue
        if len<6:
            print("Length Must be greater than six")
            continue
        break

    c = []
    c.extend(list(u))
    c.extend(list(l))
    c.extend(list(d))
    c.extend(list(p))
    # print(c)
    random.shuffle(c)
    # print(c)
    print("Random Password is :")
    # print("".join(random.sample(c,len)))
    print("".join(c[0:len]))