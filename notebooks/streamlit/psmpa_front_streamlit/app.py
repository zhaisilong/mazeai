import streamlit as sl
from utils import (
    write_tmp,
    resource_is_available,
    is_sequence_file_valid,
    is_feature_file_valid,
    send_mail,
)
from core import run_anylisis

r = None

sl.title('PSMPA')
sl.subheader('Analysis')

sl.text('Input Info')
sl.text_input('Email:', key='email')
sl.text_input('Name:', key='name')
sl.text_input('Institution:', key='institution')

sl.text('Data Input')
sequence = sl.file_uploader('Load a sequence file')
feature = sl.file_uploader('Load a feature table')
similarity = sl.slider(
    label='Pick a similarity for sequence',
    min_value=40,
    max_value=100,
    value=90,
    step=1
)

@sl.cache()
def run():
    if resource_is_available():
        if is_feature_file_valid(feature) and is_sequence_file_valid(sequence):
            try:
                result = run_anylisis(sequence.name, feature.name)
                return result
            except:
                sl.warning('something went wrong')
        else:
            sl.warning('feature file or sequence file is not valid')
    else:
        sl.warning('resource is not available')

if sl.button('Run'):
     sl.write('Running')
     r = run()
     sl.write('Down')


if sl.button('Send me email'):
     send_response = send_mail(sl.session_state.email, r)
     print(send_response)
     if send_response:
         sl.write(f'send succeeds: {r}')
     else:
         sl.write('send failed')
