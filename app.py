import streamlit as st

# --- UI Styling (පින්තූරයේ ඇති Diamond Layout එක සඳහා CSS) ---
st.set_page_config(page_title="Binary Beatz Astro - Diamond Layout", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .chart-wrapper {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
        padding: 20px;
    }
    .horo-box {
        background: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        width: 450px;
        height: 450px;
        position: relative;
        border: 1px solid #ddd;
    }
    /* පින්තූරයේ ඇති ආකාරයට රේඛා ඇඳීම */
    .svg-container {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
    }
    .svg-line {
        stroke: #000;
        stroke-width: 1.5;
    }
    /* දත්ත පෙන්වන ස්ථාන (Positions) */
    .data-label {
        position: absolute;
        font-size: 13px;
        font-weight: bold;
        text-align: center;
        width: 60px;
    }
    .center-title {
        position: absolute;
        top: 45%;
        left: 35%;
        width: 30%;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

def create_diamond_chart(title, planets, center_label):
    # දත්ත පෙන්විය යුතු නිවැරදි ස්ථාන (Coordinates)
    # පින්තූරයේ ඇති අංක පිළිවෙළට අනුව
    h = {str(i): "" for i in range(1, 13)}
    if planets: h.update(planets)

    return f"""
    <div class="horo-box">
        <p style="text-align:center; font-weight:bold; margin-top:-5px;">{title}</p>
        <svg class="svg-container" viewBox="0 0 400 400">
            <rect x="10" y="10" width="380" height="380" fill="none" class="svg-line"/>
            <line x1="10" y1="10" x2="390" y2="390" class="svg-line"/>
            <line x1="390" y1="10" x2="10" y2="390" class="svg-line"/>
            <line x1="200" y1="10" x2="390" y2="200" class="svg-line"/>
            <line x1="390" y1="200" x2="200" y2="390" class="svg-line"/>
            <line x1="200" y1="390" x2="10" y2="200" class="svg-line"/>
            <line x1="10" y1="200" x2="200" y2="10" class="svg-line"/>
        </svg>
        
        <div class="center-title">{center_label}</div>

        <div class="data-label" style="top: 60px; left: 170px;">{h['1']}</div> <div class="data-label" style="top: 30px; left: 80px;">{h['2']}</div>  <div class="data-label" style="top: 100px; left: 30px;">{h['3']}</div> <div class="data-label" style="top: 185px; left: 80px;">{h['4']}</div> <div class="data-label" style="top: 280px; left: 30px;">{h['5']}</div> <div class="data-label" style="top: 340px; left: 80px;">{h['6']}</div> <div class="data-label" style="top: 310px; left: 170px;">{h['7']}</div> <div class="data-label" style="top: 340px; left: 260px;">{h['8']}</div> <div class="data-label" style="top: 280px; left: 310px;">{h['9']}</div> <div class="data-label" style="top: 185px; left: 260px;">{h['10']}</div> <div class="data-label" style="top: 100px; left: 310px;">{h['11']}</div> <div class="data-label" style="top: 30px; left: 260px;">{h['12']}</div>  </div>
    """

st.title("🔮 Binary Beatz Astrology Center")

with st.sidebar:
    st.header("පාලක පුවරුව")
    name = st.text_input("නම", "සචිර")
    submit = st.button("කේන්දරය සාදන්න")

# පින්තූරයේ ඇති පරිදි ග්‍රහයන් ඇතුළත් කිරීම
rashi_data = {"1": "", "12": "ර බු කේ", "11": "ශු", "3": "කු", "7": "ගු", "10": "ච ශ"}
navamsa_data = {"1": "කු", "12": "ගු රා", "3": "ච", "6": "ර කේ", "9": "බු", "8": "ශු"}

if submit:
    st.markdown('<div class="chart-wrapper">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(create_diamond_chart("රාශි සටහන", rashi_data, "වෘෂභ ලග්නය"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_diamond_chart("නවාංශක සටහන", navamsa_data, "කුම්භ නවාංශකය"), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.success(f"{name} මයාගේ කේන්දරය පින්තූරයේ පරිදි සාර්ථකව සකස් කරන ලදී.")
