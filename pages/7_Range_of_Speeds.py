import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('RollerCoasters-Geo.csv')
df = pd.DataFrame(data, columns=["Top_Speed"])

st.title(':blue[Range of Roller Coaster Speeds]	:roller_coaster::dash:')

st.write('Want to know what the range is for roller coaster speeds? Look at the histogram below!')
fig,ax = plt.subplots()

plt.hist(df, bins=[0,20,40,60,80,100,120, 140, 160],color='paleturquoise', edgecolor= 'lightseagreen')
plt.title("Histogram of Roller Coaster Speeds")
plt.xlabel('Speed MPH')
plt.ylabel('No. of Roller Coasters')
plt.show()
st.pyplot(fig)

st.write('Above is a histogram depicting the range of speeds that the roller coasters in this dataset have, as well as how many roller coasters have that bracket of speed. The most common speed is between 40 and 60 MPH with about 68 roller coasters at that speed.')
