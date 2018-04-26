from firebase import firebase
firebase = firebase.FirebaseApplication('https://ep1-dsoft.firebaseio.com/', None)
ESTOQUES = firebase.get('/dados', None)
ESTOQUES=ESTOQUES['Índice de Lojas']
# Fazer uma lista com o nome de todas as lojas

lnomes=[]
for dicionarios in ESTOQUES:
    for nomes in dicionarios:
        lnomes.append(nomes)


# Fazer a escolha de loja
# Escolher ou declarar um estoque
# Declarar a posição do estoque na lista ESTOQUES pela variável index


index=len(ESTOQUES)
if lnomes!=[]:
    while True:
        lnomes=[]
        for dicionarios in ESTOQUES:
            for nomes in dicionarios:
                lnomes.append(nomes)
        
        print('\nMenu inicial\nLojas disponíveis no arquivo:')
        print(', '.join(lnomes))
        loja=input('Digite o nome da loja ou digite 0 para remover uma loja: ')
        if loja!='0':
            if loja not in lnomes:
                condloja=input('Deseja criar um estoque para uma nova loja?(s/n): ')
                condloja=condloja.lower()
                # Verificar se houve erro de digitação
                
                if condloja=='s' and loja!='':
                    estoque={}
                    break
                elif condloja!='n':
                    print('Opção inválida')
            else:
                for index in range(len(ESTOQUES)):
                    if loja in ESTOQUES[index]:
                        estoque=ESTOQUES[index][loja]
                        break
                break
        else:
            if len(lnomes)>1:
                remove=input('Digite o nome da loja que deseja remover: ')
                if remove not in lnomes:
                    print('Loja não encontrada')
                else:
                    c=True
                    i=0
                    while c:
                        for k in ESTOQUES[i]:
                            if k==remove:
                                del ESTOQUES[i]
                                c=False
                        i+=1
            else:
                print('Não é possível remover todos os estoques')
                            
                        
                        
else:
    loja=input('Digite o nome da nova loja: ')
    estoque={}



while True:
    print('\nControle de estoque \n0: sair \n1: adicionar item \n2: remover item \n3: alterar item \n4: imprimir estoque')
    op=(input('Faça sua escolha: '))
    
    # Checar se o input é um valor inteiro e menor ou igual a 4
    
    try:
        op=int(op)
        if op>4 or op!=int(op):
            print('Opção inválida')
    except:
        print('Opção inválida')

    
    if op==0:
        print('Até mais')
        break
    
    elif op==1:    
        nomeprod=input('Nome do produto: ')
        if nomeprod not in estoque:
            while True:
                a=True
                b=True
                while a:
                    try:
                        qti=int(input('Quantidade inicial: '))
                        #Verificar se o valor qti é válido
                        try:
                            if qti>0:
                                a=False
                            else: print('A quantidade inicial não pode ser negativa ou nula')
                        except:
                            print('Valor inválido')
                    except:
                        print('Valor inválido')
                while b:
                    try:
                        vali=float(input('Valor do produto: '))
                        #Verificar se o valor qti é válido
                        try:
                            if vali>=0:
                                b=False
                            else: print('O valor não pode ser negativo')
                        except:
                            print('Valor inválido')
                    except:
                        print('Valor inválido')             
            
                estoque[nomeprod]={}
                estoque[nomeprod]['quantidade']=qti
                estoque[nomeprod]['valor']=vali
                break
        else:
            print('Produto já está cadastrado')
    
    elif op==2:
        ndel=input('Nome do produto: ')
        if ndel in estoque:
            del estoque[ndel]
        else:
            print('Elemento não encontrado')
    
    elif op==3:
        nalt=input('Nome do produto: ')
        quop=''
        if nalt not in estoque:
            print('Elemento não encontrado')
        else:
            qoup=input('Deseja alterar quantidade (q) ou preço (p): ')
            if qoup=='q':
                cond=True
                while cond:    
                    perg = input("Você deseja adicionar ou tirar itens? (A/T) ")
                    perg=perg.lower()
                    if perg == "a":
                        try:
                            # Checar se o valor a ser inserido é válido
                            qte=int(input('Quantidade: '))
                            if qte!=int(qte) or qte<=0:
                                print('Valor inválido')
                            else:
                                estoque[nalt]['quantidade']+=qte
                                print(estoque[nalt]['quantidade'])
                                cond = False
                        except:
                            print("Valor inválido")
                    elif perg == "t":
                        try:
                            # Checar se o valor a ser inserido é válido
                            qte=int(input('Quantidade: '))
                            if qte!=int(qte) or qte<=0:
                                print('Valor inválido')
                            else:
                                estoque[nalt]['quantidade']-=qte
                                print(estoque[nalt]['quantidade'])
                                cond = False
                        except:
                            print('Valor inválido')
                    else:
                        print("Opção inválida")
               
            elif qoup=='p':
                # Checar se o valor a ser inserido é válido
                
                try:
                    val=float(input('Valor: '))
                    if val>0:
                        estoque[nalt]['valor']=val
                    else:
                        print('Valor inválido')
                except:
                    print('Valor inválido')
            else:
                print('Opção inválida')

    elif op==4:
        if not estoque:
            print("Estoque vazio")
        else:
            print('Q: Imprimir quantidades \nN: Imprimir produtos com estoque negativo\nM: Imprimir valor monetário total\nV: Imprimir o valor de cada produto')
            imp=input('Opção: ')
            imp=imp.lower()
        
            if imp=='q':
               for i in estoque:
                   print('{0} : {1}'.format(i,estoque[i]['quantidade']))
        
            elif imp=='n':
                for i in estoque:
                    if estoque[i]['quantidade']<0:
                        print('{0} : {1}'.format(i,estoque[i]['quantidade']))
        
            elif imp=='m':
                s=0
                for i in estoque:
                    s+=estoque[i]['valor']*estoque[i]['quantidade']
                    print('Valor total: R$ {}'.format(s))
        
            elif imp=='v':
                for i in estoque:
                    print('{0} : {1}'.format(i,estoque[i]['valor']))
                else:
                    print('Opção inválida')

# Recolocar/adicionar o estoque da loja em uso para a lista ESTOQUES
try:
    ESTOQUES[index][loja]=estoque

except:
    ESTOQUES.append({loja:estoque})

firebase.put('/dados', 'Índice de Lojas',ESTOQUES)