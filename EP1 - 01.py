# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:42:26 2018

@author: Adm
"""
estoque=dict()

while True:
    print()
    print('Controle de estoque')
    print('0: sair')
    print('1: adicionar item')
    print('2: remover item')
    print('3: alterar item')
    print('4: imprimir estoque')
    op=int(input('Faça sua escolha: '))
    if op==0:
        print('Até mais')
        break
    elif op==1:
        temp={}
        nomeprod=input('Nome do produto: ')
        if nomeprod not in estoque:
            while True:
                qti=int(input('Quantidade inicial: '))
                if qti>0:
                    break
                else: print('A quantidade inicial não pode ser negativa')
            temp['quantidade']=qti
            estoque[nomeprod]=temp
        else:
            print('Produto já está cadastrado')
    elif op==2:
        #while True:
        ndel=input('Nome do produto: ')
        if ndel in estoque:
            del estoque[ndel]
        else:
            print('Elemento não encontrado')
    elif op==3:
        nalt=input('Nome do produto: ')
        if nalt in estoque:
            qte=int(input('Quantidade: '))
            estoque[nalt]['quantidade']+=qte
            print(estoque[nalt]['quantidade'])
        else:
            print('Elemento não encontrado')
    elif op==4:
        for i in estoque:
            print('{0} : {1}'.format(i,estoque[i]['quantidade']))
    