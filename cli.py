import streamlit as st

st.set_page_config(layout="wide") # expand tu width of the layout

col1, col2 = st.columns(2) # return 2 column objects

with col1:
    st.image("Portfolio_Icons\\insta_profile_pic2.png", width=400)

with col2:
    st.title("Gundars Plume")

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



print("PORTFOLIO")