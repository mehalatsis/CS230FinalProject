import streamlit as st
import pandas as pd

def findMaxHeight(dict):
    max_heightW = 0
    nameW = ''

    for index, row in dict.iterrows():
        if row['Type'] == 'Wooden':
            if row['Max_Height'] > max_heightW:

                max_heightW = row['Max_Height']
                nameW = row['Coaster']
    st.write("The wooden roller coaster with the maximum height of ", max_heightW, "is ", nameW, ".")
    st.image('SonOfBeast.jpg')
    st.caption('https://www.cincinnati.com/picture-gallery/entertainment/2014/04/15/kings-islands-retired-rides/7744843/')
    st.write('Son of Beast roller coaster is now retired.')

    max_heightS = 0
    nameS = ''
    for index, row in dict.iterrows():
        if row['Type'] == 'Steel':
            if row['Max_Height'] > max_heightS:
                max_heightS = row['Max_Height']
                nameS = row['Coaster']
    st.write("The steel roller coaster with the maximum height of ", max_heightS, "is ", nameS, ".")
    st.image('TopThrillDrag2.jpg')
    st.caption('https://wwmt.com/news/state/cedar-point-teases-reopening-of-top-thrill-dragster')
    st.write('Top Thrill Dragster is expected to reopen in 2024!')




data = pd.read_csv('RollerCoasters-Geo.csv')
df = pd.DataFrame(data, columns=["Coaster", "Type", "Max_Height"])
st.title(':blue[Tallest Wooden and Steel Roller Coasters]')

test = findMaxHeight(df)





