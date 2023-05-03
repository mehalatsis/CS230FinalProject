import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

data = pd.read_csv('RollerCoasters-Geo.csv')
df = pd.DataFrame(data, columns=['Design'])

st.title(':blue[Roller Coasters Frequency of Designs]')
designCount = df.groupby("Design")["Design"].count()
designs = ['4th Dimension', 'Flying', 'Inverted', 'Pipeline', 'Sit Down', 'Stand Up', 'Suspended', 'Wing']
coaster = ['1', '2', '3', '4', '5', '6', '7', '8']
fig, axes = plt.subplots()
c = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'pink']

axes.bar(coaster, designCount, color= c)
axes.set_title('Frequency of Roller Coaster Designs')
axes.set_ylabel("Number of Roller Coasters")
axes.set_xlabel("Designs of Roller Coasters")
handles = [mpatches.Patch(color=c[i], label=designs[i]) for i in range(len(designs))]
plt.legend(handles=handles)

plt.show()
st.pyplot(fig)

st.write('Above is a bar chart of the frequencies of each roller coaster design. The legend tells you which color bar is which roller coaster design.')