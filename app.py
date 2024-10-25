import streamlit as st
import math

# Set the title of the app
st.title("🧮 Scientific Calculator")

# Create a sidebar for operations
st.sidebar.header("Select Operation")
operation = st.sidebar.selectbox("Choose an operation:", 
                                   ["Addition", "Subtraction", "Multiplication", 
                                    "Division", "Power", "Square Root", 
                                    "Sine", "Cosine", "Tangent"])

# Input field for numbers
numbers = st.text_input("Enter numbers separated by commas (e.g., 1, 2, 3):")

# Process input numbers
if numbers:
    num_list = [float(num) for num in numbers.split(",")]

# Display the operation selected
st.write(f"**Selected Operation:** {operation}")

# Calculate and display results based on the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = sum(num_list)
        st.success(f"The result of **{' + '.join(map(str, num_list))}** is **{result:.2f}**")

    elif operation == "Subtraction":
        result = num_list[0] - sum(num_list[1:])
        st.success(f"The result of **{' - '.join(map(str, num_list))}** is **{result:.2f}**")

    elif operation == "Multiplication":
        result = math.prod(num_list)
        st.success(f"The result of **{' * '.join(map(str, num_list))}** is **{result:.2f}**")

    elif operation == "Division":
        if 0 in num_list[1:]:
            st.error("Error! Division by zero.")
        else:
            result = num_list[0]
            for num in num_list[1:]:
                result /= num
            st.success(f"The result of **{' / '.join(map(str, num_list))}** is **{result:.2f}**")

    elif operation == "Power":
        if len(num_list) != 2:
            st.error("Power operation requires exactly two numbers.")
        else:
            result = math.pow(num_list[0], num_list[1])
            st.success(f"The result of **{num_list[0]} ^ {num_list[1]}** is **{result:.2f}**")

    elif operation == "Square Root":
        if len(num_list) != 1:
            st.error("Square root operation requires exactly one number.")
        else:
            if num_list[0] < 0:
                st.error("Error! Square root of negative number.")
            else:
                result = math.sqrt(num_list[0])
                st.success(f"√{num_list[0]} is **{result:.2f}**")

    elif operation == "Sine":
        if len(num_list) != 1:
            st.error("Sine operation requires exactly one number.")
        else:
            result = math.sin(math.radians(num_list[0]))
            st.success(f"sin({num_list[0]}) is **{result:.2f}**")

    elif operation == "Cosine":
        if len(num_list) != 1:
            st.error("Cosine operation requires exactly one number.")
        else:
            result = math.cos(math.radians(num_list[0]))
            st.success(f"cos({num_list[0]}) is **{result:.2f}**")

    elif operation == "Tangent":
        if len(num_list) != 1:
            st.error("Tangent operation requires exactly one number.")
        else:
            result = math.tan(math.radians(num_list[0]))
            st.success(f"tan({num_list[0]}) is **{result:.2f}**")

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
