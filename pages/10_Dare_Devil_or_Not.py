import streamlit as st

st.title(':blue[How Much of a Dare Devil Are You?] :smiling_imp:')


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


st.header('Would you ride the Top Thrill Dragster?')
st.image('TopThrillDragster.jpg')
st.caption('https://www.thenews-messenger.com/story/news/2021/08/16/top-thrill-dragster-cedar-point-sandusky-ohio-closed-after-injury/8147917002/')
st.radio("Select an option",
                ('Definitely Yes', 'Yes', 'No', 'Hard No'))

st.header('Would you ride the Viper?')
st.image("ViperRC.jpg")
st.caption('https://www.reddit.com/r/rct/comments/cfgodb/viper_ncso_imgur_album_in_comments/')
st.radio("Select one of the options",
                ('Definitely Yes', 'Yes', 'No', 'Hard No'))

st.header('Would you ride Both?')
st.radio("Please select an option",
                ('Definitely Yes', 'Yes', 'No', 'Hard No'))