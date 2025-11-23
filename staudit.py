import streamlit as st
import pandas as pd

st.set_page_config(page_title="Audit de flux produits", page_icon="📡", layout="centered")

st.title("Audit de flux produits Shopping")

st.write("""
Bienvenue dans notre outil d’audit de flux produits !  
1. **Upload ton flux** ci contre
2. Accède ensuite à l'analyse des champs de ton flux produits.
""")

st.write("Pour cela rendez-vous dans votre sur votre merchant center dans Paramétres > Sources de données > Affichez l'historique des mises à jour")

st.image("./images/MC-histo_maj.png", use_column_width=True)

st.write("Clique ensuite sur 'Télécharger le fichier de la source de données' pour uploader votre flux.")

st.image("./images/MC-histo_upload.png", use_column_width=True)

st.write("Vous n'avez plus qu'à uplaoder le fichir dans l'outil via le menu de gauche !")

st.sidebar.write("## Upload de flux produit")

uploaded_file = st.sidebar.file_uploader("📥 Charge ton flux produit", type=["csv"])

if uploaded_file:
    try:
        flux = pd.read_csv(uploaded_file, sep=None, engine='python')
        st.session_state["flux_data"] = flux  # 🔹 Stockage dans la session
        st.success("✅ Flux chargé et enregistré en mémoire.")
        st.dataframe(flux.head())
        st.info("Tu peux maintenant aller dans les pages d’analyse via la barre latérale.")
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
else:
    st.info("💡 En attente d’un fichier CSV.")