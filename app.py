%%writefile app.py
import streamlit as st
import google.generativeai as genai

# Gemini Setup
genai.configure(api_key="ඔයාගේ_KEY_එක_මෙතැනට")
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Binary Beatz AI Astro", layout="wide")

# UI එක ලස්සන කරන CSS
st.markdown("""
<style>
    .main { background-color: #0f172a; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #1e293b; border-radius: 10px; color: white; padding: 10px 20px; }
    .stTabs [aria-selected="true"] { background-color: #f39c12; color: black; font-weight: bold; }
    .horo-chart { 
        display: grid; grid-template-columns: repeat(4, 1fr); 
        gap: 5px; background-color: #f39c12; border: 3px solid #f39c12;
        max-width: 400px; margin: auto; padding: 5px; border-radius: 5px;
    }
    .house { 
        background-color: white; color: black; height: 90px; 
        display: flex; flex-direction: column; align-items: center; 
        justify-content: center; font-size: 13px; font-weight: bold; border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔮 Binary Beatz AI Astrology Center")
tab1, tab2 = st.tabs(["කේන්දර පරීක්ෂාව (Horoscope)", "පෝරොන්දම් සැසඳීම (Matching)"])

# --- TAB 1: HOROSCOPE ---
with tab1:
    col_a, col_b = st.columns([1, 1.5])
    with col_a:
        st.subheader("ඔබේ විස්තර")
        name = st.text_input("නම")
        dob = st.date_input("උපන් දිනය", key="dob1")
        tob = st.time_input("උපන් වේලාව", key="tob1")
        pob = st.text_input("උපන් ස්ථානය", key="pob1")
        btn1 = st.button("කේන්දරය බලන්න")

    if btn1:
        with col_b:
            st.markdown(f'<div class="horo-chart">'
                        '<div class="house">12<br>මීන</div><div class="house">1<br>මේෂ</div><div class="house">2<br>වෘෂභ</div><div class="house">3<br>මිථුන</div>'
                        '<div class="house">11<br>කුම්භ</div><div class="house" style="grid-column: span 2; grid-row: span 2; background-color:#ffd54f;">' + name + '</div><div class="house">4<br>කටක</div>'
                        '<div class="house">10<br>මකර</div><div class="house">5<br>සිංහ</div>'
                        '<div class="house">9<br>ධනු</div><div class="house">8<br>වෘශ්චික</div><div class="house">7<br>තුලා</div><div class="house">6<br>කන්‍යා</div>'
                        '</div>', unsafe_allow_html=True)
            with st.spinner("AI පලාඵල ලියමින් පවතී..."):
                prompt = f"මම {name}. {dob} {tob} ට {pob} දී උපන්නෙමි. වෛදික ජ්‍යොතිෂයට අනුව පලාඵල විස්තරයක් සිංහලෙන් ලබා දෙන්න."
                res = model.generate_content(prompt)
                st.write(res.text)

# --- TAB 2: MATCHING ---
with tab2:
    st.subheader("දෙදෙනාගේ ගැලපීම පරීක්ෂා කරන්න")
    c1, c2 = st.columns(2)
    with c1:
        st.info("පුරුෂ පාර්ශවය")
        m_name = st.text_input("ඔහුගේ නම")
        m_dob = st.date_input("උපන් දිනය", key="mdob")
        m_tob = st.time_input("උපන් වේලාව", key="mtob")
    with c2:
        st.info("ස්ත්‍රී පාර්ශවය")
        f_name = st.text_input("ඇයගේ නම")
        f_dob = st.date_input("උපන් දිනය", key="fdob")
        f_tob = st.time_input("උපන් වේලාව", key="ftob")
    
    match_btn = st.button("පෝරොන්දම් ගැලපීම බලන්න")
    
    if match_btn:
        with st.spinner("පෝරොන්දම් ගණනය කරමින් පවතී..."):
            match_prompt = f"""
            පහත දෙදෙනාගේ උපන් විස්තර අනුව පෝරොන්දම් ගැලපීම (Matching) සිදු කරන්න:
            පුරුෂයා: {m_name}, උපත: {m_dob} {m_tob}
            ස්ත්‍රිය: {f_name}, උපත: {f_dob} {f_tob}
            
            මෙම දෙදෙනාගේ ගැලපීම ඉතා හොඳද, මධ්‍යමද නැතිනම් අහිතකරද යන්න සිංහලෙන් පැහැදිලි කරන්න. 
            විවාහය සඳහා සුදුසුද යන්න අවසාන නිගමනය ලෙස ලබා දෙන්න.
            """
            match_res = model.generate_content(match_prompt)
            st.success("විශ්ලේෂණය අවසන්!")
            st.write(match_res.text)
