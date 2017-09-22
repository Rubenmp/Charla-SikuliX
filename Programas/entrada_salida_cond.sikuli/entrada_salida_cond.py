nombre = input("Dime tu nombre")
popup("Hola " + nombre + "!")

click("1504457636494.png")
wait("1504457677792.png")
type("Calculator"+Key.ENTER)
wait("1504459379659.png")
click(Pattern("1504459379659.png").targetOffset(-81,19))

operaciones = ["Sumar", "Restar", "Multiplicar", "Dividir"]
opcion = select("Vamos a: ", options=operaciones)
if (opcion == operaciones[0]):
    click(Pattern("1504459379659.png").targetOffset(21,52))
elif (opcion == operaciones[1]):
    click(Pattern("1504459379659.png").targetOffset(28,19))
elif (opcion == operaciones[2]):
    click(Pattern("1504459379659.png").targetOffset(30,-14))
else:
    click(Pattern("1504459379659.png").targetOffset(27,-51))

click(Pattern("1504459379659.png").targetOffset(-81,19))
click(Pattern("1504459379659.png").targetOffset(108,54))

sleep(5)
