import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
st.markdown("<h1 style='text-align:center;'>Web Scrapping Using Streamlit</h2>",unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Enter your Keyword")
    search = st.form_submit_button("Search")
placeholder = st.empty()
if keyword:

        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup = BeautifulSoup(page.content,'lxml')
        rows = soup.find_all("div",class_="ripi6")
        col1, col2 = placeholder.columns(2)
        for index,row in enumerate(rows):
            figures = row.find_all("div",class_="MorZF")
            anchor = row.find_all("a", class_="rEAWd")
            for i in range(6):
                img = figures[i].find("img")
                list = img["srcset"].split("?")
                anch=anchor[i]
                print(anch["href"])
                if i % 2 == 0:
                    col1.image(list[0])
                    btn=col1.button("Download",key=str(index)+str(i))
                    if btn:
                        webbrowser.open_new_tab("https://unsplash.com"+anch["href"])

                else:
                    col2.image(list[0])
                    btn = col2.button("Download", key=str(index)+str(i))
                    if btn:
                        webbrowser.open_new_tab("https://unsplash.com"+anch["href"])
                print("\n\n\n")

