import streamlit as st

# --- UI Styling (පින්තූරයේ ඇති Grid + Diagonal lines Layout එක සඳහා) ---
st.set_page_config(page_title="Binary Beatz Astro", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; color: white; }
    .stApp { background-color: #0e1117; }
    
    .chart-container {
        background-color: white;
        width: 400px;
        height: 400px;
        position: relative;
        border: 2px solid #000;
        margin: 20px auto;
    }
    
    /* කොටු 9ක Grid එක ඇඳීම */
    .grid-line {
        position: absolute;
        background-color: #000;
    }
    
    /* දත්ත පෙන්වන ස්ථාන (Labels) */
    .cell-text {
        position: absolute;
        color: black;
        font-size: 14px;
        font-weight: bold;
        text-align: center;
        width: 60px;
    }
    
    /* මැද කොටුවේ මාතෘකාව */
    .center-title {
        position: absolute;
        top: 170px;
        left: 140px;
        width: 120px;
        text-align: center;
        color: black;
        font-size: 18px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def create_astro_chart(title, planets, center_txt):
    p = {str(i): "" for i in range(1, 13)}
    if planets: p.update(planets)

    # SVG භාවිතයෙන් පින්තූරයේ ඇති සියලුම ඉරි නිවැරදිව ඇඳීම
    svg_html = f"""
    <div style="text-align: center; color: white; margin-bottom: 5px; font-weight: bold;">{title}</div>
    <div class="chart-container">
        <svg width="400" height="400" viewBox="0 0 400 400" style="position: absolute;">
            <line x1="133" y1="0" x2="133" y2="400" stroke="black" stroke-width="2"/>
            <line x1="266" y1="0" x2="266" y2="400" stroke="black" stroke-width="2"/>
            <line x1="0" y1="133" x2="400" y2="133" stroke="black" stroke-width="2"/>
            <line x1="0" y1="266" x2="400" y2="266" stroke="black" stroke-width="2"/>
            
            <line x1="0" y1="0" x2="133" y2="133" stroke="black" stroke-width="2"/>
            <line x1="400" y1="0" x2="266" y2="133" stroke="black" stroke-width="2"/>
            <line x1="0" y1="400" x2="133" y2="266" stroke="black" stroke-width="2"/>
            <line x1="400" y1="400" x2="266" y2="266" stroke="black" stroke-width="2"/>
        </svg>
        
        <div class="center-title">{center_txt}</div>
        
        <div class="cell-text" style="top: 20px; left: 170px;">{p['1']}</div>
        <div class="cell-text" style="top: 20px; left: 40px;">{p['2']}</div>
        <div class="cell-text" style="top: 70px; left: 10px;">{p['3']}</div>
        <div class="cell-text" style="top: 190px; left: 40px;">{p['4']}</div>
        <div class="cell-text" style="top: 310px; left: 10px;">{p['5']}</div>
        <div class="cell-text" style="top: 350px; left: 40px;">{p['6']}</div>
        <div class="cell-text" style="top: 350px; left: 170px;">{p['7']}</div>
        <div class="cell-text" style="top: 350px; left: 300px;">{p['8']}</div>
        <div class="cell-text" style="top: 310px; left: 330px;">{p['9']}</div>
        <div class="cell-text" style="top: 190px; left: 300px;">{p['10']}</div>
        <div class="cell-text" style="top: 70px; left: 330px;">{p['11']}</div>
        <div class="cell-text" style="top: 20px; left: 300px;">{p['12']}</div>
    </div>
    """
    return svg_html

st.title("🔮 Binary Beatz Astrology Center")

with st.sidebar:
    name = st.text_input("නම", "සචිර")
    submit = st.button("කේන්දරය බලන්න")

# පින්තූරයේ තිබූ පරිදිම දත්ත ඇතුළත් කිරීම
rashi_data = {"12": "ර බු කේ", "11": "ශු", "3": "කු", "7": "ගු", "10": "ච ශ"}
navam_data = {"1": "කු", "12": "ගු රා", "3": "ච", "6": "ර කේ", "9": "බු", "8": "ශු"}

if submit:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(create_astro_chart("රාශි සටහන", rashi_data, "වෘෂභ ලග්නය"), unsafe_allow_html=True)
    with col2:
        st.markdown(create_astro_chart("නවාංශක සටහන", navam_data, "කුම්භ නවාංශකය"), unsafe_allow_html=True)
    
    st.success(f"{name} මයාගේ කේන්දරය සාර්ථකව සකස් කරන ලදී.")
