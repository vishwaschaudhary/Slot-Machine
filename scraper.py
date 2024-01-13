import streamlit as st
import requests
from bs4 import BeautifulSoup
st.set_page_config(page_title="Web Scraper",page_icon=":globe_with_meridians:")
st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>",unsafe_allow_html=True)
with st.form("Search"):
    keyword=st.text_input("Enter the keyword you want to search")
    search=st.form_submit_button("Search")
placeholder=st.empty()
if keyword!="":
    page=requests.get(f"https://unsplash.com/s/photos/{keyword}")#this will access the url based on the keyword given by the user
    soup=BeautifulSoup(page.content.decode('utf-8', 'ignore'),"lxml")#this will give us all the html code of that page from that code we will access the image 
    rows=soup.find_all("div",class_="ripi6")#this will access all the rows from the web page whose div has clas=ripi6
    col1,col2=placeholder.columns(2)
    for j,row in enumerate(rows):
        figures=row.find_all("figure")#we are going inside figures in each row
        for i in range(4):
            img=figures[i].find("img",class_="tB6UZ a5VGX")#this will access the contents of first ten images of each row
            lst=img["srcset"].split("?")#this will split the contents of image on ? and the first part will have the address of the image which is all we need 
            anchor=figures[i].find("a",class_="rEAWd")
            href=anchor["href"]#to get the hyperreference from the anchor tag to redirect to download button
            if i%2==0:
                col1.image(lst[0])#this will show the image on my webpage
                col1.download_button("Download",data=lst[0],file_name="my_image.jpg", mime="image/jpeg",key=str(j)+str(i))
            else:
                col2.image(lst[0])
                col2.download_button("Download",data=lst[0],file_name="my_image.jpg", mime="image/jpeg",key=str(j)+str(i))
                


