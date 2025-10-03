
import streamlit as st

st.set_page_config(page_title="The Chase Board", layout="centered")

st.title("🎯 The Chase Board Movement")

# Initialize session state
if "contestant_pos" not in st.session_state:
    st.session_state.contestant_pos = 0
if "chaser_pos" not in st.session_state:
    st.session_state.chaser_pos = 0

# Board layout
board_length = 8
board = ["⬜"] * board_length

# Update board with positions
def render_board():
    display = board.copy()
    if st.session_state.chaser_pos == st.session_state.contestant_pos:
        display[st.session_state.contestant_pos] = "💥"
    else:
        if st.session_state.contestant_pos < board_length:
            display[st.session_state.contestant_pos] = "🧍"
        if st.session_state.chaser_pos < board_length:
            display[st.session_state.chaser_pos] = "😈"
    st.write(" ".join(display))

# Move functions
def move_contestant(step):
    st.session_state.contestant_pos = max(0, min(board_length - 1, st.session_state.contestant_pos + step))

def move_chaser(step):
    st.session_state.chaser_pos = max(0, min(board_length - 1, st.session_state.chaser_pos + step))

# Display board
render_board()

# Buttons
st.subheader("Move Contestant")
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Back"):
        move_contestant(-1)
with col2:
    if st.button("➡️ Forward"):
        move_contestant(1)

st.subheader("Move Chaser")
col3, col4 = st.columns(2)
with col3:
    if st.button("⬅️ Back", key="chaser_back"):
        move_chaser(-1)
with col4:
    if st.button("➡️ Forward", key="chaser_forward"):
        move_chaser(1)

# Outcome
if st.session_state.contestant_pos == board_length - 1:
    st.success("🎉 Contestant reached Home!")
elif st.session_state.chaser_pos == st.session_state.contestant_pos:
    st.error("😱 Chaser caught the Contestant!")
