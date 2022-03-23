'''
https://discuss.streamlit.io/t/barfi-flow-based-programming-for-data-science-new-component/23237/7?u=krishadi
'''

from unicodedata import name
from barfi import st_barfi, barfi_schemas
import streamlit as st
from blocks import file_block, load_file_block, select_file_block, label_encoder_block

base_blocks = [file_block, load_file_block, select_file_block, label_encoder_block]

barfi_schema_name = st.selectbox(
    'Select a saved schema to load:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=True)

barfi_result = st_barfi(base_blocks=base_blocks, compute_engine=compute_engine, load_schema=barfi_schema_name)

if barfi_result:
    st.write(barfi_result['Label Encoder-1']['block'].get_interface(name='Labels'))
    st.write(barfi_result['Label Encoder-1']['block'].get_interface(name='Labeled Data'))
