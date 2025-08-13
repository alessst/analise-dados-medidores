import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# Carregar os dados do CSV
arquivo = "Botafogo - CheckList.csv"
df = pd.read_csv(arquivo)
# Colunas usadas

colunas = df.columns

# Títulos das colunas
Titulo = "Título"
Shopping = "Shopping"
Data = "Data"
NOC = "NOC"
Instalador = "Instalador"
TAG = "TAG"
Numero_da_probe_telemetria = "Número da probe/telemetria"
Local_de_instalacao = "Local de instalação"
Identificacao_do_ponto = "Identificação do ponto"
Modelo_do_medidor = "Modelo do medidor"
Local_LUC = "Local / LUC"
Configuracao_MODBUS_Endereco = "Configuração MODBUS - Endereço"
Configuracao_MODBUS_Baud_Rate = "Configuração MODBUS - Baud Rate"
Configuracao_MODBUS_Paridade = "Configuração MODBUS - Paridade"
TC = "TC"
Codigo_de_erro = "Código de erro"
Medidor_Pulsos = "Medidor - Pulsos"
Medidor_Corrente_Ia = "Medidor - Corrente Ia"
Medidor_Prefixo_Ia = "Medidor - Prefixo Ia"
Medidor_Corrente_Ib = "Medidor - Corrente Ib"
Medidor_Prefixo_Ib = "Medidor - Prefixo Ib"
Medidor_Corrente_Ic = "Medidor - Corrente Ic"
Medidor_Prefixo_Ic = "Medidor - Prefixo Ic"
Medidor_Tensao_Van = "Medidor - Tensão Van"
Medidor_Prefixo_Van = "Medidor - Prefixo Van"
Medidor_Tensao_Vbn = "Medidor - Tensão Vbn"
Medidor_Prefixo_Vbn = "Medidor - Prefixo Vbn"
Medidor_Tensao_Vcn = "Medidor - Tensão Vcn"
Medidor_Prefixo_Vcn = "Medidor - Prefixo Vcn"
Medidor_Tensao_Vab = "Medidor - Tensão Vab"
Medidor_Prefixo_Vab = "Medidor - Prefixo Vab"
Medidor_Tensao_Vbc = "Medidor - Tensão Vbc"
Medidor_Prefixo_Vbc = "Medidor - Prefixo Vbc"
Medidor_Tensao_Vca = "Medidor - Tensão Vca"
Medidor_Prefixo_Vca = "Medidor - Prefixo Vca"
Medidor_Potencia_Ativa = "Medidor - Potência Ativa"
Medidor_Prefixo_Potencia_Ativa = "Medidor - Prefixo Potência Ativa"
Medidor_Potencia_Reativa = "Medidor - Potência Reativa"
Medidor_Prefixo_Potencia_Reativa = "Medidor - Prefixo Potência Reativa"
Medidor_Energia_Ativa_Acumulada = "Medidor - Energia Ativa Acumulada"
Medidor_Prefixo_Energia_Ativa = "Medidor - Prefixo Energia Ativa"
Medidor_Anterior_Energia_Ativa_Acumulada = "Medidor Anterior - Energia Ativa Acumulada"
Medidor_Anterior_Prefixo_Energia_Ativa = "Medidor Anterior - Prefixo Energia Ativa"
Alicate_Ia = "Alicate Ia"
Alicate_Prefixo_Ia = "Alicate - Prefixo Ia"
Alicate_Ib = "Alicate Ib"
Alicate_Prefixo_Ib = "Alicate - Prefixo Ib"
Alicate_Ic = "Alicate Ic"
Alicate_Prefixo_Ic = "Alicate - Prefixo Ic"
Alicate_Van = "Alicate Van"
Alicate_Prefixo_Van = "Alicate - Prefixo Van"
Alicate_Vbn = "Alicate Vbn"
Alicate_Prefixo_Vbn = "Alicate - Prefixo Vbn"
Alicate_Vcn = "Alicate Vcn"
Alicate_Prefixo_Vcn = "Alicate - Prefixo Vcn"
Alicate_Vab = "Alicate Vab"
Alicate_Prefixo_Vab = "Alicate - Prefixo Vab"
Alicate_Vbc = "Alicate Vbc"
Alicate_Prefixo_Vbc = "Alicate - Prefixo Vbc"
Alicate_Vca = "Alicate Vca"
Alicate_Prefixo_Vca = "Alicate - Prefixo Vca"
Zordon_Ia = "Zordon Ia"
Zordon_Prefixo_Ia = "Zordon - Prefixo Ia"
Zordon_Ib = "Zordon Ib"
Zordon_Prefixo_Ib = "Zordon - Prefixo Ib"
Zordon_Ic = "Zordon Ic"
Zordon_Prefixo_Ic = "Zordon - Prefixo Ic"
Zordon_Van = "Zordon Van"
Zordon_Prefixo_Van = "Zordon - Prefixo Van"
Zordon_Vbn = "Zordon Vbn"
Zordon_Prefixo_Vbn = "Zordon - Prefixo Vbn"
Zordon_Vcn = "Zordon Vcn"
Zordon_Prefixo_Vcn = "Zordon - Prefixo Vcn"
Zordon_Vab = "Zordon Vab"
Zordon_Prefixo_Vab = "Zordon - Prefixo Vab"
Zordon_Vbc = "Zordon Vbc"
Zordon_Prefixo_Vbc = "Zordon - Prefixo Vbc"
Zordon_Vca = "Zordon Vca"
Zordon_Prefixo_Vca = "Zordon - Prefixo Vca"
Zordon_Potencia_Ativa = "Zordon Potência Ativa"
Zordon_Prefixo_Potencia_Ativa = "Zordon - Prefixo Potência Ativa"
Zordon_Potencia_Reativa = "Zordon Potência Reativa"
Zordon_Prefixo_Potencia_Reativa = "Zordon - Prefixo Potência Reativa"
Zordon_Energia_Ativa_Acumulada = "Zordon Energia Ativa Acumulada"
Zordon_Prefixo_Energia_Ativa = "Zordon - Prefixo Energia Ativa"
Relatorio_Exportado = "Relatório Exportado"
Observacoes = "Observações"
Validacao = "Validação"
Integracao = "Integração"
Anexos = "Anexos"

# Define o estilo CSS dentro do Streamlit
style = """
        <style>
        .card {
            width: 160px;
            padding: 6px;
            margin: 10px auto;
            border-radius: 10px;
            3px 3px 5px #4F4F4F;
            text-align: center;
            background-color: #363636	;
        }
         .data-card {
            width: 200px;
            padding: 10px;
            margin: 5px auto;
            border-radius: 10px;
            
            text-align: center;
            background-color: #363636	;
        }
         .probes-data-card {
            width: 400px;
            padding: 10px;
            margin: 5px auto;
            border-radius: 10px;
            
            text-align: center;
            background-color: #363636	;
        }
        .ponto-data-card {
            width: 300px;
            padding: 3px;
            margin: 5px auto;
            border-radius: 10px;
            
            text-align: left;;
            background-color: #363636	;
        }
        .pot-card {
            width: 200px;
            padding: 10px;
            margin: 5px auto;
            border-radius: 10px;
            
            text-align: center;
            background-color: #363636	;
        }
        .small-text {
            font-size: 8px;
            font-weight: bold;
            color: #D3D3D3	;
        }
        .medium-text {
            font-size: 12px;
            font-weight: bold;
            color: #D3D3D3	;
            text-transform: uppercase;
            
        }
        .large-text {
            font-size: 20px;
            font-weight: bold;
            color: #D3D3D3	;
        }
        .data-medium-text {
            font-size: 10px;
            color: #D3D3D3	;
            text-transform: uppercase;
            
        }
        .data-large-text {
            font-size: 16x;
            font-weight: bold;
            color: #D3D3D3	;
            text-transform: uppercase;
        }
        .data-text {
            font-size: 14px;
            font-weight: bold;
            color: #D3D3D3	;
            
        }
        .ponto-data-medium-text {
            font-size: 12px;
            color: #D3D3D3	;
            font-weight: bold;
            text-transform: uppercase;
            
        }
        </style>
        """

#Função para pegar dados do ponto
def dados_ponto(data, index):

    data = data.iloc[index]
    shop = str(data[Shopping].iloc[0])
    tag = str(data[TAG].iloc[0])
    probe = str(data[Numero_da_probe_telemetria].iloc[0])
    local_painel = data[Local_de_instalacao].iloc[0]
    data_hora = str(data[Data].iloc[0])
    identificacao = data[Identificacao_do_ponto].iloc[0]
    luc  = data[Local_LUC].iloc[0]

   
    if pd.isna(local_painel):
        local_painel = ""
    else:
        local_painel = str(local_painel)
    if pd.isna(luc):
        luc = ""
    else:
        luc = str(luc)
    if pd.isna(identificacao):
        identificacao = ""
    else:
        identificacao = str(identificacao)

    # HTML 
    html2 = f""" 
        {style}
        
        <div class="ponto-data-card ">
            <div class="data-large-text">Dados do Ponto</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Shopping: {shop}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Tag: {tag}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Telemetria: {probe}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Local Instalação: {local_painel}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Data e hora: {data_hora}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Identificação Ponto: {identificacao}</div>
        </div>
         <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Local Luc: {luc}</div>
        </div>
        """

    return html2


#Função para pegar os dados do medidor, alicate e zordon
def pegar_dados(valor1, pref1, valor2, pref2, valor3, pref3,  data, index):
    data = data.iloc[index]

    valor_1 = data[valor1]  # Isso pode incluir informações de dtype se data[valor1] for uma Series
    pref_1 = str(data[pref1].iloc[0])  # para pegar o primeiro valor da Series

    valor_2 = data[valor2]  # Isso pode incluir informações de dtype se data[valor1] for uma Series
    pref_2 = str(data[pref2].iloc[0])  # para pegar o primeiro valor da Series

    valor_3 = data[valor3] # Isso pode incluir informações de dtype se data[valor1] for uma Series
    pref_3 = str(data[pref3].iloc[0])  # para pegar o primeiro valor da Series

    id_1 =  str(valor1)
    titulo1 = id_1.rsplit(maxsplit=1)[0]
    id_1 =  id_1.rsplit(maxsplit=1)[-1]
    id_2 =  str(valor2)
    id_2 =  id_2.rsplit(maxsplit=1)[-1]
    id_3 =  str(valor3)
    id_3 =  id_3.rsplit(maxsplit=1)[-1]
    

    if valor_1.isna().any() or np.isinf(valor_1).any():
        valor_1 = "Invalido"
    else: 
        valor_1 = f"{float(valor_1)} {str(pref_1)}"
    if valor_2.isna().any() or np.isinf(valor_2).any():
        valor_2 = "Invalido"
    else:
        valor_2 = f"{float(valor_2)} {str(pref_2)}"
    if valor_3.isna().any() or np.isinf(valor_3).any():
        valor_3 = "Invalido"
    else:
        valor_3 = f"{float(valor_3)} {str(pref_3)}"
        

    # HTML 
    html1 = f""" 
        {style}
        <div class="data-card">
        <div class="data-large-text">{titulo1}</div>
        </div>
        <div class="data-card">
            <div class="data-medium-text">{str(id_1)}</div>
            <div class="data-text">{valor_1}</div>
        </div>
        <div class="data-card">
            <div class="data-medium-text">{str(id_2)}</div>
            <div class="data-text">{valor_2} </div>
        </div>
        <div class="data-card">
            <div class="data-medium-text">{str(id_3)}</div>
            <div class="data-text">{valor_3}</div>
        </div>
        """

    
    return html1


#Função para pegar os dados da Potencia
def pegar_dados_potencia(valor1, pref1, valor2, pref2, valor3, pref3,  data, index):
    data = data.iloc[index]

    valor_1 = data[valor1].iloc[0]  # Isso pode incluir informações de dtype se data[valor1] for uma Series
    pref_1 = str(data[pref1].iloc[0])  # para pegar o primeiro valor da Series
    id_1 =    str(valor1)

    valor_2 = data[valor2].iloc[0]  # Isso pode incluir informações de dtype se data[valor1] for uma Series
    pref_2 = str(data[pref2].iloc[0])  # para pegar o primeiro valor da Series
    id_2 =    str(valor2)

    valor_3 = data[valor3].iloc[0]  # Isso pode incluir informações de dtype se data[valor1] for uma Series
    pref_3 = str(data[pref3].iloc[0])  # para pegar o primeiro valor da Series
    id_3 =    str(valor3)


    # HTML 
    html1 = f""" 
        {style}
        <div class="pot-card">
            <div class="data-medium-text">{str(id_1)}</div>
            <div class="data-text">{valor_1} {str(pref_1)}</div>
        </div>
        """
    # HTML 
    html2 = f""" 
        {style}
        <div class="pot-card">
            <div class="data-medium-text">{str(id_2)}</div>
            <div class="data-text">{valor_2} {str(pref_2)}</div>
        </div>
        """
      # HTML 
    html3 = f""" 
        {style}
        <div class="pot-card">
            <div class="data-medium-text">{str(id_3)}</div>
            <div class="data-text">{valor_3} {str(pref_3)}</div>
        </div>
        """

    col1, col2, col3 = st.columns(3)

    col1.markdown(html1, unsafe_allow_html=True)
    col2.markdown(html2, unsafe_allow_html=True)
    col3.markdown(html3, unsafe_allow_html=True)


#Função pegar dados do medidor
def pegar_dados_medidor(data, index):

    data = data.iloc[index]

    modelo_medidor = str(data[Modelo_do_medidor].iloc[0])
    endereco = str(data[Configuracao_MODBUS_Endereco].iloc[0])
    baud_Rate = str(data[Configuracao_MODBUS_Baud_Rate].iloc[0])
    paridade = str(data[Configuracao_MODBUS_Paridade].iloc[0])
    tc =  data[TC].iloc[0]
    erro = data[Codigo_de_erro].iloc[0]


    if pd.isna(tc):
        tc = ""
    else:
        tc = str(tc)
    if pd.isna(erro):
        erro = ""
    elif erro == 0:
        erro = "0 - Medidor OK"
    elif erro == 1:
        erro = "1 - Inversão ou falta de fases"
    else:
        erro = str(erro)


    html = f""" 
        {style}
        
        <div class="ponto-data-card ">
            <div class="data-large-text">Dados do Medidor</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Medidor: {modelo_medidor}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Endereço Modbus: {endereco}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Baud Rate Modbus: {baud_Rate}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Paridade Modbus: {paridade}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">TC: {tc}</div>
        </div>
        <div class="ponto-data-card">
            <div class="ponto-data-medium-text">Codigo de erro: {erro}</div>
        </div>
        """


    return html


#Função calcula diferença entre pontos e retorna a porcetagem
def diferenca_valores(valor1, pref1, valor2, pref2, data, index):
    # Selecionar os dados para o índice especificado
    data = data.iloc[index]
    
    valor_1 = data[valor1]  # Isso pode incluir informações de dtype se data[valor1] for uma Series
    pref_1 = str(data[pref1].iloc[0])  # para pegar o primeiro valor da Series
    id_1 = valor1.split(" ")[0]
    valor_2 = data[valor2]  # Isso pode incluir informações de dtype se data[valor1] for uma Series
    pref_2 = str(data[pref2].iloc[0])  # para pegar o primeiro valor da Series
    id_2 = valor2.split(" ")[0]

    grandeza = valor2.split(" ")[1]
    # Calcular a diferença percentual
    diferenca = ((valor_1 - valor_2) / valor_2) * 100

    # Arredondar os valores para duas casas decimais
    diferenca = round(diferenca, 2)

    if diferenca.isna().any() or np.isinf(diferenca).any():
        diferenca = "Invalido"
    else:
        diferenca = f"{float(diferenca)} %"
    if valor_1.isna().any() or np.isinf(valor_1).any():
        valor_1 = "Invalido"
    else: 
        valor_1 = f"{float(valor_1)} {str(pref_1)}"
    if valor_2.isna().any() or np.isinf(valor_2).any():
        valor_2 = "Invalido"
    else:
        valor_2 = f"{float(valor_2)} {str(pref_2)}"
    
    
     # HTML 
    html = f""" 
        {style}
        <div class="card">
            <div class="small-text">DIFERENÇA EM PORCENTAGEM {grandeza}</div>
            <div class="small-text">{id_1} = {valor_1} X {id_2} = {valor_2}</div>
            <div class="large-text">{diferenca}</div>
        </div>
        """

    return html


#Função desvio padrão
def desvio_padrao(valor1, pref1, valor2, pref2, valor3, pref3, data, index):

    data = data.iloc[index]
    # Extrair os dados dos valores fornecidos
    valor_1 = data[valor1]
    pref_1 = str(data[pref1].iloc[0])  # para pegar o primeiro valor da Series
    valor_2 = data[valor2]
    pref_2 = str(data[pref2].iloc[0])  # para pegar o primeiro valor da Series
    valor_3 = data[valor3]
    pref_3 = str(data[pref3].iloc[0])  # para pegar o primeiro valor da Series
    
    # Calcular o desvio padrão para cada linha
    valores = [valor_1, valor_2, valor_3]
    
    resultado_desvio_padrao = np.std(valores)
    resultado_desvio_padrao = round(resultado_desvio_padrao,2)


    # Tratamento para resultado_desvio_padrao
    if pd.isna(resultado_desvio_padrao) or np.isinf(resultado_desvio_padrao):
        resultado_desvio_padrao = "Invalido"
    else:
        resultado_desvio_padrao = float(resultado_desvio_padrao)
    
    # Tratamento para valor_1
    if pd.isna(valor_1).any() or np.isinf(valor_1).any():
        valor_1 = "Invalido"
    else:
        valor_1 = f"{float(valor_1)} {str(pref_1)}"
    
    # Tratamento para valor_2
    if pd.isna(valor_2).any() or np.isinf(valor_2).any():
        valor_2 = "Invalido"
    else:
        valor_2 = f"{float(valor_2)} {str(pref_2)}"
    # Tratamento para valor_3
    if pd.isna(valor_3).any() or np.isinf(valor_3).any():
        valor_3 = "Invalido"
    else:
        valor_3 = f"{float(valor_3)} {str(pref_3)}"
    
    titulo = valor1.split(" ")[3]
    # HTML 
    html_dp = f""" 
        {style}
        <div class="card">
            <div class="small-text">DESVIO PADRÃO {titulo}</div>
            <div class="small-text">{valor_1} | {valor_2} | {valor_3}</div>
            <div class="large-text">{resultado_desvio_padrao}</div>
        </div>
        """
    
    return html_dp


#Função para verificar balanceamento das correntes (Precisa de ajuste)
def verificar_balanceamento(data, index):
    data = data.iloc[index]
    # Supondo que as colunas das correntes sejam 'corrente_L1', 'corrente_L2', 'corrente_L3'
    correntes = data[[Medidor_Corrente_Ia, Medidor_Corrente_Ib, Medidor_Corrente_Ic]]
    
    # Calcular o desvio padrão das correntes
    desvio_padrao = correntes.std()
    
    # Definir um limite para desequilíbrio
    limite_desequilibrio = 1  # Defina um limite adequado
    desequilibrio = desvio_padrao > limite_desequilibrio
    
    return [desequilibrio, desvio_padrao]


#Função para verificar a qualidade da energia nas tensões (Precisa de ajustes)
def verificar_qualidade_energia(data, index):
    data = data.iloc[index]
    # Supondo que as colunas das tensões sejam 'Medidor_Tensao_Van', 'Medidor_Tensao_Vbn', 'Medidor_Tensao_Vcn' e a tensão nominal seja 230V
    tensoes = data[[Medidor_Tensao_Van, Medidor_Tensao_Vbn, Medidor_Tensao_Vcn]]
    
      # Definir a tensão nominal
    tensao_nominal = 230
    
    # Calcular a diferença percentual em relação à tensão nominal
    diferenca_percentual = (tensoes - tensao_nominal) / tensao_nominal * 100
    
    # Definir um limite para qualidade de energia
    limite_qualidade = 5  # Defina um limite adequado
    qualidade_ruim = (diferenca_percentual.abs() > limite_qualidade).any()
    
    return qualidade_ruim, diferenca_percentual


# Função para exibir gráficos gerais
def exibir_graficos():
    # Contagem dos modelos de medidor
    medidor_contagem = df["Modelo do medidor"].value_counts().reset_index()
    medidor_contagem.columns = ['Modelo do medidor', 'Quantidade']
    
    # Gráfico de pizza para medidores
    fig_medidor = px.pie(medidor_contagem, values='Quantidade', names='Modelo do medidor', hole=0.5,
                         title='Modelos de Medidores')

    # Contar a ocorrência de cada código de erro
    erro_cod = df["Código de erro"].value_counts().reset_index()
    erro_cod.columns = ['Código de erro', 'Quantidade']
    
    # Mapear os códigos de erro para as legendas apropriadas
    legend_map = {0: 'Sem erros', 1: 'Inversão ou falta de fases'}
    erro_cod['Código de erro'] = erro_cod['Código de erro'].replace(legend_map)
    
    # Definir cores personalizadas
    colors = ['green', 'darkred']
    
    # Gráfico de pizza com cores personalizadas para erros
    fig_erro = px.pie(erro_cod, values='Quantidade', names='Código de erro', hole=0.5, 
                      color_discrete_sequence=colors, title='Distribuição dos Códigos de Erro')
    
    # Exibir gráficos lado a lado
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_medidor,use_container_width=True)
    with col2:
        st.plotly_chart(fig_erro, use_container_width=True)


# Função para calcular contagem de probes e plotar gráfico
def plot_probe_counts(df):
    # Calcular contagem de probes e pontos instalados
    contagem_probe = df[Numero_da_probe_telemetria].value_counts()
    quantidade_probe = len(contagem_probe)
    ponto_instalados = contagem_probe.sum()

    # Montar o HTML para exibir informações sobre as probes
    html =f"""{style}
    <div class="probes-data-card">
        <div class="medium-text">Quantidade de probes: {quantidade_probe} X Pontos instalados: {ponto_instalados}</div>
    </div>

    """
    st.markdown(html, unsafe_allow_html=True)
  
 # Configurar estilo para o gráfico
    plt.style.use('default')  # Voltar ao estilo padrão do Matplotlib

    # Plotar o gráfico de barras com fundo cinza e barras brancas
    plt.figure(figsize=(10, 6), facecolor='#B0C4DE')  # Tamanho opcional da figura
    plt.barh(contagem_probe.index, contagem_probe.values)  # Cor das barras é cinza
    plt.xlabel('Número da Probe')
    plt.ylabel('Probes')
    plt.title('Contagem de Número da Probe')
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor legibilidade
    plt.gca().set_facecolor('#B0C4DE')  # Define a cor de fundo do gráfico como cinza claro

    st.pyplot(plt)  # Mostra o gráfico no Streamlit


#Função para criar colunas para calculos
def colunas_calculos(valor1, pref1, valor2, pref2, valor3, pref3, data, ind):
    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(diferenca_valores(valor1, pref1, valor2, pref2 ,data, ind), unsafe_allow_html=True)
    col2.markdown(diferenca_valores(valor1, pref1 ,valor3, pref3, data, ind), unsafe_allow_html=True)
    col3.markdown(diferenca_valores(valor2, pref2, valor3, pref3,  data, ind), unsafe_allow_html=True)
    col4.markdown(desvio_padrao(valor1, pref1, valor2, pref2, valor3, pref3, data, ind), unsafe_allow_html=True)
        

# Configuração da barra lateral para navegação
st.sidebar.title("Navegação")
opcao = st.sidebar.radio("Opções - Shopping Botafogo", ["Visão geral - Shopping Botafogo", "Área comum - Shopping Botafogo"])


# Página de gráficos gerais
if opcao == "Visão geral - Shopping Botafogo":
    st.markdown("<h1 style='text-align: center;'>Visualização Geral</h1>", unsafe_allow_html=True)
    exibir_graficos()
    plot_probe_counts(df)


# Página de dados dos pontos
elif opcao == "Área comum - Shopping Botafogo":
    
    tags = df['TAG'].tolist()
    selected_tag  = st.sidebar.selectbox("Selecionar o local", tags)
    st.markdown("""<h1 style='text-align: center;'>Área comum - Shopping Botafogo</h1>""", unsafe_allow_html=True)
    filtered_df = df[df['TAG'] == selected_tag]
    index = df.index[df['TAG'] == selected_tag]
    
    
    col1, col2, col3, col4 = st.columns(4)
    
    
    col1.markdown(dados_ponto(df, index), unsafe_allow_html=True)
    col3.markdown(pegar_dados_medidor(df, index), unsafe_allow_html=True)
    
    st.divider()
    st.markdown("""<h3 style='text-align: center;'>Grandezas</h3>""", unsafe_allow_html=True)
    with st.expander("Grandezas do Medidor"):
        col1, col2, col3 = st.columns(3)  
        col1.markdown(pegar_dados(Medidor_Corrente_Ia, Medidor_Prefixo_Ia, Medidor_Corrente_Ib, Medidor_Prefixo_Ib, Medidor_Corrente_Ic, Medidor_Prefixo_Ic, df, index), unsafe_allow_html=True)
        col2.markdown(pegar_dados(Medidor_Tensao_Van, Medidor_Prefixo_Van, Medidor_Tensao_Vbn, Medidor_Prefixo_Vbn, Medidor_Tensao_Vcn, Medidor_Prefixo_Vcn, df, index), unsafe_allow_html=True)
        col3.markdown(pegar_dados(Medidor_Tensao_Vab, Medidor_Prefixo_Vab, Medidor_Tensao_Vbc, Medidor_Prefixo_Vbc, Medidor_Tensao_Vca, Medidor_Prefixo_Vca, df, index), unsafe_allow_html=True)
    
    with st.expander("Grandezas do Alicate"):
        col1, col2, col3 = st.columns(3)  
        col1.markdown(pegar_dados(Alicate_Ia, Alicate_Prefixo_Ia, Alicate_Ib, Alicate_Prefixo_Ib, Alicate_Ic, Alicate_Prefixo_Ic, df, index), unsafe_allow_html=True)
        col2.markdown(pegar_dados(Alicate_Van, Alicate_Prefixo_Van, Alicate_Vbn, Alicate_Prefixo_Vbn, Alicate_Vcn, Alicate_Prefixo_Vcn, df, index), unsafe_allow_html=True)
        col3.markdown(pegar_dados(Alicate_Vab, Alicate_Prefixo_Vab, Alicate_Vbc, Alicate_Prefixo_Vbc, Alicate_Vca, Alicate_Prefixo_Vca, df, index), unsafe_allow_html=True)
    
    with st.expander("Grandezas do Alicate"):
        col1, col2, col3 = st.columns(3)  
        col1.markdown(pegar_dados(Zordon_Ia, Zordon_Prefixo_Ia, Zordon_Ib, Zordon_Prefixo_Ib, Zordon_Ic, Zordon_Prefixo_Ic, df, index), unsafe_allow_html=True)
        col2.markdown(pegar_dados(Zordon_Van, Zordon_Prefixo_Van, Zordon_Vbn, Zordon_Prefixo_Vbn, Zordon_Vcn, Zordon_Prefixo_Vcn, df, index), unsafe_allow_html=True)
        col3.markdown(pegar_dados(Zordon_Vab, Zordon_Prefixo_Vab, Zordon_Vbc, Zordon_Prefixo_Vbc, Zordon_Vca, Zordon_Prefixo_Vca, df, index), unsafe_allow_html=True)
    
        pegar_dados_potencia(Zordon_Energia_Ativa_Acumulada, Zordon_Prefixo_Energia_Ativa, 
                                Zordon_Potencia_Ativa, Zordon_Prefixo_Potencia_Ativa,
                                Zordon_Potencia_Reativa, Zordon_Prefixo_Potencia_Reativa, df, index)
    st.divider()
    
    st.markdown("""<h3 style='text-align: center;'>Calculos</h3>""", unsafe_allow_html=True)
    with st.expander("Calculos das Correntes:"):
      
        colunas_calculos(Medidor_Corrente_Ia, Medidor_Prefixo_Ia, Alicate_Ia, Alicate_Prefixo_Ia, Zordon_Ia, Zordon_Prefixo_Ia, df, index)
        colunas_calculos(Medidor_Corrente_Ib, Medidor_Prefixo_Ib, Alicate_Ib, Alicate_Prefixo_Ib, Zordon_Ib, Zordon_Prefixo_Ib, df, index)
        colunas_calculos(Medidor_Corrente_Ic, Medidor_Prefixo_Ic, Alicate_Ic, Alicate_Prefixo_Ic, Zordon_Ic, Zordon_Prefixo_Ic, df, index)
    
    with st.expander("Calculos das Tensão Vn:"):
      
        colunas_calculos(Medidor_Tensao_Van, Medidor_Prefixo_Van, Alicate_Van, Alicate_Prefixo_Van, Zordon_Van, Zordon_Prefixo_Van, df, index)
        colunas_calculos(Medidor_Tensao_Vbn, Medidor_Prefixo_Vbn, Alicate_Vbn, Alicate_Prefixo_Vbn, Zordon_Vbn, Zordon_Prefixo_Vbn, df, index)
        colunas_calculos(Medidor_Tensao_Vcn, Medidor_Prefixo_Vcn, Alicate_Vcn, Alicate_Prefixo_Vcn, Zordon_Vcn, Zordon_Prefixo_Vcn, df, index)
    
    with st.expander("Calculos das Tensão Trifasica:"):
      
        colunas_calculos(Medidor_Tensao_Vab, Medidor_Prefixo_Vab, Alicate_Vab, Alicate_Prefixo_Vab, Zordon_Vab, Zordon_Prefixo_Vab, df, index)
        colunas_calculos(Medidor_Tensao_Vbc, Medidor_Prefixo_Vbc, Alicate_Vbc, Alicate_Prefixo_Vbc, Zordon_Vbc, Zordon_Prefixo_Vbc, df, index)
        colunas_calculos(Medidor_Tensao_Vca, Medidor_Prefixo_Vca, Alicate_Vca, Alicate_Prefixo_Vca, Zordon_Vca, Zordon_Prefixo_Vca, df, index)

    with st.expander("Observações:"):
        pass