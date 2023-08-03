import streamlit as st

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

    phone_number = "+5521979215685"
    message = "Olá, estou interessado em seus produtos."

    if st.button("Iniciar Conversa no WhatsApp"):
        whatsapp_link = create_whatsapp_link(phone_number, message)
        st.write(f"Para iniciar a conversa, clique no link abaixo:\n[{whatsapp_link}]({whatsapp_link})")
        
if __name__ == "__main__":
    main()
