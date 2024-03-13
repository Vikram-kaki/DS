import streamlit as st
from datetime import datetime

st.title("Title -> Vikram's Web Page")
st.header("Header -> Welcome to my web page.")
st.subheader("Please Share and bookmark the webpage for further updates.")
st.text("Text -> This web page about me!")

st.markdown("HI")
st.markdown("# HI")
st.markdown("## HI")
st.markdown('### HI')
st.markdown('#### HI')

st.success("Successfully added the file.")
st.info("Hurray, You are eligible for the 5lpa package.")
st.warning("File is unable to add")
st.error("Error 404")
st.exception(ZeroDivisionError("Div isn't possible with zero '0'"))

st.write(range(10))
st.write('range(10)')
st.write(1 * 2 * 3)

st.code("name = 'vikram'\n"
        "for i in range(10):\n"
        "\tprint(str(i)+' '+name)")

st.checkbox('Male')

if st.checkbox('Female'):
    st.info("You're Eligible for 15% OFF on the product")
st.checkbox('Others')

radio1 = st.radio('Select any one', ['AIDS', 'CSBS', 'CSE', 'CIVIL', 'ECE', 'EEE', 'MECH'])

if radio1 == 'CSBS':
    st.text('Make sure to look out for the off campus jobs.')
else:
    st.text('97% you will get on campus jobs.')

selectbox1 = st.selectbox("Select : ",
                          ['MERN STACK', 'ML OPS', 'DATA SCIENCE', 'DATA ANALYSIS', 'DEVOPS', 'SOFTWARE DEVELOPER'])

st.text(selectbox1)

multibox1 = st.multiselect('Select : ',
                           ['Java', 'Python', 'C', 'C++', 'C#', 'Ruby', 'Java Script', 'Php', 'Kotlin', 'Golang',
                            'Perl', 'Swift'])
st.write(multibox1)

st.button('I Agree')

st.slider("Select you're level of knowledge : ", 0, 100, step=2)

name = st.text_input("Enter you're name : ")

if name:
    st.write(name)

password = st.text_input("Enter you're password : ", type= 'password')

if password:
    st.success("Account created successfully.")
else:
    st.warning("Please Enter the password to continue further.")


suggestions = st.text_area("Any Suggestions")

if suggestions:
    st.text("Thank you for the feedback")


st.date_input("Enter dob ",value=datetime.today(), min_value=datetime(1900,1,1), max_value=datetime.today(), format='DD/MM/YYYY')
st.time_input("When will you be available")
# st.camera_input("Photo")
# st.image("Photo")
st.number_input("Enter you're number", 1)
st.chat_input("Anything to say ")
