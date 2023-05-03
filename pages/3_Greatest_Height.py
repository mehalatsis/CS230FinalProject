import streamlit as st
import pandas as pd


def findMaxHeight(dataset):
    df = pd.DataFrame(dataset, columns=["Design", "Coaster", "Max_Height"])
    df = df.sort_values(["Design", "Max_Height"], ascending=[False, False])
    df = df.drop_duplicates(subset=["Design"], keep="first")
    return df[["Design", "Coaster", "Max_Height"]]


data = pd.read_csv('RollerCoasters-Geo.csv')
test = findMaxHeight(data)
print(test)


st.title(':blue[What Is The Maximum Height For A Sit Down Roller Coaster?]	:straight_ruler:')
st.header("Below is a chart of the maximum heights for each of the different designs of roller coasters")
st.write(test)
st.write("From the table we can see that sit down roller coaster Top Thrill Dragster has the max height for a sit down roller coaster at 420 feet!")
st.write("Also note we can see the other maximum heights for the other roller coasters. The sit down roller coaster is the highest roller coaster out of the designs.")
st.write("If you would like to view the code I used to create this chart, click the button below:")
seeCode = st.checkbox('See Code')
if seeCode:
    code = '''def findMaxHeight(dataset):
        df = pd.DataFrame(dataset, columns=["Design", "Coaster", "Max_Height"])
        df = df.sort_values(["Design", "Max_Height"], ascending=[False, False])
        df = df.drop_duplicates(subset=["Design"], keep="first")
        return df[["Design", "Coaster", "Max_Height"]]"'''
    st.code(code, language='python')


st.image("TopThrillDragster.jpg")
st.caption("https://www.thenews-messenger.com/story/news/2021/08/16/top-thrill-dragster-cedar-point-sandusky-ohio-closed-after-injury/8147917002/")
st.write("This roller coaster is now closed because someone got injured on it by a piece of the roller coaster, follow the link above to read more!")