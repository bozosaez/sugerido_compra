import streamlit as st
from conexion_sql import conexion  # Asegúrate de que este archivo contenga la función de conexión corregida
from procesamiento import extraer_datos  # Asegúrate de que este archivo contenga la función de extracción de datos

def set_layout():
    st.set_page_config(page_title="Stock Assistant", layout="wide")

def apply_custom_styles():
    st.markdown("""
        <style>
        .stApp {
            background-color: white;
        }
        /* Cambia el color de fondo de los mensajes st.info */
        .stAlert {
            background-color: black;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

def display_header():
    st.markdown("""
        <h1 style='text-align: center; color: black; background-color: white;'>
            Hi! I am Piero
        </h1>
        <h2 style='text-align: center; color: gray; background-color: white;'>
            Your personal stock assistant
        </h2>
    """, unsafe_allow_html=True)

def input_form():
    with st.form(key='my_form'):
        server = st.text_input('Server', placeholder="Enter server address")
        database = st.text_input('Database', placeholder="Enter database name")
        password = st.text_input('Password', type='password', placeholder="Enter your password")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            conn_result = conexion(server, database, password)
            if isinstance(conn_result, str):
                # Si se devuelve una cadena, es un mensaje de error
                st.error(conn_result)
            else:
                # Si no es una cadena, es el objeto de conexión
                st.session_state['cnxn'] = conn_result
                # Cambiamos a la página de carga
                st.experimental_rerun()

def load_data_page(cnxn):
    st.info('Conectando con la base de datos...')
    with st.spinner('Cargando datos...'):
        try:
            df_maestro = extraer_datos(cnxn)
            st.success('Datos cargados con éxito!')
            st.write(df_maestro)
        except Exception as e:
            st.error(f"Se ha producido un error en la extracción del maestro: {e}")

def main():
    set_layout()
    apply_custom_styles()
    if 'cnxn' in st.session_state:
        # Mostramos la página de carga de datos si existe una conexión en el estado de la sesión
        load_data_page(st.session_state['cnxn'])
    else:
        # Mostramos el formulario si no se ha establecido la conexión
        display_header()
        input_form()

if __name__ == "__main__":
    main()