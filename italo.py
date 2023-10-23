# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.
print("ATENÇÃO! Responda apenas com 'sim' ou nao'.")
alt1 = str(input("Você é idoso? "))
if alt1 == 'sim':
    print("Você tem acesso a fila de prioridade! 👍")
elif alt1 == 'nao':
    alt2 = str(input("Você é gestante? "))
    if alt2 == 'sim':
        print("Você tem acesso a fila de prioridade! 👍")
    elif alt2 == 'nao':
        alt3 = str(input("Você é cadeirante? "))
        if alt3 == 'sim':
            print("Você tem acesso a fila de prioridade! 👍")
        else:
            print("Você não tem acesso a fila de prioridade!!!")
            