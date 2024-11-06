import streamlit as st
from viz import *
from get_data import *
from config import *
from load_data import *
import warnings
warnings.filterwarnings("ignore")
from xlsxwriter import Workbook

#################################################### BUILD DASHBOARD ############################################

st.set_page_config(page_title=dashboard_main_title, layout="wide")
st.markdown(f"<h1 style='color:{default_color1};'>{dashboard_main_title}</h1>", unsafe_allow_html=True)

# white Logo
st.sidebar.markdown(f'<a><img src="{travel_logo_url}" alt="Logo" style="width: 100%;"></a>', unsafe_allow_html=True)

st.sidebar.header("Select index:")
indicador = st.sidebar.selectbox(
    "Choose an indicator to analyse:", sidebar_indicators
)

if indicador == "Fear & Greed Index":
    st.markdown(f"<div style='text-align: center;'><h2>Fear & Greed (CNN index)</h2></div>", unsafe_allow_html=True)
    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_greed_fear, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_greed_fear),
                           file_name='greed_fear.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    fear_greed_plot(df_greed_fear)

    plot_interactive_time_series(df_greed_fear[['Date', 'Rating']], option_to_choose_variables='no')

    if st.sidebar.checkbox("Show anomalies"):
        method = st.selectbox("Select anomaly detection method", options=["zscore", "isolation_forest"])
        plot_anomalies(df_greed_fear, 'Rating', method)

elif indicador == "Warren Buffett indicator - Marketcap to GDP":
    st.markdown(f"<div style='text-align: center;'><h2>Warren Buffett indicator - Marketcap to GDP</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_warren_buff, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_warren_buff),
                           file_name='warren_buffett_index.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_warren_buff[['Date', 'Indicador de Warren Buffett (%)']], option_to_choose_variables='no')

    if st.sidebar.checkbox("Show anomalies"):
        method = st.selectbox("Select anomaly detection method", options=["zscore", "isolation_forest"])
        plot_anomalies(df_warren_buff, 'Indicador de Warren Buffett (%)', method)

elif indicador == "VIX":
    st.markdown(f"<div style='text-align: center;'><h2>VIX - Volatility index</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_vix, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_vix),
                           file_name='vix.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_vix, option_to_choose_variables='no')

    if st.sidebar.checkbox("Show anomalies"):
        method = st.selectbox("Select anomaly detection method", options=["zscore", "isolation_forest"])
        plot_anomalies(df_vix, 'VIX', method)

elif indicador == "Benchmark Indexs":
    st.markdown(f"<div style='text-align: center;'><h2>Benchmark Indexs</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_benchmarks, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_benchmarks),
                           file_name='benchmarks.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_benchmarks)

    if st.sidebar.checkbox("Show anomalies"):
        column = st.selectbox("Select column to analyze anomalies", options=df_benchmarks.columns[1:], index=0)
        method = st.selectbox("Select anomaly detection method", options=["zscore", "isolation_forest"])
        plot_anomalies(df_benchmarks, column, method)

elif indicador == "Euribor rates - 1M, 3M, 6M, 12M":
    st.markdown(f"<div style='text-align: center;'><h2>Euribor rates - 1M, 3M, 6M, 12M</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_eur, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_eur),
                           file_name='euribors.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_eur)

elif indicador == "Yield Bonds 5Y - Spain, Germany, Portugal, Euro Area":
    st.markdown(f"<div style='text-align: center;'><h2>Yield Bonds 5Y - Spain, Germany, Portugal, Euro Area</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_all_bonds, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_all_bonds),
                           file_name='bonds_5y.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_all_bonds)

elif indicador == "Yield CDS 5Y - Spain, Germany, USA":
    st.markdown(f"<div style='text-align: center;'><h2>Yield bonds 5Y - Spain, Germany, USA</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_all_cds, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_all_cds),
                           file_name='cds_5y.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_all_cds)

elif indicador == "Commercial Property prices":
    st.markdown(f"<div style='text-align: center;'><h2>Commercial Property prices - Portugal and Euro Area</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_aux_cppi, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_aux_cppi),
                           file_name='cppi.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series_years(df_aux_cppi)

elif indicador == "Residential Property prices":
    st.markdown(f"<div style='text-align: center;'><h2>Residential Property prices - Portugal and Euro Area</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_hpi, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_hpi),
                           file_name='residential_price_index.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_hpi)

    if st.sidebar.checkbox("Show anomalies"):
        column = st.selectbox("Select column to analyze anomalies", options=df_hpi.columns[1:], index=0)
        method = st.selectbox("Select anomaly detection method", options=["zscore", "isolation_forest"])
        plot_anomalies(df_hpi, column, method)

elif indicador == "Inflation - Portugal":
    st.markdown(f"<div style='text-align: center;'><h2>Inflation - Portugal</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_ipc_pt, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_ipc_pt),
                           file_name='inflation_portugal.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_ipc_pt, option_to_choose_variables='no')

elif indicador == "Currency exchange rates":
    st.markdown(f"<div style='text-align: center;'><h2>Currency exchange rates</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_fx, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_fx),
                           file_name='fx_rates.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_fx)

elif indicador == "Euro short-term rate (€STR)":
    st.markdown(f"<div style='text-align: center;'><h2>Euro short-term rate (€STR)</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_ir_str, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_ir_str),
                           file_name='short_term_rates.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_ir_str, option_to_choose_variables='no')

    if st.sidebar.checkbox("Show anomalies"):
        method = st.selectbox("Select anomaly detection method", options=["zscore", "isolation_forest"])
        plot_anomalies(df_ir_str, 'IR STR', method)

    st.markdown(ir_str_str, unsafe_allow_html=True)

elif indicador == "SOFR":
    st.markdown(f"<div style='text-align: center;'><h2>SOFR</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_sofr, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_sofr),
                           file_name='sofr.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_sofr, option_to_choose_variables='no')

    st.markdown(sofr_str, unsafe_allow_html=True)

elif indicador == "Key ECB interest rates":
    st.markdown(f"<div style='text-align: center;'><h2>Key ECB interest rates</h2></div>", unsafe_allow_html=True)

    if st.sidebar.checkbox("Show raw data"):
        st.markdown(f"<h6 style='color:{default_color1};'>Raw data</h6>", unsafe_allow_html=True)
        st.dataframe(df_key_ecb_ir, hide_index=True)

        st.download_button(label="Download in xlsx format",
                           data=convert_df_to_excel(df_key_ecb_ir),
                           file_name='key_ecb_ir.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    plot_interactive_time_series(df_key_ecb_ir)

    st.markdown(key_ecb_str, unsafe_allow_html=True)




