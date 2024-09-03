from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np


url_rg = "https://www.researchgate.net/profile/Ran-Tu-3"
url_gs = 'https://scholar.google.com/citations?user=ueR4KsUAAAAJ&hl=en'
#st.write("check out this [link](%s)" % url)

st.set_page_config(
    page_title="Welcome to Ran Tu's Homepage",
    page_icon=":rocket:",  # You can use an emoji or a local image path
    layout="wide",         # "centered" or "wide"
    initial_sidebar_state="collapsed",  # "expanded" or "collapsed"
)

pages = {
    "Home": {
        "title": "Welcome to the Home Page",
        "content": "This is the home page of the app. Here, you can find an overview of what this app offers."
    },
    "Work": {
        "title": "Work Experiences",
        "content": "This page gives you more information about the purpose and creators of this app."
    },
    "Education": {
        "title": "Education Experiences",
        "content": "Here you can find the contact information to reach out to the team."
    },
    "Projects": {
        "title": "Projects",
        "content": "Explore detailed data and insights on this page."
    },
    "Showcases": {
        "title": "Case studies",
        "content": "Explore detailed data and insights on this page."
    },
    "Supervision & Mentorship": {
        "title": "My students",
        "content": "Explore detailed data and insights on this page."
    },
    "Publications": {
        "title": "Peer-reviewed journal & conference articles",
        "content": "Explore detailed data and insights on this page."
    }
}
# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Direct to:",
     ('Home', 'Education', 'Work', 'Projects', 'Showcases', 'Supervision & Mentorship', 'Publication'))

# Display the selected page content
st.title(pages[page]["title"])
st.write(pages[page]["content"])

if pages == "Home":
    ###title
    st.markdown("# Welcome to the world of TreesLab*")
    st.markdown("### Technical and Strategical Solutions to Transport Decarbonization")
    st.markdown('##### *"Trees" stands for: Transportation, Environment, Economy, Sustainability')
    st.markdown("---")  # Horizontal line

    ##customize background and text color
    st.markdown(
        """
        <style>
        body {
            background-color: #eff5e4;
            color: #333333;
        }
        .stTextInput {
            color: #4CAF50;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    #news
    st.markdown('Recent news')
    col1, col2 = st.columns(2)

    with col1:
        st.header("Taking a breath and a half-year break at UofT (Aug-16-2024)")
        st.write("Starting from Aug 16, I will be visiting the Department of Chemical Engineering and Applied Chemistry at the University of Toronto. Hopefully, this visiting will bring much new ideas on the travel-related environmental and social impact and mitigation practices from a different perspective")

    with col2:
        st.header("An in-depth communication with Austria-based NGO IIASA (Jul-17-2024)")
        st.write("Sponsored by the NSFC-funded international collaboration project, Decarbonization of Residents Life Behavior, we traveled to Vienna, Austria, and had a talk at the IIASA. MaaS business, travelers' behavior analysis, and influencing factors were discussed.")

#st.sidebar.header('Dictionary')

#if st.sidebar.button('Return to home'):
#  st.title(' ')

#st.sidebar.header('Dictionary')
#genre = st.sidebar.radio(
#     "Direct to:",
#     ('Home', 'Education', 'Working experience', 'Projects', 'Teaching', 'Studnets', 'Publication'))

elif pages == 'Education':
  st.subheader('Education')
  st.write('1. 2016-2020, PhD, Civil Engineering, University of Toronto')
  st.write(str('   '+ 'Supervisor: Marianne Hatzopoulou'))
  st.write(' ')
  st.write('2. 2014-2016, Master of Science, Civil Engineering, Virginia Tech')
  st.write(str('   '+ 'Supervisor: Hesham Rakha'))
  st.write(' ')
  st.write('3. 2013-2014, Exchange, Civil Engineering, EPFL')
  st.write(' ')
  st.write('4. 2010-2014, Bachelor of Engineering, Civil Engineering, Tongji University')
  st.write(str('   '+ 'Supervisor: Chao Yang'))

elif pages == 'Work':
  st.subheader('Working experience')
  st.write('1. 2021-current, Associate Professor, School of Transportation, Southeast University')
  st.write('2. 2020, Postdoctoral fellow, Civil Engineering, University of Toronto')

elif pages == "Showcases":
    st.write('')

elif pages == 'Projects':
  with st.expander("Current projects"):
    st.write("1. Eco-driving Guidance Decision Modelling Based on Drivers' Dynamic Cognitive Behaviour, National Natural Science Foundation of China (Young Scholar), PI, 2022-2024")
    st.write("2. Eco-driving Guidance Based on the Heterogeneity of Drivers’ Cognitive Workload, Natural Science Foundation of Jiangsu Province (Young Scholar), PI, 2021-2024")
    st.write("3. Modify Drivers' behaviour to Adapt for Lower Emissions, National Key R&D Program of China, Co-PI, 2021-2024")
    st.write("4. Dynamic Optimization of Electric Bus Services with Energy Consumption Uncertainties, FAW-Volkswagen China Environmental Protection Foundation Automotive Environmental Innovation Leading Program, PI, 2022-2023")
  with st.expander('Past projects'):
    st.write('1. Eco-Score: environmental evaluation of driving operations, NSERC of Canada, Participation, 2019-2020')

elif pages == 'Supervision & Mentorship':
  st.subheader('Courses')
  st.write("2nd-year undergraduate in the major of transportation, Transportation Management")

  with st.expander("Master students"):
    st.write("1. (2022-2024) Qiuzi Chen")
  with st.expander("Undergraduate students"):
    st.write("1. (2021) Yifei Su")
    st.caption("**Congraduations to Yifei for the acceptance of her paper in the TRB 2022🎉🎉🎉!**")
    st.write("2. (2022) Qiuzi Chen")
    st.write("3. (2022) Haoran Chen")
  with st.expander("SRTP"):
    st.write("1. (2021-2022) Eco-Scoring for Ride-hailing Vehicles; Led by Yaofeng Yu")
    st.caption("Check out the latest updates @[link](%s)" % "https://share.streamlit.io/trjade1234/eco_score/main")
    st.write("2. (2021-2022) Carbon Benefit Design to Encourage Greener Travel Behaviour; Led by Ruoyu Chen")
    st.write("3. (2021-2022) Low-Carbon MaaS (Mobility-as-a-Service) Design; Led by Yuchen Ling")

elif pages == 'Publication':
  st.subheader('Publication')
  #st.success("More papers, check my [ResearchGate](%s), or [GoogleScholar](%s)" % (url_rg, url_gs))
  st.write('1.	Tu, R., Xu, J., Wang, A., Zhang, M., Zhai, Z., Hatzopoulou, M., 2022. Real-world emissions and fuel consumption of gasoline and hybrid light duty vehicles under local and regulatory drive cycles. Sci. Total Environ. 805, 150407. https://doi.org/10.1016/j.scitotenv.2021.150407')
  st.write('2.	Tu, R., Xu, J., Wang, A., Zhai, Z., Hatzopoulou, M., 2021. Effects of ambient temperature and cold starts on excess NOx emissions in a gasoline direct injection vehicle. Sci. Total Environ. 760, 143402.')
  st.write('3.	Tu, R., Li, T., Meng, C., Xie, Y., Xie, F., Yang, F., Chen, H., Li, Y., Gao, J., Liu, Y., 2021. Real-world Emissions of Construction Mobile Machines and Comparison to a Non-road Emission Model. Sci. Total Environ. 771, 145365. https://doi.org/10.1016/j.scitotenv.2021.145365')
  st.write('4.	Tu, R., Gai, Y. (Jessie), Farooq, B., Posen, D., Hatzopoulou, M., 2020. Electric vehicle charging optimization to minimize marginal greenhouse gas emissions from power generation. Appl. Energy 277, 115517. https://doi.org/10.1016/j.apenergy.2020.115517')
  st.write('5.	Tu, R., Alfaseeh, L., Djavadian, S., Farooq, B., Hatzopoulou, M., 2019. Quantifying the impacts of dynamic control in connected and automated vehicles on greenhouse gas emissions and urban NO2 concentrations. Transp. Res. Part D Transp. Environ. 73, 142–151. https://doi.org/10.1016/j.trd.2019.06.008')
  st.write('6.	Tu, R., Kamel, I., Abdulhai, B., Hatzopoulou, M., 2018. Reducing Transportation Greenhouse Gas Emissions Through the Development of Policies Targeting High-Emitting Trips. Transp. Res. Rec. https://doi.org/10.1177/0361198118755714')
  st.write('7.	Tu, R., Kamel, I., Wang, A., Abdulhai, B., Hatzopoulou, M., 2018. Development of a hybrid modelling approach for the generation of an urban on-road transportation emission inventory. Transp. Res. Part D Transp. Environ. 62, 604–618. https://doi.org/10.1016/j.trd.2018.04.011')
  st.write('8.	Tu, R., Wang, A., Hatzopoulou, M., 2019. Improving the Accuracy of Emission Inventories with a Machine-Learning Approach and Investigating Transferability across Cities. J. Air Waste Manage. Assoc. 69, 1377–1390. https://doi.org/10.1080/10962247.2019.1668872')
  st.write('9.	Zhang, A., Li, T., Tu, R., Dong, C., Chen, H., Gao, J., Liu, Y., 2021. The Effect of Nonlinear Charging Function and Line Change Constraints on Electric Bus Scheduling. Promet - Traffic&Transportation 33, 527–538. https://doi.org/10.7307/ptt.v33i4.3730')
  st.write('10.	Zhai, Z., Tu, R., Xu, J., Wang, A., Hatzopoulou, M., 2020. Capturing the variability in instantaneous vehicle emissions based on field test data. Atmosphere (Basel). 11. https://doi.org/10.3390/ATMOS11070765')
  st.write('11.	Wang, A., Tu, R., Xu, J., Zhai, Z., Hatzopoulou, M., 2022. A novel modal emission modelling approach and its application with on-road emission measurements. Appl. Energy 306, 117967.')
