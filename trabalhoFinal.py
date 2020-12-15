# estrutura (class) com os atributos da agenda
class agenda:
  nome=''
  email=''
  diamesnasc=''
  idade=0
#
## função para listar todos os contatos cadastrados
def listaContatos(contatos):
  print('{:20} {:20} {:6} {:5}'.format('Nome','email','Aniv','Idade'))
  for i in range(len(contatos)):
    print('{:20} {:20} {:6} {:5d}'.format(contatos[i].nome,contatos[i].email,contatos[i].diamesnasc,contatos[i].idade))
##
# função para procurar um nome na lista de contatos (retorna a posição do nome)
def procuraContato(nome, contatos):
  for i in range(len(contatos)):
    if contatos[i].nome==nome:
      return i #posição do nome na lista
  return -1 # indica que o nome não foi encontrado
## insere contato
def insereContato(amigo):
  amigo.nome=input('Nome : ')
  amigo.email=input('email: ')
  amigo.diamesnasc=input('Niver: ')
  amigo.idade=int(input('Idade: '))
#
def alterContato(pos,contatos):
  print('Falta Implementar')
#
def excluiContato(pos,contatos):
  print('Falta Implementar')
## função de menu
def menu():
  print('1 - Inserir')
  print('2 - Consultar')
  print('3 - Alterar')
  print('4 - Excluir')
  print('5 - Listar todos')
  print('6 - Sair')
  return int(input(': '))
##
lcontato=[] # armazena a lista de contatos
op=1
while op!=6:
  op=menu()
  if op==1:
    newc=agenda()
    insereContato(newc)
    lcontato.append(newc)
  elif op==2:
    nome=input('Nome para procurar: ')
    pos=procuraContato(nome,lcontato)
    if pos!=-1: # encontrou o nome?
      print('Nome : ',lcontato[pos].nome)
      print('email: ',lcontato[pos].email)
      print('Niver: ',lcontato[pos].diamesnasc)
      print('Idade: ',lcontato[pos].idade)
    else:
      print('Contato não encontrado!')
  elif op==3:
    nome=input('Nome a ser alterado: ')
    pos=procuraContato(nome,lcontato)
    if pos!=-1:
      alterContato(pos,lcontato)
    else:
      print('Contato não encontrado')
  elif op==4:
    nome=input('Nome a ser excluído: ')
    pos=procuraContato(nome,lcontato)
    if pos!=-1:
      excluiContato(pos,lcontato)
    else:
      print('Contato não encontrado')
  elif op==5:
    listaContatos(lcontato)
print('*** Obrigado por Utilizar Nosso Sistema ***')