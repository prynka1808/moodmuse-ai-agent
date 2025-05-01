import streamlit as st

# ---------------------- App Configuration ----------------------
st.set_page_config(page_title="MoodMuse", page_icon="🎵", layout="centered")

# ---------------------- App Title ----------------------
st.title("🎧 MoodMuse")
st.subheader("Let your mood choose your vibe.")

st.write("Type in how you're feeling today, and I'll share an uplifting quote and a song suggestion to match your mood! 💜")

# ---------------------- Mood Mapping ----------------------
mood_map = {
    "happy": {
        "quote": "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
        "song": "🎶 *‘Happy’ by Pharrell Williams*"
    },
    "sad": {
        "quote": "Tears come from the heart and not from the brain. – Leonardo da Vinci",
        "song": "🎧 *‘Fix You’ by Coldplay*"
    },
    "anxious": {
        "quote": "You don’t have to control your thoughts. You just have to stop letting them control you. – Dan Millman",
        "song": "🌊 *‘Weightless’ by Marconi Union*"
    },
    "angry": {
        "quote": "Speak when you are angry and you will make the best speech you will ever regret. – Ambrose Bierce",
        "song": "🔥 *‘Demons’ by Imagine Dragons*"
    },
    "lonely": {
        "quote": "The greatest thing in the world is to know how to belong to oneself. – Michel de Montaigne",
        "song": "🌧️ *‘Someone Like You’ by Adele*"
    },
    "motivated": {
        "quote": "The future depends on what you do today. – Mahatma Gandhi",
        "song": "💪 *‘Stronger’ by Kanye West*"
    },
    "romantic": {
        "quote": "Love is composed of a single soul inhabiting two bodies. – Aristotle",
        "song": "💖 *‘Perfect’ by Ed Sheeran*"
    }
}

# ---------------------- User Input ----------------------
user_mood = st.text_input("💬 How are you feeling today? (e.g., happy, sad, anxious...)")

# ---------------------- Output Section ----------------------
if user_mood:
    mood = user_mood.lower().strip()
    if mood in mood_map:
        st.success("Here's something to match your mood 🎁")
        st.markdown(f"### 💡 Quote:\n> *{mood_map[mood]['quote']}*")
        st.markdown(f"### 🎵 Song Suggestion:\n{mood_map[mood]['song']}")
    else:
        st.warning("Oops! I don't recognize that mood yet. Try one of these: happy, sad, anxious, angry, lonely, motivated, romantic.")

# ---------------------- Footer ----------------------
st.markdown("---")
st.caption("🚀 Made with 💜 by Priyanka · AI Agent Project · April 2025")
