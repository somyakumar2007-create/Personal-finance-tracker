import streamlit as st
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title = "Add Income",
    page_icon = "💰",
    layout = "wide"
)

# Background gradient
st.markdown("""
<style>
.stApp{
    background: linear-gradient(
        135deg,
        #1e3c72,
        #2a5298,
        #6dd5fa
        );
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <h1 style="text-align:center; color:white;">
        💰 Add Income
    </h1>
""",
unsafe_allow_html=True
)

st.divider()

# Navigation Buttons

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home", width="stretch"):
        st.switch_page("finance_trk.py")

with col2:
    if st.button("📊 Dashboard",width="stretch"):
        st.switch_page("pages/1_📊_Dashboard.py")

st.divider()

# Income form 
with st.form("income_form"):

    source = st.text_input(
        "Income Source",
        placeholder="Enter the source of income"
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        step=500.0,
        placeholder="Enter the amount of income"
    )

    category = st.selectbox(
        "Category",
        [
            "Salary",
            "Business",
            "Investments",
            "Freelancing",
            "Other"
        ]
    )

    date = st.date_input("Date")

    description = st.text_area(
        "Description",
        placeholder="Optional"
    )

    submitted = st.form_submit_button(
        "💾 Save Income",
        width="stretch"
    )

if submitted:

    income_data = {
        "Type": "Income",
        "Source": source,
        "Amount": amount,
        "Category": category,
        "Date": date,
        "Description": description
    }

    df = pd.DataFrame([income_data])

    file_exists = os.path.isfile("transactions.csv")

    df.to_csv(
        "transactions.csv",
        mode="a",
        header=not file_exists,
        index=False
    )

    st.success("✅ Income saved successfully!")