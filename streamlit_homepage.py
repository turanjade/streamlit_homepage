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
            st.header("_Heart healing trip to the Northeastern province of China, Heilongjiang (Aug-03-2024)_")
            st.write("An annual breakdown with my beloved friends. This year, we went to Heilongjiang Province, Northeast of China.")
            #st.image('/Users/ran/weiyun_sycn/5_Github/learngit/streamlit_homepage/Photos/Heilongjiang/luyuan.jpg', caption = 'Feed land of deer', use_column_width=True)

    with st.container():
        # Create columns in the first container
        col1, col2 = st.columns(2)
        with col1:
            st.header("_Annual TRB KPI completed! (Aug-01-2024)_")
            st.write("Our TreesLab members have successfully submitted their papers to the TRBAM. Shout out to the magnificent work of Yanfeng, Qiuzi, Shan, and Suyang!")
            #st.image

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
    with st.expander('**_Behavior analysis_**'):
        st.write('Xu, J., R. Tu, U. Ahmed, G. Amirjamshidi, M. Hatzopoulou, and M. Roorda. How to Fairly Evaluate Eco-Driving? An Eco-Score System Developed Using Vehicle Characteristics and Traffic Conditions. 2021.')
        st.write('Xu, J., R. Tu, U. Ahmed, G. Amirjamshidi, M. Hatzopoulou, and M. J. Roorda. An Eco-Score System Incorporating Driving Behavior, Vehicle Characteristics, and Traffic Conditions. Transportation Research Part D: Transport and Environment, Vol. 95, 2021, p. 102866. https://doi.org/10.1016/j.trd.2021.102866.')
        st.write('Tu, R., J. Xu, T. Li, and H. Chen. Effective and Acceptable Eco-Driving Guidance for Human-Driving Vehicles: A Review. International journal of environmental research and public health, Vol. 19, No. 12, 2022, p. 7310.')
        st.write('Wang, J., C. Huang, D. He, and R. Tu. Range Anxiety Among Battery Electric Vehicle Users: Both Distance and Waiting Time Matter. arXiv preprint arXiv:2306.05768, 2023.')
        st.write('Ahmed, U., R. Tu, J. Xu, G. Amirjamshidi, M. Hatzopoulou, and M. J. Roorda. GPS-Based Traffic Conditions Classification Using Machine Learning Approaches. Transportation research record, Vol. 2677, No. 2, 2023, pp. 1445–1454.')
        st.write('Wang, J., C. Huang, R. Tu, and D. He. Influential Factors of Users’ Trust in the Range Estimation Systems of Battery Electric Vehicles–A Survey Study in China. arXiv preprint arXiv:2301.10076, 2023.')
        st.write('Chen, Y., Z. Qian, S. Zhao, R. Tu, and C. Wu. Incentive Mechanism Design of “Mobility as a Service” for Carbon Emission Reduction. 2023.')
        st.write('Wang, J., R. Tu, A. Wang, and D. He. Trust in Range Estimation System in Battery Electric Vehicles--A Mixed Approach. IEEE Transactions on Human-Machine Systems, 2024.')
        st.write('Wang, J., C. Huang, W. Xie, D. He, and R. Tu. Rethink Data-Driven Human Behavior Prediction: A Psychology-Powered Explainable Neural Network. Computers in Human Behavior, Vol. 156, 2024, p. 108245.')
        st.write('Chen, R., S. Xu, Y. Du, Y. Wu, S. Zhao, R. Tu, and C. Wu. Carbon Generalized System of Preferences (CGSP) Programs: Key Design Dimensions and Attitudes of Potential Participants. Case Studies on Transport Policy, Vol. 16, 2024, p. 101205.')
        st.write('Xu, Z., Z. Zheng, D. Xiao, R. Tu, W. Ma, and N. Zheng. Assessing the Impact of Passenger Compliance Behavior in CAVs on Environmental Benefits. Transportation Research Part D: Transport and Environment, Vol. 133, 2024, p. 104278.')
    with st.expander('**_Control & optimization_**'):
        st.write('Dong, N., T. Li, S. Xu, R. Tu, H. Chen, and Y. Li. Capacity of Right-Turn Lane Affected by Bicycles during Red Phase. In CICTP 2023, pp. 1978–1987.')
        st.write('Tu, R. Network-Wide Assessment of Eco-Cooperative Adaptive Cruise Control Systems on Freeway and Arterial Facilities. Virginia Tech, 2016.')
        st.write('Tu, R., J. Du, H. A. Rakha, and H. Yang. System-Wide Impacts of Arterial and Freeway Eco-Cooperative Adaptive Cruise Control. 2017.')
        st.write('Alfaseeh, L., S. Djavadian, R. Tu, B. Farooq, and M. Hatzopoulou. Multi-Objective Eco-Routing in a Distributed Routing Framework. 2019.')
        st.write('Nan, S., L. Yan, R. Tu, and T. Li. Modeling Lane-Transgressing Behavior of e-Bike Riders on Road Sections with Marked Bike Lanes: A Survival Analysis Approach. Traffic injury prevention, Vol. 22, No. 2, 2020, pp. 153–157.')
        st.write('Tu, R., Y. (Jessie) Gai, B. Farooq, D. Posen, and M. Hatzopoulou. Electric Vehicle Charging Optimization to Minimize Marginal Greenhouse Gas Emissions from Power Generation. Applied Energy, Vol. 277, 2020, p. 115517. https://doi.org/10.1016/j.apenergy.2020.115517.')
        st.write('Djavadian, S., R. Tu, B. Farooq, and M. Hatzopoulou. Multi-Objective Eco-Routing for Dynamic Control of Connected \& Automated Vehicles. Transportation Research Part D: Transport and Environment, Vol. 87, 2020, p. 102513. https://doi.org/10.1016/j.trd.2020.102513.')
        st.write('Zhang, A., T. Li, R. Tu, C. Dong, H. Chen, J. Gao, and Y. Liu. The Effect of Nonlinear Charging Function and Line Change Constraints on Electric Bus Scheduling. Promet-Traffic&Transportation, Vol. 33, No. 4, 2021, pp. 527–538.')
        st.write('Su, Y., A. Zhang, T. Li, Q. Chen, J. Sun, and R. Tu. Optimizing the Charging Plan and Fleet Size of Electric Buses with Energy Consumption Variations. 2022.')
        st.write('Huang, P., R. Tu, X. Zhang, M. Han, Y. Sun, S. A. Hussain, and L. Zhang. Investigation of Electric Vehicle Smart Charging Characteristics on the Power Regulation Performance in Solar Powered Building Communities and Battery Degradation in Sweden. Journal of Energy Storage, Vol. 56, 2022, p. 105907.')
        st.write('Dong, C., Y. Li, H. Wang, R. Tu, Y. Chen, D. Ni, and Y. Liu. Lane-Changing Trajectory Control Strategy on Fuel Consumption in an Iterative Learning Framework. Expert Systems with Applications, Vol. 228, 2023, p. 120251.')
        st.write('Chen, Q., C. Niu, R. Tu, T. Li, A. Wang, and D. He. Cost-Effective Electric Bus Resource Assignment Based on Optimized Charging and Decision Robustness. Transportation Research Part D: Transport and Environment, Vol. 118, 2023, p. 103724.')
        st.write('Dong, N., T. Li, T. Liu, R. Tu, F. Lin, H. Liu, and Y. Bo. A Method for Short-Term Passenger Flow Prediction in Urban Rail Transit Based on Deep Learning. Multimedia Tools and Applications, Vol. 83, No. 22, 2024, pp. 61621–61643.')
        st.write('Niu, C., Q. Chen, R. Tu, D. Huang, and Y. Ye. Co-Optimizing Electric Bus Dispatching and Charging Considering Limited Resources and Battery Degradation. Multimodal Transportation, 2024, p. 100165.')
    with st.expander('**_Emission & air quality_**'):
        st.write('Margaritis, D., N. Dimokas, A. Dimitriadis--CERTH, Y. Li--DYNNOTEQ, T. Li, R. Tu, B. Liang, E. Özatay, O. Alanku\cs--OKAN, S. Faye, and others. MODALES D4. 2: Recommendations for Anti-Tampering and an Improved Mandatory Vehicle Inspection. ')
        st.write('Tu, R., I. Kamel, A. Wang, B. Abdulhai, and M. Hatzopoulou. Development of a Hybrid Modelling Approach for the Generation of an Urban On-Road Transportation Emission Inventory. Transportation Research Part D: Transport and Environment, Vol. 62, 2018. https://doi.org/10.1016/j.trd.2018.04.011.')
        st.write('Xu, J., R. Tu, A. Wang, L. Minet, C. Stogios, M. Saleh, N. Hilker, J. Wang, G. Evans, M. Hatzopoulou, A. Chemistry, J. Wang, A. Chemistry, G. Evans, and A. Chemistry. Quantifying the Contribution of Diesel Vehicles to Traffic Emissions Along an Urban Corridor: Implications for Cleaner Public Transit. The 97th Transportation Research Board Annual Meeting, 2018.')
        st.write('Xu, J., J. Wang, N. Hilker, M. Fallah-Shorshani, R. Tu, A. Wang, L. Minet, C. Stogios, G. Evans, and M. Hatzopoulou. Evaluation of MOVES Emission Factors Against Data from On-Road Measurements in a Large Canadian City. 2018.')
        st.write('Xu, J., N. Hilker, M. Turchet, M. K. Al-Rijleh, R. Tu, A. Wang, M. Fallahshorshani, G. Evans, and M. Hatzopoulou. Contrasting the Direct Use of Data from Traffic Radars and Video-Cameras with Traffic Simulation in the Estimation of Road Emissions and PM Hotspot Analysis. Transportation Research Part D: Transport and Environment, Vol. 62, 2018, pp. 90–101. https://doi.org/10.1016/j.trd.2018.02.010.')
        st.write('Xu, J., J. Wang, N. Hilker, M. Fallah-Shorshani, M. Saleh, R. Tu, A. Wang, L. Minet, C. Stogios, G. Evans, and M. Hatzopoulou. Comparing Emission Rates Derived from a Model with Those Estimated Using a Plume-Based Approach and Quantifying the Contribution of Vehicle Classes to on-Road Emissions and Air Quality. Journal of the Air and Waste Management Association, Vol. 68, No. 11, 2018. https://doi.org/10.1080/10962247.2018.1484395.')
        st.write('Stogios, C., M. Saleh, A. Ganji, R. Tu, J. Xu, M. Roorda, and M. Hatzopoulou. Determining the Effects of Automated Vehicle Driving Behavior on Vehicle Emissions and Performance of an Urban Corridor. 2018.')
        st.write('Tu, R., I. Kamel, B. Abdulhai, and M. Hatzopoulou. Reducing Transportation Greenhouse Gas Emissions through the Development of Policies Targeting High-Emitting Trips. Transportation Research Record, Vol. 2672, No. 25, 2018, pp. 11–20. https://doi.org/10.1177/0361198118755714.')
        st.write('Tu, R., I. Kamel, A. Wang, B. Abdulhai, and M. Hatzopoulou. Developing Urban Transportation GHG Emission Inventories: Which Model Resolution and Input Detail Is Appropriate? 2018.')
        st.write('Wang, A., R. Tu, Y. Gai, L. G. Pereira, I. D. Posen, and M. Hatzopoulou. Capturing the Uncertainties in Regional Emission Estimates Related to Vehicle Electrification Can Improve the Robustness of Decision-Making. 2019.')
        st.write('Tu, R., L. Alfaseeh, S. Djavadian, B. Farooq, and M. Hatzopoulou. Quantifying the Impacts of Dynamic Control in Connected and Automated Vehicles on Greenhouse Gas Emissions and Urban NO2 Concentrations. Transportation Research Part D: Transport and Environment, Vol. 73, 2019, pp. 142–151. https://doi.org/10.1016/j.trd.2019.06.008.')
        st.write('Tu, R., A. Wang, and M. Hatzopoulou. Improving the Accuracy of Emission Inventories with a Machine-Learning Approach and Investigating Transferability across Cities. Journal of the Air & Waste Management Association, Vol. 69, No. 11, 2019, pp. 1377–1390.')
        st.write('Xu, J., M. Saleh, A. Wang, R. Tu, and M. Hatzopoulou. Embedding Local Driving Behaviour in Regional Emission Models to Increase the Robustness of On-Road Emission Inventories. Transportation Research Part D: Transport and Environment, Vol. 73, 2019. https://doi.org/10.1016/j.trd.2019.05.011.')
        st.write('Tu, R., A. Wang, and M. Hatzopoulou. Improving the Accuracy of Emission Inventories with a Machine-Learning Approach and Investigating Transferability across Cities (Vol 69, Pg 1377, 2020). JOURNAL OF THE AIR \& WASTE MANAGEMENT ASSOCIATION, Vol. 70, No. 10, 2020, p. 1060.')
        st.write('Zhai, Z., R. Tu, J. Xu, A. Wang, and M. Hatzopoulou. Capturing the Variability in Instantaneous Vehicle Emissions Based on Field Test Data. Atmosphere, Vol. 11, No. 7, 2020, p. 765.')
        st.write('Wang, A., R. Tu, Y. Gai, L. G. Pereira, J. Vaughan, I. D. Posen, E. J. Miller, and M. Hatzopoulou. Capturing Uncertainty in Emission Estimates Related to Vehicle Electrification and Implications for Metropolitan Greenhouse Gas Emission Inventories. Applied Energy, Vol. 265, 2020, p. 114798. https://doi.org/10.1016/j.apenergy.2020.114798.')
        st.write('Xu, J., R. Tu, A. Wang, Z. Zhai, and M. Hatzopoulou. Generation of Spikes in Ultrafine Particle Emissions from a Gasoline Direct Injection Vehicle during On-Road Emission Tests. Environmental Pollution, Vol. 267, 2020, p. 115695. https://doi.org/10.1016/j.envpol.2020.115695.')
        st.write('Wang, A., J. Xu, R. Tu, M. Saleh, and M. Hatzopoulou. Potential of Machine Learning for Prediction of Traffic Related Air Pollution. Transportation Research Part D: Transport and Environment, Vol. 88, No. October, 2020, p. 102599. https://doi.org/10.1016/j.trd.2020.102599.')
        st.write('Alfaseeh, L., R. Tu, B. Farooq, and M. Hatzopoulou. Greenhouse Gas Emission Prediction on Road Network Using Deep Sequence Learning. Transportation Research Part D: Transport and Environment, Vol. 88, 2020, p. 102593. https://doi.org/10.1016/j.trd.2020.102593.')
        st.write('Gao, J., H. Chen, Y. Liu, J. Laurikko, Y. Li, T. Li, and R. Tu. Comparison of NOx and PN Emissions between Euro 6 Petrol and Diesel Passenger Cars under Real-World Driving Conditions. Science of the Total Environment, Vol. 801, 2021, p. 149789.')
        st.write('Gao, J., H. Chen, Y. Liu, Y. Li, T. Li, R. Tu, B. Liang, and C. Ma. The Effect of After-Treatment Techniques on the Correlations between Driving Behaviours and NOx Emissions of Passenger Cars. Journal of Cleaner Production, Vol. 288, 2021, p. 125647.')
        st.write('Wang, A., J. Xu, R. Tu, M. Zhang, M. Adams, and M. Hatzopoulou. Near-Road Air Quality Modelling That Incorporates Input Variability and Model Uncertainty. Environmental Pollution, Vol. 284, 2021, p. 117145.')
        st.write('Tu, R., T. Li, C. Meng, J. Chen, Z. Sheng, Y. Xie, F. Xie, F. Yang, H. Chen, Y. Li, J. Gao, and Y. Liu. Real-World Emissions of Construction Mobile Machines and Comparison to a Non-Road Emission Model. Science of the Total Environment, Vol. 771, 2021, p. 145365. https://doi.org/10.1016/j.scitotenv.2021.145365.')
        st.write('Tu, R., J. Xu, A. Wang, Z. Zhai, and M. Hatzopoulou. Effects of Ambient Temperature and Cold Starts on Excess NOx Emissions in a Gasoline Direct Injection Vehicle. Science of the Total Environment, Vol. 760, 2021, p. 143402. https://doi.org/10.1016/j.scitotenv.2020.143402.')
        st.write('Liu, Y., H. Chen, Y. Li, J. Gao, K. Dave, J. Chen, T. Li, and R. Tu. Exhaust and Non-Exhaust Emissions from Conventional and Electric Vehicles: A Comparison of Monetary Impact Values. Journal of Cleaner Production, Vol. 331, 2022, p. 129965.')
        st.write('Nan, S., R. Tu, T. Li, J. Sun, and H. Chen. From Driving Behavior to Energy Consumption: A Novel Method to Predict the Energy Consumption of Electric Bus. Energy, Vol. 261, 2022, p. 125188.')
        st.write('Tu, R., L. Xue, C. Meng, L. Xu, T. Li, and H. Chen. Identifying Specifications of In-Use Vehicles Failing the Inspection/Maintenance Emission Test. Transportation Research Part D: Transport and Environment, Vol. 108, 2022, p. 103327.')
        st.write('Wang, A., R. Tu, J. Xu, Z. Zhai, and M. Hatzopoulou. A Novel Modal Emission Modelling Approach and Its Application with On-Road Emission Measurements. Applied Energy, Vol. 306, 2022, p. 117967.')
        st.write('Yu, Q., L. Lu, T. Li, and R. Tu. Quantifying the Impact of Alternative Bus Stop Platforms on Vehicle Emissions and Individual Pollution Exposure at Bus Stops. International Journal of Environmental Research and Public Health, Vol. 19, No. 11, 2022, p. 6552.')
        st.write('Tu, R., J. Xu, A. Wang, M. Zhang, Z. Zhai, and M. Hatzopoulou. Real-World Emissions and Fuel Consumption of Gasoline and Hybrid Light Duty Vehicles under Local and Regulatory Drive Cycles. Science of The Total Environment, Vol. 805, 2022, p. 150407. https://doi.org/10.1016/J.SCITOTENV.2021.150407.')
        st.write('Liu, Y., H. Chen, S. Wu, J. Gao, Y. Li, Z. An, B. Mao, R. Tu, and T. Li. Impact of Vehicle Type, Tyre Feature and Driving Behaviour on Tyre Wear under Real-World Driving Conditions. Science of the Total Environment, Vol. 842, 2022, p. 156950.')
        st.write('Tu, R., T. Li, C. Meng, J. Chen, Z. Sheng, Y. Xie, F. Xie, F. Yang, H. Chen, Y. Li, and others. 2.23 Emission Estimation and Uncertainty Analysis of Nonroad Construction Machinery. 2022.')
        st.write('Xu, H., R. Tu, T. Li, and H. Chen. Interpretable Bus Energy Consumption Model with Minimal Input Variables Considering Powertrain Types. Transportation Research Part D: Transport and Environment, Vol. 119, 2023, p. 103742.')
        st.write('Nan, S., R. Tu, T. Li, and J. Sun. Identifying Route-Wise Energy-Saving Driving Operations of Electric Buses with Real-Word Measurements. International Journal of Green Energy, Vol. 20, No. 5, 2023, pp. 497–507.')
        st.write('Tu, H., L. Zhao, and R. Tu. Does Early-Stage Automatic Driving Save Energy? Empirical Evidence from Large-Scale Public Road Testing with Varied Road Scenarios and Vehicle Types. 2023.')
        st.write('Zhang, L., J. Wei, and R. Tu. Temporal-Spatial Analysis of Transportation CO2 Emissions in China: Clustering and Policy Recommendations. Heliyon, Vol. 10, No. 2, 2024.')
        st.write('Tu, H., L. Zhao, R. Tu, and H. Li. The Energy-Saving Effect of Early-Stage Autonomous Vehicles: A Case Study and Recommendations in a Metropolitan Area. Energy, Vol. 297, 2024, p. 131274.')
        st.write('Wang, S., T. Qin, R. Tu, T. Li, G. I. Chen, D. C. Green, X. Zhang, J. Feng, H. Liu, M. Hu, and others. Indoor Air Quality in Subway Microenvironments: Pollutant Characteristics, Adverse Health Impacts, and Population Inequity. Environment International, Vol. 190, 2024, p. 108873.')
