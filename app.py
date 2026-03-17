import streamlit as st
import datetime
import pandas as pd
import numpy as np
import time

# --- 1. SET PAGE CONFIG ---
st.set_page_config(page_title="AI Study Planner", page_icon="🔮", layout="wide")

# --- 2. THE CSS OVERHAUL (Keeping your exact UI intact) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    .gradient-text {
        background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3rem;
        margin-bottom: 0px;
    }

    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.8);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    div.stButton > button:first-child {
        background: linear-gradient(45deg, #4f46e5, #7c3aed);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
    }

    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        font-weight: 700;
        color: #f8fafc;
    }
    
    /* Timer specific styling */
    .pomodoro-timer {
        font-size: 5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #a855f7, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3858/3858711.png", width=80) 
    st.markdown("### AI Study Planner")
    menu = st.radio("Navigation", 
                    ["Dashboard", "Add Subject", "Generate Schedule", "Revision", "Productivity"], 
                    label_visibility="collapsed")
    st.divider()
    # Removed the AI Model info box as requested

# --- 4. PAGE LOGIC ---

# ---------------------------------
# PAGE: DASHBOARD (Newly Built)
# ---------------------------------
if menu == "Dashboard":
    st.markdown('<p class="gradient-text">Overview Dashboard</p>', unsafe_allow_html=True)
    st.write("Welcome back. Here is your academic telemetry.")
    
    # Top Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Total Topics", "42", "+3 this week")
        st.markdown('</div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Focus Hours", "18.5", "On track")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Completion", "64%", "+2%")
        st.markdown('</div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Current Streak", "5 Days", "🔥")
        st.markdown('</div>', unsafe_allow_html=True)

    # Activity Chart Area
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Weekly Activity Heatmap")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Data Structures', 'Quantum Theory', 'Linear Algebra'])
    st.area_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------
# PAGE: ADD SUBJECT (Original)
# ---------------------------------
elif menu == "Add Subject":
    st.markdown('<p class="gradient-text">New Target</p>', unsafe_allow_html=True)
    st.write("Set your academic milestones and difficulty parameters.")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        subject = st.text_input("Subject Title", placeholder="Enter subject name...")
        exam_date = st.date_input("Deadline / Exam Date", value=datetime.date(2026, 3, 15))
        difficulty = st.select_slider("Intensity Level", options=["Low", "Medium", "High", "Critical"])
    
    with col2:
        st.write("Current Standing")
        topics = st.number_input("Total Topics", value=10)
        done = st.number_input("Topics Finished", value=0, max_value=topics)
        
        progress = (done/topics) if topics > 0 else 0
        st.progress(progress)
        st.caption(f"Status: {int(progress*100)}% Complete")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Initialize Subject"):
        st.balloons()
        st.success(f"Successfully integrated {subject} into your neural net.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------
# PAGE: GENERATE SCHEDULE (Original)
# ---------------------------------
elif menu == "Generate Schedule":
    st.markdown('<p class="gradient-text">AI Schedule</p>', unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Study Velocity", "4.2 hrs/day", "+0.5h")
        st.markdown('</div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Exam Proximity", "12 Days", "Priority: HIGH")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("Cognitive Load", "68%", "Optimal")
        st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("Customize AI Generation Parameters", expanded=True):
        col_a, col_b = st.columns(2)
        with col_a:
            st.multiselect("Active Subjects", ["Data Structures", "Quantum Theory", "Linear Algebra"], default=["Data Structures"])
        with col_b:
            st.selectbox("Optimization Goal", ["Retention Max", "Speed Run", "Balanced"])
        
        if st.button("Generate Optimized Path"):
            with st.spinner("Synthesizing optimal study blocks..."):
                time.sleep(1)
            st.write("### 📅 Weekly Roadmap")
            df = pd.DataFrame({
                "Time Block": ["08:00 - 10:00", "10:30 - 12:30", "14:00 - 16:00", "19:00 - 21:00"],
                "Activity": ["Deep Work: Theory", "Problem Sets", "Active Recall", "Light Review"],
                "Subject": ["Data Structures", "Data Structures", "Quantum Theory", "General"]
            })
            st.table(df)

# ---------------------------------
# PAGE: REVISION (Newly Built)
# ---------------------------------
elif menu == "Revision":
    st.markdown('<p class="gradient-text">Spaced Repetition</p>', unsafe_allow_html=True)
    st.write("Topics the AI determined you are most likely to forget today.")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("⚠️ Critical Review Needed")
    st.checkbox("Data Structures: Big O Notation")
    st.checkbox("Quantum Theory: Schrödinger equation")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🔄 Routine Reinforcement")
    st.checkbox("Linear Algebra: Matrix Multiplication")
    st.checkbox("Data Structures: Linked Lists")
    st.checkbox("General: Study Techniques")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Log Revision Session"):
        st.success("Neurological pathways reinforced! Memory updated.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------
# PAGE: PRODUCTIVITY (Newly Built)
# ---------------------------------
elif menu == "Productivity":
    st.markdown('<p class="gradient-text">Focus Engine</p>', unsafe_allow_html=True)
    st.write("Deep work timer to maximize your cognitive output.")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    mode = st.radio("Mode", ["Pomodoro (25m)", "Deep Work (90m)", "Short Break (5m)"], horizontal=True)
    
    # Fake timer display
    if mode == "Pomodoro (25m)":
        st.markdown('<p class="pomodoro-timer">25:00</p>', unsafe_allow_html=True)
    elif mode == "Deep Work (90m)":
        st.markdown('<p class="pomodoro-timer">90:00</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="pomodoro-timer">05:00</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.button("▶️ Start Focus Block", use_container_width=True)
    with col2:
        st.button("⏸️ Pause", use_container_width=True)
    with col3:
        st.button("🔄 Reset", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Distraction block toggle
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🛡️ Distraction Shield")
    st.toggle("Block Social Media (Requires Browser Extension)")
    st.toggle("Enable Ambient White Noise")
    st.markdown('</div>', unsafe_allow_html=True)