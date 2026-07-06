import streamlit as st
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title = "Add Expense",
    page_icon = "💸",
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

st.markdown(""" 
    <h1 style="text-align:center; color:white;">
    💸 Add Expense
    </h1>
    """, unsafe_allow_html=True)

st.divider()

# Navigation Button
# Navigation Buttons

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home", width="stretch"):
        st.switch_page("finance_trk.py")

with col2:
    if st.button("📊 Dashboard",width="stretch"):
        st.switch_page("pages/1_📊_Dashboard.py")

st.divider()

# Expense form
with st.form("expense_form"):
    source = st.text_input(
        "Expense Source",
        placeholder="Enter the source of expense"
    )

    amount = st.number_input(
        "Amount (₹)",
        min_value=0.0,
        step=500.0,
        placeholder="Enter the amount of expense"
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Rent",
            "Transport",
            "Entertainment",
            "Bills",
            "Utilities",
            "Healthcare",
            "Education",
            "Shopping",
            "Other"
        ]
    )

    from datetime import date

    expense_date = st.date_input(
        "Date",
        value=date.today()
    )

    description = st.text_area(
        "Description",
        placeholder="Optional"
    )

    submitted = st.form_submit_button(
        "💾 Save Expense",
        width="stretch"
    )

if submitted:

    expense_data = {
        "Type": "Expense",
        "Source": source,
        "Amount": amount,
        "Category": category,
        "Date": expense_date,
        "Description": description
    }

    df = pd.DataFrame([expense_data])

    file_exists = os.path.isfile("transactions.csv")

    df.to_csv(
        "transactions.csv",
        mode="a",
        header=not file_exists,
        index=False
    )
    
    st.success("✅ Expense saved successfully!")
    