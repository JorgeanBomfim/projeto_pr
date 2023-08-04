import streamlit as st
import base64

st.set_page_config(
    page_title="MRF",
    layout="centered",
    page_icon=":hammer:"
)

def create_whatsapp_link(phone_number, message):
    base_url = f"https://wa.me/{phone_number}/"
    if message:
        return f"{base_url}?text={message}"
    else:
        return base_url

def show_products(products, title, description):
    st.subheader(title)
    st.write(description)
    
    num_products = len(products)
    num_columns = 4  # Exibir 4 produtos em uma fileira

    for i in range(0, num_products, num_columns):
        product_row = products[i:i + num_columns]

        cols = st.columns(num_columns)

        for idx, product in enumerate(product_row):
            with cols[idx]:
                st.image(product['image_url'], use_column_width=True, caption=product['name'], output_format='auto')
                st.write(product['description'])

def main():
    st.title("App do MRF")

    products_col_1 = [
        {"name": "Produto 1", "description": "Descrição do Produto 1", "image_url": "https://cdn.leroymerlin.com.br/contents/40_tipos_de_ferramentas_nomes_e_para_que_servem_345c_original.jpg"},
        {"name": "Produto 2", "description": "Descrição do Produto 2", "image_url": "https://cdn.leroymerlin.com.br/contents/40_tipos_de_ferramentas_nomes_e_para_que_servem_c3ee_original.jpg"},
        {"name": "Produto 3", "description": "Descrição do Produto 3", "image_url": "https://cdn.leroymerlin.com.br/contents/40_tipos_de_ferramentas_nomes_e_para_que_servem_2b12_original.jpg"},
        {"name": "Produto 4", "description": "Descrição do Produto 4", "image_url": "https://cdn.leroymerlin.com.br/contents/40_tipos_de_ferramentas_nomes_e_para_que_servem_554c_original.jpg"}
    ]


    products_col_2 = [
        {"name": "Produto 1", "description": "Descrição do Produto 1", "image_url": "https://cdn.leroymerlin.com.br/products/chave_de_cano_grifo_heavy_duty_36_91cm_lotus_ref_5281_1567036098_ffcf_600x600.jpg"},
        {"name": "Produto 2", "description": "Descrição do Produto 2", "image_url": "https://down-br.img.susercontent.com/file/0a9b3ac3f254598a19dd86a7ee9f58a4"},
        {"name": "Produto 3", "description": "Descrição do Produto 3", "image_url": "https://chatuba.vtexassets.com/arquivos/ids/160824-800-auto?v=637147144152500000&width=800&height=auto&aspect=true"},
        {"name": "Produto 4", "description": "Descrição do Produto 4", "image_url": "https://cdn.awsli.com.br/1659/1659184/produto/93887665/b56e1e85f3.jpg"}
    ]
    st.header("Produtos em Estoque")

    show_products(products_col_1, "Ferramentas", "Temos uma grande variedade de ferramentas disponíveis.")
    show_products(products_col_2, "Encanamento", "Tudo que você precisa para trabalhos de encanamento.")



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

        
if __name__ == "__main__":
    main()