import streamlit as st
st.title("Registration Form")
first, last = st.columns(2)
first.text_input("First Name")
last.text_input("Second Name")

# In Streamlit, the st.columns() function takes a list of column widths, which controls how space is divided among the columns.
# If you pass a list of two values like [3, 1], this creates two columns with widths proportional to those values. Here's what happens when using this list:
# The first column has a relative width of 3.
# The second column has a relative width of 1.
# The ratio between the two is therefore 3:1, meaning the first column takes up three times the space of the second column. In a 100% width scenario, this would translate to:
# The first column occupying 75% of the available space.
# The second column occupying 25% of the available space.

email,mob = st.columns([3,1])
email.text_input("Enter the Email:")
mob.text_input("Enter the mobile number")

user,pw1,pw2 = st.columns(3)
user.text_input("Enter the username")
pw1.text_input("Enter the password", type='password')
pw2.text_input("Retype the password",type='password')

ch, submit = st.columns(2)
ch.checkbox("Confirm Details")
submit.button("Submit")