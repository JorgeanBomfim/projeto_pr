import streamlit as st
import base64

def create_whatsapp_link(phone_number, message):
    base_url = "https://api.whatsapp.com/send/"
    params = f"?phone={phone_number}&text={message}&type=phone_number&app_absent=0"
    return base_url + params

phone_number = "21979215685"
message = "Olá, estou interessado em comprar o produto XYZ."

whatsapp_link = create_whatsapp_link(phone_number, message)

# Carrega a imagem do ícone do WhatsApp
with open(r"WhatsApp-icone.png", "rb") as img_file:
    whatsapp_icon = base64.b64encode(img_file.read()).decode()

button_html = f"""
    <a href="{whatsapp_link}" target="_blank">
        <button style="background-color: #25d366; border: none; color: #ffffff; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; border-radius: 4px; cursor: pointer;">
            <img src="data:image/png;base64,{whatsapp_icon}" alt="WhatsApp Icon" width="20" style="margin-right: 10px;">
            Conversar no WhatsApp
        </button>
    </a>
"""
st.markdown(button_html, unsafe_allow_html=True)
