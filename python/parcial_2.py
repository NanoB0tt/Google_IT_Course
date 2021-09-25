
dic={} 
fin="listo" 
while True: 
    alumno=input('Ingrese el nombre del alumno(para finalizar ingrese listo): ') 
    if alumno.lower()==fin: 
        break 
    else: 
        notas=[] 
        for i in range(3): 
            while True: 
                n=float(input('Ingrese las notas del alumno {}: '.format(alumno))) 
                if n>=1 and n<=10: 
                    notas.append(n) 
                    break 
                else: 
                    print('Las notas van de [1,10]') 
        dic[alumno]=notas 
print(dic) 
for i in dic: 
    m=max(dic[i]) 
    n=min(dic[i]) 
    c=i 
    print('El alumno {} su mayor nota es {} y la menor nota con  {}'.format(c,m,n)) 
for i in dic: 
    a=i 
    acum=0 
    for j in dic[i]: 
        acum+=j 
    prom=acum/3 
    print('El promedio del alumno {} es {}'.format(a,prom))