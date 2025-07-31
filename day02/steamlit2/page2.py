import urllib


import streamlit as st
from PIL import Image

from llm.MyApi import openAiModel

def main():

    st.markdown("# Page 2 🎉")
    st.sidebar.markdown("# Page 2 🎉")


    picture = st.camera_input("Take a picture")

    if picture is not None:
        with open('test.png', 'wb') as file:
            file.write(picture.getvalue())
        Image.open('test.png').save("test.png")

    if st.button("생성"):
        st.write("생성합니다.")

        client = openAiModel()
        response = client.images.create_variation(
            model="dall-e-2",
            image=open("test.png", "rb"),
            n=3,
            size="512x512"
        )

        for n, data in enumerate(response.data):
            print(data.url)
            st.image(data.url)
            #save_path = f"dogs_variation_{n}.png"
            #urllib.request.urlretrieve(data.url, save_path)

if __name__ == '__main__':
    main()