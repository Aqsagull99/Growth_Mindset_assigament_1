import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    body {
        background-color: #f4f6f7;
    }
    .main {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    h1{
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
     }

   h2 {
    font-family: 'Arial', sans-serif;
    font-weight: bold;
    padding: 10px;
    border-radius: 5px;
   
}
    .stButton>button {
        background-color: #ac3f7a;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1b4f72;
        transform: scale(1.05);
    }
    .stSidebar {
        background-color: #000000;
        padding: 1rem;
        border-radius: 10px;
    }
    
    .custom-header {
        color: #ff6347 !important;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
    }
    
    </style>
    """, unsafe_allow_html=True)

    


# App title and introduction
st.title("🌱 Growth Mindset Challenge")
st.markdown("### Welcome to the Growth Mindset Challenge!")
st.write("This interactive app helps you embrace challenges, track progress, and grow continuously.")

# Add a  image
st.image("https://images.unsplash.com/photo-1509822929063-6b6cfc9b42f2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", 
         caption="Keep moving forward on your growth journey!", 
         use_container_width=True)

# Sidebar for user input
with st.sidebar:
    st.markdown("<div class='stSidebar'>", unsafe_allow_html=True)
    # st.header("Your Growth Journey")
    st.markdown('<h1 class="custom-header">Your Growth Journey</h1>', unsafe_allow_html=True)

    name = st.text_input("Enter your name:", placeholder="e.g., John Doe")
    goal = st.text_area("What is your learning goal for today?", placeholder="Write your goal here...")
    if st.button("Submit"):
        st.session_state.name = name
        st.session_state.goal = goal
        st.success("Data submitted successfully!")
    st.write("💡 *Remember: Every step forward is progress!*")
    st.markdown("</div>", unsafe_allow_html=True)

# Main Content
st.header("Why Adopt a Growth Mindset?")
st.write("""
- 🌟 **Embrace Challenges**: View obstacles as opportunities to learn.
- 🔄 **Learn from Mistakes**: Understand that errors are part of the process.
- 💪 **Persist Through Difficulties**: Stay determined and keep going.
- 🎯 **Celebrate Effort**: Reward your hard work, not just the outcome.
- 🚀 **Keep an Open Mind**: Stay curious and adaptable.
""")

# Interactive section: Track progress
st.header("📊 Track Your Progress")
growth_score = st.slider("Rate your Growth Mindset today (1-10)", 1, 10, 5)

# Visualize Progress
st.subheader("📈 Your Growth Over Time")
data = pd.DataFrame({
    "Day": np.arange(1, 8),
    "Growth Score": np.random.randint(1, 11, size=7)
})
fig = px.line(data, x="Day", y="Growth Score", 
              title="Your Growth Journey", 
              markers=True, 
              line_shape="spline",
              template="plotly_white")

st.plotly_chart(fig, use_column_width=True)

# Call to Action
st.header("🚀 Take the Challenge!")
if st.button("Start Your Growth Journey"):
    st.balloons()
    if "name" in st.session_state and "goal" in st.session_state:
        st.success(f"🎯 {st.session_state.name}, you're on your way to achieving your goal: {st.session_state.goal}!")
    else:
        st.warning("Please submit your name and goal in the sidebar first!")

# Footer
st.markdown("---")
st.markdown("**Built with ❤️ using Streamlit** | [Learn more about Growth Mindset](https://www.mindsetworks.com/science/)")



