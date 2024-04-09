import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

from graph import parcours_timeline_fr, parcours_timeline_eng
from datadella_fr import page_fr
from datadella_eng import page_eng

##############################################
#                                            #
#                  SETTINGS                  #
#                                            #
##############################################

page_title = 'Datadella'
page_icon = 'logo/Logo2b.png'
st.set_page_config(layout='wide', page_icon=page_icon, page_title=page_title)

st.markdown(" <style> div[class^='block-container'] { padding-top: 2rem; } </style> ", unsafe_allow_html=True)

@st.cache_data(hash_funcs={dict: lambda _: None}) # hash_funcs because dict can't be hashed
def exp_timeline():
    xp_fig = {}
    xp_fig['xp_timeline_fr'] = parcours_timeline_fr()
    xp_fig['xp_timeline_eng'] = parcours_timeline_eng()

    return xp_fig 

xp_fig = exp_timeline()

##########################################
#                                        #
#                  MAIN                  #
#                                        #
##########################################

ci, ct = st.columns([.9, .1])
with ci:
    st.image('logo/Logo2c.png', width=300)
with ct:
    eng = st.toggle('English')

if eng:
    page_eng(xp_fig['xp_timeline_eng'])
elif not eng:
    page_fr(xp_fig['xp_timeline_fr'])