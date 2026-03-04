import streamlit as st
import google.generativeai as genai
import json

# --- Gemini AI Configuration ---
# ඔයා ලබාගත් API Key එක මෙතැනට ඇතුළත් කරන්න
API_KEY = "ඔAIzaSyBG50Auv1WY8-OmhKN8R7JN-4ynlSTpjdk"

def get_stable_model():
    genai.configure(api_key=API_KEY)
    # 404 Error එක මඟහැරීමට වඩාත් ස්ථාවර 'gemini-pro' පාවිච්චි කිරීම
    try:
        return genai.GenerativeModel('gemini-pro')
    except:
        return genai.GenerativeModel('models/gemini-pro')

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
        background-color: white; height: 70px; 
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
    houses = {i: "" for i in range(1, 13)}
    if planets_data:
        for k, v in planets_data.items():
            try: houses[int(k)] = v
            except: pass
    
    return f"""
    <div class="report-card">
        <p style="text-align:center; font-weight:bold; margin-bottom:5px;">{title}</p>
        <div class="horo-chart">
            <div class="house">{houses[12]}</div><div class="house">{houses[1]}</div><div class="house">{houses[2]}</div><div class="house">{houses[3]}</div>
            <div class="house">{houses[11]}</div><div class="center-box">{center_text}</div><div class="house">{houses[4]}</div>
            <div class="house">{houses[10]}</div><div class="house">{houses[5]}</div>
            <div class="house">{houses[9]}</div><div class="house">{houses[8]}</div><div class="house">{houses[7]}</div><div class="house">{houses[6]}</div>
        </div>
    </div>
    """

st.title("🔮 Binary Beatz AI Astrology Center")

with st.sidebar:
    st.header("උපන් විස්තර")
    name = st.text_input("නම")
    dob = st.date_input("උපන් දිනය")
    tob = st.time_input("උපන් වේලාව")
    pob = st.text_input("උපන් ස්ථානය (නගරය)")
    submit = st.button("කේන්දරය සාදන්න")

if submit:
    if name and pob:
        model = get_stable_model()
        prompt = f"""
        නම: {name}, උපන් දිනය: {dob}, වේලාව: {tob}, ස්ථානය: {pob}.
        වෛදික ජ්‍යොතිෂයට අනුව 'rashi' සහ 'navamsa' සටහන් වල ග්‍රහ පිහිටීම් json එකක් ලෙස සිංහලෙන් ලබා දෙන්න:
        {{
            "rashi": {{"1": "රවි", "5": "සිකුරු"}},
            "navamsa": {{"2": "ගුරු", "10": "සඳු"}},
            "details": "කරුණාකර මෙහි ලග්නය, නැකත සහ පලාඵල විස්තරය ලියන්න."
        }}
        කරුණාකර json පමණක් ලබා දෙන්න.
        """
        
        with st.spinner("AI මගින් දත්ත විශ්ලේෂණය කරමින් පවතී..."):
            try:
                response = model.generate_content(prompt)
                res_text = response.text.strip().replace('```json', '').replace('```', '')
                data = json.loads(res_text)
                
                col1, col2 = st.columns([1, 1.5])
                with col1:
                    st.markdown(create_chart_html("රාශි සටහන", data.get('rashi'), "රාශි"), unsafe_allow_html=True)
                    st.markdown(create_chart_html("නවාංශක සටහන", data.get('navamsa'), "නවාංශක"), unsafe_allow_html=True)
                with col2:
                    st.markdown(f'<div class="report-card"><h3>ජ්‍යොතිෂ වාර්තාව</h3><hr>{data.get("details")}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error("API Error: Model එක සමඟ සම්බන්ධ වීමට නොහැකි විය.")
    else:
        st.warning("කරුණාකර සියලු විස්තර ඇතුළත් කරන්න.")
