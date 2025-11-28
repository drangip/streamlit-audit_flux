import streamlit as st
import pandas as pd

st.set_page_config(page_title="Audit de flux produits", page_icon="📡", layout="centered")

st.title("Audit de flux produits Shopping")

st.write("""Cette application à pour but de faire un audit de votre flux produits shopping.
""")
st.write("Pour importer votre flux, suivez les étapes suivantes :")
st.write("Rendez-vous dans votre sur votre merchant center dans Paramétres > Sources de données > Affichez l'historique des mises à jour")

st.image("./images/MC-histo_maj.png", use_column_width=True)

st.write("Cliquez ensuite sur 'Télécharger le fichier de la source de données' pour uploader votre flux.")

st.image("./images/MC-histo_upload.png", use_column_width=True)

st.write("Vous n'avez plus qu'à uploader le fichier dans ci contre dans la sidebar.")

st.sidebar.write("## Upload de flux produit")

uploaded_file = st.sidebar.file_uploader("📥 Charge ton flux produit")

if uploaded_file:
    try:
        flux = pd.read_csv(uploaded_file, sep="|", engine='python')
        st.session_state["flux_data"] = flux  # 🔹 Stockage dans la session
        st.success("✅ Flux chargé et enregistré en mémoire.")
        st.dataframe(flux.head())
        st.info("Tu peux maintenant aller dans les pages d’analyse via la barre latérale.")
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
else:
    st.info("💡 En attente d’un fichier CSV.")
