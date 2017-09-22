seguir = True

def parar(evento):
    global seguir
    seguir = False

# Pulsar Ctrl+F1 para salir del programa correctamente
Env.addHotkey(Key.F1, KeyModifier.CTRL, parar)

click("1504457636494.png")
wait("1504457677792.png")
type("Calculator"+Key.ENTER)
wait("1504459379659.png")
click(Pattern("1504459379659.png").targetOffset(-135,19))

for item in range(10):
    if (seguir):
        click(Pattern("1504459379659.png").targetOffset(27,54))
        click(Pattern("1504459379659.png").targetOffset(-135,19))

    
click(Pattern("1504459379659.png").targetOffset(108,54))


sleep(5)
