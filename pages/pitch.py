import streamlit as st
import time
import streamlit.components.v1 as components
import os

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to top, white 0%, #d9e1f0 13%, #d9e1f0 83%, white 90%);
    }
    </style>
    """, 
    unsafe_allow_html=True
)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1.8rem;
                    padding-bottom: 0rem;
                    padding-left: 4rem;
                    padding-right: 4rem;
                }
        </style>
        """, unsafe_allow_html=True)
# components.iframe(
#     "https://docs.google.com/presentation/d/e/2PACX-1vSBeu8eyMy7bvcN49Lkyia8aw9fXbJ6tMnPBN5Y2qHLrpOaHHZNQDL7YQmi6NutIIRTwRVZEfJZNpOS/embed?start=false&loop=false&delayms=3000",

# )

def list_files_in_directory(directory_path):
    file_list = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            file_list.append(file_name)
    return file_list

pitch, side_bar =  st.columns([.9, .4])

with pitch.container(border=True):
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

with side_bar.popover("Edit my Presentation", use_container_width=True):
    add_slide, transform_slide = st.tabs(["**Add Slide**", "**Transform Slide**"],)
    with add_slide:
        slide_title = st.text_input("*Slide Title*", placeholder="Slide Title")
        slide_content = st.text_area("*Slide Content*", placeholder="This slide provides an overview of the sustainable benefits of GCP")
        theme = st.selectbox(
            label="*Theme & Layout*",
            options=["Google Cloud Style 2024"],
            placeholder="Select Theme",
            index=None
            )
        layout = st.selectbox(
            label="",
            label_visibility="collapsed",
            options=["Case Study", "Charts", "Circle Charts", "Next Steps", "Timeline", "Context"],
            placeholder="Select Layout",
            index=None
        )
        
        with st.container(border=False):
            if layout == "Case Study":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQjnv7IgftNnIBH_gZH9U6Rvw7e6pmWMYBLfY9cd0lnyPMe6lWHQCbfVzzVQDDKaysVrQNUJMWyeZIb/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Charts":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTWQhkfeLcB-BUX2AXykfA4oihzWXIv92IJfyk-A0YEwj29geyUNboiUDSWeJMwRizWqb5we94w3ofi/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Context":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTs0_f7f0z99GyExfcpU6FS8ZqptoOgcYoBodQ_PtdHTbYMnOV5RHu0mprW4s8u5rp0c3nNeYqh-oOo/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Timeline":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRKx_IflRWq6KmroNHwqFutHAy95OQW_YbXsvrrFeB4hL1RcHaCVv8ijMNO5myVAgWwOdfTYG3Cq4DR/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Next Steps":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vT4qOYAdiPMBQsdZKohgze0cTnocfp2Ruc0S6UijiMf_vM_WyINv7Vgk7KjqaMY-B_BIQ1sAwll_P-s/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Circle Charts":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ9DsmjjiV-zmaySzrluyEi4X__uNGBEONKyvof28_2jA0q5Orra1m_DQyaIssfwSzlPZkCmcDp4nDd/embed?start=false&loop=false&delayms=3000", height=300)
        
        if st.button("Generate Slide", use_container_width=True, disabled=True):
            with st.spinner('Generating...'):
                time.sleep(3)
            st.success("Success")
    with transform_slide:
        criteria = st.text_area("*Desired output criteria*", placeholder="Optional details to reshuffle your slide (eg. provide more details, rewrite for specific audience, make it visual)")
        theme = st.selectbox(
            label="*Theme & Layout*",
            options=["Google Cloud Style 2024"],
            placeholder="Select Theme",
            index=None,
            key="transform_theme"
            )
        layout = st.selectbox(
            label="",
            label_visibility="collapsed",
            options=["Case Study", "Charts", "Circle Charts", "Next Steps", "Timeline", "Context"],
            placeholder="Select Layout",
            index=None,
            key="transform_layout"
        )

        with st.container(border=False):
            if layout == "Case Study":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQjnv7IgftNnIBH_gZH9U6Rvw7e6pmWMYBLfY9cd0lnyPMe6lWHQCbfVzzVQDDKaysVrQNUJMWyeZIb/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Charts":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTWQhkfeLcB-BUX2AXykfA4oihzWXIv92IJfyk-A0YEwj29geyUNboiUDSWeJMwRizWqb5we94w3ofi/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Context":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTs0_f7f0z99GyExfcpU6FS8ZqptoOgcYoBodQ_PtdHTbYMnOV5RHu0mprW4s8u5rp0c3nNeYqh-oOo/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Timeline":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRKx_IflRWq6KmroNHwqFutHAy95OQW_YbXsvrrFeB4hL1RcHaCVv8ijMNO5myVAgWwOdfTYG3Cq4DR/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Next Steps":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vT4qOYAdiPMBQsdZKohgze0cTnocfp2Ruc0S6UijiMf_vM_WyINv7Vgk7KjqaMY-B_BIQ1sAwll_P-s/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Circle Charts":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQ9DsmjjiV-zmaySzrluyEi4X__uNGBEONKyvof28_2jA0q5Orra1m_DQyaIssfwSzlPZkCmcDp4nDd/embed?start=false&loop=false&delayms=3000", height=300)
        
        if st.button("Transform Slide", use_container_width=True, key="tansform_button", disabled=True):
            with st.spinner('Transforming...'):
                time.sleep(3)
            st.success("Success")
if st.button("HOME"):
    st.switch_page("main.py")
    st.rerun()