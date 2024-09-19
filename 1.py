def main():
    import numpy
    print("numpy imported, v", numpy.__version__)

    print("Hello")
    name = input("enter your name: ")

    print(f"hey, {name}")
    input(f"press enter to begin task 1, {name}")

    while True:
        a,b = input("Введіть цілі числа (integer) a та b (через пробіл): ").split()

        try:
            a = int(a)
            b = int(b)
            print(f"a = {a}\n"
                  f"b = {b}\n"
                  f"cyma: {a+b}\n"
                  f"piz: {a-b}\n"
                  f"dob: {a*b}\n"
                  f"dil: {a/b}\n"
                  f"zal: {a%b}\n"
                  f"ln a: {numpy.log10(a)}\n"
                  f"power a to b: {a**b}\n"
                  f"sqareroot a: {numpy.sqrt(a)}")
            break
        except ValueError:
            print("я сказав введи цілі числа")

    print("a id is: ", id(a))
    print("b id is: ", id(b))

    input("press enter to change values of a and b")

    c = int(a)
    d = int(b)
    a = int(d)
    b = int(c)

    print(f"a = {a},b = {b}")
    print(f"a id is: {id(a)}\n"
          f"b id is: {id(b)}\n")

    input("stage 1 completed, press enter to begin stage 2")


    while True:
        c = input("Введіть ціле тризначне число: ")

        try:
           c = int(c)
           g = c**3
           mb = g//1024
           gb = mb//1024
           r = str(c)
           m = r[1:3]+r[0]
           hui = int(r[1]+r[0]+r[2])
           im0, im1, im2 = int(m[0]), int(m[1]), int(m[2])

           if 100 <= c <= 999:
               print(f"Number: {c}\n"
                     f"Number^3: {g}\n"
                     f"kB: {g}kB\n"
                     f"mB: {mb}mB\n"
                     f"gB: {gb}gB\n")
               print(f"left to right: {m}\n"
                     f"sum: {im0+im1+im2}\n"
                     f"multiply: {im0+im1+im2}\n"
                     f"dozens to hund: {hui}")
               break
           else:
               print("needs to be 3 digits")

        except ValueError:
            print("needs to be an integer")


    print(f"okay {name} good job so far")
    input("press enter to begin stage 3")



    while True:
        tempc = input(f"Введіть температуру в Цельс: ")

        try:
            tempc = float(tempc)
            tempk = float(tempc+273.15)
            tempf = float((tempc*1.8)+32)
            print(f"Temp in C: {tempc}\n"
                  f"Temp in K: {tempk}\n"
                  f"Temp in F: {tempf}\n")
            break
        except ValueError:
            print("needs to be int or float NUMBER")

    input("last stage 4 press enter to begin")



    while True:
        st41, st42, st43 = input("Введіть 3 цілі числа (через пробіл): ").split()

        try:
            st41 = int(st41)
            st42 = int(st42)
            st43 = int(st43)
            print(f"max: {max(st41, st42, st43)}\n"
                  f"min: {min(st41, st42, st43)}")
            break


        except ValueError:
            print("need to be intergers")



    print(f"gg wp {name}\n")
    input(f"press ENTER to exit")

main()

