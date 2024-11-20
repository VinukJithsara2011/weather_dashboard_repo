import streamlit as st  # type: ignore
import pandas as pdI # type: ignore
import requests
from PIL import Image # type: ignore
import json
import pandas as pd


st.title("Daily Weather Report")



img = Image.open ("weather report.png")
st.image(
    img ,
    width=400,
    channels = "RGB"
    )

st.header("Today Weather Report")
resp = requests.get("https://api.open-meteo.com/v1/forecast?latitude=6.883&longitude=79.9071&current=temperature_2m,is_day,rain,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,rain_sum")
value = json.loads(resp.text)
st.sidebar.write("Latitude ",value["latitude"])
st.sidebar.write("Longitude",value["longitude"])


collom1, collom2, collom3 = st.columns(3)
collom1.metric("Temperature", value["current"]["temperature_2m"], "1.2 °F")
collom2.metric("Wind", value["current"]["wind_speed_10m"], "-8%")
collom3.metric("Rainfall", value["current"]["rain"], "2%")

st.subheader("Do You Want Yesterday Weather Report?") 

st.button("Click Here")


st.video("https://www.youtube.com/watch?v=OK6S7XTpCF8")

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

option=st.sidebar.selectbox("You can select here ⤵️",
    ("temperature max", "temperature min", "sunset"),
)


daily_max_temp_df = pd.DataFrame(value["daily"]["temperature_2m_max"],value["daily"]["time"])
daily_min_temp_df = pd.DataFrame(value["daily"]["temperature_2m_min"], value["daily"]["time"])
daily_sunset_df = pd.DataFrame(value["daily"]["sunset"],value["daily"]["time"])

if option == "temperature max":
    st.line_chart(daily_max_temp_df)
if option == "temperature min":
    st.line_chart(daily_min_temp_df)
if option == "sunset":
    st.line_chart(daily_sunset_df)
# def new_func():c
#     st.markdown("# Dashboard")
#     st.sidebar.markdown("# Dashboard")

#     st.markdown("# All Reports ")
#     st.sidebar.markdown("# All Reports")

#     st.markdown("# About")
#     st.sidebar.markdown("# About")

# new_func()
