import streamlit as st
import time
import streamlit.components.v1 as components

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to top, white 0%, #d9e1f0 13%, #d9e1f0 83%, white 90%);
    }
    </style>
    """, 
    unsafe_allow_html=True
)
# components.iframe(
#     "https://docs.google.com/presentation/d/e/2PACX-1vSBeu8eyMy7bvcN49Lkyia8aw9fXbJ6tMnPBN5Y2qHLrpOaHHZNQDL7YQmi6NutIIRTwRVZEfJZNpOS/embed?start=false&loop=false&delayms=3000",

# )
with st.container(border=True):
    try:
        if st.session_state.deck_url == '':
            st.error("Unable to generate Pitch, Please check inputs!")
            if st.button("HOME", use_container_width=True):
                st.switch_page("main.py")
                st.rerun()
            st.stop()
    except Exception as e:
        st.error(f"Exception occoured. Unable to generate Pitch, Please check inputs!")
        if st.button("HOME", use_container_width=True):
            st.switch_page("main.py")
            st.rerun()
        st.stop()
    components.iframe(
        src=st.session_state.deck_url,
        height=450,
        # width=650,
    )
            # pass
    # st.markdown("""
    #     <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSBeu8eyMy7bvcN49Lkyia8aw9fXbJ6tMnPBN5Y2qHLrpOaHHZNQDL7YQmi6NutIIRTwRVZEfJZNpOS/embed?start=false&loop=false&delayms=3000" frameborder="0" height="400" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    #     """, 
    #     unsafe_allow_html=True
    # )
    # _, __, ___, = st.columns([0.2, 0.6, 0.2])
    # with __:
    
    
if st.button("HOME"):
    st.switch_page("main.py")
    st.rerun()