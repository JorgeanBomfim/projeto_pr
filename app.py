import streamlit as st
import base64

st.set_page_config(
    page_title="MRF",
    layout="wide"    
)


# URL da imagem do banner
banner_image_url = "https://img.freepik.com/vetores-premium/modelo-de-banner-de-servico-de-loja-de-ferramentas-de-construcao_38901-507.jpg?w=1380"

# Exibe a imagem do banner
st.image(banner_image_url, use_column_width=True)



## ocultando menu e marca d'agua
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



def create_whatsapp_link(phone_number, message):
    base_url = "https://api.whatsapp.com/send/"
    params = f"?phone={phone_number}&text={message}&type=phone_number&app_absent=0"
    return base_url + params

def show_products(products, title, description):
    st.subheader(title)
    st.write(description)
    
    num_products = len(products)
    num_columns = 4  # Exibir 4 produtos em uma fileira

    # Define o tamanho das colunas para ajustar o espaçamento
    col_width = 1 / num_columns

    for i in range(0, num_products, num_columns):
        product_row = products[i:i + num_columns]

        cols = st.columns(num_columns)

        for idx, product in enumerate(product_row):
            with cols[idx]:
                # Utiliza um wrapper de div para aplicar estilos de borda
                st.markdown(
                    f'<div style="border: 2.0px solid #eaeaea; padding: 50px;">'
                    f'<img src="{product["image_url"]}" alt="{product["name"]}" style="width: 100%;"/>'
                    f'<p><strong>{product["name"]}</strong></p>'
                    f'<p>Descrição: {product["description"]}</p>'
                    f'<p>Valor: {product["value"]}</p>'
                    '</div>',
                    unsafe_allow_html=True
                )

def main():
    
    products_col_1 = [
        {"name": "Produto 1", "value": "50,99R$", "description": "Descrição do Produto 1...", "image_url": "https://cdn.leroymerlin.com.br/contents/40_tipos_de_ferramentas_nomes_e_para_que_servem_345c_original.jpg"},
        {"name": "Produto 2", "value": "50,99R$", "description": "Descrição do Produto 2...", "image_url": "https://cdn.leroymerlin.com.br/contents/40_tipos_de_ferramentas_nomes_e_para_que_servem_c3ee_original.jpg"},
        {"name": "Produto 3", "value": "50,99R$", "description": "Descrição do Produto 3...", "image_url": "https://cdn.leroymerlin.com.br/contents/40_tipos_de_ferramentas_nomes_e_para_que_servem_2b12_original.jpg"},
        {"name": "Produto 4", "value": "50,99R$", "description": "Descrição do Produto 4...", "image_url": "https://cdn.leroymerlin.com.br/contents/40_tipos_de_ferramentas_nomes_e_para_que_servem_554c_original.jpg"}
    ]


    products_col_2 = [
        {"name": "Produto 1", "value": "50,99R$", "description": "Descrição do Produto 1...", "image_url": "https://cdn.leroymerlin.com.br/products/chave_de_cano_grifo_heavy_duty_36_91cm_lotus_ref_5281_1567036098_ffcf_600x600.jpg"},
        {"name": "Produto 2", "value": "50,99R$", "description": "Descrição do Produto 2...", "image_url": "https://down-br.img.susercontent.com/file/0a9b3ac3f254598a19dd86a7ee9f58a4"},
        {"name": "Produto 3", "value": "50,99R$", "description": "Descrição do Produto 3...", "image_url": "https://chatuba.vtexassets.com/arquivos/ids/160824-800-auto?v=637147144152500000&width=800&height=auto&aspect=true"},
        {"name": "Produto 4", "value": "50,99R$", "description": "Descrição do Produto 4...", "image_url": "https://cdn.awsli.com.br/1659/1659184/produto/93887665/b56e1e85f3.jpg"}
    ]

    show_products(products_col_1, "Ferramentas", "Temos uma grande variedade de ferramentas disponíveis.")
    show_products(products_col_2, "Encanamento", "Tudo que você precisa para trabalhos de encanamento.")


    phone_number = "5521979215685"
    message = "Olá, estou interessado em comprar o produto XYZ."

    whatsapp_link = create_whatsapp_link(phone_number, message)

    # Carrega a imagem do ícone do WhatsApp
    with open(r"WhatsApp-icone.png", "rb") as img_file:
        whatsapp_icon = base64.b64encode(img_file.read()).decode()

    button_whatsapp = f"""
        <a href="{whatsapp_link}" target="_blank">
            <button style="background-color: #25d366; border: none; color: #ffffff; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; border-radius: 4px; cursor: pointer;">
                <img src="data:image/png;base64,{whatsapp_icon}" alt="WhatsApp Icon" width="20" style="margin-right: 10px;">
                Conversar no WhatsApp
            </button>
        </a>
    """
    '\n'
    '\n'
    st.markdown(button_whatsapp, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
