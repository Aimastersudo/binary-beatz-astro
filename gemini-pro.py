import streamlit as st
import google.generativeai as genai
import json

# --- Gemini AI Configuration ---
API_KEY = "AIzaSyDPW_CL3i0GZNHwwAxEedkVtXyaDZicsTE"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Binary Beatz AI Astro", layout="wide")

# --- UI Styling (පින්තූරයට ගැළපෙන සේ සැකසූ CSS) ---
st.markdown("""
<style>
    .report-card { 
        background-color: white; padding: 15px; border-radius: 10px; 
        box-shadow: 0 2px 10px rgba(0,0,0,0.1); border: 1px solid #ddd;
    }
    .horo-chart { 
        display: grid; grid-template-columns: repeat(4, 1fr); 
        gap: 2px; background-color: #334155; border: 2px solid #334155;
        width: 300px; margin: auto;
    }
    .house { 
        background-color: white; color: black; height: 75px; 
        display: flex; flex-direction: column; align-items: center; 
        justify-content: center; font-size: 10px; text-align: center;
    }
    .house-num { font-size: 8px; color: #999; margin-bottom: 2px; }
    .center-box {
        grid-column: span 2; grid-row: span 2; 
        background-color: #f8fafc; display: flex;
        align-items: center; justify-content: center;
        font-weight: bold; color: #ef4444; border: 1px solid #cbd5e1;
    }
</style>
""", unsafe_allow_html=True)

def create_chart_html(title, planets_data, center_text):
    # කොටු 12 සඳහා දත්ත සැකසීම
    houses = {i: "" for i in range(1, 13)}
    houses.update(planets_data)
    
    html = f"""
    <div class="report-card">
        <p style="text-align:center; font-weight:bold; margin-bottom:5px;">{title}</p>
        <div class="horo-chart">
            <div class="house"><span class="house-num">12</span>{houses[12]}</div>
            <div class="house"><span class="house-num">1</span>{houses[1]}</div>
            <div class="house"><span class="house-num">2</span>{houses[2]}</div>
            <div class="house"><span class="house-num">3</span>{houses[3]}</div>
            <div class="house"><span class="house-num">11</span>{houses[11]}</div>
            <div class="center-box">{center_text}</div>
            <div class="house"><span class="house-num">4</span>{houses[4]}</div>
            <div class="house"><span class="house-num">10</span>{houses[10]}</div>
            <div class="house"><span class="house-num">5</span>{houses[5]}</div>
            <div class="house"><span class="house-num">9</span>{houses[9]}</div>
            <div class="house"><span class="house-num">8</span>{houses[8]}</div>
            <div class="house"><span class="house-num">7</span>{houses[7]}</div>
            <div class="house"><span class="house-num">6</span>{houses[6]}</div>
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
    # Gemini AI එකට දත්ත යවා Chart එකට අවශ්‍ය ග්‍රහ පිහිටීම් ලබා ගැනීම
    prompt = f"""
    මම {name}. {dob} දින {tob} ට {pob} හි උපන්නෙමි. 
    මෙම උපන් වේලාවට අදාළ 'රාශි' සහ 'නවාංශක' සටහන් වල ග්‍රහ පිහිටීම් පහත JSON Format එකට සිංහලෙන් ලබා දෙන්න:
    {{
        "rashi": {{"1": "රවි", "5": "සිකුරු"}},
        "navamsa": {{"2": "ගුරු", "10": "සඳු"}},
        "details": "නැකත, ලග්නය සහ අනෙකුත් විස්තර මෙහි ලියන්න"
    }}
    (කරුණාකර JSON එක පමණක් ලබා දෙන්න)
    """
    
    with st.spinner("දත්ත ගණනය කරමින් පවතී..."):
        response = model.generate_content(prompt)
        # JSON කොටස පමණක් වෙන් කර ගැනීම
        try:
            raw_data = response.text.strip().replace('```json', '').replace('```', '')
            data = json.loads(raw_data)
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown(create_chart_html("රාශි සටහන", data['rashi'], "රාශි"), unsafe_allow_html=True)
                st.write("")
                st.markdown(create_chart_html("නවාංශක සටහන", data['navamsa'], "නවාංශක"), unsafe_allow_html=True)
                
            with col2:
                st.subheader("පරිපූර්ණ පලාඵල වාර්තාව")
                st.info(f"නම: {name} | උපන් දිනය: {dob}")
                st.write(data['details'])
                
        except:
            st.error("දත්ත සැකසීමේදී දෝෂයක් ඇති විය. කරුණාකර නැවත උත්සාහ කරන්න.")
