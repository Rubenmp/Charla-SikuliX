click("1504457636494.png")
wait("1504457677792.png")
type("Calculator" + Key.ENTER)
wait("1504457960692.png")
click("1504458191596.png")
operaciones = ["Sumar", "Restar", "Multiplicar", "Dividir"]
opcion = select("Vamos a: ", options=operaciones)
if (opcion == operaciones[0]):
    click(Pattern("1506101191694.png").similar(0.74).targetOffset(-2,54))
elif (opcion == operaciones[1]):
    click(Pattern("1506101191694.png").similar(0.74).targetOffset(-1,19))
elif (opcion == operaciones[2]):
    click(Pattern("1506101191694.png").similar(0.74).targetOffset(0,-17))
else:
    click(Pattern("1506101191694.png").similar(0.74).targetOffset(-1,-50))


click("1506101327186.png")


click("1504458609595.png")

sleep(5)

