from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import requests
import pydeck as pdk
import pandas as pd


url_rg = "https://www.researchgate.net/profile/Ran-Tu-3"
url_gs = 'https://scholar.google.com/citations?user=ueR4KsUAAAAJ&hl=en'
url_LI = "https://www.linkedin.com/in/ran-tu-jade/"
url_INS = "https://www.instagram.com/tr_jade/"
#st.write("check out this [link](%s)" % url)

st.set_page_config(
    page_title="Welcome to Ran Tu's Homepage",
    page_icon=":car:",  # You can use an emoji or a local image path
    layout="wide",         # "centered" or "wide"
    #initial_sidebar_state="collapsed",  # "expanded" or "collapsed"
)


pages = {
    "Home": {
        "title": "Welcome to the world of TreesLab*",
        "content": ""
    },
    "Professional milestons": {
        "title": "Experiences of work and education",
        "content": ""
    },
    #"Education": {
    #    "title": "Education Experiences",
    #    "content": ""
    #},
    "Projects": {
        "title": "Projects",
        "content": ""
    },
    "Showcases": {
        "title": "Case studies",
        "content": ""
    },
    "Supervision & Mentorship": {
        "title": "My students",
        "content": ""
    },
    "Publications": {
        "title": "Peer-reviewed journal & conference articles",
        "content": ""
    }
}

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Direct to:",
     ('Home', 'Professional milestons', 'Projects', 'Showcases', 'Supervision & Mentorship', 'Publications'))

# Display the selected page content
st.title(pages[page]["title"])
st.write(pages[page]["content"])

if page == "Home":
    ###title
    #st.write("Welcome to the world of TreesLab*")
    st.markdown("### Technical and Strategical Solutions to Transport Decarbonization")
    st.markdown('##### *"Trees" stands for: Transportation, Environment, Economy, Sustainability')
    st.caption('Check out my social media at: [LinkedIn](%s), or [Instagram](%s)' % (url_LI, url_INS))
    st.markdown("---")  # Horizontal line

    #news
    st.markdown('Recent updates')

    with st.container():
        # Create columns in the first container
        col1, col2 = st.columns(2)
        with col1:
            st.header("_Taking a breath and a half-year break at UofT (Aug-16-2024)_")
            st.write("Starting from Aug 16, I will be visiting the Department of Chemical Engineering and Applied Chemistry at the University of Toronto. Hopefully, this visiting will bring much new ideas on the travel-related environmental and social impact and mitigation practices from a different perspective")

        with col2:
            st.header("_Heart healing trip to the Northeastern province of China, Heilongjiang (Aug-03-20204)_")
            st.write("An annual breakdown with my beloved friends. This year, we went to Heilongjiang Province, Northeast of China.")

    with st.container():
        # Create columns in the first container
        col1, col2 = st.columns(2)
        with col1:
            st.header("_Annual TRB KPI completed! (Aug-01-2024)_")
            st.write("Our TreesLab members have successfully submitted their papers to the TRBAM. Shout out to the magnificent work of Yanfeng, Qiuzi, Shan, and Suyang!")
        with col2:
            st.header("_An in-depth communication with Austria-based NGO IIASA (Jul-17-2024)_")
            st.write("Sponsored by the NSFC-funded international collaboration project, Decarbonization of Residents Life Behavior, we traveled to Vienna, Austria, and had a talk at the IIASA. MaaS business, travelers' behavior analysis, and influencing factors were discussed.")

    st.markdown("---")  # Horizontal line


elif page == 'Professional milestons':
    st.subheader('Working experience')
    st.write('2024.08-current, Visiting Professor, Dept. Chemical Engineering & Applied Chemistry, University of Toronto')
    st.write('2023.01-current, Chief Scientist, Green-Distributor, Suzhou, China')
    st.write('2020.11-current, Associate Professor, School of Transportation, Southeast University')
    st.write('2020.05-2020.10, Postdoctoral Researcher, Dept. Civil & Mineral Engineering, University of Toronto & TD Inc.')

    st.subheader('Education')
    st.write('2016-2020, PhD, Dept. Civil & Mineral Engineering, University of Toronto, _Supervisor: Marianne Hatzopoulou_')
    #st.write('_Supervisor: Marianne Hatzopoulou_')

    st.write('2014-2016, Master of Science, Dept. Civil & Environmental Engineering, Virginia Tech, _Supervisor: Hesham Rakha_')
    #st.write('_Supervisor: Hesham Rakha_')

    st.write('2013-2014, Exchange, Civil Engineering, EPFL')

    st.write('2010-2014, Bachelor of Engineering, College of Transportation Engineering, Tongji University, _Supervisor: Chao Yang_')
    #st.write('_Supervisor: Chao Yang_')

elif page == "Showcases":
    st.write('')

elif page == 'Projects':
    with st.expander("Ongoing projects"):
        st.write("Eco-driving Guidance Decision Modelling Based on Drivers' Dynamic Cognitive Behaviour, National Natural Science Foundation of China, PI, 2022-2024")
        st.write("Eco-driving Guidance Based on the Heterogeneity of Drivers’ Cognitive Workload, Natural Science Foundation of Jiangsu Province, PI, 2021-2024")
        st.write("Modify Drivers' behaviour to Adapt for Lower Emissions, National Key R&D Program of China, Co-PI, 2021-2024")
        st.write("Dynamic Optimization of Electric Bus Services with Energy Consumption Uncertainties, FAW-Volkswagen China Environmental Protection Foundation Automotive Environmental Innovation Leading Program, PI, 2022-2023")
    with st.expander('Past projects'):
        st.write('Eco-Score: environmental evaluation of driving operations, NSERC of Canada, collaboration with TD Inc., Participation, 2019-2020')

elif page == 'Supervision & Mentorship':
    with st.expander('Courses'):
        st.write("2nd-year undergraduate in the major of transportation, Transportation Management")
    with st.expander("Master students"):
        st.write("(2024-2028) Xinran Ju. Thesis topic: Vehicle non-exhaust emission measurement and model development")
        st.write("(2024-2026) Suyang Xu. Thesis topic: Electric bus operation improvement")
        st.write("(2023-2027) Yanfeng Xu. Thesis topic: Air traveling emission mitigation considering air-rail transit")
        st.write("(2023-2025) Shan Xue. Thesis: On-road eco-driving guidance design and human factor analysis")
        st.write("(2022-2024) Qiuzi Chen. Thesis: Brakewear emission modeling and spatiotemporal distribution characteristics")
        st.caption("**(Updated 2024) Although Qiuzi is not able to be here in-person, his poster on non-exhaust emissions attracted a lot of interests!**")
        st.caption("**(Updated 2023) congratulations to Qiuzi for his first paper published in TR-D. This paper discusses about the robust solution for electric bus resource assignment. Check details here: @[link](%s)**" % "https://doi.org/10.1016/j.trd.2023.103724")

    with st.expander("Undergraduate thesis"):
        st.write('(2023) Chenming Niu')
        st.caption("**(Updated 2024) congratulations to Chenming for graduating from the UCB and starting a new journey at HKU for his PHD!**")
        st.caption("**(Updated 2024) also, check out our latest publication on E-bus resource allocation @[link](%s)**" % "https://doi.org/10.1016/j.multra.2024.100165")
        st.write('(2023) Shiyu Zhao')
        st.caption("**Congraduations to Shiyu for entering the Univeristy of British Columbia! Fingers crossed!**")
        st.write("(2022) Qiuzi Chen")
        st.write("(2022) Haoran Chen")
        st.write("(2021) Yifei Su")
        st.caption("**congratulations to Yifei for the acceptance of her paper in the TRB 2022🎉🎉🎉!**")
    with st.expander("Undergraduate student innovation projects"):
        st.write('(2022-2023) Transport-Renewable Energy Integration for Community and EV Charging')
        st.write("(2021-2022) Eco-Scoring for Ride-hailing Vehicles")
        #st.caption("Check out the latest updates @[link](%s)" % "https://share.streamlit.io/trjade1234/eco_score/main")
        st.write("(2021-2022) Carbon Benefit Design to Encourage Greener Travel Behaviour")
        st.caption('**congratulations to this excellent group for the publication on the carbon incentive design framework! Check out here: @[link](%s)**' % "https://doi.org/10.1016/j.cstp.2024.101205")
        st.write("(2021-2022) Low-Carbon MaaS (Mobility-as-a-Service) Design")

elif page == 'Publications':
    st.subheader('Publication')
    st.success("More papers, check my [ResearchGate](%s), or [GoogleScholar](%s)" % (url_rg, url_gs))
    st.write('(Updated in Aug-2024: 50+ peer-reviewed articles, 855 citations, h-index: 18)')
    with st.expander('Electric-vehicle related'):
        st.write('')
    with st.expander('Emission & Air quality related'):
        st.write('')
    with st.expander('Behavior analysis related'):
        st.write('')
