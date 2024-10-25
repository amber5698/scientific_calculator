import streamlit as st
import numpy as np
import sympy as sp

st.title("Scientific Calculator")

# Display for calculations
expression = st.text_input("Enter expression")

# Buttons for functions
if st.button("sin"):
    expression += "np.sin("
if st.button("cos"):
    expression += "np.cos("
# Add other scientific functions like sqrt, tan, log, etc.

# Calculate result
if st.button("="):
    try:
        result = eval(expression)
        st.write("Result:", result)
    except Exception as e:
        st.write("Error:", e)
