import streamlit as st
import matplotlib.pyplot as plt

# --- Configuration de la page ---
st.set_page_config(page_title="Analyse des titres", layout="centered")

st.header("Analyse des titres produits")

st.write("> Les bonnes pratiques sur le titre")
st.write("Le titre du produit est important à deux niveaux")
st.write("- **Son contenu** : Le titre conditionne les requêtes sur lesquelles nous allons apparaître.")
st.write("- **Sa mise en forme** : Il est l’un des 3 éléments essentiels avec l’image et le prix qui construit l’annonce shopping et a donc un impact important sur le taux de clic. Il doit contenir le générique produits, sa marque, ses caractéristiques. Il est recommandé que le titre soit unique à chacun des produits du flux.")


# --- Vérifie si le flux est déjà chargé ---
if "flux_data" not in st.session_state:
    st.error("⚠️ Aucun flux détecté. Reviens sur la page d’accueil pour charger ton fichier.")
    st.stop()

flux = st.session_state["flux_data"]

# --- Vérification de la colonne 'title' ---
if "title" not in flux.columns:
    st.error("⚠️ La colonne 'title' est absente du flux.")
    st.stop()

# --- Statistiques globales sur les titres ---
nbtitre = len(flux['title'])
nbtitreunique = len(flux['title'].unique())
nbtitredoublon = nbtitre - nbtitreunique

st.write(
    f"Le flux comporte **{nbtitre}** titres dont **{nbtitreunique}** uniques "
    f"et **{nbtitredoublon}** doublons."
)

# --- Préparation des données du camembert ---
pourcentagetitre = {
    "Titres uniques": nbtitreunique,
    "Titres en doublon": nbtitredoublon
}

# --- Création du graphique ---
fig, ax = plt.subplots(figsize=(4, 4))  # Taille plus compacte
wedges, texts, autotexts = ax.pie(
    pourcentagetitre.values(),
    labels=pourcentagetitre.keys(),
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.4, 'edgecolor': 'white'},
    colors=[(0, 0.7, 0, 0.6), (1, 0, 0, 0.6)],  # Vert / Rouge semi-transparents
    pctdistance=0.7
)

# --- Style du texte ---
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# --- Centrage du graphe ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.pyplot(fig)
