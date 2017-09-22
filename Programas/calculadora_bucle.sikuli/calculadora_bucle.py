import random

def pulsar_numero(numero):
    if (numero == 1):
        click(Pattern("1504459379659.png").targetOffset(-135,19))
    elif (numero == 2):
        click(Pattern("1504459379659.png").targetOffset(-83,17))
    elif (numero == 3):
        click(Pattern("1504459379659.png").targetOffset(-26,18))
    elif (numero == 4):
        click(Pattern("1504459379659.png").targetOffset(-135,-16))
    elif (numero == 5):
        click(Pattern("1504459379659.png").similar(0.75).targetOffset(-80,-15))
    elif (numero == 6):
        click(Pattern("1504459379659.png").targetOffset(-26,-16))
    elif (numero == 7):
        click(Pattern("1504459379659.png").targetOffset(-134,-52))
    elif (numero == 8):
        click(Pattern("1504459379659.png").targetOffset(-82,-53))
    elif (numero == 9):
        click(Pattern("1504459379659.png").targetOffset(-27,-51))    

def pulsar_operacion(op):
    if (op == 1):
        click(Pattern("1504459379659.png").targetOffset(29,53))
    elif (op == 2):
        click(Pattern("1504459379659.png").targetOffset(28,19))
    elif (op == 3):
        click(Pattern("1504459379659.png").targetOffset(27,-15))
    elif (op == 4):
        click(Pattern("1504459379659.png").targetOffset(30,-51))    

def acelerar():
    Settings.MoveMouseDelay = 0 # Tiempo para mover el ratón a la siguiente posición
    Settings.ObserveScanRate = 0.1 # Tiempo entre comprobaciones de pantalla
    Settings.DelayBeforeMouseDown = 0 # Tiempo desde que se coloca el ratón en la posición y pincha



"Empieza el programa:"

click("1504457636494.png")
wait("1504457677792.png")
type("Calculator"+Key.ENTER)
wait("1504459379659.png")    
pulsar_numero(random.randint(1, 9))
acelerar()

for item in range(10):
    pulsar_operacion(random.randint(1, 4)) 
    pulsar_numero(random.randint(1, 9))

    
click(Pattern("1504459379659.png").targetOffset(108,54))


sleep(5)




