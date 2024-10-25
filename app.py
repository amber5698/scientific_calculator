import streamlit as st
import math

# Title of the app
st.title("📚 Student-Friendly Scientific Calculator")

# Sidebar for navigation
st.sidebar.header("Choose an Operation")
operation = st.sidebar.selectbox(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root", "Sine", "Cosine", "Tangent")
)

# Input fields
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num1 = st.number_input("Enter first number:", format="%.2f")
    num2 = st.number_input("Enter second number:", format="%.2f")

if operation in ["Square Root", "Sine", "Cosine", "Tangent"]:
    num = st.number_input("Enter the number:", format="%.2f")

# Calculate and display results
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of {num1} + {num2} is {result:.2f}")
    
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of {num1} - {num2} is {result:.2f}")
    
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of {num1} * {num2} is {result:.2f}")
    
    elif operation == "Division":
        if num2 == 0:
            st.error("Error! Division by zero.")
        else:
            result = num1 / num2
            st.success(f"The result of {num1} / {num2} is {result:.2f}")
    
    elif operation == "Power":
        result = math.pow(num1, num2)
        st.success(f"The result of {num1} ^ {num2} is {result:.2f}")

    elif operation == "Square Root":
        if num < 0:
            st.error("Error! Square root of negative number.")
        else:
            result = math.sqrt(num)
            st.success(f"√{num} is {result:.2f}")

    elif operation == "Sine":
        result = math.sin(math.radians(num))
        st.success(f"sin({num}) is {result:.2f}")

    elif operation == "Cosine":
        result = math.cos(math.radians(num))
        st.success(f"cos({num}) is {result:.2f}")

    elif operation == "Tangent":
        result = math.tan(math.radians(num))
        st.success(f"tan({num}) is {result:.2f}")
