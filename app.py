import streamlit as st
import google.generativeai as genai
import json

# --- Gemini Configuration ---
# ඔබ ලබා දුන් අලුත්ම API Key එක මෙහි ඇතුළත් කර ඇත
API_KEY = "AIzaSyA7VCTAzBTMzDAVpUg5spYVm24fWfPLg-Y"

def get_astrology_response(prompt):
    try:
        genai.configure(api_key=API_KEY)
        # 404 Error එක මඟහැරීමට පවතින විවිධ Model Versions පරීක්ෂා කිරීම
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

# --- UI Styling (පින්තූරයට ගැළපෙන CSS) ---
st.set_page_config(page_title="Binary Beatz AI Astro", layout="wide")

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
            try: houses[str(k)] = v
            except: pass
    
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

if submit:
    if name and pob:
        # Gemini හට JSON එකක් පමණක් ලබා දෙන ලෙස උපදෙස් දීම
        prompt = f"නම: {name}, {dob} {tob} ට {pob} දී උපත. වෛදික ජ්‍යොතිෂයට අනුව 'rashi' සහ 'navamsa' ග්‍රහයන් json එකක් ලෙස සිංහලෙන් ලබා දෙන්න. json එක හැර වෙනත් කිසිවක් එපා."
        
        with st.spinner("AI මගින් දත්ත විශ්ලේෂණය කරමින් පවතී..."):
            response = get_astrology_response(prompt)
            if response:
                try:
                    res_text = response.text.strip().replace('```json', '').replace('```', '')
                    data = json.loads(res_text)
                    
                    col1, col2 = st.columns([1, 1.5])
                    with col1:
                        st.markdown(create_chart_html("රාශි සටහන", data.get('rashi'), "රාශි"), unsafe_allow_html=True)
                        st.markdown(create_chart_html("නවාංශක සටහන", data.get('navamsa'), "නවාංශක"), unsafe_allow_html=True)
                    with col2:
                        st.markdown(f'<div class="report-card"><h3>ජ්‍යොතිෂ වාර්තාව</h3><hr>{data.get("details", response.text)}</div>', unsafe_allow_html=True)
                except Exception:
                    st.error("දත්ත ලබා ගැනීමේදී ගැටලුවක් පවතී. කරුණාකර නැවත උත්සාහ කරන්න.")
            else:
                st.error("API සේවාව සමඟ සම්බන්ධ වීමට නොහැකි විය. කරුණාකර ඔබගේ API Key එක පරීක්ෂා කර ඇප් එක Reboot කරන්න.")
    else:
        st.warning("කරුණාකර සියලු විස්තර ඇතුළත් කරන්න.")
