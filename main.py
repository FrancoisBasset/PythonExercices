import basic1.functions

i = 1

while True:
    try:
        exo = getattr(basic1.functions, 'exo' + str(i))
        print("\nExo" + str(i) + " :")
        exo()
        i += 1
    except AttributeError:
        break
