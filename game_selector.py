import streamlit as st
import random
import time

# -----------------------------
# Typing effect simulation for Streamlit
# -----------------------------
def type_writer(message, placeholder=None, delay=0.03):
    """Simulate typewriter effect in Streamlit using a placeholder."""
    if placeholder is None:
        placeholder = st.empty()
    text = ""
    for char in message:
        text += char
        placeholder.text(text)
        time.sleep(delay)
    return placeholder

# -----------------------------
# Suspense reveal function
# -----------------------------
def suspense_reveal(game, placeholder=None):
    if placeholder is None:
        placeholder = st.empty()

    # Start reveal line
    placeholder.text("The game you should play is")
    
    # Dramatic dots
    dots = ""
    for _ in range(3):
        dots += "."
        placeholder.text(f"The game you should play is{dots}")
        time.sleep(0.7)

    # Final reveal
    time.sleep(0.5)
    placeholder.success(f"✅ You should play {game.title()} 🎉")

# -----------------------------
# Streamlit App
# -----------------------------
st.title("🎮 GAME SELECTOR 3000")

# Input for games
games_input = st.text_input("Enter your games (comma separated):")

# Pick a game button
if st.button("Pick a Game"):
    if not games_input.strip():
        st.warning("Please enter at least one game!")
    else:
        games_list = [game.strip() for game in games_input.split(",") if game.strip()]
        
        # Optional: simulate slot machine cycling effect
        placeholder = st.empty()
        for _ in range(10):
            choice = random.choice(games_list).title()
            placeholder.text(f"🎲 {choice}")
            time.sleep(0.1)

        # Final choice with suspense reveal
        final_choice = random.choice(games_list).title()
        suspense_reveal(final_choice, placeholder)
