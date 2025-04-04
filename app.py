import pandas as pandas
import geopandas as gpd 
import matplotlib.pyplot as plt 
import streamlit as st 

st.title("Esto es una app")

year = st.selectbox('Seleccione un año:', [2022,2023,2024])

if year == 2024:
   tgp_MASC = gpd.read_parquet('hombres.parquet')
   tgp_FEM = gpd.read_parquet('mujeres.parquet') 

if year == 2023:
    tgp_MASC = gpd.read_parquet('hombres23.parquet')
    tgp_FEM = gpd.read_parquet('mujeres23.parquet') 

if year == 2022:
    tgp_MASC = gpd.read_parquet('hombres22F.parquet')
    tgp_FEM = gpd.read_parquet('mujeres22F.parquet') 

fig, ax = plt.subplots(1,2,figsize=(10,6))

tgp_MASC.plot(column='FT', ax=ax[0], legend=True)
tgp_FEM.plot(column='FT', ax=ax[1], legend=True)

ax[0].set_title('TGP = Hombres')
ax[1].set_title('TGP = Mujeres')

st.pyplot(fig)

