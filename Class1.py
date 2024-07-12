#Try e except in a list 

#Erros
#Excelente para testes
#Não realiza o 'stop' no programa 
#Mensagens customizadas quando encontra o erro

try:
    letters = ['a', 'b', 'c']
    print(letters[2])
except IndexError:
    print('Index does not exist')