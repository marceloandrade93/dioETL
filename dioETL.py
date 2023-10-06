import pandas as pd
import os

### ---- EXTRACT [OK]
# - Carregar csv
path_root = os.path.abspath(os.getcwd())
df_calls = pd.read_csv(f'{path_root}/dbchamados.csv', delimiter=',', encoding='UTF-8') 

print(df_calls)

### ---- TRANSFORM [OK]
# - Inserir novo chamado
list_addnew = {
    'Atendente': [''],
    'CNPJ': [''],
    'Título': [''],
    'Descrição': [''],
    'Status': ['']
}

df_new_call = pd.DataFrame(list_addnew)

new_atendente = input('Quem é o atendente? \nR= ')
new_cnpj = input('Qual o CNPJ do cliente! \nR= ')
new_titulo = input('Defina um titulo para o chamado. \nR= ')
new_descricao = input('O que ocorreu no atendimento? \nR= ')
new_status = 0
list_status = {'Fechado', 'Aberto'}

while new_status not in list_status:
    new_status = int(input('Qual status do chamado? \n1 = Fechado \n2 = Aberto \nR= '))
    if new_status == 1:
        new_status = 'Fechado'
    elif new_status == 2:
        new_status = 'Aberto'

df_new_call['Atendente'] = new_atendente
df_new_call['CNPJ'] = new_cnpj
df_new_call['Título'] = new_titulo
df_new_call['Descrição'] = new_descricao
df_new_call['Status'] = new_status

### ---- LOAD [OK]
# - Salvar novo chamado no DF
df_calls = df_calls.append(df_new_call).reset_index(drop=True)

df_calls.to_csv(f'{path_root}/dbchamados.csv', index=False)

print(df_calls)
