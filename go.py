import streamlit as st
import time
from datetime import datetime


# Title
st.title("Perjalanan Memanjangkan Rambut Redo")

# Real-time clock
while True:
    now = datetime.now()
    day_name = now.strftime('%A')
    date_str = now.strftime('%d %B %Y')
    time_str = now.strftime('%H:%M:%S')

    st.markdown(f"### Hari: {day_name}")
    st.markdown(f"### Tanggal: {date_str}")
    st.markdown(f"### Waktu: {time_str}")

    time.sleep(1)
    st.rerun()
