import streamlit as st

st.title(":blue[Would You Ride These Roller Coasters?] :roller_coaster:")
st.header("See How Much Of A DareDevil You Are")
st.image("HomePageRC.jpg")
st.caption("https://www.pinterest.com/andrue14/rollercoasters/")

def findDevil(num):
    if num == 0:
        st.write('Oh I am a scared-y cat, not a dare devil at all.')
    elif num == 1:
        st.write('I take only very calculated risks, not like going on roller coasters.')
    elif num == 2:
        st.write('I do not really enjoy taking too many uncalculated risks.')
    elif num == 3:
        st.write('I could take an uncalculated risk once in a while!')
    elif num == 4:
        st.write('I am more of a scared-y cat most times than a dare devil.')
    elif num == 5:
        st.write('I will be a dare devil half of the time.')
    elif num == 6:
        st.write('I could get down with doing something crazy.')
    elif num == 7:
        st.write('Some of my days are spent being a dare devil.')
    elif num == 8:
        st.write('I would rather take risks to be a dare devil.')
    elif num == 9:
        st.write('I would do almost everything, pretty much a full dare devil.')
    else:
        st.write('I am a hard core dare devil, nothing I do is safe! Definitely no scared-y cat in me!')
    return


dareDevil = st.slider('On a scale of 1-10, how much of a dare devil are you?', 0, 10)
st.write(findDevil(dareDevil))

st.write("CS 230 Final Project")
st.write("Melissa Halatsis")


# fix titles to blue
# rewrite text to make it more user interface
