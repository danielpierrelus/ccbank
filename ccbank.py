
class agenda:
  nome=''
  email=''
  diamesnasc=''
  idade=0
  cpf=0
  endereco=' '
  numero_da_conta=0
  saldo=0
  limite_de_credito=0

  ## função para listar todos os contatos cadastrados
def listaContatos(contatos):

    print("****Os nossos clientes****")
    for i in range(len(contatos)):
        print()
        print('Nome: ',contatos[i].nome)
        print('Email: ',contatos[i].email)
        print('Niver: ',contatos[i].diamesnasc)
        print('Idade: ',contatos[i].idade)
        print('Cpf: ',contatos[i].cpf)
        print('Endereco de cliente: ',contatos[i].endereco)
        print('Numero da conta: ',contatos[i].numero_da_conta)
        print('Saldo do cliente: ',contatos[i].saldo)
        print('Limite de credito: ',contatos[i].limite_de_credito)
        print()


    # função para procurar um nome na lista de contatos (retorna a posição do nome)
def procuraContato(nome, contatos):
  for i in range(len(contatos)):
    if contatos[i].nome==nome:
      return i #posição do nome na lista
  return -1 # indica que o nome não foi encontrado

  ## insere contato
def insereContato(cliente):
  cliente.nome=input('Nome : ')
  cliente.email=input('email: ')
  cliente.diamesnasc=input('Niver: ')
  cliente.idade=int(input('Idade: '))

  valor = input("Digite o CPF: ")
  cpf = list(map(int, valor))
  if validaCPF(cpf):
    print("CPF valido")
    cliente.cpf = int("".join(str(x) for x in cpf))
  else:
    print("CPF nao e valido")

  #cliente.cpf=int(input('Cpf: '))
  cliente.endereco=input('Endereço de cliente: ')
  
  cliente.numero_da_conta=int(input('Numero da conta: '))
  cliente.saldo=int(input('Saldo do cliente: '))

  cliente.limite_de_credito=int(input('Limite de credito: '))
  cliente.limite_de_credito=1000
  
  # Ok, insere contato
  lcontato.append(cliente)
  print( )
  print('Um novo cliente foi adicionado com successo')

#cpf valida
def validaCPF(cpf):
  parte_inicial = cpf[0:9]
  num = 10
  soma = 0
    # Faz a multiplicação
  for i in range(0,len(parte_inicial)):
      soma += (parte_inicial[i] * num)
      num -= 1       
  
  digito_um = 0

    # Determina o valor do primeiro digito
  resto = soma % 11
  if resto >= 2:
      digito_um = 11-resto
        
    # Anexa o primeiro digito
  parte_inicial.append(digito_um)

    # Faz a multiplicação incluindo o novo digito
  num = 11
  soma = 0
  for i in range(0,len(parte_inicial)):
      soma += parte_inicial[i] * num
      num -= 1      
    
  digito_dois = 0
    
    # Determina o valor do segundo digito
  resto = soma % 11
  if resto >= 2:
      digito_dois = 11-resto
        
    # Anexa segundo digito
  parte_inicial.append( digito_dois )
    
    # Se sao iguais, então é valido
  return (cpf == parte_inicial)
  
  #altera dados
def alterContato(pos,contatos):
  print()
  print('Nome: ',contatos[pos].nome)
  print('Email: ',contatos[pos].email)
  print('Niver: ',contatos[pos].diamesnasc)
  print('Idade: ',contatos[pos].idade)
  print('Cpf: ',contatos[pos].cpf)
  print('Endereco de cliente: ',contatos[pos].endereco)
  print('Numero da conta: ',contatos[pos].numero_da_conta)
  print('Saldo do cliente: ',contatos[pos].saldo)
  print('Limite de credito: ',contatos[pos].limite_de_credito)
  print()
  print('digite 1 para altera Nome: ')
  print('digite 2 para altera Email: ')
  print('digite 3 para altera Niver: ')
  print('digite 4 para altera Idade: ')
  print('digite 5 para altera Cpf: ')
  print('digite 6 para altera Endereco do cliente: ')
  print('digite 7 para altera o numero da conta: ')
  print('digite 8 para altera o saldo do cliente: ')
  print('digite 9 para altera o limite de credito: ')
  print()
  alteracao=int(input('digite a opcao desejada:'))
  if alteracao==1:
    novo_nome=input('Novo nome: ')
    contatos[pos].nome=novo_nome
  elif alteracao==2:
    novo_email=input('Novo email: ')
    contatos[pos].email=novo_email
  elif alteracao==3:
    novo_diamesnasc=input('Novo niver: ')
    contatos[pos].diamesnasc=novo_diamesnasc
  elif alteracao==4:
    novo_idade=input('Novo idade: ')
    contatos[pos].idade=novo_idade
  elif alteracao==5:
    novo_cpf=input('Novo cpf: ')
    contatos[pos].cpf=novo_cpf
  elif alteracao==6:
    novo_endereco=input('Novo endereco do cliente: ')
    contatos[pos].endereco=novo_endereco
  elif alteracao==7:
    novo_numero_da_conta=input('Novo numero da conta: ')
    contatos[pos].numero_da_conta=novo_numero_da_conta
  elif alteracao==8:
    novo_saldo=input('Novo saldo de cliente: ')
    contatos[pos].saldo=novo_saldo
  elif alteracao==9:
    novo_limite_de_credito=input('Novo limite de credito: ')
    contatos[pos].limite_de_credito=novo_limite_de_credito
  
  print()
  print('Nome: ',contatos[pos].nome)
  print('Email: ',contatos[pos].email)
  print('Niver: ',contatos[pos].diamesnasc)
  print('Idade: ',contatos[pos].idade)
  print('Cpf: ',contatos[pos].cpf)
  print('Endereco de cliente: ',contatos[pos].endereco)
  print('Numero da conta: ',contatos[pos].numero_da_conta)
  print('Saldo do cliente: ',contatos[pos].saldo)
  print('Limite de credito: ',contatos[pos].limite_de_credito)
  print()
  print('Dados alterados com sucesso')
  
  #
def excluiContato(pos,contatos):
  contatos.remove(contatos[pos])
  print()
  print('Dados excluidos com sucesso')

  #funcao para movimentar das contas

def movimento(cliente):
  print()
  print('digite 1 para operacao credito: ')
  print('digite 2 para para operacao debito: ')
  print()
  add=int(input('A opcao desejada: '))
  valor=int(input('O valor desejada: '))
  if add==1:
    cliente.saldo+=valor
    print('saldo do cliente: ',lcontato[i].saldo)
  elif add==2 and -cliente.limite_de_credito<cliente.saldo-valor:
    cliente.saldo-=valor
    print('saldo do cliente: ',lcontato[i].saldo)
  elif add==2 and -cliente.limite_de_credito>cliente.saldo-valor:
    print()
    print('Infelizmente a operação não é possivél')


## função de menu
def menu():
  print(' ***Sistema CCBank*** ')
  print('='*30)
  print()
  print('1 - Inserir')
  print('2 - Consultar')
  print('3 - Alterar')
  print('4 - Excluir')
  print('5 - Listar todos')
  print('6 - Movimento da conta')
  print('7 - alterar limite ')
  print('8 - Sair')
  return int(input(': '))


  ##
lcontato=[] # armazena a lista de contatos
op=1
senha='549053'
while op!=8:
  op=menu()
  if op==1:
    s=input('Digite a senha: ')
    if s==senha:
      newc=agenda()
      insereContato(newc)
      lcontato.append(newc)
    else:
      print('Senha incorreto')
  elif op==2:
    nome=input('Nome para procurar: ')
    pos=procuraContato(nome,lcontato)
    if pos!=-1: # encontrou o nome?
      print('Nome : ',lcontato[pos].nome)
      print('email: ',lcontato[pos].email)
      print('Niver: ',lcontato[pos].diamesnasc)
      print('Idade: ',lcontato[pos].idade)
      print('CPF: ',lcontato[pos].cpf)
      print('Endereço Cliente: ',lcontato[pos].endereço)
      print('Numero da conta: ',lcontato[pos].numero_da_conta)
      print('Saldo da Cliente: ',lcontato[pos].saldo)
      print('Limite de credito: ',lcontato[pos].limite_de_credito)


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
    nome=input('nome a ser excluído: ')
    pos=procuraContato(nome,lcontato)
    if pos!=-1:
      excluiContato(pos,lcontato)
    else:
      print('Contato não encontrado')
  elif op==5:
    listaContatos(lcontato)
  elif op==6:
    cpf_buscar=int(input('digite o cpf do cliente:'))
    for i in range(len(lcontato)-1):
      if cpf_buscar==lcontato[i].cpf:
        movimento(lcontato[i])
      else:
        print('Este cpf nao existe no sistema: ')
  elif op==7:
    s=input('Digite a senha: ')
    # if s==senha:
      

    # else:
    #   print('senha incorreta: ')

  # if op==6 and (len(lcontato))==false:
    #print('infelimente nao temos cliente: ')
  #   # print()
print('*** Obrigado por Utilizar Nosso Sistema ***')