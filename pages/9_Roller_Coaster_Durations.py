import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('RollerCoasters-Geo.csv')
df = pd.DataFrame(data, columns=['Duration'])

st.title(':blue[How Long Are The Roller Coaster Durations?]:clock1:')

fig,ax = plt.subplots()

plt.hist(df, bins=[0,25,50,75,100,125,150, 175, 200, 225, 250], color='lightskyblue', edgecolor= 'mediumblue')
plt.title("Histogram of Roller Coaster Durations")
plt.xlabel('Duration SECONDS')
plt.ylabel('No. of Roller Coasters')
plt.show()
st.pyplot(fig)

st.write('Above is a histogram depicting the range of durations that the roller coasters in this dataset have in seconds, as well as how many roller coasters have that bracket of duration. The most common duration is between 100 and 125 seconds, which is around a minute and 40 seconds to two minutes. Around 37 roller coasters have that duration.')
