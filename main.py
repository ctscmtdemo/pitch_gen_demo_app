import time
import json
import streamlit as st
# from st_screen_stats import ScreenData, StreamlitNativeWidgetScreen, WindowQuerySize, WindowQueryHelper

# screenD = ScreenData(setTimeout=1000)
# screen_d = screenD.st_screen_data()
# st.write(screen_d)

def home_page():
    # st-emotion-cache-1wmy9hl
    with st.container(border=True, key="hc"):#, height=320):
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
            <img src="https://lh3.googleusercontent.com/Xtt-WZqHiV8OjACMMMr6wMdoMGE7bABi-HYujupzevufo1kiHUFQZukI1JILhjItrPNrDWLq6pfd=s600-w600" alt="Logo" style="height: 60px;">
            <h1 style="margin-left: 0px; font-size: 40px">Pitch Generator</h1>
            </div>
            """, 
            unsafe_allow_html=True
        )        
        st.session_state.context = st.text_area(
            label="**What is the context of your pitch?**",
            placeholder="Eg. Build a \"why google cloud\" pitch for a US-based ecommerce company. Include GenAI solutions, as well as slide on sustainablity.",
            height=68
        )
        st.markdown(
            """
            <p>Enter a prompt above to create your presentation. Add details below to further customize the content of your asset. <a href="">Learn more</a></p>
            """,
            unsafe_allow_html = True
        )
        ind, sol, cust, dum = st.columns(4)
        with ind:
            st.session_state.industry = st.selectbox(
                "*Industry*",
                options=["Financial Services","Retail","Technology"],
                index=None,
                placeholder="select"
            )
            
        with sol:
            st.session_state.solution = st.multiselect(
                "*Solution*",
                options=["Artificial Intelligence", "Data Analytics"],
                # index=None,
                placeholder="select",
            )
            
        with cust:
            st.session_state.customer_name = st.text_input('*Customer Name*')
        # dum1, dum2, dum3, er = st.columns(4, vertical_alignment="center")
        with dum:
            # st.text("")
            # st.text("")
            # st.text("")
            st.session_state.er_num = st.text_input('*Version Number* *', placeholder="VR #")
        reg, prod, aud, dum = st.columns(4)
        with reg:
            st.session_state.region = st.selectbox(
                "*Region*",
                options=["GLOBAL"],
                index=None,
                placeholder="select",
            )
        with prod:
            st.session_state.product = st.multiselect(
                "*Product*",
                options=["AI Accelerators", "AI Accelerators & ML Frameworks", "AI Component - Natural Language", "AI Platform Training", "AI Platform Vision NAS", "Advisory Notifications", "Agent Assist", "AlloyDB", "Analytics Hub", "Anthos", "Anthos Config Management", "Anthos for Virtual Machines", "Anti-Money Laundering (AML)", "Apigee", "Apigee Platform", "App Engine", "AppSheet", "Artifact Registry", "Backup for GKE", "BeyondCorp Enterprise", "BigQuery", "BigQuery / Dremel", "BigQuery BI Engine", "BigQuery ML", "BigQuery Omni", "Blockchain Node Engine", "CCAI Insights", "CCAI Platform", "Certificate Authority Service", "Chrome Enterprise", "Chrome OS", "Chronicle SIEM", "Chronicle SOAR", "Chronicle Security Operations", "Cloud Access Policy (CAP) (Formerly IAM)", "Cloud Armor", "Cloud Backup & DR", "Cloud Bigtable", "Cloud Build", "Cloud CDN", "Cloud Composer", "Cloud DNS", "Cloud Data Catalog", "Cloud Data Fusion", "Cloud Data Loss Prevention (DLP) / Syft", "Cloud Data Transfer - Appliance", "Cloud Dataprep by Trifacta", "Cloud Dataflow", "Cloud Debugger", "Cloud Deploy", "Cloud Endpoints & API Gateway", "Cloud Firestore", "Cloud Functions", "Cloud Functions for Firebase", "Cloud Generative AI", "Cloud Graphics Processing Unit (GPU)", "Cloud HSM", "Cloud Identity-Aware Proxy", "Cloud Interconnect", "Cloud IoT Core", "Cloud KMS", "Cloud Load Balancing", "Cloud Logging", "Cloud Memorystore", "Cloud Monitoring", "Cloud NAT", "Cloud Marketplace", "Cloud Run", "Cloud SQL", "Cloud Scheduler", "Cloud Spanner", "Cloud Tasks", "Cloud Tensor Processing Unit (TPU)", "Cloud Trace", "Cloud VPN", "Cloud Workflows", "Connected Sheets", "Core Compute", "Cross Cloud Network", "Contact Center Insights", "Data Fusion", "Data Studio", "Database Migration Service", "Databases", "Dataplex", "Dataproc", "Datastream", "Dialogflow", "Document AI - Human in the Loop", "Document AI - Pretrained Models", "Document AI Warehouse", "Document AI Workbench (Custom Models)", "Document OCR", "Earth Engine", "Eventarc", "Filestore", "Firebase App Distribution", "Firebase Auth", "Firebase Machine Learning", "GCE - Autoscaler", "GCP Support", "Gemini for Google Cloud", "Gemini in Workspace", "Google Cloud Storage", "Google Distributed Cloud (GDC) in connected configuration", "Google Edge Cloud (GEC)", "Google Kubernetes Engine (GKE)", "Google Maps Platform", "Google Workspace", "Google Workspace Security", "Immersive Stream for XR", "Local SSD", "Looker", "ML Pipelines", "Mandiant", "Mandiant Consulting", "Mandiant Managed Defense", "Mandiant Threat Intelligence", "Media CDN", "Media Rendering APIs", "Natural Language API", "Networking", "Optimization AI", "Oracle on Bare Metal Servers", "Persistent Disk (PD)", "Pub/Sub", "Retail Recommendations AI", "Retail Search", "Secret Manager", "Security Analytics & Operations", "Security Command Center (SCC)", "Service Infrastructure", "Smart Factory Platform: Manufacturing", "Speech-to-Text API", "Storage Transfer Service", "TensorFlow Enterprise", "Transcode API", "Translation API", "VMware Engine", "Virtual Private Cloud (VPC)", "VPC Service Controls", "Vertex AI", "Vertex AI Agent Builder", "Video Intelligence API", "Vision API", "Visual Inspection AI", "Web Risk", "Web3", "reCAPTCHA Enterprise and Web Risk"],
                # index=None,
                placeholder="select",
            )

        with aud:
            st.session_state.audience = st.multiselect(
                "*Audience*",
                options=["CDO", "CEO", "CFO", "CIO", "CMO", "CTO", "ITDM", "Line of Business", "Others"],
                # index=None,
                placeholder="select",
            )
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
        page_title="CTS-PitchGen Demo",
        layout="wide",
        # initial_sidebar_state="collapsed"
    )
    # background: linear-gradient(to top, white 0%, #e4eaf5 13%, #e4eaf5 86%, white 95%);
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to top, white 8%, #d9e1f0 13%, #d9e1f0 83%, white 90%);
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 6rem;
                    padding-right: 6rem;
                }

        </style>
        """, unsafe_allow_html=True)


    st.session_state.context = ''
    st.session_state.industry = ''
    st.session_state.solution = ''
    st.session_state.customer_name = ''
    st.session_state.region = ''
    st.session_state.product = ''
    st.session_state.audience = ''
    st.session_state.er_num = ''
    st.session_state.deck_url = ''
    st.session_state.outlines = []
    
    home_page()

if __name__ == '__main__':
    main()