import streamlit as st
import random

# ---------------------- App Configuration ----------------------
st.set_page_config(page_title="MoodMuse", page_icon="🎵", layout="centered")

# ---------------------- App Title ----------------------
st.title("🎧 MoodMuse")
st.subheader("Let your mood choose your vibe.")
st.write("Pick how you're feeling today, and I'll match it with a quote and a song that vibes with you 💜")

# ---------------------- Mood Mapping ----------------------
mood_map = {
    "😊 Happy": {
        "quote": "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
        "song": "‘Happy’ by Pharrell Williams 🎶",
        "youtube": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "bgcolor": "#FFFDE7"
    },
    "😢 Sad": {
        "quote": "Tears come from the heart and not from the brain. – Leonardo da Vinci",
        "song": "‘Fix You’ by Coldplay 🎧",
        "youtube": "https://www.youtube.com/watch?v=k4V3Mo61fJM",
        "bgcolor": "#E3F2FD"
    },
    "😰 Anxious": {
        "quote": "You don’t have to control your thoughts. You just have to stop letting them control you. – Dan Millman",
        "song": "‘Weightless’ by Marconi Union 🌊",
        "youtube": "https://www.youtube.com/watch?v=UfcAVejslrU",
        "bgcolor": "#F3E5F5"
    },
    "😡 Angry": {
        "quote": "Speak when you are angry and you will make the best speech you will ever regret. – Ambrose Bierce",
        "song": "‘Demons’ by Imagine Dragons 🔥",
        "youtube": "https://www.youtube.com/watch?v=mWRsgZuwf_8",
        "bgcolor": "#FFEBEE"
    },
    "😔 Lonely": {
        "quote": "The greatest thing in the world is to know how to belong to oneself. – Michel de Montaigne",
        "song": "‘Someone Like You’ by Adele 🌧️",
        "youtube": "https://www.youtube.com/watch?v=hLQl3WQQoQ0",
        "bgcolor": "#ECEFF1"
    },
    "💪 Motivated": {
        "quote": "The future depends on what you do today. – Mahatma Gandhi",
        "song": "‘Stronger’ by Kanye West 💪",
        "youtube": "https://www.youtube.com/watch?v=PsO6ZnUZI0g",
        "bgcolor": "#E8F5E9"
    },
    "❤️ Romantic": {
        "quote": "Love is composed of a single soul inhabiting two bodies. – Aristotle",
        "song": "‘Perfect’ by Ed Sheeran 💖",
        "youtube": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
        "bgcolor": "#FCE4EC"
    }
}

# ---------------------- Mood Dropdown ----------------------
mood_options = list(mood_map.keys())
selected_mood = st.selectbox("💬 Select your mood:", [""] + mood_options)

# ---------------------- Surprise Me Button ----------------------
if st.button("🎲 Surprise Me!"):
    selected_mood = random.choice(mood_options)
    st.info(f"Feeling lucky? We picked **{selected_mood}** for you!")

# ---------------------- Show Mood Content ----------------------
if selected_mood:
    data = mood_map[selected_mood]

    # Background color
    st.markdown(
        f"""<style>
        .stApp {{
            background-color: {data['bgcolor']};
        }}
        </style>""",
        unsafe_allow_html=True
    )

    # Mood Response
    st.success("Here's something to match your mood 🎁")
    st.markdown(f"### 💡 Quote:\n> *{data['quote']}*")
    st.markdown(f"### 🎵 Now Playing:\n**{data['song']}**")
    st.video(data["youtube"])

    # Gratitude Input
    gratitude = st.text_area("💌 What's one thing you're grateful for today?")
    if gratitude:
        st.markdown(f"✅ _“{gratitude}”_ – That’s beautiful 💜")

    # Reset Button
    if st.button("🔁 Try Another Mood"):
        st.experimental_rerun()

# ---------------------- Footer ----------------------
st.markdown("---")
st.caption("🚀 Made with 💜 by Priyanka · AI Agent Project · MoodMuse 3.0 · April 2025")
