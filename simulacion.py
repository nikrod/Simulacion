import random


def primera(n):
    horas=0
    i=0
    costo=0
    ocio=0
    costov=0
    s=str('N°\tRND\tHORA\tOCIO\tCOSTO   \n')
    archi=open('informe 1 valvula.txt','a')
    archi.write((s))
    
    while (horas<=n): 
        costo=costo+30
        ocio=ocio+1
        costov=costov+10
        x=random.randrange(100)
        i=i+1
        if(x<5):
            horas=horas+20
        elif(x<15 and x>=5):
            horas=horas+40
        elif(x<45 and x>=15):
            horas=horas+30
        elif(x<75 and x>=45):
            horas=horas+30
        elif(x<95 and x>=75):
            horas=horas+85
        elif(x<100 and x>=95):
            horas=horas+100
        h=(str(i)+'\t'+str(x)+'\t'+str(horas)+'\t'+str(ocio)+'\t'+str(costo)+'\n\n')
        archi.write(h)    
    p=('finalmente el costo total, considerando el costo de las valvulas es: $US '+ str(costov+costo)+'\n')
    archi.write(p)
    k=('Se registraron '+str(ocio)+' horas de ocio de la maquina correspondiente')
    archi.write(k)
    archi.close()


def tres(n):
    horas=0
    i=0
    costo=0
    ocio=0
    costov=0
    s=str('N\tRND\tHORA\tOCIO\tCOSTO   \n')
    archi=open('informe 3 valvulas.txt','a')
    archi.write((s))
    
    while (horas<=n): 
        costo=costo+30
        ocio=ocio+1
        costov=costov+30
        x=random.randrange(100)
        i=i+1
        if(x<10):
            horas=horas+170
        elif(x<30 and x>=10):
            horas=horas+175
        elif(x<70 and x>=30):
            horas=horas+180
        elif(x<90 and x>=70):
            horas=horas+185
        elif(x<100 and x>=90):
            horas=horas+190
            
        h=(str(i)+'\t'+str(x)+'\t'+str(horas)+'\t'+str(ocio)+'\t'+str(costo)+'\n\n')
        archi.write(h)
        
    p=('Finalmente el costo total, considerando el costo de las valvulas es: $US '+ str(costov+costo)+'\n')
    archi.write(p)
    k=('Se registraron '+str(ocio)+' horas de ocio de la maquina correspondiente')
    archi.write(k)
    archi.close()

print(u' A continuacion resolveremos el siguiente problema:\n')
print(u'La empresa ACME LTDA tiene una máquina con tres válvulas de vacíoidénticas, que son la causa principal de las descomposturas que ocasionan tiempo ocioso, las válvulas se cambian cada vez que fallan.\n')
print (u'Se ha propuesto que se cambien todas las válvulas cada vez que falla una, a fin de reducir la frecuencia con que tie que detenerse el equipo.\n')
print(u'En la actualidad, la máquina tiene que pararse durante una hora para cambiar una válvula o durante dos horas y cuarto para cambiar las tres válvulas.\n')
print(u'El costo asociado al tiempo ocioso de la máquina asciende a US$ 30 por hora, debido a la producción perdida. El costo de cada válvula asciende a US$ 10. Además, se cuenta con la siguiente información:\n')


      
l=1
while (l!=0):
    print('Seleccione una opcion:\n')
    print('1-Resolver el problema con una sola valvula\n')
    print('2-Resolver el problema con tres valvulas\n')
    print('0-salir\n')
    op=input('ingrese opcion:\n')
    if (op==1):
        n=input('Ingrese numero de horas\n')
        print('Se generara un archivo txt, dentro de su carpeta, deacuerdo a la opcion correspondiente\n')
        print('---------------------------------------------------------------------------------------------------------------------------------------')
        primera(n)
    elif(op==2):
        n=input('Ingrese numero de horas\n')
        print('Se generara un archivo txt, dentro de su carpeta, deacuerdo a la opcion correspondiente\n')
        print('---------------------------------------------------------------------------------------------------------------------------------------')
        tres(n)
    elif(op==0):
        l=0
    elif(op!=1 and op!=2 and op!=0):
        print 'opcion incorrecta'
        
        

raw_input('gracias Atte. Nicolas Rodriguez Ormazabal')
