import random
import collections
PINTA=["pica","corazon","trebol","diamante"]
VALOR=[1,2,3,4,5,6,7,8,9,10,11,12,13]

manos=[]

def tamano_pinta():
    j=["Par","Doble Par","Trio","Poker","Full House","Color","Escalera","Escalera Color","Escalera_Real"]
    tamano_mano=5
    return j,tamano_mano

def crear_baraja():
    barajas=[]
    for pinta in PINTA:
        for valor in VALOR:
            barajas.append((pinta,valor))
    return barajas


def obtener_mano(barajas, tamano_mano):
    mano= random.sample(barajas,tamano_mano)
    return mano


def can_manos(intentos):
     for _ in range(intentos):
        mano=obtener_mano(barajas,tamano_mano)
        manos.append(mano)

def main(manos):
    
    # Ejecuta todo la probabilidad, y retorna el conteo de  pares, doble_par, trio,poker,full_house,color,escalera,escalera_color,escalera_real

    doble_par= 0
    pares= 0
    trio= 0
    poker= 0
    full_house= 0
    escalera= 0
    color= 0
    escalera_color= 0
    escalera_real= 0

    for mano in manos:
        valores=[]
        pintas=[]
        for carta in mano:
            valores.append(carta[ 1 ])
            pintas.append(carta[ 0 ])
        
        counter= dict(collections.Counter(valores))
        counter_pintas=dict(collections.Counter(pintas))
        minando_escalera=sorted(list(dict(collections.Counter(valores)).keys()))


    
        def escalera_funcion(minando_escalera):
            esc=False
            escr=False

            # Identificando si tenemos escapera
            if len(minando_escalera) == 5:
                    if (abs(minando_escalera[ 0 ] - minando_escalera[4]) == 4): esc=True
                        
                    if (minando_escalera[ 0 ] == 1):
                        if (minando_escalera[ 1 ] == 10) & (abs(minando_escalera[ 1 ] - minando_escalera[ 4 ]) == 3): escr=True
                            
            
            return esc,escr

  
        def color_funcion(counter_pintas):
            # Identificando si hay Color
            cr=False
            if len(counter_pintas) == 1: cr= True
            return cr


        def valor_pareja(counter):
            # Funcion que Clasifica Los Valores par, doble par, Trio, Poker y Full House

            c=False
            dob_par=False
            par=False
            pok=False
            tr=False
            fh=False

            for val in counter.values():
                # Clasificando Poker
                if val == 4: pok=True
                # Clasificando Trio
                if val == 3: tr=True
                # Clasificando Doble Par
                if (val == 2) & (c == True): dob_par= True
                # Clasificando Par
                if (val == 2) & (c == False): par= True; c= True
                # Clasificando Full House
                if (tr == True) & (c == True): fh= True
                   
            return  pok,fh,tr,par, dob_par
        

        # Obtengo todos los valores Contadores en Counter_pares y CLasifico c/u
        counter_pares= valor_pareja(counter)
        

        # CLasificando:
        doble_par= doble_par + counter_pares[ 4 ]
        
        pares= pares + counter_pares[ 3 ]
        
        trio= trio + counter_pares[ 2 ]
        
        full_house= full_house + counter_pares[ 1 ]
        
        poker= poker + counter_pares[ 0 ]


        contador_escaleras= escalera_funcion(minando_escalera)

        escalera= escalera + contador_escaleras[ 0 ] + contador_escaleras[ 1 ]
        
        # # contador Color

        contado_color= color_funcion(counter_pintas)
        color= color + contado_color

        # Indentificando Escalera Real
        if (contador_escaleras[ 1 ] == True) & (contado_color == True): escalera_real+=1; print(f"Aparecio la mano Milagrosa {mano}")
        
        if (contador_escaleras[ 0 ] == True) & (contado_color == True): escalera_color+=1; print(f"Escalera color {mano}")
            
    
    return (pares,      doble_par,      trio,
            poker,      full_house,     color,
            escalera,   escalera_color, escalera_real)
    
if __name__=="__main__":
    
    j,tamano_mano= tamano_pinta()
    intentos=int(input("cuantos numeros de intentos"))
    
    # Creando Las Cartas
    barajas= crear_baraja()
    manos_1= can_manos(intentos)
    
    # Probabilidad:
    probabilidades=main(manos)
    
    for i in range(len(probabilidades)):
        print(f"Probabilidad de {j[i]}: {probabilidades[i]/intentos}")