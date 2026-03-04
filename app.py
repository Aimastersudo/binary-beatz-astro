import streamlit as st
import google.generativeai as genai

# --- Gemini AI Configuration ---
# ඔයාගේ API Key එක මෙතැනට ඇතුළත් කරන්න
API_KEY = "AIzaSyDPW_CL3i0GZNHwwAxEedkVtXyaDZicsTE"

try:
    genai.configure(api_key=API_KEY)
    # NotFound error එක මඟහරවා ගැනීමට models/ පදය එක් කිරීම
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    # Flash වැඩ නැත්නම් Pro version එක උත්සාහ කරයි
    model = genai.GenerativeModel('models/gemini-pro')

# --- UI Styling (CSS) ---
st.set_page_config(page_title="Binary Beatz AI Astro", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0f172a; color: white; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { 
        height: 50px; 
        background-color: #1e293b; 
        border-radius: 10px; 
        color: white; 
        padding: 10px 20px; 
    }
    .stTabs [aria-selected="true"] { 
        background-color: #f39c12; 
        color: black; 
        font-weight: bold; 
    }
    .horo-chart { 
        display: grid; 
        grid-template-columns: repeat(4, 1fr); 
        gap: 5px; 
        background-color: #f39c12; 
        border: 3px solid #f39c12;
        max-width: 400px; 
        margin: auto; 
        padding: 5px; 
        border-radius: 5px;
    }
    .house { 
        background-color: white; 
        color: black; 
        height: 90px; 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center; 
        font-size: 13px; 
        font-weight: bold; 
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# --- App Header ---
st.title("🔮 Binary Beatz AI Astrology Center")
st.markdown("Gemini AI තාක්ෂණයෙන් ක්‍රියාත්මක වන ජ්‍යොතිෂ සේවාව")

# --- Navigation Tabs ---
tab1, tab2 = st.tabs(["📊 කේන්දර පරීක්ෂාව (Horoscope)", "💑 පෝරොන්දම් සැසඳීම (Matching)"])

# --- TAB 1: HOROSCOPE ---
with tab1:
    col_a, col_b = st.columns([1, 1.5])
    with col_a:
        st.subheader("ඔබේ උපන් විස්තර")
        u_name = st.text_input("නම")
        u_dob = st.date_input("උපන් දිනය", key="u_dob")
        u_tob = st.time_input("උපන් වේලාව", key="u_tob")
        u_pob = st.text_input("උපන් ස්ථානය (නගරය)", key="u_pob")
        generate_btn = st.button("කේන්දරය විශ්ලේෂණය කරන්න")

    if generate_btn:
        if u_name and u_pob:
            with col_b:
                st.subheader(f"{u_name} මහතාගේ/මියගේ රාශි චක්‍රය")
                st.markdown(f"""
                <div class="horo-chart">
                    <div class="house">12<br>මීන</div><div class="house">1<br>මේෂ</div><div class="house">2<br>වෘෂභ</div><div class="house">3<br>මිථුන</div>
                    <div class="house">11<br>කුම්භ</div><div class="house" style="grid-column: span 2; grid-row: span 2; background-color:#ffd54f;">{u_name}</div><div class="house">4<br>කටක</div>
                    <div class="house">10<br>මකර</div><div class="house">5<br>සිංහ</div>
                    <div class="house">9<br>ධනු</div><div class="house">8<br>වෘශ්චික</div><div class="house">7<br>තුලා</div><div class="house">6<br>කන්‍යා</div>
                </div>
                """, unsafe_allow_html=True)
                
                with st.spinner("AI පලාඵල ලියමින් පවතී..."):
                    prompt = f"මම {u_name}. උපන් දිනය: {u_dob}, වේලාව: {u_tob}, ස්ථානය: {u_pob}. වෛදික ජ්‍යොතිෂයට අනුව පලාඵල විස්තරයක් සිංහලෙන් ලබා දෙන්න."
                    try:
                        response = model.generate_content(prompt)
                        st.markdown("### Gemini AI පලාඵල විස්තරය")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        else:
            st.error("කරුණාකර සියලු විස්තර ඇතුළත් කරන්න.")

# --- TAB 2: MATCHING ---
with tab2:
    st.subheader("විවාහ පෝරොන්දම් ගැලපීම")
    col1, col2 = st.columns(2)
    with col1:
        st.info("👦 පුරුෂ පාර්ශවය")
        m_name = st.text_input("ඔහුගේ නම")
        m_dob = st.date_input("උපන් දිනය", key="m_dob")
        m_tob = st.time_input("උපන් වේලාව", key="m_tob")
    with col2:
        st.info("👧 ස්ත්‍රී පාර්ශවය")
        f_name = st.text_input("ඇයගේ නම")
        f_dob = st.date_input("උපන් දිනය", key="f_dob")
        f_tob = st.time_input("උපන් වේලාව", key="f_tob")
    
    match_btn = st.button("පෝරොන්දම් සැසඳීම ආරම්භ කරන්න")
    if match_btn:
        if m_name and f_name:
            with st.spinner("පෝරොන්දම් ගැලපීම ගණනය කරමින් පවතී..."):
                match_prompt = f"පුරුෂයා: {m_name} ({m_dob}), ස්ත්‍රිය: {f_name} ({f_dob}). මොවුන්ගේ පෝරොන්දම් ගැලපීම ගැන සිංහලෙන් වාර්තාවක් දෙන්න."
                try:
                    match_res = model.generate_content(match_prompt)
                    st.success("විශ්ලේෂණය අවසන්!")
                    st.write(match_res.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
