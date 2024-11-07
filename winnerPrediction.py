import plotly
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.offline as pyo
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def app():
    st.markdown('''
    <h1 style='text-align:center; color: #700961;'><strong> 🎲 PRIDICTING WIN PROBABILITY FOR A TEAM 🎲</strong></h1>
    <hr style="border-top: 3px solid #700961;">
    ''', unsafe_allow_html=True)
