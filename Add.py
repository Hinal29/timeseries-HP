import streamlit as st

# Add a colorful title
st.markdown("<h1 style='color: darkorange;'>🌞 Fun Adding App for Toddlers 🎈</h1>", unsafe_allow_html=True)

# Description for the app
st.markdown("<p style='color: teal; font-size: 18px;'>Let's add two numbers together!</p>", unsafe_allow_html=True)

# Input for the first number
first_number = st.number_input("Enter the first number:", step=1, format="%d", key="first")

# Input for the second number
second_number = st.number_input("Enter the second number:", step=1, format="%d", key="second")

# Button to calculate the sum
if st.button("Add"):
    # Calculate the sum
    result = first_number + second_number
    # Display the result with a colorful message
    st.markdown(f"<p style='color: green; font-size: 24px;'>🌟 The sum is: {result} 🌟</p>", unsafe_allow_html=True)
