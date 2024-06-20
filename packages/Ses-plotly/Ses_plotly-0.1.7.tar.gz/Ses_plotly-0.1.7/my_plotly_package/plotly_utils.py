
import json
import unidecode
import geopandas as gpd
import plotly.express as px
import pandas as pd
import geopandas as gpd
import json
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go



def criar_grafico_barras(dataframe, x_valores, y_valores, titulo, altura, largura, matriz, coluna_rotulo, cores_matriz, nome_eixos, orientacao):
    fig2 = px.bar(
        dataframe,
        x=x_valores,
        y=y_valores,
        color=matriz,
        title=titulo,
        barmode='group',
        text=coluna_rotulo,
        color_discrete_map=cores_matriz,
        labels=nome_eixos,
        orientation=orientacao  # Adicionando a orientação horizontal
    )
    fig2.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        height=altura,
        width=largura,
        xaxis_title=x_valores,
        yaxis_title=y_valores
    )

    fig2.update_layout(
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1.1,
            xanchor="center",
            x=-0.12
        )
    )
    return fig2


def processo_geojson_municipio(dataframe, geojson_path):
    with open(geojson_path, 'r', encoding='utf-8') as geojson_file5:
        geojson_data5 = json.load(geojson_file5)
    geojson_df5 = pd.DataFrame(geojson_data5['features'])
    geojson_df5['GEOCODIGO'] = geojson_df5['properties'].apply(lambda x: x.get('GEOCODIGO'))
    geojson_df5['Município'] = geojson_df5['properties'].apply(lambda x: x.get('Município'))
    geojson_df5['Município'] = geojson_df5['Município'].str.upper()
    geojson_df5


    merged_data5 = pd.merge(dataframe, geojson_df5, left_on='Municipio', right_on='Município', how='left')
    gdf_geojson5 = gpd.GeoDataFrame.from_features(geojson_data5['features'])
    gdf_geojson5.crs = 'EPSG:4326'
    gdf_geojson5['Município'] = gdf_geojson5['Município'].str.upper()
    gdf_geojson5 = gdf_geojson5.merge(merged_data5, left_on='Município', right_on='Município', how='left')
    gdf_geojson5 = gpd.GeoDataFrame(gdf_geojson5, geometry='geometry_x', crs='EPSG:4326')
    geojson_for_plot5 = json.loads(gdf_geojson5.to_json())
    return geojson_for_plot5



def processo_geojson_regiao(dataframe, geojson_path):
    with open(geojson_path, 'r', encoding='utf-8') as geojson_file:
        geojson_data = json.load(geojson_file)
    
    geojson_df = pd.DataFrame(geojson_data['features'])
    geojson_df['GEOCODIGO'] = geojson_df['properties'].apply(lambda x: x.get('GEOCODIGO'))
    geojson_df['REGIAO_SAU'] = geojson_df['properties'].apply(lambda x: x.get('REGIAO_SAU'))
    geojson_df['coordinates'] = geojson_df['geometry'].apply(lambda x: x.get('coordinates'))
    geojson_df['GEOCODIGO'] = geojson_df['GEOCODIGO'].astype(str)
    geojson_df = geojson_df.rename(columns={'REGIAO_SAU': 'regiao_saude'})
    
    merged_data = pd.merge(left=dataframe, right=geojson_df, left_on='Região Saude', right_on='regiao_saude', how='left')
    
    gdf_geojson = gpd.GeoDataFrame.from_features(geojson_data['features'])
    gdf_geojson.crs = 'EPSG:4326'
    gdf_geojson['GEOCODIGO'] = gdf_geojson['GEOCODIGO'].astype(str)
    merged_data['GEOCODIGO'] = merged_data['GEOCODIGO'].astype(str)
    gdf_geojson = gdf_geojson.merge(merged_data, left_on='GEOCODIGO', right_on='GEOCODIGO', how='left')
    
    gdf_geojson = gpd.GeoDataFrame(gdf_geojson, geometry='geometry_x', crs='EPSG:4326')
    geojson_for_plot = json.loads(gdf_geojson.to_json())
    
    return geojson_for_plot


def mapa_coropletico(dataframe, geojson, localizacao, key_geojson, coloracao, hover_data, estilo_mapa, zoom, coordenadas_centralizar, opacite, escala_coloracao, altura, largura, titulo):
    """
    Cria um mapa coroplético usando Plotly Express.

    Parametros:
    dataframe = DataFrame contendo os dados a serem plotados.
    geojson = Dados GeoJSON para o mapa.
    localizacao = Nome da coluna no DataFrame que contém os identificadores de localização.
    key_geojson = Chave no GeoJSON que corresponde aos identificadores de localização.
    coloracao = Nome da coluna no DataFrame para definir a cor.
    hover_data = Lista de colunas no DataFrame para exibir nos dados de hover.
    estilo_mapa  = Estilo do mapa Mapbox.
    zoom = Nível de zoom do mapa.
    coordenadas_centralizar = Dicionário com 'lat' e 'lon' para centralizar o mapa.
    opacite = Opacidade das áreas do mapa.
    escala_coloracao = Escala de cores para o mapa.
    largura = Largura da figura.
    altura = Altura da figura.
    titulo = Título do mapa.

    Returns:
    Figure: Figura do Plotly Express.
    """
    
    figure = px.choropleth_mapbox(
        dataframe,
        geojson=geojson,
        locations=localizacao,
        featureidkey=key_geojson,
        color=coloracao,
        hover_data=hover_data,
        mapbox_style=estilo_mapa,
        zoom=zoom,
        center=coordenadas_centralizar,
        opacity=opacite,
        color_continuous_scale=escala_coloracao,
        color_continuous_midpoint=True
    )
    figure.update_layout(
        height=altura,
        width=largura,
        coloraxis_showscale=True,
        coloraxis_colorbar=dict(
            yanchor="bottom",
            len=0.5,
            y=0.05,
            xanchor="left",
            x=0.05
        ),
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        title_text=titulo,
        title_x=0.5,
        title_font=dict(
            family="Arial",
            size=20,
            color='black'
        )
    )
    return figure

def criar_grafico_pizza_simples(dataframe, valores, nomes, titulo, altura, largura, cores_matriz):
    fig = px.pie(
        dataframe,
        values=valores,
        names=nomes,
        title=titulo,
        color=nomes,
        color_discrete_map=cores_matriz
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        width=largura,
        height=altura
    )
    return fig


def card(valor, altura,largura, titulo):
    titulo_ = f"<span style='font-size:14px; font-weight:bold'><b>{titulo}</b></span>"
    valores = f"{titulo_}<br><span style='font-size:27px'>{valor}</span>"

    card_layout = go.Layout(
        height=altura,
        width=largura,
        title="",  # Remova o título do indicador
        paper_bgcolor="#f8f9fa",  # Define a cor de fundo do interior do card como transparente
        plot_bgcolor="#f8f9fa",  # Define a cor de fundo do gráfico como transparente
        margin={'l': 1, 't': 1, 'b': 2, 'r': 1},
        xaxis={'visible': False},  # Remove a escala numérica do eixo x
        yaxis={'visible': False},   # Remove a escala numérica do eixo y
        annotations=[{
            'x': 0.5,  # Define a posição horizontal do texto no cartão (no meio)
            'y': 0.5,  # Define a posição vertical do texto no cartão (no meio)
            'xref': 'paper',
            'yref': 'paper',
            'text': valores,  # Adiciona o texto combinado como anotação
            'showarrow': False,  # Não mostra a seta de indicação
            'font': {'size': 19},  # Define o tamanho da fonte da anotação para os valores
            'align': 'center',  # Alinha o texto ao centro
        }]
    )

    return go.Figure(layout=card_layout)

def card_porcentagem(valor, altura,largura, titulo):
    titulo_ = f"<span style='font-size:14px; font-weight:bold'><b>{titulo}</b></span>"
    valores = f"{titulo_}<br><span style='font-size:27px'>{valor:.2f}%</span>"

    card_layout = go.Layout(
        height=altura,
        width=largura,
        title="",  # Remova o título do indicador
        paper_bgcolor="#f8f9fa",  # Define a cor de fundo do interior do card como transparente
        plot_bgcolor="#f8f9fa",  # Define a cor de fundo do gráfico como transparente
        margin={'l': 1, 't': 1, 'b': 2, 'r': 1},

        xaxis={'visible': False},  # Remove a escala numérica do eixo x
        yaxis={'visible': False},   # Remove a escala numérica do eixo y
        annotations=[{
            'x': 0.5,  # Define a posição horizontal do texto no cartão (no meio)
            'y': 0.5,  # Define a posição vertical do texto no cartão (no meio)
            'xref': 'paper',
            'yref': 'paper',
            'text': valores,  # Adiciona o texto combinado como anotação
            'showarrow': False,  # Não mostra a seta de indicação
            'font': {'size': 19},  # Define o tamanho da fonte da anotação para os valores
            'align': 'center',  # Alinha o texto ao centro
        }]
    )

    return go.Figure(layout=card_layout)


def grafico_linhas(tabela, eixo_x, eixo_y, colocarao, titulo, label, altura, largura):
    fig = px.line(tabela, 
                x=eixo_x, 
                y=eixo_y, 
                color=colocarao, 
                title=titulo,
                labels=label,
                height=altura,
                width=largura)

    return fig
