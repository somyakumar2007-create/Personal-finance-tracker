import streamlit as st

# Page configuration
st.set_page_config(
    page_title = "Personal Finance Tracker",
    page_icon = "💰",
    layout = "wide",
    )

# Background gradient
st.markdown("""
<style>
            .stApp {
            background: linear-gradient(
            135deg,
            #1e3c72,
            #2a5298,
            #6dd5fa
            );
            }
            </style>
            """, unsafe_allow_html=True)

# Title and welcome message
st.markdown(
    """
    <h1 style="font-size:60px; color:white; text-align:center;">
       📊 <b>Personal Finance Tracker</b>
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html = True)

st.markdown(
    """
    <p style="font-size:45px; color:#87CEFA; text-align:center;">
       <b> Welcome! </b><br>
    </p>
    """,
    unsafe_allow_html = True
    )

col1, col2, col3 = st.columns([1,3,1])

with col2:
   st.markdown(
      """
      <p style="font-size:32px; color:#D3D3D3; text-align:center;">
      Manage your money smarter.<br>
      Track income, expenses, and savings—all in one place.
      </p>
      """,
      unsafe_allow_html=True
)

# Button to go to the dashboard
st.markdown("<br><br>", unsafe_allow_html = True)

st.write("")

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
   if st.button("🚀 Go to Dashboard", width="stretch"):
      st.switch_page("pages/1_📊_Dashboard.py")
