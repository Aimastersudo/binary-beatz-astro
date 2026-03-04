import streamlit as st
import google.generativeai as genai
import json

# --- Gemini Configuration ---
# ඔයා ලබා දුන් API Key එක මෙහි ඇත
API_KEY = "AIzaSyA7VCTAzBTMzDAVpUg5spYVm24fWfPLg-Y"

def get_astrology_response(prompt):
    try:
        genai.configure(api_key=API_KEY)
        # පවතින සියලුම Model ID පරීක්ෂා කිරීම (404 Error එක මඟහැරීමට)
        for model_id in ['gemini-1.5-flash', 'models/gemini-1.5-flash', 'gemini-pro', 'models/gemini-pro']:
            try:
                model = genai.GenerativeModel(model_id)
                response = model.generate_content(prompt)
                if response and response.text:
                    return response
            except Exception:
                continue
        return None
    except Exception:
        return None

# --- UI Styling (පින්තූරයට අනුව සැකසූ CSS) ---
st.set_page_config(page_title="Binary Beatz AI Astro", layout="wide")

st.markdown("""
<style>
    .report-card { background: white; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px; color: black; }
    .horo-chart { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2px; background: #334155; border: 2px solid #334155; width: 280px; margin: auto; }
    .house { background: white; height: 70px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; }
    .center-box { grid-column: span 2; grid-row: span 2; background: #f1f5f9; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #ef4444; }
</style>
""", unsafe_allow_html=True)

def draw_chart(title, planets, center):
    h = {str(i): "" for i in range(1, 13)}
    if planets: h.update({str(k): v for k, v in planets.items()})
    return f"""
    <div class="report-card">
        <p style="text-align:center; font-weight:bold;">{title}</p>
        <div class="horo-chart">
            <div class="house">{h['12']}</div><div class="house">{h['1']}</div><div class="house">{h['2']}</div><div class="house">{h['3']}</div>
            <div class="house">{h['11']}</div><div class="center-box">{center}</div><div class="house">{h['4']}</div>
            <div class="house">{h['10']}</div><div class="house">{h['5']}</div>
            <div class="house">{h['9']}</div><div class="house">{h['8']}</div><div class="house">{h['7']}</div><div class="house">{h['6']}</div>
        </div>
    </div> """

st.title("🔮 Binary Beatz AI Astrology Center")
with st.sidebar:
    st.header("ඔබේ විස්තර")
    name = st.text_input("නම")
    dob = st.date_input("උපන් දිනය")
    tob = st.time_input("උපන් වේලාව")
    pob = st.text_input("උපන් ස්ථානය (නගරය)")
    submit = st.button("කේන්දරය බලන්න")

if submit:
    if name and pob:
        with st.spinner("AI දත්ත විශ්ලේෂණය කරමින් පවතී..."):
            prompt = f"නම: {name}, {dob} {tob} ට {pob} දී උපත. වෛදික ජ්‍යොතිෂයට අනුව 'rashi' සහ 'navamsa' ග්‍රහ පිහිටීම් json එකක් ලෙස සිංහලෙන් ලබා දෙන්න."
            response = get_astrology_response(prompt)
            if response:
                try:
                    res_txt = response.text.strip().replace('```json', '').replace('```', '')
                    data = json.loads(res_txt)
                    col1, col2 = st.columns([1, 1.5])
                    with col1:
                        st.markdown(draw_chart("රාශි සටහන", data.get('rashi'), "රාශි"), unsafe_allow_html=True)
                        st.markdown(draw_chart("නවාංශක සටහන", data.get('navamsa'), "නවාංශක"), unsafe_allow_html=True)
                    with col2:
                        st.markdown(f'<div class="report-card"><h3>ජ්‍යොතිෂ වාර්තාව</h3><hr>{data.get("details", response.text)}</div>', unsafe_allow_html=True)
                except Exception: st.error("දත්ත සැකසීමේ දෝෂයකි. නැවත උත්සාහ කරන්න.")
            else: st.error("API සම්බන්ධතාවය අසාර්ථකයි. කරුණාකර ඔබගේ API Key එක පරීක්ෂා කරන්න.")
