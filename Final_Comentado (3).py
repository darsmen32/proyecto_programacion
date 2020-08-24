# SECCIÓN DE LABORATORIO: 10110-1-G-2268
# PROFESOR DE LABORATORIO: PATRICIA RIQUELME
# PROFESOR DE TEORÍA: GABRIEL GODOY
# INTEGRANTES
# 1.
# NOMBRE: RODRIGO LARENAS
# RUT: 20.590.593-6
# CARRERA: Ingeniería Civil INFORMÁTICA
# 2.
# NOMBRE: DIEGO RIQUELME
# RUT: 20.595.397-3
# CARRERA: Ingeniería CIVIL INFORMÁTICA
# 3.
# NOMBRE: JOSÉ SANTIS
# RUT: 19.985.256-6
# CARRERA: Ingeniería de Ejecución Eléctrica

###DESCRIPCIÓN DEL PROGRAMA
#IMPORTACIONES
#Importamos la funcion sleep del modulo time para dar tiempos al usuario de que lea y la funcion randint del modulo random para la aleatoriedad de las acciones y la toma de desiciones
from time import sleep
from random import randint
#DEFINICION DE CONSTANTES
#Se definen como listas cada uno de los personajes del juego , los seleccionables y la computadora,cada posicion indica una distinta caracteristica de los personajes
#con el mismo orden que se indica adelante
#posicione
#0=vida ,1=velocidad ,2=ataque,3=defensa,4=umbralhechizo ,5=probabilidadhechizoataque
#6=probhechizodefensa ,7=probhechizocuracion ,8=dañominimo,9=dañomaximo,10=dañohechizomin, 11=dañohechizomax
fighter=[12,3,5,14,20,0,0,0,2,8,0,0]
wizard=[6,2,2,12,10,20,40,0,1,4,4,12]
cleric=[8,2,4,12,12,0,20,40,1,6,0,0]
#ENEMIGOS CPU
kobold=[4,2,2,12,20,0,0,4,1,6,0,0]
goblin=[6,4,1,12,0,0,0,0,1,4,0,0]
guerreroOrco=[12,2,5,14,0,0,0,0,1,8,0,0]
#se crea una lista con las listas de los enemigos para poder hacer una seleccion random mas adelante con las posiciones de esta lista
listaEnemigos=[kobold,goblin,guerreroOrco]
nombresEnemigos=["kobold","goblin","guerrero orco"]

### se definen los prints que se utilizarán más adelante
def menu():
    print(
        """
              ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████    ▄█   ▄█▄    ▄████████ ████████▄
             ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   ███ ▄███▀   ███    ███ ███   ▀███
             ███   ███   ███   ███    ███   ███    █▀    ███▐██▀     ███    ███ ███    ███
             ███   ███   ███   ███    ███   ███         ▄█████▀     ▄███▄▄▄▄██▀ ███    ███
             ███   ███   ███ ▀███████████ ▀███████████ ▀▀█████▄    ▀▀███▀▀▀▀▀   ███    ███
             ███   ███   ███   ███    ███          ███   ███▐██▄   ▀███████████ ███    ███
             ███   ███   ███   ███    ███    ▄█    ███   ███ ▀███▄   ███    ███ ███   ▄███
              ▀█   ███   █▀    ███    █▀   ▄████████▀    ███   ▀█▀   ███    ███ ████████▀
                                                         ▀           ███    ███

            1)Comenzar
            2)Salir



            """

    )
def printPersonaje():
    print(
        """
           __  ___   _   _ _ __    _ __   ___ _ __ ___  ___  _ __   __ _ _   ___  _ __   __ _ (_) ___
         / _ \/ __|/ __/ _ \ / _` |/ _ \ | | | | '_ \  | '_ \ / _ \ '__/ __|/ _ \| '_ \ / _` || |/ _ |
        |  __/\__ \ (_| (_) | (_| |  __/ | |_| | | | | | |_) |  __/ |  \__ \ (_) | | | | (_| || |  __/
         \___||___/\___\___/ \__, |\___|  \__,_|_| |_| | .__/ \___|_|  |___/\___/|_| |_|\__,_|/ |\___|
    
        |-------------------------------------------------------------------------|
        |-------FIGHTER------ | ---------WIZARD---------|-------CLERIC----------- |
        |    ___________      |    ___________      _   |    ___________      _   |
        |   |  __  __  |      |   |  _____  __|    / \  |   |  __  __  |     / \  |
        |   |   |   |  |      |   | /     \/  |   /   \ |   |   |   |  |    /   \ | 
        |   |      -   |      |   |/    ___   |   \   / |   |----------|    \   / |
        |   |----------|      |   |-----------|    \ /  |    \--------/      \ /  |
        |         /|\         |         /|\        /    |    |    /|\        /    |
        |        / | \        |        / | \      /     |    |   / | \      /     |
        |       /  |  \       |       /  |  \ ___/      |    |  /  |  \    /      |        
        |      /   |   \      |      /   |      /       |   _|_/   |   \  /       |    
        |     /    |    \     |     /    |     /        |    |/    |    \/        |
        |   (   )  |   (   )  |          |    /         |          |    /         |       
        |  OPCION:fighter     |    OPCION: wizard       |    OPCION: cleric       |           
        --------------------------------------------------------------------------
        | Vida:         12    | Vida:      6            | Vida:      8
        | Velocidad:    3     | Velocidad: 2            | Velocidad: 2
        | Ataque:       5     | Ataque:    2            | Ataque:    4
        | Defensa:      14    | Defensa:   2            | Defensa:   12
        | Maná:         20    | Maná:      10           | Maná:      12
    
    
                    """
    )
def GuerreroOrco():
    print("""
                        ██        ██████     ██                    
                        ██████████     ████████                    
                        █                ██    █                   
              ██████    ██    ▄▄      ▄        █        ██████     
         ██████     ██   ███    █▀  █▀   ███████       ██     █    
      ███           ██     █    █   █     ██           ██    ███   
    ██            ███      █               █            █      ██  
    █       ██████         █       █▀▀█    █             ███     ██
    █       ██        ███████              ████             ██    █
     █        ████████                        ██████         █    █
     █                                              ██████████    █
      ██               ███████          █████                    ██
       ██         ██████                    ████              ████ 
        ██████████              ▄               ██████████████     
              ██       ▀█▄    ▄█     ▀█▄▄▄▄█      ██               
              █            ▀▀▀                     ██              
             █                                      ██             
             █                                       █             
             █                                       █             
             █                    █                  █             
              █                   █                  █             
              ██                  █                 █              
                ██                                 ██              
                  ██                             ██                
                    ██                         ██                  
                      █                       █                    

    """)
def Goblin():
    print("""

                         ████
          ███████████████  ██████     
          ████ ███   \  /    █  ██
             ██      █  █    █   ██
            ███████          ███  █
            █     █          █  ███
            █ █ █ █          █
            ███████          █     ▐███▄█  
         ▄▄▄      █         ██     ▐    █
      ▄██████     ██       ██      ▐▄▄▄█
    █████▀  ▀    ███       ██        ▌
    ██▀▐█▌    ███          █████   █████
    █▌  ██   ██ █          ███  ████   █
    █▌  ▐█▌███  █         █   ███ ███  █
    ▀    ███    ████████████    ███  ███
         █   ███          ██      █████
         █████ █           █
               █ █  █  ██  █
              ██████████████
              █     ███  ██ █
             ██     █ █     █
            █     █  ██    █
         ██████    █   ███  ██
         ███  ██ ███     ████████
           █████████     ████████


    """)

def Kobold():
    print("""
                 ██████                           
              ▄▄██ \  ████▀█▄                     
           ▐▀▀  ██ █  /  ██  ▀▄                   
    █       ▀█▄ █  ▄  █   █▄▄▄██                  
    ██          ██▀       █                    ███
     █       ▄████▄▄▄▌    █                   ██  
     ██           ███   ██                   ██   
      ██            █████████               ██    
       ██  ██    ███   ██   ██████     ██ ██      
         ███   ██       ██       ███    ███       
        ███  ██          ██         ███ ███       
       ██ ████            █           ██   █      
           ██              █          █           
            █              █                      
                          ███                     
                        ███ ██                    
                     ███      ██                  
                     █         ██                 
                    █           █                 
                   ██           ██                
                   █             █                
             ███████             ██████         
             """)
def MuerteOrco():
    print("""
                   ▄▄        ██████                                
          ▄▄▄     ▀  ▄      ███   █                                
        ██████   ▐  ▄ ▌     ██    █   ¡Nunca tuviste ninguna oportunidad!                             
       ▐█▀  ██▌   ▀██▀        ████                                 
       ▐█    █▌    ██      ▀▀█▄▄  ▄█                               
       ▐███▄██▌  ████          ███                                 
       ▄███████████▀       ▄█▀▀   █▄                               
       █████████▀▀                                                 
      ██ █▌                    █                                   
    ▄███ █▌                    █                                   
    ██▀ ▐█▌     ████             ▌                                 
    █   ▐█     █████▌          ▄▀                                  
    █   ▐█    ███  ██                                              
    █   ▐█  ███▀    ██                                             
    █▀▌ ▐█▄███      ██▌                                            
      ▐ ▐███▀        ████████████████████                          
    ▄▄█ ███         ███                 █████                      
        ██        ██                        ████                   
        ██▌      ███     ██   █   █            ██                  
        ██▌     █ ████   ██  ██   █    █   █    ██                 
        ██▌    █  █  ██ ███ ███   ██  ██   █     ██                
        ▐█▌    █  ██  ███ ███ █   ██████████      ██               
        ▐█▌█████   █           █  █        █       ██████          
       █████   █   █           █  █        █        █   ██████████ 
    ████▐█     ██  ██          █  █        █       ██            ██
    ██████▄▄▄▄▄▄▄█▄▄█▄▄▄▄▄▄▄▄▄█▄▄▄█▄▄▄▄▄▄▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄▄▄▄▄▄▄▄█                   
                    """)
def MuerteGoblin():
    print("""
                                                              
                                                              
                                                              
                                                              
       ██████      Me quede con tu vela                       
      █     ██         Easy                       ▄           
      █       █                           ▄▄▄█▄▄█▀            
      ██      █                                               
       ███ ███                                                
         █████                           █                    
          ███████      ████             ███                   
         ██ ██  █████████  █            █ █                   
        ██   █         █████            █ ██                  
  ███  ██    ██                       ███████                 
 ██ ███       █                     ██      ██                
  ████        █                   ██         ██               
              █                 ██            ██              
             ██                ██              █              
             ███              █         █       █             
            ██ █             ██      ███████    █             
           ██  ██            █          █       █             
           █    █            █          █        █            
          █     █           █           █        █            
         ██     ██          █           █        █            
        ██       █          █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █            
       ██        █         ▄████████████████████▄█▄▄          
       █         █       ██████▀              ▀██████         
    """)
def MuerteKobold():
    print("""
                                                              
                                                              
                                                              
                                                              
 Que bien, ¡Dagas Nuevas!                                     
           De seguro se venderan muy bien en ebay             
                                                              
                                ▄▄▄   █▀▀▀▀▀▀▀▀▀▀▀█▄▄         
           ▄                   ▐████   ▀▄            ▀▄       
          █ ▀▀▀█                 ██      ▀█▄           ▀█     
         ▐      ▌             ▀▀▀█▄ ▄█      ▀▀▄▄         █    
          █     ▌               ▄█▀▀█▄          █▄        █   
   ▌       ▀███▀                                  ▀█▄      █  
   █        ▐                         ▐▄             █▄     █ 
    █      ██▄                         ▐               █▄   ▐ 
     █▄  ▄█ ▌ █▄                ██▄                      █▄ █ 
    ▀▌ ▄█  ▐    █▄              ▌▄███▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██  
     █▀    ▐▄    ██▄█▄▄▄▄▄▄▄    ▌█ ▌                       ▐  
           █▌       █          █ ▐▄▌                       ▐  
           ▌▌                  █  █▌                       ▐  
          ▐ ▌                     █▌                        ▌ 
          ▌ █                      ▌                        ▌ 
         █  ▐                      ▌                        ▌ 
        ▐    █                     ▌                        █ 
 ▄▄▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█                        ▐ 
        ▌      █                   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        """)

#se define una funcion para  la seleccion del personaje ya que el usuario va a entregar el nombre de su personaje en formato string y dependiendo de eso como entrada de la funcion
#se selecciona la lista del personaje seleccionado por este
def seleccionpersonaje(personajeUsuario):
    if personajeUsuario=='fighter' :
        print('A seleccionado a fighter')

        personaje=fighter
    if personajeUsuario=='wizard':
        print('A seleccionado a wizard')
        personaje=wizard
    if personajeUsuario=='cleric' :
        print('A seleccionado a cleric')
        personaje=cleric
#tiene como salida o retorno la lista personaje que va ser seleccionada dependiendo del personaje elegido y tendra sus caracteristicas
#para luego ser utilizada en la funcion de accion del personaje
    return personaje
#se define la funcion de seleccion del personaje para la cpu y se pide como entrada el string que ingresa el usuario para la seleccion del personaje
def personajeCPU(personajeUsuario):
#se selecciona el enemigo del personaje de manera aleatoria entre las posiciones de la lista de enemigos anteriormente definida 

    enemigo=listaEnemigos[aleatorio]
    if enemigo==kobold:
        print('Su enemigo sera kobold')
        Kobold()
    if enemigo==goblin:
        print('Su enemigo sera goblin')
        Goblin()
    if enemigo==guerreroOrco:
        print('Su enemigo sera Guerrero orco')
        GuerreroOrco()
#tiene como salida o retorno la lista con caracteristicas del enemigo las cuales fueron definidas al inicio
#luego se utilizara como entrada en la funcio de accion de personaje
    return enemigo
    
#se define la funcion de accion para el personaje seleccionado por el usuario tiene como entrada 2 listas que son las caracteristicas del personaje y las de su enemigo
#tambien tiene como entrada las vidas iniciales de cada personaje para no exeder esta cuando se realiza el hechizo de curacion 
def accion(personaje,enemigo,vidaInicialPersonaje,vidaInicialEnemigo):
#se definen las probabilidades de hechizo,accion,critico y se definen strings vacios para luego ser utilizados
    #la probabilidad de hechizo es un numero random que debe superar al humbral de hechizo del personaje para que este pueda lanzar su hechizo si no lo logra este no puede lanzar el hechizo    
    probHechizo=randint(1,20)
    #la probabilidad de accion es un numero entre 0 y 100 que define que accion tomara el personaje dependiendo de entre que intervalos se encuentre este numero
    probAccion=randint(0,100)
    #la probabilidad de critico sirve como esta lo dice para saber si es que el personaje realizo un ataque critico o falló en el ataque o hechizo si este numero random es 1 falla, si es 20 acierta un critico 
    probCRIT=randint(1,20)
    accionpersonaje=''
    hechizoOataque=''
#se toman las decisiones sobre que accion debe tomar el personaje dependiendo del numero obtenido anteriormente de manera aleatorea en la variable probAccion
#si el numero es menor a la probabilidad de hechizo de ataque del personaje este va a realizar un hechizo de ataque 
    if probAccion<personaje[5]:
        #la variable hechizoOataque sirve para verificar mas adelante como ahi lo dice si la accion fue un hechizo o un ataque basico
        hechizoOataque='hechizo'
        #la accion del personaje se utiliza mas adelante para tomar el camino de accion y hacer los calculos 
        accionpersonaje='hechizoAtaque'
#si el numero es mayor a la probabilidad de hechizo de ataque y menor a la de hechizo de defensa el personaje realiza un hechizo de defensa
    if probAccion>personaje[5] and probAccion<personaje[6]:
        hechizoOataque='hechizo'
        accionpersonaje='hechizoDefensa'
#si el numero es mayor a la prob. de ataque y la de defensa pero al mismo tiempo es menor a la de curacion el personaje realiza un hechizo de curacion 
    if probAccion>personaje[5] and probAccion>personaje[6] and probAccion<personaje[7]:
        hechizoOataque='hechizo'
        accionpersonaje='hechizoCuracion'
#de otro modo si el numero es mayor a todas las probabilidades de hechizo el personaje realiza un ataque basico 
    if probAccion>personaje[5] and probAccion>personaje[6] and probAccion>personaje[7]:
        hechizoOataque='ataque'
        accionpersonaje='Ataque basico'   
#se verifica si el humbral de hechizo es menor al numero obtenido en la probabilidad de realizar el hechizo , si es mayor el numero obtenido , se utiliza la desicion de accion del personaje     
    if personaje[4]<probHechizo and hechizoOataque=='hechizo': 
    #HECHIZO DE ATAQUE
        #si la accion del personaje fue un hechizo de ataque y se logro realizar el hechizo , se entrega por pantalla que lo hizo 
        if accionpersonaje=='hechizoAtaque':
            print('Su personaje a realizado un hechizo de ataque')
            #se genera el daño del hechizo en un numero random entre el daño minimo y el maximo de hechizo
            dañoHataque=randint(personaje[10],personaje[11])
            #como para lograr hacer daño al enemigo necesitamos sumar el daño de ataque a un numero aleatorio entre 1 y 20 si este es mayor a la defensa del enemigo se logra hacer daño de lo contrario no se puede superar la defensa
            #como la probabilidad de critico tambien es un numero aleatorio del 1 al 20 utilizamos ese mismo para hacer este calculo
            if probCRIT+dañoHataque>=enemigo[3]:
                #si la probabilidad de critico fue el numero 20 , el personaje realiza un golpe critico y multiplica el daño de su hechizo por 1.5 y se imprime por pantalla que se logro un golpe critico
                if probCRIT==20:
                    dañoHataque=dañoHataque*1.5
                    print('a realizado un golpe critico')
                #si la probabilidad de critico fue el numero 1 , el personaje falla en el lanzamiento del hechizo y se autoinflinge un daño por la mitad de su vida actual y se muestra por pantalla que fallo en el lanzamiento del hechizo
                if probCRIT==1:
                    personaje[0]=personaje[0]*0.5
                    print('A fallado y se a autoinflingido daño por la mitad de su vida ')
                #si la probabilidad de critico es distinto a 1 se imprime por pantalla el daño que realizo y se quitan los puntos de vida al enemigo 
                if probCRIT!=1:
                    print('por ' ,dañoHataque ,' puntos de vida al enemigo')
                    enemigo[0]=enemigo[0]-dañoHataque
            #si el daño obtenido sumado al numero aleatorio del 1 al 20 no fue mayor que la defensa del enemigo no se logra superar la defensa por lo tanto el daño no tiene efecto
            #por lo tanto se muestra por pantalla que no se logró superar la defensa 
            else:
                print('El daño realizado no es suficiente para superar la defensa del enemigo')
    #HECHIZO DE DEFENSA
        #si la accion del personaje fue hechizo de defensa se entrega por pantalla que realizo este hechizo
        #y se define el aumento de la defensa basico 
        if accionpersonaje=='hechizoDefensa':
            print('Su personaje a realizado un hechizo de defensa')
            aumentoDef=1
            #si el el critico fue 20 se etrega por pantalla que lo fue, y el aumento de defensa ahora es 2 
            if probCRIT==20:
                print('Su personaje a logrado un critico')
                aumentoDef=2
            #si el hechizo falla al ser lanzado se aumenta la defensa actual del enemigo en 1 y el aumento de defensa se vuelve 0 
            if probCRIT==1:
                print('Su personaje a fallado al lanzar el hechizo y a aumentado la defensa del enemigo en 1 ')
                enemigo[3]=enemigo[3]+1
                aumentoDef=0
            #se muestra por pantalla los puntos en los que a aumentado la defensa y luego se suman a la defensa del personaje
            print('A aumentado su defensa en ',aumentoDef,' puntos')
            personaje[3]=personaje[3]+aumentoDef
    #HECHIZO CURACION
        #si la accion del personaje fue hechizo de curacion se muestra por pantalla y se calcula el aumento de vida en un numero aleatorio entre 1 y 8 
        if accionpersonaje=='hechizoCuracion':
            print('Su personaje a realizado un hechizo de curacion')
            aumentoVida=randint(1,8)
            #si el critico fue exitoso el aumento de vida se aumenta en 4
            if probCRIT==20:
                print('Su personaje a realizado un critico y suma 4 puntos mas a su curacion')
                aumentoVida=aumentoVida+4
            #si el hechizo falla se aumenta la vida del enemigo en 4 puntos 
            if probCRIT==1:
                print('Su personaje a fallado el hechizo de curacion y a curado a su oponente en 4 puntos')
                #si la suma en tre la vida actual del enemigo y 4  es mayor a la vida original del enemigo entonces queda con el maximo de vida (su vida original)
                if enemigo[0]+4>vidaInicialEnemigo:
                    enemigo[0]=vidaInicialEnemigo
                #de otro modo se le suma 4 a la vida actual del enemigo y el aumento de vida del personaje se vuelve 0
                else:
                    enemigo[0]=enemigo[0]+4
                aumentoVida=0
            #si la vida actual del personaje mas el aumento de vida es mayor a la vida del personaje solo se aumenta hasta que vuelve a tener su vida inicial
            if personaje[0]+aumentoVida>vidaInicialPersonaje:
                print('Su personaje tiene su vida al maximo')
                personaje[0]=vidaInicialPersonje
            #si la suma entre la vida actual y el aumento de vida es menor a la vida inicial , se suma el aumento de vida por completo y se muestra por pantalla los puntos aumentados y la vida actual                
            if personaje[0]+aumentoVida<=vidaInicialPersonaje:
                personaje[0]=personaje[0]+aumentoVida
                print('Su personaje a recibido una curacion por ',aumentoVida,' puntos ,su vida ahora es de : ',personaje[0] ,'pts')          
    #si la probabilidad de hechizo es menor al umbral de hechizo del personaje , este no logra realizar ningun hechizo 
    if personaje[4]>=probHechizo and hechizoOataque=='hechizo':
        print('El personaje no a logrado realizar el hechizo')
    #ATAQUE BASICO
    #si el la desicion de hechizo o ataque fue ataque el personaje realiza un ataque basico
    if hechizoOataque=='ataque':
        #se calcula un valor aleatorio entre el 1 y el 20 mas el ataque base del personaje para ver si este logra superar la defensa de su enemigo
        #se muestra por pantalla que el personaje realizo un ataque basico
        valorAleatorio=(randint(1,20))+personaje[2]
        print('Su personaje a realizado un ataque basico')
        #si el valor aleatorio supera la defensa del enemigo 
        if valorAleatorio>enemigo[3]:
            #se hace el calculo del daño entre el daño minimo del personaje y su ataque maximo
            dañoAtaque=randint(personaje[8],personaje[9])
            #si el critico fue exitoso se muestra por pantalla que logro el golpe critico y lo que conlleva esto 
            if probCRIT==20:
                print('Su personaje a dado un golpe critico y duplica el daño realizado')
                #al lograr el critico el daño realizado por el personaje se duplica
                dañoAtaque=dañoAtaque*2
            #si el personaje falla en el ataque que es cuando el critico  da 1 ,el personaje se autoinflinge un daño aleatorio entre 1 y 3
            if probCRIT==1:
                dañoFALLO=randint(1,3)
                #se muestra por pantalla que el personaje falló y los puntos de daño que se autoinflingio
                print('Su personaje a fallado en el ataque y se a autoinfligido daño por ',dañoFALLO,' puntos')
                #se restan los puntos a la vida del personaje y el daño de ataque se vuelve 0
                personaje[0]=personaje[0]-dañoFALLO
                dañoAtaque=0
            #muestra por pantalla el daño inflingido al enemigo 
            print('Su personaje a realizado un daño por ',dañoAtaque,' puntos a la vida del enemigo')
            #se actualiza la vida actual del personaje restando a la misma el daño de ataque calculado
            enemigo[0]=enemigo[0]-dañoAtaque
        #si el numero aleatorio mas el ataque basico no logran superar la defensa del enemigo , se muestra por pantalla que no logro hacerlo       
        else:
            print('El ataque no a logrado superar la defensa del enemigo')
    #cada vez que se repite la accion se muestra la vida del personaje actual y la vida de su enemigo 
    print('la vida de el personaje es ' ,personaje[0])
    print('la vida de la cpu es ',enemigo[0])
    #tiene como salida o retorno la vida actual de cada personaje en una lista de largo 2
    return [personaje[0],enemigo[0]]
#es igual a la funcion de accion de personaje pero tiene distintos print para poder diferenciar entre las acciones del personaje y las de la cpu
def accionCPU(personaje,enemigo,vidaInicialPersonaje,vidaInicialEnemigo):
    
    probHechizo=randint(1,20)
    probAccion=randint(0,100)
    probCRIT=randint(1,20)
    accionpersonaje=''
    hechizoOataque=''
    if probAccion<=personaje[5]:
        hechizoOataque='hechizo'
        accionpersonaje='hechizoAtaque'
    if probAccion>personaje[5] and probAccion<=personaje[6]:
        hechizoOataque='hechizo'
        accionpersonaje='hechizoDefensa'
    if probAccion>personaje[5] and probAccion>personaje[6] and probAccion<=personaje[7]:
        hechizoOataque='hechizo'
        accionpersonaje='hechizoCuracion'
    if probAccion>personaje[5] and probAccion>personaje[6] and probAccion>personaje[7]:
        hechizoOataque='ataque'
        accionpersonaje='Ataque basico'   
    
    if personaje[4]<probHechizo and hechizoOataque=='hechizo': 
    #HECHIZO DE ATAQUE
        if accionpersonaje=='hechizoAtaque':
            print('La CPU a realizado un hechizo de ataque')
            dañoHataque=randint(personaje[10],personaje[11])
            if probCRIT+dañoHataque>=enemigo[3]:
                if probCRIT==20:
                    dañoHataque=dañoHataque*1.5
                    print('a realizado un golpe critico')
                if probCRIT==1:
                    personaje[0]=personaje[0]*0.5
                    print('A fallado y se a autoinflingido daño por la mitad de su vida ')
                if probCRIT!=1:
                    print('por ' ,dañoHataque ,' puntos de vida al enemigo')
                    enemigo[0]=enemigo[0]-dañoHataque
            else:
                print('El daño realizado no es suficiente para superar la defensa del enemigo')
    #HECHIZO DE DEFENSA
        if accionpersonaje=='hechizoDefensa':
            print('La CPU a realizado un hechizo de defensa')
            aumentoDef=1
            if probCRIT==20:
                print('Su personaje a logrado un critico')
                aumentoDef=2
            if probCRIT==1:
                print('Su personaje a fallado al lanzar el hechizo y a aumentado la defensa del enemigo en 1 ')
                enemigo[3]=enemigo[3]+1
                aumentoDef=0
            print('A aumentado su defensa en ',aumentoDef,' puntos')
            personaje[3]=personaje[3]+aumentoDef
    #HECHIZO CURACION
        if accionpersonaje=='hechizoCuracion':
            print('La CPU a realizado un hechizo de curacion')
            aumentoVida=randint(1,8)
            if probCRIT==20:
                print('La CPU a realizado un critico y suma 4 puntos mas a su curacion')
                aumentoVida=aumentoVida+4    
            if probCRIT==1:
                print('La CPU a fallado el hechizo de curacion y a curado a su oponente en 4 puntos')
                if enemigo[0]+4>vidaInicialEnemigo:
                    enemigo[0]=vidaInicialEnemigo
                else:
                    enemigo[0]=enemigo[0]+4
                aumentoVida=0
            if personaje[0]+aumentoVida>vidaInicialPersonaje:
                print('La CPU tiene su vida al maximo')
                personaje[0]=vidaInicialPersonje
            if personaje[0]+aumentoVida<=vidaInicialPersonaje:
                personaje[0]=personaje[0]+aumentoVida
                print('La CPU a recibido una curacion por ',aumentoVida,' puntos ,su vida ahora es de : ',personaje[0] ,'pts')          
    if personaje[4]>=probHechizo and hechizoOataque=='hechizo':
        print('El personaje no a logrado realizar el hechizo')
    #ATAQUE BASICO
    if hechizoOataque=='ataque':
        valorAleatorio=(randint(1,20))+personaje[2]
        print('La CPU a realizado un ataque basico')
        if valorAleatorio>enemigo[3]:
            dañoAtaque=randint(personaje[8],personaje[9])
            if probCRIT==20:
                print('La CPU a dado un golpe critico y duplica el daño realizado')
                dañoAtaque=dañoAtaque*2
            if probCRIT==1:
                dañoFALLO=randint(1,3)
                print('La CPU a fallado en el ataque y se a autoinfligido daño por ',dañoFALLO,' puntos')
                personaje[0]=personaje[0]-dañoFALLO
                dañoAtaque=0
            print('La CPU a realizado un daño por ',dañoAtaque,' puntos a la vida del enemigo')
            enemigo[0]=enemigo[0]-dañoAtaque
                
        else:
            print('El ataque no a logrado superar la defensa del enemigo')
    print('la vida de la cpu es ' ,personaje[0])
    print('la vida de el personaje es ',enemigo[0])
    return [personaje[0],enemigo[0]]
#definimos la funcion de gauge para el tiempo que demora la accion del personaje dependiendo de la velocidad de este
#por enede tiene como entrada la velocidad del personaje 
def gauge(velocidad,player):
    i=0
    #el gauge se rellena cuando llega a 10 por lo tanto lo ponemos como limite con un contador que se actualiza dependiendo de su velocidad y se muestra cada un sedundo
    #se mestra cuantos ticks faltan para la accion del personaje 
    while i<10:
        sleep(1)
        i=i+velocidad
        print('faltan :',10-i,' ticks para que',player,'actúe')



#BLOQUE DE PROCESOS
salir=True
while salir==True:
    menu()
    opt=input("ingrese una opción")
    if opt=='1':

        aleatorio = randint(0, 2)
        enemigoPrint = nombresEnemigos[aleatorio]
        #imprimimos a los personajes disponibles
        printPersonaje()
        #se pide como entrada al usuario el personaje que desea seleccionar entre los cuales esta fighter wizard y cleric y el string obtenido se guarda en la variable personaje usuario
        personajeusuario=input('Escriba su personaje : ')

        #verificamos la opcion a través de un while
        while personajeusuario!='fighter' and personajeusuario!='wizard' and personajeusuario!='cleric':
            print("SELECCIONE UN PERSONAJE DE LA LISTA")
            personajeusuario=input('Escriba su personaje : ')

        #se aplica la funcion de seleccion de personaje para obtener la lista con caracteristicas de este y se guardan en la variable personaje
        personaje=seleccionpersonaje(personajeusuario)
        #se aplica la funcion del personaje para la computadora al mismo string de entrada y se guarda la lista del enemigo con sus caracteristicas en su variable
        enemigo=personajeCPU(personajeusuario)



        #se guarda la vida inicial de cada uno de los personajes (el elegido por el usuario y el de la computadora
        vidainicial1=personaje[0]
        vidainicial2=enemigo[0]

        #se definen los prints que se utilizarán para mostrar por consola el avance del usuario

        #se crea un ciclo que se repita mientras la vida de los 2 personajes sea mayor a 0 , es decir mientras ambos esten vivos
        while personaje[0]> 0 and enemigo[0] > 0:
            # se aplica la funcion gauge para el personaje seleccionado con su velocidad
            gauge(personaje[1],personajeusuario)
            #se aplica la funcion de accion al personaje la cual tiene como salida la vida al terminar la accion de el personaje y su enemigo por lo tanto se guardan en una variable
            #para utilizarla en los limites
            accionpersonaje=accion(personaje,enemigo,vidainicial1,vidainicial2)
            #si la primera posicion de la lista que es la vida del personaje seleccionado  es menor o igual a 0 se muestra por pantalla que a ganado la computadora
            if accionpersonaje[0]<=0:
                print('A ganado la cpu mas suerte para la proxima')
                print('GAME OVER (︶︹︶)')
                sleep(1)
                personaje[0]
            #si la segunda posicion de la lista es menor a 0 quiere decir que el personaje seleccionado a ganado  por lo tanto se muestra por pantalla su victoria
            if accionpersonaje[1]<=0:

                    print('Su personaje a ganado felicitaciones ')
                    #dependiendo del enemigo, imprimirá la muerte de cada uno
                    if enemigo==guerreroOrco:
                        MuerteOrco()
                    if enemigo==goblin:
                        MuerteGoblin()
                    if enemigo==kobold:
                        MuerteKobold()

            #se hace una verificacion de las vidas de ambos personajes luego de la accion anterior para saber si continuar el proceso , si ambas son mayores a 0 continua
            if personaje[0]> 0 and enemigo[0] > 0:
                #se dan 5 segundos para leer la consola y lo que sucedio en la aacion y luego se aplica el gauge de la computadora
                sleep(5)
                gauge(enemigo[1],enemigoPrint)
                #se guarda la lista con la vida de los personajes al aplicar la accion de la cpu y se dan 5 segundos mas para leer la accion realizada
                acciondelacpu=accionCPU(enemigo,personaje,vidainicial2,vidainicial1)
                sleep(5)
                #se verifica la vida del la computadora y la del personaje seleccionado
                if acciondelacpu[0]<=0:
                    print('Su personaje a ganado felicitaciones ')
                    #dependiendo del enemigo, imprimirá la muerte de cada uno
                    if enemigo==guerreroOrco:
                        MuerteOrco()
                    if enemigo==goblin:
                        MuerteGoblin()
                    if enemigo==kobold:
                        MuerteKobold()
                if acciondelacpu[1]<=0:
                    print('A ganado la cpu mas suerte para la proxima')
                    print('GAME OVER (︶︹︶)')
                    sleep(1)
            salir=False
    #SALIDA
    if opt=='2':
        print("Hasta la proxima!")
        salir=False
    if opt!='1' and opt!='2':
        print("ingresa una opción correcta")
        sleep(1)

