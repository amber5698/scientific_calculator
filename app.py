import streamlit as st
import math

# Title of the app
st.title("📚 Scientific Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f", value=0.0)

# Operation selection
operation = st.selectbox("Select operation:", 
                          ["Addition", "Subtraction", "Multiplication", "Division", 
                           "Power", "Square Root", "Sine", "Cosine", "Tangent"])

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
        if num1 < 0:
            st.error("Error! Square root of negative number.")
        else:
            result = math.sqrt(num1)
            st.success(f"√{num1} is {result:.2f}")

    elif operation == "Sine":
        result = math.sin(math.radians(num1))
        st.success(f"sin({num1}) is {result:.2f}")

    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
        st.success(f"cos({num1}) is {result:.2f}")

    elif operation == "Tangent":
        result = math.tan(math.radians(num1))
        st.success(f"tan({num1}) is {result:.2f}")
