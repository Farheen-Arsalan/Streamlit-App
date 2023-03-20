import streamlit as st

st.title("Our First Streamlit App")

from PIL import Image

st.subheader("This is subheader")

image = Image.open('data.jpg')

st.image(image, caption='Sunrise by the mountains')

st.write("Writing here")

st.markdown("This is markdown")

st.success("Congrats you run App successfully")

st.info("This is information")

st.warning("Be cautious")
st.error("Error")

st.help(range)

import numpy as np
import pandas as pd

dataframe=np.random.rand(10,20)

st.dataframe(dataframe)
st.text("---"*100)

df=pd.DataFrame(np.random.rand(10,20),columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=1))

st.text("---"*100)
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])

st.line_chart(chart_data)
st.text("---"*100)

st.area_chart(chart_data)

chart_data=pd.DataFrame(np.random.randn(50,3),columns=['a','b','c'])
st.bar_chart(chart_data)




import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)

plt.hist(arr, bins=20)

st.pyplot()


st.text("---"*100)


import plotly
import numpy as np
from plotly.figure_factory import create_distplot



# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = create_distplot(
        hist_data, group_labels,curve_type='normal',
    show_rug=False,bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

st.text("---"*100)

df=pd.DataFrame(np.random.randn(100,2)/[50,50]+[37.76,-122.4],columns=['lat','lon'])

st.map(df)

st.text("---"*100)

if st.button("Say Hello"):
        st.write("Hello is here")
else:
        st.write("Why are you here")


st.text("---"*100)

genre=st.radio("What is your favourite genre?", ("comedy","Drama","Documantary"))

if genre=='comedy':
        st.write("oh you like Comedy")
elif genre=="Drama":
        st.write("Yeah Drama cool")
else:
        st.write("i see!!")


st.text("---"*100)

option=st.selectbox("How was your night?",("Fantastic","Awesome","so-so"))
st.write("You said you was ",option)

st.text("---"*100)

option=st.multiselect("How was your night, you can select multiple choice?",("Fantastic","Awesome","so-so"))
st.write("You said you was ",option)


st.text("---"*100)
age=st.slider("How old are you?",0,100,18)
st.write("Your age is: ",age )

values=st.slider("Select a range of values", 0,200,(15,80))

st.write("You selected a range between :", values)


number=st.number_input("Input number ")
st.write("The number you inputted is:",number)

st.text("---"*100)
st.text("---"*100)

upload_file=st.file_uploader("Choose a csv file", type='csv')

if upload_file is not None:
        data=pd.read_csv(upload_file)
        st.write(data)
        st.success("Successfully uploaded")
else:
        st.markdown("Please upload a csv file")

color = st.sidebar.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


st.text("---"*100)
st.text("---"*100)



add_sidebar=st.sidebar.selectbox("What is your favourite course?",('A course from TDS on building Data Web Application','others','Am Not sure'))


import time

my_bar=st.progress(0)
for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete+1)

with st.spinner('Wait for it'):
        time.sleep(5)
st.success('successful')

st.balloons()
































