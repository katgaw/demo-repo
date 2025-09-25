import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(
    page_title="Central European History Explorer",
    page_icon="🇨🇿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2c5aa0;
        font-size: 2.5rem;
        margin-bottom: 2rem;
        border-bottom: 3px solid #2c5aa0;
        padding-bottom: 1rem;
    }
    .country-button {
        background-color: #2c5aa0;
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 10px;
        font-size: 1.2rem;
        cursor: pointer;
        margin: 1rem;
        transition: background-color 0.3s;
    }
    .country-button:hover {
        background-color: #1e3d6f;
    }
    .history-container {
        background-color: #f9f9f9;
        padding: 2rem;
        border-radius: 10px;
        border-left: 4px solid #2c5aa0;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">Central European History Explorer</h1>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("Select a country to explore its rich history!")

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Choose a Country")
    st.markdown("Click on one of the buttons below to learn about the history of these Central European nations:")
    
    # Create two columns for the buttons
    btn_col1, btn_col2 = st.columns(2)
    
    with btn_col1:
        # Button for Czech Republic
        if st.button("🇨🇿 Czech Republic", key="czech_btn", help="Learn about Czech Republic history"):
            st.session_state.selected_country = "czech"
            st.session_state.show_history = True
    
    with btn_col2:
        # Button for Slovakia
        if st.button("🇸🇰 Slovakia", key="slovakia_btn", help="Learn about Slovakia history"):
            st.session_state.selected_country = "slovakia"
            st.session_state.show_history = True

with col2:
    st.markdown("### History Display")
    
    # Czech Republic History
    if hasattr(st.session_state, 'selected_country') and st.session_state.selected_country == "czech":
        st.markdown('<div class="history-container">', unsafe_allow_html=True)
        st.markdown("**🇨🇿 Czech Republic History**")
        st.markdown("""
        The Czech Republic, located in Central Europe, has a rich and complex history that spans over a millennium. 
        The region was first settled by Celtic tribes before becoming part of the Great Moravian Empire in the 9th century. 
        The Kingdom of Bohemia emerged in the 10th century under the Přemyslid dynasty and became one of the most powerful 
        states in Central Europe, particularly during the reign of Charles IV (1346-1378), who made Prague the capital of 
        the Holy Roman Empire. The Hussite Wars in the 15th century marked a period of religious reform and national identity 
        formation, while the 17th century brought the Thirty Years' War and Habsburg domination. The 19th century saw the 
        Czech National Revival, leading to the creation of Czechoslovakia in 1918 following World War I. After Nazi occupation 
        during World War II and communist rule from 1948-1989, the peaceful Velvet Revolution brought democracy, and in 1993, 
        the Czech Republic peacefully separated from Slovakia, becoming an independent nation that joined the European Union in 2004.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Slovakia History
    elif hasattr(st.session_state, 'selected_country') and st.session_state.selected_country == "slovakia":
        st.markdown('<div class="history-container">', unsafe_allow_html=True)
        st.markdown("**🇸🇰 Slovakia History**")
        st.markdown("""
        Slovakia, a landlocked country in Central Europe, has a fascinating history that reflects its strategic position 
        between East and West. The territory was first inhabited by Celtic tribes, followed by Germanic tribes and later 
        Slavic settlers in the 5th-6th centuries. The Great Moravian Empire (9th century) was the first major Slavic state 
        in the region, with its center in present-day Slovakia. After the empire's fall, the territory came under Hungarian 
        rule for nearly 1000 years, becoming part of the Kingdom of Hungary and later the Austro-Hungarian Empire. 
        The Slovak National Revival in the 19th century fostered national consciousness and cultural identity. Following 
        World War I, Slovakia became part of Czechoslovakia in 1918. During World War II, Slovakia briefly existed as an 
        independent state under Nazi influence (1939-1945). After the war, it rejoined Czechoslovakia, which fell under 
        communist rule from 1948-1989. The Velvet Revolution brought democracy, and in 1993, Slovakia peacefully separated 
        from the Czech Republic, becoming an independent nation. Slovakia joined the European Union in 2004 and adopted 
        the Euro in 2009.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Default message when no country is selected
    else:
        st.info("👆 Please select a country above to view its history!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
