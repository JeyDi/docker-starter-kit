import logging

import src.dashboard.menu as main_menu


if __name__ == "__main__":
    # create the dashboard heading
    logging.info("Launching Python Biella Group Streamlit Dashboard")
    main_menu.launch()