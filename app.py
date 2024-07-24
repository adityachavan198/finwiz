import streamlit as st
from llama3 import llama3  # Assuming llama3 is a custom module you have

def suggest_investments(income, age, marital_status, risk_appetite, fixed_expenses, savings, liabilities, investment_goals):
    prompt = (
        f"Income: {income}, Age: {age}, Marital Status: {marital_status}, "
        f"Risk Appetite: {risk_appetite}, Fixed Monthly Expenses: {fixed_expenses}, "
        f"Current Savings: {savings}, Liabilities: {liabilities}, Investment Goals: {investment_goals}\n"
        "Based on these attributes, suggest suitable investments.\n"
        "For example, suggest specific ETFs, mutual funds, stocks, or other investment vehicles that provide good returns based on the risk appetite."
    )
    try:
        result = llama3(prompt)
        return result
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit interface configuration
st.set_page_config(page_title="Finance Wizard", layout="centered")

st.title("💼 Finance Wizard")
st.write("Enter your financial details to get personalized investment suggestions.")

# Layout the input fields in a grid
col1, col2 = st.columns(2)
with col1:
    income = st.number_input("Annual Income in USD", min_value=100000.0, format="%f", step=500.0, help="Enter your annual income in USD.")
    age = st.number_input("Age", min_value=18, format="%d", help="Enter your age.")
    savings = st.number_input("Current Savings in USD", min_value=0.0, format="%f", step=1000.0, help="Enter your current savings in USD.")

with col2:
    marital_status = st.radio("Marital Status", ['Single', 'Married', 'Divorced', 'Widowed'], help="Select your marital status.")
    fixed_expenses = st.number_input("Fixed Monthly Expenses in USD", min_value=1000.0, format="%f", step=100.0, help="Enter your fixed monthly expenses in USD.")
    liabilities = st.number_input("Liabilities in USD", min_value=0.0, format="%f", step=500.0, help="Enter your liabilities in USD.")

investment_goals = st.selectbox("Investment Goals", 
                                options=[
                                    "Retirement",
                                    "Buying a house",
                                    "Education fund",
                                    "Emergency fund",
                                    "Vacation",
                                    "Wealth accumulation",
                                    "Other"
                                ], 
                                help="Select your primary investment goal.")

risk_appetite = st.selectbox("Risk Appetite",
                             options=[
                                 ("1", "Conservative (Low Risk)"),
                                 ("2", "Moderate (Low-Medium Risk)"),
                                 ("3", "Balanced (Medium Risk)"),
                                 ("4", "Growth (Medium-High Risk)"),
                                 ("5", "Aggressive (High Risk)")
                             ],
                             format_func=lambda x: x[1],
                             help="Select your risk appetite.")

# Add a button to get investment suggestions
if st.button("Get Investment Suggestions"):
    with st.spinner("Calculating..."):
        risk_appetite_value = risk_appetite[0]  # Extracting the numeric value
        result = suggest_investments(income, age, marital_status, risk_appetite_value, fixed_expenses, savings, liabilities, investment_goals)
    st.success("Investment Suggestions:")
    st.text_area("", result, height=500)

# Add a reset button to clear all inputs
if st.button("Reset"):
    st.experimental_rerun()


# Add a footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        color: grey;
        font-size: small;
    }
    </style>
    <div class="footer">
        Created by Your Name
    </div>
    """,
    unsafe_allow_html=True
)
