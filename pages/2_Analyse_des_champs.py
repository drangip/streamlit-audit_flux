import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Configuration de la page ---
st.set_page_config(page_title="Analyse des titres", layout="centered")

st.header("Analyse des titres produits")

st.write("> Les bonnes pratiques sur le titre")
st.write("Le titre du produit est important à deux niveaux")
st.write("- **Son contenu** : Le titre conditionne les requêtes sur lesquelles nous allons apparaître.")
st.write("- **Sa mise en forme** : Il est l’un des 3 éléments essentiels avec l’image et le prix qui construit l’annonce shopping et a donc un impact important sur le taux de clic. Il doit contenir le générique produits, sa marque, ses caractéristiques. Il est recommandé que le titre soit unique à chacun des produits du flux.")

st.write("> Analyse des titres en doublon")

# --- Vérification du flux ---
if "flux_data" not in st.session_state:
    st.error("⚠️ Aucun flux détecté. Reviens sur la page d’accueil pour charger ton fichier.")
    st.stop()

flux = st.session_state["flux_data"]

if "title" not in flux.columns:
    st.error("⚠️ La colonne 'title' est absente du flux.")
    st.stop()

# --- Statistiques globales ---
nbtitre = len(flux['title'])
nbtitreunique = len(flux['title'].unique())
nbtitredoublon = nbtitre - nbtitreunique

st.write(
    f"Le flux comporte **{nbtitre}** titres dont **{nbtitreunique}** uniques "
    f"et **{nbtitredoublon}** doublons."
)

# --- Camembert ---
pourcentagetitre = {
    "Titres uniques": nbtitreunique,
    "Titres en doublon": nbtitredoublon
}

fig_pie, ax_pie = plt.subplots(figsize=(4, 4))
wedges, texts, autotexts = ax_pie.pie(
    pourcentagetitre.values(),
    labels=pourcentagetitre.keys(),
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.4, 'edgecolor': 'white'},
    colors=[(0, 0.7, 0, 0.6), (1, 0, 0, 0.6)],
    pctdistance=0.7
)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.pyplot(fig_pie)

st.markdown("---")

# --- Analyse longueur des titres ---
st.write("> Analyse de la longueur des titres")

dftitle = pd.DataFrame(flux['title'])
dftitle['nb_caracteres'] = dftitle['title'].str.len()

titlemean = round(dftitle['nb_caracteres'].mean(), 2)
titlemedian = round(dftitle['nb_caracteres'].median(), 2)
titlemax = int(dftitle['nb_caracteres'].max())
titlemin = int(dftitle['nb_caracteres'].min())

st.write("La longueur maximale recommandée est généralement d’environ **150 caractères**.")

st.write(f"- Moyenne : **{titlemean}** caractères")
st.write(f"- Médiane : **{titlemedian}** caractères")
st.write(f"- Titre le plus court : **{titlemin}** caractères")
st.write(f"- Titre le plus long : **{titlemax}** caractères")

# --- Histogramme ---
fig_hist, ax_hist = plt.subplots(figsize=(8, 4))
ax_hist.hist(
    dftitle['nb_caracteres'],
    bins=30,
    edgecolor='black'
)

ax_hist.set_title("Distribution du nombre de caractères des titres", fontsize=14, fontweight='bold')
ax_hist.set_xlabel("Nombre de caractères")
ax_hist.set_ylabel("Nombre de titres")

st.pyplot(fig_hist)
