# Criei uma função que utiliza a leitura de um arquivo .csv, utilizando a biblioteca Pandas e organizando os dados apenas com as colunas:
# A, B, C, D e y (target), removendo as colunas E e F e retornando um dataframe(df).
# Importei um arquivo 'data.csv'
# Printando alguns valores como teste do código.

import pandas as pd


def organize_data(file_name):
    df = None
    ### seu código começa aqui ###
    df = pd.read_csv('data.csv')
    delete = ['E', 'F']
    df.drop('E', axis=1, inplace=True, errors='ignore')
    df.drop('F', axis=1, inplace=True, errors='ignore')
    ### seu código termina aqui ###
    return df


if __name__ == '__main__':
    print(type(organize_data('data.csv')))
    print(organize_data('data.csv').shape)
    print(organize_data('data.csv').columns)
    print(organize_data('data.csv').loc[1].values)
    print(organize_data('data.csv').loc[100].values)
