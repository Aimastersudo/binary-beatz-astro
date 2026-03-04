import streamlit as st
import google.generativeai as genai
import json
import time

# --- Gemini AI Configuration ---
# ඔයාගේ API Key එක මෙතැනට දාන්න
API_KEY = "AIzaSyDPW_CL3i0GZNHwwAxEedkVtXyaDZicsTE"

def get_model():
    """Model එක නිවැරදිව Load කරගැනීමේ ශ්‍රිතය"""
    genai.configure(api_key=API_KEY)
    # පවතින අලුත්ම සහ ස්ථාවර Model එක තෝරා ගැනීම
    return genai.GenerativeModel('gemini-1.5-flash')

# --- UI Styling (පින්තූරයට අනුව සැකසූ CSS) ---
st.set_page_config(page_title="Binary Beatz AI Astro", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .report-card { 
        background-color: white; padding: 15px; border-radius: 10px; 
        box-shadow: 0 2px 10px rgba(0,0,0,0.1); border: 1px solid #ddd;
        margin-bottom: 20px;
    }
    .horo-chart { 
        display: grid; grid-template-columns: repeat(4, 1fr); 
        gap: 2px; background-color: #334155; border: 2px solid #334155;
        width: 300px; margin: auto;
    }
    .house { 
        background-color: white; color: black; height: 75px; 
        display: flex; flex-direction: column; align-items: center; 
        justify-content: center; font-size: 11px; text-align: center; font-weight: bold;
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
        houses.update(planets_data)
    
    html = f"""
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
    return html

st.title("🔮 Binary Beatz AI Astrology Center")

with st.sidebar:
    st.header("උපන් විස්තර")
    name = st.text_input("නම")
    dob = st.date_input("උපන් දිනය")
    tob = st.time_input("උපන් වේලාව")
    pob = st.text_input("උපන් ස්ථානය")
    submit = st.button("කේන්දරය සාදන්න")

if submit:
    if not name or not pob:
        st.error("කරුණාකර සියලු විස්තර ඇතුළත් කරන්න.")
    else:
        try:
            model = get_model()
            prompt = f"""
            නම: {name}, උපන් දිනය: {dob}, වේලාව: {tob}, ස්ථානය: {pob}.
            මෙම විස්තර අනුව 'රාශි' සහ 'නවාංශක' සටහන් වල ග්‍රහ පිහිටීම් පහත JSON ආකෘතියට පමණක් සිංහලෙන් ලබා දෙන්න:
            {{
                "rashi": {{"1": "රවි", "5": "සඳු"}},
                "navamsa": {{"2": "කුජ", "10": "ගුරු"}},
                "details": "කරුණාකර මෙහි පින්තූරයේ ඇති ආකාරයට ලග්නය, නැකත සහ අනෙකුත් විස්තර සිංහලෙන් ලියන්න."
            }}
            """
            
            with st.spinner("AI මගින් දත්ත විශ්ලේෂණය කරමින් පවතී..."):
                response = model.generate_content(prompt)
                
                # JSON එක පිරිසිදු කර ගැනීම
                clean_content = response.text.replace('```json', '').replace('```', '').strip()
                data = json.loads(clean_content)
                
                col1, col2 = st.columns([1, 1.5])
                
                with col1:
                    st.markdown(create_chart_html("රාශි සටහන", data.get('rashi'), "රාශි"), unsafe_allow_html=True)
                    st.markdown(create_chart_html("නවාංශක සටහන", data.get('navamsa'), "නවාංශක"), unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f'<div class="report-card"><h3>ජ්‍යොතිෂ වාර්තාව</h3><hr>{data.get("details")}</div>', unsafe_allow_html=True)
                    
        except Exception as e:
            st.error("API සේවාව සමඟ සම්බන්ධ වීමේදී ගැටලුවක් ඇති විය. කරුණාකර තව සුළු මොහොතකින් උත්සාහ කරන්න.")
            st.info("විස්තර: " + str(e))
