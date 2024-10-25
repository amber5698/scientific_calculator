import streamlit as st

# Title of the app
st.title("Scientific Calculator")

# Input for numbers
st.write("Enter numbers you want to calculate:")
numbers = []

# Allow users to input multiple numbers
while True:
    num_input = st.text_input("Enter a number (or type 'done' to finish):")
    
    if num_input.lower() == 'done':
        break
    
    try:
        number = float(num_input)
        numbers.append(number)
    except ValueError:
        st.error("Please enter a valid number.")

# Operations selection
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
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
