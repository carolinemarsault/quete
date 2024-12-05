import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# PREMIERE CHOSE A METTRE LE TITRE :
st.title("Manipulation des données et création de graphiques")

#   pour avoir un seul dataframe de la bib seaborn   (df_flights = sns.load_dataset(flights))
# Pour avoir l'ensembles des dataframe seaborn

data_option = sns.get_dataset_names()
data_selectionne = st.selectbox("Quel dataset veux-tu utiliser", data_option)

#stocker le dataframe de seaborn dans une variable df
df = sns.load_dataset(data_selectionne)

# afficher les tableaux
st.dataframe(df)

# Afficher les colonnes du df choisi
colonnes = df.columns.tolist()

# Sélectionner les colonnes X et Y du df
colonne_x = st.selectbox("Choisissez la colonne X", colonnes)
colonne_y = st.selectbox("Choisissez la colonne Y", colonnes)

# graphique à utiliser par l'utilisateur
options_graphiques = ["Scatter plot", "Bar chart", "Line chart"]
graphique_selectionne = st.selectbox("Quel graphique veux-tu utiliser ?", options_graphiques)

# Créer le graphique à sélectionné par l'utilisateur
if graphique_selectionne == "Scatter plot":
    st.scatter_chart(x=colonne_x, y=colonne_y, data=df)
elif graphique_selectionne == "Bar chart":
    st.bar_chart(x=colonne_x, y=colonne_y, data=df)
elif graphique_selectionne == "Line chart":
    st.line_chart(x=colonne_x, y=colonne_y, data=df)

# case à cocher :
if st.checkbox("Afficher la matrice de corrélation"):
    st.subheader("Matrice de corrélation")

# je garde que les valeurs numériques
    valeurs_numériques = df.select_dtypes(include="number")

# Matrice
    matrice_corr = valeurs_numériques.corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(matrice_corr, annot=True, cmap="rocket") # annot=True : Ajoute les valeurs de corrélation directement sur les carrés de la
    st.pyplot(plt)