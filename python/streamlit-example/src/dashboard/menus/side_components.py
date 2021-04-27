import streamlit as st
import pandas as pd


from src.dashboard.menus.main_components import main_room_type
from src.common.dashboard import get_table_download_link


def visualize_dataset(dataframe: pd.DataFrame) -> bool:

    button = st.sidebar.button(
        "Visualize dataframe without filters", key="bvisualize"
    )

    if button:
        main_room_type(dataframe)
        return True

    return False


def search_room(dataframe: pd.DataFrame) -> bool:

    # Search top 100
    top100 = st.sidebar.checkbox(
        "Filter top 100 apartments",
        help="filter only the top 100 apartments by price",
    )

    # Search by price
    min_price, max_price = st.sidebar.slider(
        "Search apartments by price",
        min(dataframe.price),
        max(dataframe.price),
        (min(dataframe.price), max(dataframe.price)),
        help="Insert the min and max price",
    )

    # Search by review_scores_rating

    # Search by room type

    # Search by Beds

    # Search by Beds

    # Search by Bathrooms

    # Search by Accomodates

    # Launch the search
    button = st.sidebar.button("Apply filters", key="bprice")

    if button:
        if top100:
            dataframe = dataframe.groupby("price").head(100)

        dataframe_filtered = dataframe.loc[
            dataframe.price.between(min_price, max_price)
        ]
        # Launch the data visualization
        main_room_type(dataframe_filtered)

        return True

    return False


def download_data(dataframe):
    button = st.sidebar.button("Download data", key="bdownload")
    excel_check = st.sidebar.checkbox(
        "Do you want to download an excel?",
        False,
        help="Press this checkbox if you want to download an excel",
    )
    if button:
        with st.beta_expander("Download data", expanded=True):
            st.markdown(
                get_table_download_link(dataframe, excel_check),
                unsafe_allow_html=True,
            )
        return True
    
    return False