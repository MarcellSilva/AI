# Criei uma função que utiliza a leitura de um arquivo .csv, utilizando a biblioteca Pandas e organizando os dados apenas com as colunas:
# A, B, C, D e y (target), removendo as colunas E e F e retornando um dataframe(df).
# Importei um arquivo 'data.csv'

# Criei uma função que recebe o a função 'organize_data()' com o dataframe organizado.
# Organização dos dados em Numpy Arrays, com X contendo as colunas 'A, B, C e D' e a coluna target o 'y'
# Embaralhamento dos dados em X e y com 'train_test_split' da biblioteca learn com o 'random_state=33 e com 75% de dados para treino e o resto para teste.
# Printando alguns valores como teste do código.

import pandas as pd
from sklearn.model_selection import train_test_split


def organize_data(file_name):
    df = None
    ### seu código começa aqui ###
    df = pd.read_csv('data.csv')
    delete = ['E', 'F']
    df.drop(delete, axis=1, inplace=True)

    return df


def shuffle_split_data(df):
    X_train, X_test, y_train, y_test = None, None, None, None
    ###
    X1 = organize_data('data.csv')
    y1 = organize_data('data.csv')
    X = X1.iloc[:, :4]
    y = y1.iloc[:, 4]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.75, random_state=33)

    ###
    return X_train, X_test, y_train, y_test


if __name__ == '__main__':
    df = organize_data('data.csv')
    print(len(shuffle_split_data(df)))
    print(shuffle_split_data(df)[0].shape)
    print(shuffle_split_data(df)[1].shape)
    print(shuffle_split_data(df)[2].shape)
    print(shuffle_split_data(df)[3].shape)
