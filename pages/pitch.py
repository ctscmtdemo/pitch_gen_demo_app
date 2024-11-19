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
            if layout == "Timeline":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vS68hEl2ijHwKdNNvuB07aBRy7wA6VRehpv355iWgFHtOJwBzIoDX5Vxrn8EBWfFiTRXgrnyEsRv9WK/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Next Steps":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSlsKdAXktizJiacJRbZSSh3Az4VGhJdQD6lse028xKGStUIO0VfmHpxWKccj9ko6VM144J20RBajgX/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Circle Charts":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRjDMeq-mL1DDEx82Ot881o89tDeBb7RfXx5VGohjTiyGvBSU_HcUm1x-Tk5YQw1Eye_kHjGESsh03b/embed?start=false&loop=false&delayms=3000", height=300)
        
        if st.button("Generate Slide", use_container_width=True):
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
            if layout == "Timeline":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vS68hEl2ijHwKdNNvuB07aBRy7wA6VRehpv355iWgFHtOJwBzIoDX5Vxrn8EBWfFiTRXgrnyEsRv9WK/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Next Steps":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSlsKdAXktizJiacJRbZSSh3Az4VGhJdQD6lse028xKGStUIO0VfmHpxWKccj9ko6VM144J20RBajgX/embed?start=false&loop=false&delayms=3000", height=300)
            elif layout == "Circle Charts":
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRjDMeq-mL1DDEx82Ot881o89tDeBb7RfXx5VGohjTiyGvBSU_HcUm1x-Tk5YQw1Eye_kHjGESsh03b/embed?start=false&loop=false&delayms=3000", height=300)
        
        if st.button("Transform Slide", use_container_width=True, key="tansform_button"):
            with st.spinner('Transforming...'):
                time.sleep(3)
            st.success("Success")
if st.button("HOME"):
    st.switch_page("main.py")
    st.rerun()