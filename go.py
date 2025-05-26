import streamlit as st
from datetime import datetime
import pytz
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# Set timezone WIB
wib = pytz.timezone('Asia/Jakarta')

st.title("Perjalanan Memanjangkan Rambut Redo")

# Auto refresh tiap 1 detik
st_autorefresh(interval=1000, limit=None, key="refresh_clock")

# Inisialisasi dataframe dan last_saved_day di session state
if "data_harian" not in st.session_state:
    st.session_state.data_harian = pd.DataFrame(columns=["Day", "Date", "Time"])
if "last_saved_day" not in st.session_state:
    st.session_state.last_saved_day = None

now = datetime.now(wib)
day_name = now.strftime('%A')
date_str_display = now.strftime('%d %B %Y')
time_str = now.strftime('%H:%M:%S')
current_day = now.strftime('%Y-%m-%d')  # format tanggal unik

st.markdown(
    f"<h1 style='font-size:100px; font-weight:bold;'>{date_str_display}</h1>"
    f"<h2 style='font-size:50px; font-weight:bold;'>{time_str}</h2>",
    unsafe_allow_html=True
)

# Simpan data hanya sekali per hari
if st.session_state.last_saved_day != current_day:
    new_row = {"Day": day_name, "Date": date_str_display, "Time": time_str}
    st.session_state.data_harian = pd.concat(
        [st.session_state.data_harian, pd.DataFrame([new_row])],
        ignore_index=True
    )
    st.session_state.last_saved_day = current_day

st.dataframe(st.session_state.data_harian)

# Simpan data ke CSV
st.download_button(
    label="Download CSV",
    data=st.session_state.data_harian.to_csv(index=False),
    file_name="data_harian.csv",
    mime="text/csv"
)