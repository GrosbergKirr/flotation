import pandas as pd


def load_df(df_path):
    df = pd.read_excel(df_path)
    # Ставим первую колонку с датой индексом
    df = df.rename(columns={df.columns[0]: 'date'})
    df.index = df['date']
    df = df.drop('date', axis=1)
    # Убираем полностью пустые колонки
    df = df.dropna(axis=1, how='all')
    return df
