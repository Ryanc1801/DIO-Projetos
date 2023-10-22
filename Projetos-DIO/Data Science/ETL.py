import pandas as pd
from DEF import defs
import random

#CONSULTA DE CLIENTES

lista = ['1','2','3','4','5','6','7','8','9','10']
while True:
    num = str(input('Selecione um ID de Cliente (1,10): '))
    
    if num in lista:
        num = int(num)

        #consumindo dataset
        users = pd.read_excel('users.xlsx')
        users_df = pd.DataFrame(users)

        #limpando dados de forma simples
        users_df = users_df.drop('Unnamed: 0',axis=1)
        users_df.rename(columns={'Unnamed: 1': 'ID', 'Unnamed: 2': 'NOME', 'Unnamed: 3': 'IDADE', 'Unnamed: 4': 'COR FAVORITA', 'Unnamed: 5': 'TIPO DE COMIDA', 'Unnamed: 6': 'COMIDA FAVORITA'}, inplace = True)
        users_df = users_df.drop(0,axis=0)

        #parametros da consulta
        cliente = users_df['NOME'][num]
        idade = users_df['IDADE'][num]
        tipo_de_comida = users_df['TIPO DE COMIDA'][num]
        favorita = users_df['COMIDA FAVORITA'][num]
        person = defs.color(users_df['COR FAVORITA'][num])


        print(f'\033[1;32m\nO cliente selecionado foi {cliente} que tem {idade} anos, prefere {tipo_de_comida} e tem como comida favorita {favorita}\nE é uma {person}\033[m\n')

        quest = sair = str(input('Deseja sair do programa ? S/N: '))
        if quest in 'Nn':
            break
        else:
            continue
    else:
        print('\033[1;31mPor Favor Digite um valor válido\033[m')
print('\033[1;33mFIM DO PROGRAMA\033[m')