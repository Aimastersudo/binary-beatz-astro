import streamlit as st

# --- UI Styling (පින්තූරයේ හැඩයටම සකසන ලද CSS) ---
st.set_page_config(page_title="Binary Beatz Astro", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f1f5f9; }
    .report-card { 
        background-color: #ffffff; padding: 20px; border-radius: 15px; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.1); 
        width: 360px; margin: 10px auto; border: 2px solid #e2e8f0;
    }
    .horo-container {
        display: grid;
        grid-template-columns: repeat(4, 80px);
        grid-template-rows: repeat(4, 80px);
        gap: 0px;
        border: 2px solid #334155;
        width: 320px;
        margin: auto;
    }
    .house {
        background-color: white;
        border: 1px solid #cbd5e1;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        font-weight: bold;
        font-size: 14px;
        color: #1e293b;
        height: 80px;
    }
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
        font-size: 18px;
        border: 1px solid #cbd5e1;
    }
</style>
""", unsafe_allow_html=True)

def create_traditional_chart(title, planets, center_label):
    h = {str(i): "" for i in range(1, 13)}
    if planets: h.update(planets)
    
    # පින්තූරයේ පරිදි නිවැරදි කොටු බෙදීම
    return f"""
    <div class="report-card">
        <h3 style="text-align:center; color:#334155; margin-bottom:10px;">{title}</h3>
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

st.title("🔮 Binary Beatz Astrology Center")

with st.sidebar:
    st.header("කේන්දර තොරතුරු")
    name = st.text_input("ඔබේ නම", "සචිර")
    submit = st.button("කේන්දරය බලන්න")

# Sample Planets (සටහනේ පෙන්වීමට දත්ත)
rashi_p = {"1": "ලග්නය", "12": "රවි", "2": "ශනි", "5": "ගුරු", "7": "රාහු", "9": "කුජ"}
navam_p = {"1": "සිකුරු", "10": "බුධ", "4": "සඳු"}

if submit:
    # මෙවර කෙලින්ම columns නැතිව පේළියට පෙන්වමු (පැහැදිලිව පෙනීමට)
    st.markdown(create_traditional_chart("රාශි සටහන", rashi_p, "රාශි"), unsafe_allow_html=True)
    st.markdown(create_traditional_chart("නවාංශක සටහන", navam_p, "නවාංශක"), unsafe_allow_html=True)
    st.success(f"ආයුබෝවන් {name}! ඔබේ කේන්දර සටහන් සාර්ථකව සකස් කරන ලදී.")
