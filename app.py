import streamlit as st

# --- UI Styling (නිවැරදි කොටු පිළිවෙළ සඳහා CSS) ---
st.set_page_config(page_title="Binary Beatz Astro - Correct Layout", layout="wide")

st.markdown("""
<style>
    .report-card { 
        background-color: white; padding: 20px; border-radius: 12px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border: 1px solid #e2e8f0;
        margin-bottom: 20px; color: #1e293b;
    }
    /* කේන්දර සටහනේ Grid එක */
    .horo-chart { 
        display: grid; 
        grid-template-columns: repeat(4, 1fr); 
        grid-template-rows: repeat(4, 1fr);
        gap: 2px; 
        background-color: #475569; 
        border: 3px solid #475569;
        width: 320px; 
        height: 320px;
        margin: auto;
    }
    .house { 
        background-color: white; 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center; 
        font-size: 13px; 
        font-weight: bold;
        position: relative;
    }
    /* කොටු අංකය පෙන්වීමට */
    .house-num {
        position: absolute;
        top: 2px;
        left: 4px;
        font-size: 9px;
        color: #94a3b8;
    }
    .center-box {
        grid-column: 2 / span 2; 
        grid-row: 2 / span 2; 
        background-color: #f8fafc; 
        display: flex;
        align-items: center; 
        justify-content: center;
        font-weight: bold; 
        color: #ef4444; 
        border: 1px solid #cbd5e1;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

def create_horo_html(title, planets, center_txt):
    # සාම්ප්‍රදායික කොටු පිළිවෙළ (ලංකාවේ ක්‍රමය)
    # [12][1][2][3]
    # [11]      [4]
    # [10]      [5]
    # [9][8][7][6]
    
    h = {str(i): "" for i in range(1, 13)}
    if planets: h.update(planets)

    html = f"""
    <div class="report-card">
        <h4 style="text-align:center; margin-bottom:15px;">{title}</h4>
        <div class="horo-chart">
            <div class="house"><span class="house-num">12</span>{h['12']}</div>
            <div class="house"><span class="house-num">1</span>{h['1']}</div>
            <div class="house"><span class="house-num">2</span>{h['2']}</div>
            <div class="house"><span class="house-num">3</span>{h['3']}</div>
            <div class="house"><span class="house-num">11</span>{h['11']}</div>
            <div class="center-box">{center_txt}</div>
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

st.title("🔮 Binary Beatz AI Astrology Center")

with st.sidebar:
    st.header("තොරතුරු ඇතුළත් කරන්න")
    name = st.text_input("නම", "සචිර")
    submit = st.button("කේන්දරය සාදන්න")

# Sample Planets (මෙහි අගයන් වෙනස් කළ හැක)
rashi_planets = {"1": "ලග්නය", "2": "ශනි", "5": "ගුරු", "12": "රවි, බුධ"}
navam_planets = {"1": "කුජ", "10": "සිකුරු", "7": "රාහු"}

if submit:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(create_horo_html("රාශි සටහන", rashi_planets, "රාශි"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_horo_html("නවාංශක සටහන", navam_planets, "නවාංශක"), unsafe_allow_html=True)
    
    st.success(f"{name} මයාගේ කේන්දර සටහන සාර්ථකව සකස් කරන ලදී!")
