def valor(img):
    "Devuelve un string con el texto de la zona seleccionada de img"
    doubleClick(img)
    type("c", KEY_CTRL)
    return(Env.getClipboard())

click("1504457636494.png")
wait("1504457677792.png")
type("Calculator"+Key.ENTER)
wait("1504459379659.png")
click(Pattern("1504459379659.png").targetOffset(-81,19))
click(Pattern("1504459379659.png").targetOffset(21,52))
click(Pattern("1504459379659.png").targetOffset(-81,19))
click(Pattern("1504459379659.png").targetOffset(108,54))


# Sacando resultado de la operación
resultado = valor(Pattern("1504478990115.png").targetOffset(146,-14))


popup("El resultado ha sido " + resultado)
sleep(2)
