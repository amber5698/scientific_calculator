import streamlit as st

# Title of the app
st.title("Scientific Calculator")

# Input for numbers
st.write("Enter numbers you want to calculate:")

# Initialize an empty list to store numbers
numbers = []

# Create a session state to keep track of the number of inputs
if 'input_count' not in st.session_state:
    st.session_state.input_count = 0

# Function to add more input fields
def add_input():
    st.session_state.input_count += 1

# Button to add more input fields
st.button("Add another number", on_click=add_input)

# Create input fields based on the count in session state
for i in range(st.session_state.input_count):
    num_input = st.text_input(f"Enter number {i + 1} (or type 'done' to finish):", key=f"input_{i}")

    if num_input.lower() == 'done':
        break
    
    try:
        number = float(num_input)
        numbers.append(number)
    except ValueError:
        if num_input:  # Check if input is not empty
            st.error("Please enter a valid number.")

# Operations selection
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if numbers:  # Ensure there are numbers to calculate
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
            st.success(f"The result is: {result}")
    else:
        st.error("Please enter at least one number.")
