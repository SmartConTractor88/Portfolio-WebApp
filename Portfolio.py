import streamlit as st
import pandas #

st.set_page_config(layout="wide") # expand to width of the layout

col1, col2 = st.columns(2) # return 2 column objects

with col1:
    st.image("Portfolio_Icons\\insta_profile_pic2.png", width=400)

with col2:
    st.title("Gundars Plūme")

    content = """
    A monkey once swung through the trees with delight,
    Then spotted a panda—fluffy and white.
    His heart did a flip, his tail curled tight,
    “I think I’m in love! Oh, what a sight!”\n

    He tried to impress, but tripped on a vine,
    Panda just laughed and said, “You’ll be fine.”
    She shared her bamboo, he offered a snack,
    Bananas for her? She gave them right back!\n

    Though one loved to climb and the other to nap,
    They fit like two pieces of one perfect map.
    Love doesn’t care if you're furry or small—
    Monkey and panda? The best match of all!\n
    \n
    -ChatGPT
    """
    st.write(content)

st.info("Below you can find some of the **apps** I have built with **Python**. Feel free to contact me!")

print("PORTFOLIO")


df = pandas.read_csv("data.csv", sep=";") # read the file, add a separator
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) # return 2 column objects and extra space in the middle

with col3:

    for index, row in df[0::2].iterrows():
        
        st.header(row["title"]) # access titles from csv file
        st.write(row["description"]) # access decriptions from the csv file
        st.image("Portfolio_Icons/" + row["image"]) # access images from the csv file
        st.write(f"[Source Code]({row['url']})") # "Source Code" text with an attached link from csv file

#with empty_col:

    

with col4:


    for index, row in df[1::2].iterrows():
        # access titles from csv file
        st.header(row["title"])
        st.write(row["description"]) # access decriptions from the csv file
        st.image("Portfolio_Icons/" + row["image"]) # access images from the csv file
        st.write(f"[Source Code]({row['url']})") # "Source Code" text with an attached link from csv file