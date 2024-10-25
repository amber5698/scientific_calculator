import streamlit as st
import math

# Set the title of the app
st.title("🧮 Scientific Calculator")

# Initialize the expression variable
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to update the expression
def update_expression(value):
    st.session_state.expression += str(value)

# Function to clear the expression
def clear_expression():
    st.session_state.expression = ""

# Function to calculate the result
def calculate_result():
    try:
        # Evaluate the expression safely
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except Exception as e:
        st.error("Invalid Input")
        clear_expression()

# Display the current expression
st.write(f"**Expression:** {st.session_state.expression}")

# Create buttons for numbers and operations
col1, col2, col3 = st.columns(3)

with col1:
    for i in range(1, 10):
        if st.button(str(i)):
            update_expression(i)

with col2:
    if st.button("0"):
        update_expression(0)
    if st.button("+"):
        update_expression("+")
    if st.button("-"):
        update_expression("-")
    if st.button("*"):
        update_expression("*")
    if st.button("/"):
        update_expression("/")

with col3:
    if st.button("="):
        calculate_result()
    if st.button("C"):
        clear_expression()
    if st.button("sin"):
        update_expression("math.sin(math.radians(")
    if st.button("cos"):
        update_expression("math.cos(math.radians(")
    if st.button("tan"):
        update_expression("math.tan(math.radians(")
    if st.button("sqrt"):
        update_expression("math.sqrt(")

# Display the updated expression with parentheses for functions
if "math.sin" in st.session_state.expression or "math.cos" in st.session_state.expression or "math.tan" in st.session_state.expression or "math.sqrt" in st.session_state.expression:
    parentheses_count = st.session_state.expression.count("(")
    if parentheses_count > 0:
        closing_parentheses = ")" * parentheses_count
        st.write(f"**Complete Expression:** {st.session_state.expression}{closing_parentheses}")
else:
    st.write(f"**Complete Expression:** {st.session_state.expression}")

# Add some styling to make it more attractive
st.markdown("""
<style>
    .stButton > button {
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 20px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)
