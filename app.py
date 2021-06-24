import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
df = pd.read_csv('vehicles_us.csv')
st.header('Data Viewer')
df['manufacturer'] = df['model'].apply(lambda x: x.split(' ')[0])
ckbox = st.checkbox(
    'Include manufacturers with less than 1000 ads', value=True)
if not ckbox:
    df = df.groupby('manufacturer').filter(
        lambda x: len(x) <= 1000).reset_index()
df
st.header('Vehicles by manufacturer')
fig = px.histogram(df, x='manufacturer', color='type')
st.write(fig)
st.header('Vehicles by model year and condition')
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)
manufacturer_list = sorted(df['manufacturer'].unique())
manufacturer_1 = st.selectbox(
    'manufacturer #1', manufacturer_list, index=manufacturer_list.index('ford'))
manufacturer_2 = st.selectbox(
    'manufacturer #2', manufacturer_list, index=manufacturer_list.index('chevrolet'))
mask_filter = (df['manufacturer'] == manufacturer_1) | (
    df['manufacturer'] == manufacturer_2)
df_filter = df[mask_filter]
df_filter
fig = px.histogram(df_filter, x='price', nbins=30,
                   color='manufacturer', histnorm='percent', barmode='overlay')
st.write(fig)
