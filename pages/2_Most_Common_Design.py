import streamlit as st
import pandas as pd


data = pd.read_csv('RollerCoasters-Geo.csv')
df = pd.DataFrame(data, columns=["Design"])
print(df)
test = df.groupby("Design")["Design"].count()
print(test)

st.title(":blue[Most Common Design of Roller Coasters]")
st.header("Below is a chart of the frequency of roller coasters for each of the designs")
st.write(test)
st.write("From the chart we see that the sit down roller coaster is the most common roller coaster design for this data set, with 124 roller coasters out of 157!")
st.write("The least common designs were 4th dimension, suspended and pipeline, which makes sense.")