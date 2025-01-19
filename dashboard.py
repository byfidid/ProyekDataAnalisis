import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
d1 = pd.read_csv("d1.csv")
min_date = d1["order_purchase_timestamp"].min()
max_date = d1["order_purchase_timestamp"].max()

# Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/byfidid/ProyekDataAnalisis/main/IMG_20221106_172529.png", caption="Fidya Faras.")
    start_date = st.date_input("Tanggal Mulai", min_date)
    end_date = st.date_input("Tanggal Akhir", max_date)
    payment_types = d1['payment_type'].unique()
    selected_payment = st.selectbox("Pilih Metode Pembayaran", payment_types)

# Filter data
filtered_df = d1[(d1['order_purchase_timestamp'] >= str(start_date)) & 
                  (d1['order_purchase_timestamp'] <= str(end_date))]

if selected_payment:
    filtered_df = filtered_df[filtered_df['payment_type'] == selected_payment]

# Visualisasi
st.title('Submission Memulai Pemrograman Data dengan Python')
st.header('Proyek Analisis Data :bear:')
st.subheader('Metode pembayaran yang paling banyak digunakan')

bypayment_df = filtered_df.groupby(by="payment_type").customer_id.nunique().reset_index()
bypayment_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(y="customer_count", x="payment_type", data=bypayment_df.sort_values(by="customer_count", ascending=False), palette=["#8A2F19", "#D3D3D3"])
ax.set_title("Metode pembayaran yang paling banyak digunakan", loc="center", fontsize=15)
st.pyplot(fig)

st.caption('Copyright (c) Fidya Farasalsabila, 2025')
