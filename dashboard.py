import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

customers_df = pd.read_csv("customers_dataset.csv")
order_items_df = pd.read_csv("order_items_dataset.csv")
order_payments_df = pd.read_csv("order_payments_dataset.csv")
order_df = pd.read_csv("orders_dataset.csv")
product_category_df =  pd.read_csv("product_category_name_translation.csv")
product_df = pd.read_csv("products_dataset.csv")
seller_df = pd.read_csv("sellers_dataset.csv")

def new_orderpayment (df) :
    order_payments_df.groupby(by="payment_type").agg({
    "order_id": "nunique"
},inplace=True)
    
def top5(df):
    customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False).head(5)

d1 = pd.read_csv("d1.csv")
d2 = pd.read_csv("d2.csv")

min_date = d1["order_purchase_timestamp"].min()
max_date = d1["order_purchase_timestamp"].max()

with st.sidebar:
    st.image(
        "https://raw.githubusercontent.com/byfidid/ProyekDataAnalisis/main/IMG_20221106_172529.png",
        caption="Fidya Faras."
    )
    
st.title('Submission Memulai Pemrograman Data dengan Python')
st.header('Proyek Analisis Data :bear:')
st.subheader('5 negara bagian teratas dengan jumlah pesanan terbanyak')

fig, ax = plt.subplots(figsize=(20, 10))

bystate_df = d2.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False).reset_index().head(5)
bystate_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)

colors_ = ["#8A2F19", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="customer_count",
    y="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors_
)
ax.set_title("5 negara bagian teratas dengan jumlah pesanan terbanyak", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=12)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

st.subheader('Metode pembayaran yang paling banyak digunakan')

fig, ax = plt.subplots(figsize=(20, 10))

bypayment_df = d1.groupby(by="payment_type").customer_id.nunique().reset_index()
bypayment_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)

colors_ = ["#8A2F19", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="customer_count",
    x="payment_type",
    data=bypayment_df.sort_values(by="customer_count", ascending=False),
    palette=colors_
)
ax.set_title("Metode pembayaran yang paling banyak digunakan", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

st.caption('Copyright (c) Fidya Farasalsabila, 2025')
