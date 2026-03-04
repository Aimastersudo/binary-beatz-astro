import streamlit as st
import json

# --- UI Styling (පින්තූරයට ගැළපෙන CSS) ---
st.set_page_config(page_title="Binary Beatz Astro - No API", layout="wide")

st.markdown("""
<style>
    .report-card { 
        background-color: white; padding: 15px; border-radius: 10px; 
        box-shadow: 0 2px 10px rgba(0,0,0,0.1); border: 1px solid #ddd;
        margin-bottom: 20px; color: black;
    }
    .horo-chart { 
        display: grid; grid-template-columns: repeat(4, 1fr); 
        gap: 2px; background-color: #334155; border: 2px solid #334155;
        width: 280px; margin: auto;
    }
    .house { 
        background-color: white; height: 75px; 
        display: flex; flex-direction: column; align-items: center; 
        justify-content: center; font-size: 11px; font-weight: bold;
    }
    .center-box {
        grid-column: span 2; grid-row: span 2; 
        background-color: #f1f5f9; display: flex;
        align-items: center; justify-content: center;
        font-weight: bold; color: #ef4444; border: 1px solid #cbd5e1;
    }
</style>
""", unsafe_allow_html=True)

def create_chart_html(title, planets_data, center_text):
    houses = {str(i): "" for i in range(1, 13)}
    if planets_data:
        for k, v in planets_data.items():
            houses[str(k)] = v
    
    return f"""
    <div class="report-card">
        <p style="text-align:center; font-weight:bold; margin-bottom:5px;">{title}</p>
        <div class="horo-chart">
            <div class="house">{houses['12']}</div><div class="house">{houses['1']}</div><div class="house">{houses['2']}</div><div class="house">{houses['3']}</div>
            <div class="house">{houses['11']}</div><div class="center-box">{center_text}</div><div class="house">{houses['4']}</div>
            <div class="house">{houses['10']}</div><div class="house">{houses['5']}</div>
            <div class="house">{houses['9']}</div><div class="house">{houses['8']}</div><div class="house">{houses['7']}</div><div class="house">{houses['6']}</div>
        </div>
    </div>
    """

st.title("🔮 Binary Beatz AI Astrology Center")

with st.sidebar:
    st.header("ඔබේ විස්තර")
    name = st.text_input("නම")
    dob = st.date_input("උපන් දිනය")
    tob = st.time_input("උපන් වේලාව")
    pob = st.text_input("උපන් ස්ථානය (නගරය)")
    submit = st.button("කේන්දරය බලන්න")

# API එකක් නැති නිසා පෙන්වීම සඳහා සාදාගත් දත්ත (Sample Data)
sample_data = {
    "rashi": {"1": "රවි, බුධ", "5": "සිකුරු", "9": "ගුරු", "12": "සඳු"},
    "navamsa": {"2": "කුජ", "7": "රාහු", "10": "ශනි"},
    "details": "මෙම කේන්දර සටහන Sample දත්ත පදනම් කරගෙන සාදන ලද්දකි. API එකක් නොමැති බැවින් ඇත්තම පලාඵල පෙන්වීමට නොහැක. පෙනුම සඳහා පමණක් මෙය භාවිතා කරන්න."
}

if submit:
    if name and pob:
        with st.spinner("දත්ත සකසමින් පවතී..."):
            col1, col2 = st.columns([1, 1.5])
            with col1:
                # මෙහිදී sample_data පාවිච්චි කරයි
                st.markdown(create_chart_html("රාශි සටහන", sample_data['rashi'], "රාශි"), unsafe_allow_html=True)
                st.markdown(create_chart_html("නවාංශක සටහන", sample_data['navamsa'], "නවාංශක"), unsafe_allow_html=True)
            with col2:
                st.markdown(f'''
                <div class="report-card">
                    <h3>ජ්‍යොතිෂ වාර්තාව - {name}</h3>
                    <hr>
                    <p><b>උපන් දිනය:</b> {dob} | <b>වේලාව:</b> {tob}</p>
                    <p>{sample_data['details']}</p>
                </div>
                ''', unsafe_allow_html=True)
    else:
        st.warning("කරුණාකර සියලු විස්තර ඇතුළත් කරන්න.")
