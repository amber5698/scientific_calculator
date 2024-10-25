import streamlit as st

# Title of the app
st.title("📐 Scientific Calculator")

# Description
st.write("Welcome to the Scientific Calculator! 🎉")
st.write("Enter as many numbers as you want and select an operation to calculate.")

# Initialize a session state for numbers
if 'numbers' not in st.session_state:
    st.session_state.numbers = []

# Function to add a number input field
def add_number_input():
    st.session_state.numbers.append(0)

# Button to add more input fields
if st.button("Add Another Number ➕"):
    add_number_input()

# Display input fields for each number
for i in range(len(st.session_state.numbers)):
    num_input = st.number_input(f"Enter number {i + 1}:", key=f"input_{i}", format="%.2f")
    if num_input:
        st.session_state.numbers[i] = num_input

# Operations selection
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate 🔍"):
    numbers = st.session_state.numbers  # Get the list of numbers

    if len(numbers) == 0 or all(num == 0 for num in numbers):
        st.error("Please enter at least one valid number.")
    else:
        if operation == "Add":
            result = sum(numbers)
        elif operation == "Subtract":
            result = numbers[0] - sum(numbers[1:]) if len(numbers) > 1 else numbers[0]
        elif operation == "Multiply":
            result = 1
            for num in numbers:
                result *= num
        elif operation == "Divide":
            result = numbers[0]
            for num in numbers[1:]:
                if num != 0:
                    result /= num
                else:
                    st.error("Cannot divide by zero!")
                    result = None
                    break
        
        if result is not None:
            st.success(f"The result is: **{result:.2f}**")

# Clear button to reset the calculator
if st.button("Clear All 🗑️"):
    st.session_state.numbers.clear()
