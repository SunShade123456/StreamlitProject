from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon="😄", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown (f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ----LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/d02107fb-e7ba-4962-b831-74a6079e59a9/9xbqPi6RBh.json")
img_contact_form = Image.open("images/boo.png")
img_lottie_animation = Image.open("images/Green Yellow Retro Aesthetic Business Paper Bag.png")
# HEADER SECTION
with st.container():
    st.subheader("Hi, I am Akshat :wave:")
    st.title("A Data Analyst From India")
    st.write("I am passionate about finding ways to use Python to be more efficient and effective in bussiness settings.")
    st.write("[Learn More >](https://github.com/SunShade123456)")

#---WHAT I DO-------
with st.container():
    st.write("---")
    left_colunm, right_column = st.columns(2)
    with left_colunm:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you,consider subscribing and turning on the notifications,so you dont miss any content.
            """
        )
        st.write("[YouTube Channel >]()")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown ("[Watch Video...](https://youtu.be/TXSOitGoINE)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown ("[Watch Video...](https://youtu.be/TXSOitGoINE)")

# ---- CONTACT -----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/akshat.anuj17@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value=""false>
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns (2)
    with left_column:
        st.markdown (contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()