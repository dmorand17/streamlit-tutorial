import streamlit as st

st.title("Streamlit tutorial App")
st.write("This is my new App!")

st.divider()

st.header("Tutorial Elements")
st.subheader("Tutorial Elements sub header...")
st.text("Hello everyone, this is some sample text")

# Markdown
st.markdown("## This is a markdown header")

st.success("Successful message")
st.info("Information message")
st.warning("Warning message")
st.error("Error message")

# Exception
st.exception("NameError: name 'xyz' is not defined")

# Help
st.help(range)

st.write("text written by 'write'")

if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding the text")

# Radio
status = st.radio("What is your status?", ("Active", "Inactive"))

if status == "Active":
    st.success("You are active")
else:
    st.warning("Inactive, Activate")

# Selectbox
occupation = st.selectbox("Your occupation", ["Programmer", "Data Scientist", "Doctor"])
st.write("You selected this option:", occupation)

location = st.multiselect("Where do you work?", ("London", "New York", "Paris"))
st.write("You selected", len(location), "locations", location)

# Slider
st.slider("Select a number", min_value=0, max_value=10)

# Buttons
st.button("Simple Button")
if st.button("About"):
    st.text("Streamlit is cool!")

# Text Input
name = st.text_input("Enter your name", "Type Here...")
if st.button("Submit"):
    result = name.title()
    st.success(result)

# Text area
message = st.text_area("Enter your message", "Type Here...")
if st.button("Submit1"):
    result = message.title()
    st.success(result)

# Date input
import datetime

today = st.date_input("Today is", datetime.datetime.now())

# Time
the_time = st.time_input("The time is", datetime.time())

# JSON
st.text("Display JSON")
st.json({"name": "Jesse", "gender": "male"})

# Display Code
with st.echo():
    import pandas as pd

    df = pd.DataFrame()

# Progress Bar
import time

my_bar = st.progress(0)
for p in range(100):
    my_bar.progress(p + 1)
    time.sleep(0.01)

# Spinner
with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Finished!")

# Balloons
st.balloons()

# Sidebars
st.sidebar.header("About")
st.sidebar.text("This is my streamlit tutorial")


# Functions
@st.cache_data
def run_fxn():
    return range(100)


# Plot
st.pyplot()

# Dataframes
st.dataframe(df)

# Table
st.table(df)

st.write(run_fxn())

# Divider
st.divider()

button1 = st.button("Click me")

if button1:
    st.write("This is some text")

st.header("Start of the checkbox section")
st.subheader("This is the checkbox subheader")
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")

if button2:
    st.write(like)
    if like:
        st.write("I like it")
    else:
        st.write("I don't like it")

st.header("Start of the radio button list")
