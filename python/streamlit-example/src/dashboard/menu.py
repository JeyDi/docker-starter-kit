
import logging
import streamlit as st
# from src.dashboard.menus.components import (
#     menu_scraper,
# )


def side_menu():
    """
    Streamlit side config menu
    """
    logging.debug("Launching side menù function")
    
    st.sidebar.markdown("**Configuration Panel**")

    #### PROJECT CONFIGURATION ####

    # menu_scraper()
    
    #### FILTER DATA ####
    
    
    #### VISUALIZATION ####
    
    
def main_menu():
    
    logging.debug("Launching main menu")
    
    #create the dashboard heading
    st.title('Python Biella Group')
    st.markdown('## Streamlit project example')
    st.markdown('How to use streamlit for your Data Project')
    st.markdown('<-- Open side menu to run functionalities')
    
    return True
    
    
def launch():
    """Main function to launch all the streamlit functionalities

    Returns:
        bool: True if the process is ok, False if there are some errors
    """
    
    logging.info("Starting streamlit program")
    
    #streamlit page settings
    st.set_page_config(
        layout="wide",
    )
    try:
        # Launch the side menu for all the configurations
        
        main_menu()
        side_menu()
        
        return True
    
    except Exception as message:
        logging.error(f"Impossible to launch the streamlit functionalities: {message}")
        return False
