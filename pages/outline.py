import json
import time
import streamlit as st

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to top, white 0%, #d9e1f0 13%, #d9e1f0 83%, white 90%);
        //padding: 500px;
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
with st.container(border=True, key="oc",height=500):
    # st.markdown("""
    #             <style>
    #             .st-key-oc {
    #                 background: linear-gradient(to top, white 0%, #d9e1f0 13%, #d9e1f0 83%, white 100%);
    #             }
    #             </style>
    #             """, unsafe_allow_html=True)
    if st.session_state.industry!=None and st.session_state.model_response["industry"] != st.session_state.industry:
        st.error(f"Unable to generate Outlines, you have mentioned {st.session_state.model_response['industry']} as industry in context but selected {st.session_state.industry}. Please check inputs!")
        if st.button("HOME", use_container_width=True):
            st.switch_page("main.py")
            st.rerun()
        st.stop()
    if st.session_state.solution!=[] and st.session_state.model_response["solution"] != st.session_state.solution:
        st.error(f"Unable to generate Outlines, you have mentioned {st.session_state.model_response['solution']} as solution in context but selected {st.session_state.solution}. Please check inputs!")
        if st.button("HOME", use_container_width=True):
            st.switch_page("main.py")
            st.rerun()
        st.stop()
    with open("mappings.json", 'r') as mappings:
        mappings = json.load(mappings)
    for mapping in mappings:
        if st.session_state.model_response["industry"] == mapping["industry"] or st.session_state.model_response["solution"] == mapping["solution"]:
            st.session_state.outlines = mapping["outlines"]
            st.session_state.deck_url = mapping["deck_url"]
            break
    if st.session_state.outlines == []:
        st.error("Unable to generate Outlines, Please check inputs!")
        st.write(st.session_state.model_response)
        if st.button("HOME", use_container_width=True):
            st.switch_page("main.py")
            st.rerun()
        st.stop()
    # outlines = ["outline a", "outline b", "outline c"]
    context_col,line_col, outlines_col= st.columns(spec=[0.2,0.02, 0.75])
    # context_col, outlines_col= st.columns(spec=[0.2,0.8])
    with context_col:
        st.text_area(
            label="**Context:**",
            value=st.session_state.context,
            height=370
        )
        st.button(
            "**Recreate**",
            use_container_width=True,
            disabled=True
        )
    with line_col:
        st.markdown("""
        <div style="width: 2px; height: 470px; background-color: grey; position: absolute; top: 0; left: 20%; transform: translateX(-50%);"></div>
        """, 
        unsafe_allow_html=True    
        )
    
    with outlines_col:
        st.write(f"**Refine any sections of the generated outlines [{len(st.session_state.outlines)}]**")
        with st.container(border=False, height=370):
            for i, outline in enumerate(st.session_state.outlines):
                container = st.container(border=True, key=f"{i}outline")
                # st.markdown(
                #     f"""
                #     <style>
                #     .st-key-{i}outline{{
                #     background-color: white;
                #     }}
                #     <style>
                #     """,
                #     unsafe_allow_html=True
                # )
                # container.write(f"**{outline}**")
                a, b, c, d = container.columns([0.7, 0.09, 0.09, 0.09], vertical_alignment="center")
                a.write(f"**{outline}**")
                b.button("🖉", key=f"{i}a", disabled=True)
                c.button("➕", key=f"{i}b", disabled=True)
                d.button("🗑", key=f"{i}c", disabled=True)
        _, __, ___ = st.columns(3)
        with ___:
            if st.button("**Generate Pitch**", use_container_width=True):
                with st.spinner('Generating new pitch...'):
                    time.sleep(2)
                    st.switch_page("pages/pitch.py")







