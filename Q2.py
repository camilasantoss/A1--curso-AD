#Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. 
# A seguir calcule a duração do jogo.

hrs_inicial=int(input("Digite a hora inicial do jogo:"))
min_inicial=int(input("Digite a minutos inicial do jogo:"))

hrs_final=int(input("Digite a hora final do jogo:"))
min_final=int(input("Digite a minutos final do jogo:"))

total_hrs= hrs_final - hrs_inicial

if(total_hrs < 0):
    total_hrs = 24 + total_hrs

total_min= min_final - min_inicial

if(total_min < 0):
    total_min = 60 + total_min
    total_hrs = total_hrs - 1   

if(min_final == min_inicial and hrs_final == hrs_inicial):
    print("O jogo durou: 24 horas") 
else:
    print("O jogo durou:" , total_hrs ," hora(s) e", total_min, "minuto(s)") 
