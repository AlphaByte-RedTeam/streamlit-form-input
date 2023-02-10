import streamlit as st

# -- Number Input
# st.write("Form input")
# st.number_input("Number input", key="num")

# num_input = st.number_input("Input another number", key="a_num")
# st.write(f"The current number is {st.session_state.num}")
# plus_ten = st.session_state.a_num + st.session_state.num
# st.write(f"Add 10: {plus_ten}")

# -- Text input
st.header("Form input")
name_input = st.text_input("What's your name?", key="name")
hobby_input = st.text_input("What's your hobby?", key="hobby")

st.write(f"Hello, world! My name is {name_input} and my hobby is {hobby_input}")

# Sir Cevi Solution
num = st.number_input("Insert a number")
st.write(f"The current number is {num}")

add_ten = num + 10
st.write(f"Add 10 {add_ten}")
