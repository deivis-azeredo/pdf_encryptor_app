import streamlit as st
from pypdf import PdfReader, PdfWriter
import io

st.title('🔒 Criptografador de PDF')

uploaded_file = st.file_uploader('Envie o PDF da apostila', type='pdf')
password = st.text_input('Digite a senha', type='password')

if uploaded_file and password:
    if st.button('Criptografar'):
        reader = PdfReader(uploaded_file)
        writer = PdfWriter()

        progress_bar = st.progress(0)
        total_pages = len(reader.pages)

        for i, page in enumerate(reader.pages):
            writer.add_page(page)
            progress_bar.progress((i + 1) / total_pages)

        writer.encrypt(password)

        output = io.BytesIO()
        writer.write(output)
        output.seek(0)

        st.success('PDF criptografado com sucesso!')
        st.download_button(
            label='Baixar PDF criptografado',
            data=output,
            file_name='apostila_criptografada.pdf',
            mime='application/pdf'
        )