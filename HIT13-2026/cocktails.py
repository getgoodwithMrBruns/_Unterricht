import streamlit as st
import pandas as pd

df = pd.read_csv("cocktails.csv")

tab1, tab2, tab3 = st.tabs(["By Name", "By Ingredients", "By Image"])


with tab1:
    categories = st.radio("Choose your category", df["category"].unique())
    # categories = st.radio("Choose your category", set(df["category"])) #set geht für beides, series und list

    if categories:
        cocktail = st.selectbox("Cocktails", df[df.category == categories].name)

    if cocktail:
        st.write(df[df.name == cocktail])

with tab2:
    st.write("lol")