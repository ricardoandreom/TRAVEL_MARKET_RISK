import plotly.graph_objects as go
from config import *
import plotly.express as px
import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore


def fear_greed_plot(df):
    rating_value = df['Rating'].iloc[-1]

    if rating_value <= 25:
        text_color = 'red'
        sentiment = "Extreme Fear"
    elif rating_value <= 50:
        text_color = 'orange'
        sentiment = "Fear"
    elif rating_value <= 75:
        text_color = 'lightgreen'
        sentiment = "Greed"
    else:
        text_color = 'green'
        sentiment = "Extreme Greed"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=rating_value,
        title={'text': "Current score", 'font': {'size': 20, 'color': 'black', 'family': 'Arial Black'}},
        gauge={
            'axis': {
                'range': [0, 100],
                'tickmode': 'array',
                'tickvals': [0, 25, 50, 75, 100],
                'ticktext': ['0', '25', '50', '75', '100']
            },
            'bar': {'color': "black"},
            'steps': [
                {'range': [0, 25], 'color': 'red', 'name': 'Extreme Fear'},
                {'range': [25, 45], 'color': 'orange', 'name': 'Fear'},
                {'range': [45, 55], 'color': 'white', 'name': 'Neutral'},
                {'range': [55, 75], 'color': 'lightgreen', 'name': 'Greed'},
                {'range': [75, 100], 'color': 'green', 'name': 'Extreme Greed'}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': rating_value
            }
        },
        number={'font': {'color': text_color, 'size': 90}}
    ))

    fig.add_annotation(
        text=sentiment,
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=20, color=text_color, weight='bold'),
        align='center'
    )

    #fig.add_annotation(text="EXTREME", x=0.36, y=0.25, showarrow=False, font=dict(size=15, color='black', weight='bold'))

    # Use st.plotly_chart em vez de fig.show() no Streamlit
    st.plotly_chart(fig, use_container_width=True)


def plot_interactive_time_series(df, option_to_choose_variables='yes'):
    df['Date'] = pd.to_datetime(df['Date']).dt.date

    if option_to_choose_variables != 'yes':
        columns_to_plot = df.columns[1:]
    else:
        columns_to_plot = st.multiselect(
            'Select columns to plot',
            options=df.columns[1:],
            default=df.columns[1:]
        )

    if len(columns_to_plot) > 0:
        fig = px.line(
            df,
            x='Date',
            y=columns_to_plot,
            labels={"value": "Rate", "Date": "Date"},
            height=600
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Values",
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1, label="1M", step="month", stepmode="backward"),
                        dict(count=3, label="3M", step="month", stepmode="backward"),
                        dict(count=6, label="6M", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1Y", step="year", stepmode="backward"),
                        dict(step="all", label="All")
                    ])
                ),
                rangeslider=dict(visible=True),
                type="date"
            ),
            plot_bgcolor='rgba(0, 0, 0, 0)',
            yaxis=dict(showgrid=True, gridcolor='lightgray'),
            hovermode="x unified",
        )

        colors = [default_color2, default_color1, 'black', 'pink', 'blue', 'red', 'skyblue']

        if len(columns_to_plot) == 1:
            fig.update_traces(
                mode='lines+markers',
                line=dict(width=1),
                marker=dict(size=5, symbol='circle', color=default_color1, line=dict(width=1, color=default_color1)),
                hovertemplate='%{y:.2f}<extra></extra>'
            )
        else:
            for idx, column in enumerate(columns_to_plot):
                color = colors[idx % len(colors)]
                fig.update_traces(
                    selector=dict(name=column),
                    mode='lines+markers',
                    line=dict(width=1, color=color),
                    marker=dict(size=4, symbol='circle', color=color),
                    hovertemplate='%{y:.2f}<extra></extra>'
                )

        fig.update_layout(
            showlegend=True
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Please select at least one column to plot.")


def plot_interactive_time_series_years(df, option_to_choose_variables='yes'):
    #df['Date'] = pd.to_datetime(df['Date']).dt.date

    if option_to_choose_variables != 'yes':
        columns_to_plot = df.columns[1:]
    else:
        columns_to_plot = st.multiselect(
            'Select columns to plot',
            options=df.columns[1:],
            default=df.columns[1:]
        )

    if len(columns_to_plot) > 0:
        fig = px.line(
            df,
            x='Year',
            y=columns_to_plot,
            labels={"value": "Rate", "Date": "Year"},
            height=600
        )

        fig.update_layout(
            xaxis_title="Year",
            yaxis_title="Values",
            plot_bgcolor='rgba(0, 0, 0, 0)',
            yaxis=dict(showgrid=True, gridcolor='lightgray'),
            hovermode="x unified",
        )

        colors = [default_color2, default_color1, 'black', 'pink', 'blue', 'red', 'skyblue']

        if len(columns_to_plot) == 1:
            fig.update_traces(
                mode='lines+markers',
                line=dict(width=1),
                marker=dict(size=5, symbol='circle', color=default_color1, line=dict(width=1, color=default_color1)),
                hovertemplate='%{y:.2f}<extra></extra>'
            )
        else:
            for idx, column in enumerate(columns_to_plot):
                color = colors[idx % len(colors)]
                fig.update_traces(
                    selector=dict(name=column),
                    mode='lines+markers',
                    line=dict(width=1, color=color),
                    marker=dict(size=4, symbol='circle', color=color),
                    hovertemplate='%{y:.2f}<extra></extra>'
                )

        fig.update_layout(
            showlegend=True
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Please select at least one column to plot.")


def calculate_anomalies(df_aux, column, method, threshold=3, contamination=0.01):

    df_copy = df_aux.copy()

    # Verificar se a coluna existe no DataFrame
    if column not in df_copy.columns:
        raise ValueError(f"A coluna '{column}' não existe no DataFrame.")

    # Verificar se a coluna contém apenas valores numéricos
    if not pd.api.types.is_numeric_dtype(df_copy[column]):
        raise ValueError(f"A coluna '{column}' deve ser numérica para calcular anomalias.")

    # Tratar valores ausentes (NaN) antes de continuar
    if df_copy[column].isnull().any():
        df_copy[column] = df_copy[column].fillna(df_copy[column].mean())  # Preencher NaN com a média da coluna

    if method == 'zscore':
        df_copy['Z-Score'] = zscore(df_copy[column])
        df_copy['Anomaly'] = df_copy['Z-Score'].abs() > threshold
    elif method == 'isolation_forest':
        model = IsolationForest(contamination=contamination)
        df_copy['Anomaly'] = model.fit_predict(df_copy[[column]]) == -1
    else:
        raise ValueError("Método inválido. Use 'zscore' ou 'isolation_forest'.")

    # Retornar a cópia do DataFrame com as alterações
    return df_copy


def plot_anomalies(df, column, method='zscore'):

    df = calculate_anomalies(df, column, method)

    fig = px.line(df, x='Date', y=column, labels={'value': column, 'Date': 'Date'}, height=600)

    fig.add_scatter(x=df[df['Anomaly'] == True]['Date'],
                    y=df[df['Anomaly'] == True][column],
                    mode='markers',
                    name='Anomalies',
                    marker=dict(color='red', size=8, symbol='x'))

    fig.update_layout(
        title=f"Anomalies in {column}",
        xaxis_title="Date",
        yaxis_title="Value",
        plot_bgcolor='rgba(0, 0, 0, 0)',
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        hovermode="x unified",
    )

    st.plotly_chart(fig, use_container_width=True)
