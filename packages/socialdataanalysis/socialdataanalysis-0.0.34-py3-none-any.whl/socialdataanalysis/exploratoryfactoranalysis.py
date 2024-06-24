import pandas as pd
import pingouin as pg
import seaborn as sns
import matplotlib.pyplot as plt

from reliabilipy import reliability_analysis
from tabulate import tabulate

def inverter_escala(df, colunas, escalas):
    """
    Inverte as escalas de colunas especificadas em um DataFrame.

    Parâmetros:
    - df (pandas.DataFrame): DataFrame contendo os dados.
    - colunas (list): Lista de colunas para as quais a escala deve ser invertida.
    - escalas (list): Lista de valores máximos das escalas correspondentes às colunas.

    Retorna:
    - DataFrame modificado, e opcionalmente, os metadados.
    """
    if not isinstance(colunas, list) or not isinstance(escalas, list) or len(colunas) != len(escalas):
        return "Erro: 'colunas' e 'escalas' devem ser listas de mesmo tamanho.", None

    for coluna, escala in zip(colunas, escalas):
        if coluna in df.columns:
            df[coluna + '_R'] = escala + 1 - df[coluna]
        else:
            return f"Erro: A coluna '{coluna}' não existe no DataFrame.", None

    return df
        
def transformar_escala(df, coluna, nova_escala_min, nova_escala_max):
    """
    Transforma os valores de uma coluna de um DataFrame de sua escala original para uma nova escala especificada.

    Parâmetros:
    - df (pandas.DataFrame): DataFrame contendo os dados.
    - coluna (str): Nome da coluna a ser transformada.
    - nova_escala_min (int): Valor mínimo da nova escala.
    - nova_escala_max (int): Valor máximo da nova escala.
    
    Retorna:
    - DataFrame com a coluna transformada.
    """
    # Extrair os valores mínimo e máximo originais da coluna
    orig_min = df[coluna].min()
    orig_max = df[coluna].max()

    # Verificar se os valores mínimos e máximos não são nulos
    if pd.isna(orig_min) or pd.isna(orig_max):
        raise ValueError("A coluna contém apenas valores nulos.")

    # Aplicar a transformação linear para a nova escala
    df[coluna + '_Nova_Escala'] = df[coluna].apply(
        lambda x: (x - orig_min) / (orig_max - orig_min) * (nova_escala_max - nova_escala_min) + nova_escala_min
        if pd.notnull(x) else None
    )

    return df
    
def analisar_consistencia_interna(df, colunas, exibir_correlacoes=False, exibir_resumo=False, exibir_heatmap=False):
    """
    Analisa o alfa de Cronbach, Ômega de MacDonald e as correlações para um conjunto específico de colunas de um DataFrame.
    
    Parâmetros:
        df (pd.DataFrame): DataFrame contendo os dados a serem analisados.
        colunas (list): Lista de colunas a serem incluídas na análise.
        exibir_correlacoes (bool): Se True, imprime a matriz de correlações.
        exibir_resumo (bool): Se True, imprime o resumo do alfa de Cronbach com e sem cada coluna.
        exibir_heatmap (bool): Se True, exibe um heatmap das correlações.

    Retorna:
        tuple: Retorna o alfa de Cronbach original, o Ômega de MacDonald, a matriz de correlações e o resumo do alfa de Cronbach se cada coluna for removida.
    """
    
    def calcular_omega(df):
        """Função auxiliar para calcular o Ômega de MacDonald."""
        correlacoes = df.corr()
        try:
            reliability_report = reliability_analysis(correlations_matrix=correlacoes)
            reliability_report.fit()
            return reliability_report.omega_total
        except Exception as e:
            print(f"Erro ao calcular o Ômega de MacDonald: {e}")
            return None
    
    df_filtrado = df[colunas]
    correlacoes = df_filtrado.corr()

    # Calcula o alfa de Cronbach original
    alfa_original = None
    if df_filtrado.shape[1] > 1:
        try:
            alfa_original = pg.cronbach_alpha(df_filtrado)[0]
        except Exception as e:
            print(f"Erro ao calcular o alfa de Cronbach original: {e}")

    # Calcula o Ômega de MacDonald original
    omega_total = None
    if df_filtrado.shape[1] > 1:
        omega_total = calcular_omega(df_filtrado)

    # Calcula o alfa de Cronbach e Ômega se cada coluna for removida
    alfas_removidos = {}
    omegas_removidos = {}
    for coluna in colunas:
        temp_df = df_filtrado.drop(columns=[coluna])
        alfas_removidos[coluna] = None
        omegas_removidos[coluna] = None
        if temp_df.shape[1] > 1:
            try:
                alfas_removidos[coluna], _ = pg.cronbach_alpha(temp_df)
                omegas_removidos[coluna] = calcular_omega(temp_df)
            except Exception as e:
                print(f"Erro ao calcular os valores removendo a coluna {coluna}: {e}")

    # Exibe o alfa de Cronbach original e o Ômega de MacDonald
    resultados = []
    if alfa_original is not None:
        resultados.append(['Alfa de Cronbach Original', round(alfa_original, 3)])
    if omega_total is not None:
        resultados.append(['Ômega de MacDonald Original', round(omega_total, 3)])

    if resultados:
        print(tabulate(resultados, headers=['Métrica', 'Valor'], tablefmt='grid'))

    # Exibe o resumo do alfa de Cronbach e Ômega de MacDonald se item removido
    if exibir_resumo:
        resumo = pd.DataFrame({
            'Alfa se item removido': alfas_removidos,
            'Ômega se item removido': omegas_removidos
        })
        resumo_tabela = [[coluna, round(alfa, 3), round(omega, 3)] for coluna, (alfa, omega) in resumo.iterrows()]
        print("\nAlfa e Ômega se item removido:")
        print(tabulate(resumo_tabela, headers=['Coluna', 'Alfa', 'Ômega'], tablefmt='grid'))

    # Exibe a matriz de correlações
    if exibir_correlacoes:
        correlacoes_tabela = correlacoes.round(3).reset_index().values.tolist()
        correlacoes_tabela.insert(0, [''] + list(correlacoes.columns))
        print("\nCorrelações:")
        print(tabulate(correlacoes_tabela, headers='firstrow', tablefmt='grid'))

    # Exibe o heatmap das correlações
    if exibir_heatmap:
        sns.heatmap(correlacoes, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title("\nMatriz de Correlações")
        plt.show()