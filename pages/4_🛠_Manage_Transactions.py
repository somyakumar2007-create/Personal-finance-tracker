import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title = "Manage Transactions",
    page_icon = "🛠",
    layout = "wide"
)

# Background
st.markdown("""
<style>
.stApp{
    background: linear-gradient(
            135deg,
            #0f172a,
            #1e293b
        );
    }
</style>
""", unsafe_allow_html=True)

# Title

st.markdown("""
<h1 style="text-align:center; color:white;">
🛠 Manage Transactions
</h1>             
""", unsafe_allow_html=True)

st.divider()

# Navigation Buttons

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home", width="stretch"):
        st.switch_page("finance_trk.py")

with col2:
    if st.button("📊 Dashboard", width="stretch"):
        st.switch_page("pages/1_📊_Dashboard.py")

st.divider()

# Load transactions

try:
    df = pd.read_csv("transactions.csv")
except FileNotFoundError:
    df = pd.DataFrame(
        columns = [
            "Type",
            "Source",
            "Amount",
            "Category",
            "Date",
            "Description"
        ]
    )

if df.empty:
    st.info("No transactions available.")
    st.stop()

# Search Section
st.subheader("🔍 Find Transaction")

search = st.text_input(
    "Search by Source",
    placeholder="Enter the source you are searching"
)

if search:
    df = df[
        df["Source"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# Show transactions
display_df = df.copy()

display_df["Amount"] = display_df["Amount"].apply(
    lambda x: f"₹{x:,.0f}"
  )

display_df = display_df.sort_values(
   by="Date",
   ascending=False
)

st.subheader("📋 All Transactions")

st.dataframe(
    display_df,
    width="stretch",
    hide_index=True
  )

# Select Transactions

st.divider()

st.subheader("✏️ Edit / Delete Transaction")

selected_index = st.selectbox(
    "Choose a transaction",
    options=df.index,
    format_func=lambda x: f"{df.loc[x, 'Type']} | {df.loc[x, 'Source']} | ₹{df.loc[x, 'Amount']:,.0f}"
    )

selected_transaction = df.loc[selected_index]

# Category Lists

income_categories = [
    "Salary",
    "Business",
    "Investments",
    "Freelancing",
    "Other"
  ]

expense_categories = [
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

# Select category list based on type

if selected_transaction["Type"]== "Income":
    category_list = income_categories
else:
    category_list = expense_categories

# Edit form

with st.form("edit_transaction_form"):

    transaction_type = st.selectbox(
        "Transaction Type",
        ["Income", "Expense"],
        index=0 if selected_transaction["Type"] == "Income" else 1
    )

    source = st.text_input(
    "Source",
    value = selected_transaction["Source"]
  )

    amount = st.number_input(
    "Amount (₹)",
    min_value=0.0,
    value=float(selected_transaction["Amount"]),
    step=100.0
   )

# Update categoy list if type changes

    if transaction_type == "Income":
     category_list = income_categories
    else:
     category_list = expense_categories

    current_category = selected_transaction["Category"]

    if current_category in category_list:
     category_index = category_list.index(current_category)
    else:
     category_index=0

    category = st.selectbox(
    "Category",
    category_list,
    index=category_index
   )

    transaction_date = st.date_input(
    "Date",
    value = pd.to_datetime(selected_transaction["Date"])
   )

    description = st.text_area(
    "Description",
    value = selected_transaction["Description"]
   )

    col1, col2 = st.columns(2)

    with col1:
     update = st.form_submit_button(
        "💾 Update Transaction",
        width="stretch"
    )

    with col2:
     delete = st.form_submit_button(
        "🗑 Delete Transaction",
        width="stretch"
    )

# Update Transaction

    if update:
      df.loc[selected_index, "Type"] = transaction_type
      df.loc[selected_index, "Source"] = source
      df.loc[selected_index, "Amount"] = amount
      df.loc[selected_index, "Category"] = category
      df.loc[selected_index, "Date"] = transaction_date
      df.loc[selected_index, "Description"] = description
    
      df.to_csv(
         "transactions.csv",
         index = False
       )

      st.success("✅ Transaction updated successfully!")

      st.rerun()

    # Delete Transactions

    if delete:
       
       df = df.drop(selected_index)

       df = df.reset_index(drop=True)

       df.to_csv(
          "transactions.csv",
          index=False
       )

       st.success("🗑 Transaction deleted successfully!")

       st.rerun()