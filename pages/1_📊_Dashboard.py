import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title = "Dashboard",
    page_icon = "📊",
    layout = "wide"
)

# Background gradient
st.markdown("""
<style>
            .stApp {
            background: linear-gradient(
            135deg,
            #0f172a,
            #1e293b
            );
            }
            </style>
            """, unsafe_allow_html=True)

# Title
st.markdown(
    """
  <h1 style="text-align: center; color:white;">
      📊 Dashboard
    </h1>
  """,
  unsafe_allow_html=True
  )

st.divider()

# Load transactions data
try:
    df = pd.read_csv("transactions.csv")
except FileNotFoundError:
    df = pd.DataFrame(
        columns=["Type", "Source", "Amount", "Category", "Date", "Description"]
    )

# Calculate total amount
total_income = df[df["Type"] == "Income"]["Amount"].sum()
total_expenses = df[df["Type"] == "Expense"]["Amount"].sum()
current_balance = total_income - total_expenses

# Filter only expense transactions for the pie chart
expense_df = df[df["Type"] == "Expense"]

# Group expenses by category
category_expense = (
    expense_df
    .groupby("Category")["Amount"]
    .sum()
    .reset_index()
)

# Columns for the dashboard content
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label = "💰 Total Income",
        value = f"₹{total_income:,.0f}"
    )

with col2:
    st.metric(
        label = "💸 Total Expenses",
        value = f"₹{total_expenses:,.0f}"
    )

with col3:
    st.metric(
        label = "💵 Current Balance",
        value = f"₹{current_balance:,.0f}"
    )

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Add Income",width="stretch"):
        st.switch_page("pages/2_💰_Add_Income.py")

with col2:
    if st.button("➖ Add Expense",width="stretch"):
        st.switch_page("pages/3_💸_Add_Expense.py")

with col3:
    if st.button("🛠 Manage Transactions", width="stretch"):
        st.switch_page("pages/4_🛠_Manage_Transactions.py")

st.subheader("📈 Financial Overview")

if expense_df.empty:
    st.info("No expense data available")
else:
    fig = px.pie(
        category_expense,
        values="Amount",
        names="Category",
        title="Expense Distribution by Category"
    )

    st.plotly_chart(fig, width="stretch")

st.divider()

st.subheader("🔍 Search & Filter")
col1, col2, col3 = st.columns(3)
with col1:
    search = st.text_input(
        "Search",
        placeholder="Search by source..."
    )

with col2:
    transaction_type= st.selectbox(
        "Transaction Type",
        ["All", "Income", "Expense"]
    )

with col3:
    categories = ["All"] + sorted(df["Category"].unique().tolist())

    category = st.selectbox(
        "Category",
        categories
    )

filtered_df = df.copy()
if search:
    filtered_df = filtered_df[
        filtered_df["Source"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

if transaction_type != "All":
    filtered_df = filtered_df[
        filtered_df["Type"] == transaction_type
    ]

if category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category
    ]

st.divider()

st.subheader("📝 Recent Transactions")

if filtered_df.empty:
    st.info("No transactions yet.")
else:
    display_df = filtered_df.copy()

    display_df["Amount"] = display_df["Amount"].apply(
        lambda x: f"₹{x:,.0f}"
    )

    display_df = display_df.sort_values(
        by="Date",
        ascending=False
    )

    st.dataframe(
        filtered_df.head(5),
        width="stretch",
        hide_index=True
    )