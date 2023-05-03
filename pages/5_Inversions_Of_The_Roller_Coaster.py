import streamlit as st
import pandas as pd

def getMaxInversions(dataset):
    df = pd.DataFrame(dataset)
    df = df[df['Inversions'] == 'Y']
    del df['Age_Group']
    del df['Park']
    del df['Type']
    del df['Year_Opened']
    del df['Longitude']
    del df['Latitude']
    del df['Top_Speed']
    del df['Max_Height']
    del df['Drop']
    del df['Length']
    df = df.sort_values("Num_of_Inversions", ascending=False)
    return df

def coasterNumInversions(dataFrame, invers):
    st.write(invers)
    if 0 in invers:
        df3 = dataFrame.query('Num_of_Inversions == 0')
        st.write('The roller coasters with no inversions are:')
        st.write(df3)
    if 1 in invers:
        df4 = dataFrame.query('Num_of_Inversions == 1')
        st.write('The roller coasters with 1 inversion are:')
        st.write(df4)
    if 2 in invers:
        df5 = dataFrame.query('Num_of_Inversions == 2')
        st.write('The roller coasters with 2 inversions are:')
        st.write(df5)
    if 3 in invers:
        df6 = dataFrame.query('Num_of_Inversions == 3')
        st.write('The roller coasters with 3 inversions are:')
        st.write(df6)
    if 4 in invers:
        df7 = dataFrame.query('Num_of_Inversions == 4')
        st.write('The roller coasters with 4 inversions are:')
        st.write(df7)
    if 5 in invers:
        df8 = dataFrame.query('Num_of_Inversions == 5')
        st.write('The roller coasters with 5 inversions are:')
        st.write(df8)
    if 6 in invers:
        df9 = dataFrame.query('Num_of_Inversions == 6')
        st.write('The roller coasters with 6 inversions are:')
        st.write(df9)
    if 7 in invers:
        df10 = dataFrame.query('Num_of_Inversions == 7')
        st.write('The roller coasters with 7 inversions are:')
        st.write(df10)




data = pd.read_csv('RollerCoasters-Geo.csv')
test = getMaxInversions(data)
print(test)

df2 = pd.DataFrame(data, columns=['Coaster', 'Num_of_Inversions'])



st.title(":blue[What Is The Max Amount of Inversions For a Roller Coaster and Where Is It, and What Is It's Duration?]")
st.write("Below we have a chart of the roller coasters with inversions showing how many inversions they have sorted in descending order, what the name of the roller coaster is and where it is located.")
st.write(test)
st.write("From the chart we see that a few roller coasters have seven inversions which is the max number for this data set. All of them are located in either Florida, California, or New Jersey. This could make sense because of Disney Land and World, and the Six Flags in New Jersey.")

inversions = st.multiselect('Choose the number of inversions to see the roller coasters that have that number of inversions',
                                    [0, 1, 2, 3, 4, 5, 6, 7])
gettingInversions = coasterNumInversions(df2, inversions)