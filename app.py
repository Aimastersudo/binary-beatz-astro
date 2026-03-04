import streamlit as st

# --- UI Styling (පින්තූරයේ හැඩයටම සකසන ලද CSS) ---
st.set_page_config(page_title="Binary Beatz Astro - Original Layout", layout="wide")

st.markdown("""
<style>
    .report-card { 
        background-color: #ffffff; padding: 25px; border-radius: 15px; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.1); 
        width: fit-content; margin: auto; border: 1px solid #e2e8f0;
    }
    /* කේන්දරේ පිටත රාමුව */
    .horo-container {
        display: grid;
        grid-template-columns: repeat(4, 85px);
        grid-template-rows: repeat(4, 85px);
        gap: 0px; /* කොටු අතර හිඩැසක් නැතිව පින්තූරයේ පරිදි */
        border: 2px solid #334155;
        background-color: #334155;
    }
    /* එක් එක් කොටුවක හැඩය */
    .house {
        background-color: white;
        border: 1px solid #cbd5e1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        font-weight: bold;
        font-size: 15px;
        color: #1e293b;
    }
    /* කොටු අංකය */
    .house-num {
        position: absolute;
        top: 3px;
        left: 5px;
        font-size: 10px;
        color: #94a3b8;
        font-weight: normal;
    }
    /* මැද ඇති ලොකු කොටුව (රාශි/නවාංශක යන නම සඳහා) */
    .center-box {
        grid-column: 2 / span 2;
        grid-row: 2 / span 2;
        background-color: #f8fafc;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: #ef4444;
        font-size: 20px;
        border: 1px solid #cbd5e1;
    }
</style>
""", unsafe_allow_html=True)

def create_traditional_chart(title, planets, center_label):
    # පින්තූරයේ කොටු බෙදා ඇති නිවැරදි පිළිවෙළ (Traditional Sri Lankan Style)
    h = {str(i): "" for i in range(1, 13)}
    if planets: h.update(planets)

    html = f"""
    <div class="report-card">
        <h3 style="text-align:center; color:#334155; margin-bottom:15px;">{title}</h3>
        <div class="horo-container">
            <div class="house"><span class="house-num">12</span>{h['12']}</div>
            <div class="house"><span class="house-num">1</span>{h['1']}</div>
            <div class="house"><span class="house-num">2</span>{h['2']}</div>
            <div class="house"><span class="house-num">3</span>{h['3']}</div>
            
            <div class="house"><span class="house-num">11</span>{h['11']}</div>
            <div class="center-box">{center_label}</div>
            <div class="house"><span class="house-num">4</span>{h['4']}</div>
            
            <div class="house"><span class="house-num">10</span>{h['10']}</div>
            <div class="house"><span class="house-num">5</span>{h['5']}</div>
            
            <div class="house"><span class="house-num">9</span>{h['9']}</div>
            <div class="house"><span class="house-num">8</span>{h['8']}</div>
            <div class="house"><span class="house-num">7</span>{h['7']}</div>
            <div class="house"><span class="house-num">6</span>{h['6']}</div>
        </div>
    </div>
    """
    return html

st.title("🔮 Binary Beatz Astrology Center")

# Sidebar for Input
with st.sidebar:
    st.header("කේන්දර තොරතුරු")
    user_name = st.text_input("නම", "සචිර")
    process = st.button("කේන්දරය බලන්න")

# Sample Data
rashi_data = {"1": "ලග්නය", "12": "රවි", "2": "ශනි", "5": "ගුරු", "7": "රාහු"}
navamsa_data = {"1": "කුජ", "10": "සිකුරු", "4": "බුධ"}

if process:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(create_traditional_chart("රාශි සටහන", rashi_data, "රාශි"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_traditional_chart("නවාංශක සටහන", navamsa_data, "නවාංශක"), unsafe_allow_html=True)
    
    st.balloons()
