# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:05:47 2018

@author: Thomas
"""




import json
arquivo_in = open("ep1.json", "r")

# Ler o arquivo de estoques

json1 = arquivo_in.readlines() 

# Colocar os dicionários do arquivo em uma lista

ESTOQUES=[]
for item in json1:
    ESTOQUES.append(json.loads(item)) 

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
        print('Lojas disponíveis no arquivo:')
        print(', '.join(lnomes))
        loja=input('Digite o nome da loja: ')
    
        if loja not in lnomes:
            condloja=input('Deseja criar um estoque para uma nova loja?(s/n): ')
            # Verificar se houve erro de digitação
            
            if condloja=='s':
                estoque={}
                break
        
        else:
            for index in range(0,len(ESTOQUES)):
                if loja in ESTOQUES[index]:
                    estoque=ESTOQUES[index][loja]
                    break
            break
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
            print('Valor inválido')
    except:
        print('Valor inválido')

    
    if op==0:
        print('Até mais')
        break
    
    elif op==1:    
        nomeprod=input('Nome do produto: ')
        if nomeprod not in estoque:
            while True:
                qti=int(input('Quantidade inicial: '))
                #Verificar se o valor qti é válido
                try:
                    if qti>0:
                        break
                    else: print('A quantidade inicial não pode ser negativa ou nula')
                except:
                    print('Valor inválido')
                 
                 
            
            estoque[nomeprod]={}
            estoque[nomeprod]['quantidade']=qti
            estoque[nomeprod]['valor']=0
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
                
                # Checar se o valor a ser inserido é válido
                
                try:
                    qte=int(input('Quantidade: '))
                    if qte!=int(qte):
                        print('Valor inválido')
                    else:
                        estoque[nalt]['quantidade']+=qte
                        print(estoque[nalt]['quantidade'])
                except:
                    print('Valor inválido')
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
    
    elif op==4:
        print('Imprimir quantidades: q \nImprimir produtos com estoque negativo: n\nImprimir valor monetário total: m\nImprimir o valor de cada produto: v')
        imp=input('Opção: ')
        
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
            print('Valor total: {}'.format(s))
        
        # Imprimir o valor de cada produto
        elif imp=='v':
            for i in estoque:
                print('{0} : {1}'.format(i,estoque[i]['valor']))
        

# Recolocar/adicionar o estoque da loja em uso para a lista ESTOQUES

try:
    ESTOQUES[index][loja]=estoque

except:
    ESTOQUES.append({loja:estoque})

# Reescrever cada elemento da lista ESTOQUES no arquivo JSON

arquivo_out = open("ep1.json", "w")

for i in ESTOQUES:    
    arquivo_out.writelines(json.dumps(i)+'\n')

arquivo_out.close()