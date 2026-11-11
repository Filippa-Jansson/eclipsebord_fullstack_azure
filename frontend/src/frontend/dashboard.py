import streamlit as st
import httpx
import pandas as pd
import os

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

def main():
    st.markdown("# eClipseBoard dashboard")
    st.markdown("Welcome to the eClipseBoard dashboard! Here you can explore data on lunar and solar eclipses🌑🌒🌕")
    st.caption("Showing the first 10 eclipses from each dataset.")

    lunar_response = httpx.get(f"{BASE_URL}/lunar/data")
    solar_response = httpx.get(f"{BASE_URL}/solar/data")

    lunar_df = pd.DataFrame(lunar_response.json())
    solar_df = pd.DataFrame(solar_response.json())

    #Tabs for lunar and solar data
    lunar_tab, solar_tab = st.tabs(["🌙 Lunar", "☀️ Solar"])

    #Lunar tab
    with lunar_tab:
        st.markdown("## Lunar Eclipses")

        eclipse_types = ["All"] + sorted(
            lunar_df["Eclipse Type"].dropna().unique().tolist()
        )

        selected_type = st.selectbox(
            "Eclipse Type",
            eclipse_types,
            key="lunar_type"
        )

        if selected_type == "All":
            filtered_lunar = lunar_df
        else:
            filtered_lunar = lunar_df[
                lunar_df["Eclipse Type"] == selected_type
            ]

        st.metric(
            "Lunar eclipses shown",
            len(filtered_lunar)
        )

        st.markdown("### Eclipse Data")
        st.dataframe(filtered_lunar)

    #Solar tab
    with solar_tab:
        st.markdown("## Solar Eclipses")

        eclipse_types = ["All"] + sorted(
            solar_df["Eclipse Type"].dropna().unique().tolist()
        )

        selected_type = st.selectbox(
            "Eclipse Type",
            eclipse_types,
            key="solar_type"
        )

        if selected_type == "All":
            filtered_solar = solar_df
        else:
            filtered_solar = solar_df[
                solar_df["Eclipse Type"] == selected_type
            ]

        st.metric(
            "Solar eclipses shown",
            len(filtered_solar)
        )

        st.markdown("### Eclipse Data")
        st.dataframe(filtered_solar)

if __name__ == "__main__":
    main()