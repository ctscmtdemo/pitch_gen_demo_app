import time
import json
import streamlit as st


def home_page():
    # st-emotion-cache-1wmy9hl
    with st.container(border=True, key="hc"):
        # st.markdown("""
        #     <style>
        #     .st-key-hc {
        #         background: linear-gradient(to top, white 0%, #d9e1f0 13%, #d9e1f0 83%, white 100%);
        #     }
        #     </style>
        #     """, unsafe_allow_html=True)
        st.markdown(
            """
            <div style="display: flex; align-items: center; justify-content: center;">
            <img src="https://lh3.googleusercontent.com/Xtt-WZqHiV8OjACMMMr6wMdoMGE7bABi-HYujupzevufo1kiHUFQZukI1JILhjItrPNrDWLq6pfd=s600-w600" alt="Logo" style="height: 70px;">
            <h1 style="margin-left: 0px;">PitchGen</h1>
            </div>
            """, 
            unsafe_allow_html=True
        )        
        st.session_state.context = st.text_area(
            label="**What is the context of your pitch?**",
            placeholder="Eg. Build a \"why google cloud\" pitch for a US-based ecommerce company. Include GenAI solutions, as well as slide on sustainablity.",
        )
        ind, sol, cust = st.columns(3)
        with ind:
            st.session_state.industry = st.selectbox(
                "**Industry**",
                options=["Retail", "Healthcare and Life Sciences", "Financial Services"],
                index=None,
                placeholder="select",
            )
        with sol:
            st.session_state.solution = st.multiselect(
                "**Solution**",
                options=["Artificial Intelligence", "Data Analytics",],
                # index=None,
                placeholder="select",
            )
            
        with cust:
            st.session_state.customer_name = st.text_input('**Customer Name**')
        _, __,___ = st.columns(3)
        with ___:
            if st.button('**Generate Outline**', use_container_width= True):
                _, __, ___, = st.columns([0.45, 0.5, 0.1])
                if st.session_state.context == '':
                    st.error("Please enter context!",)
                else:
                    with __:
                        with st.spinner('Generating Outlines...'):
                            time.sleep(3)
                            st.switch_page("pages/outline.py")
            # st.success("generating outline")


def main():
    st.set_page_config(
        page_icon="icons/gemini.png",
        page_title="PitchGen Demo",
        layout="wide"
        # initial_sidebar_state="collapsed"
    )
    # background: linear-gradient(to top, white 0%, #e4eaf5 13%, #e4eaf5 86%, white 95%);
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to top, white 0%, #d9e1f0 13%, #d9e1f0 83%, white 90%);
    }
    </style>
    """, unsafe_allow_html=True)
    st.session_state.context = ''
    st.session_state.industry = ''
    st.session_state.solution = ''
    st.session_state.customer_name = ''
    st.session_state.deck_url = ''
    st.session_state.outlines = []
    # if 'context' not in st.session_state:
    #     st.session_state.context = ''
    # if 'industry' not in st.session_state:
    #     st.session_state.industry = ''
    # if 'solution' not in st.session_state:
    #     st.session_state.solution = ''
    # if 'customer_name' not in st.session_state:
    #     st.session_state.customer_name = ''
    # if 'deck_url' not in st.session_state:
    #     st.session_state.deck_url = ''
    # if 'outlines' not in st.session_state:
    #     st.session_state.outlines = []
    home_page()

if __name__ == '__main__':
    main()