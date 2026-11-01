import os
from datetime import date

import streamlit as st


st.set_page_config(page_title="Video Studio", page_icon="🎬", layout="wide")

FREE_DAILY_DRAFTS = 3
STRIPE_CHECKOUT_URL = os.getenv("STRIPE_CHECKOUT_URL", "").strip()

if st.session_state.get("usage_date") != date.today().isoformat():
    st.session_state["usage_date"] = date.today().isoformat()
    st.session_state["drafts_remaining"] = FREE_DAILY_DRAFTS

if "is_premium" not in st.session_state:
    st.session_state["is_premium"] = False

st.title("Video Studio")
st.caption("Turn a brief into a production-ready storyboard draft.")

with st.sidebar:
    st.header("Your account")
    if st.session_state["is_premium"]:
        st.success("Premium access")
    else:
        st.info("Free plan")
        st.write(f"Storyboard drafts left today: **{st.session_state['drafts_remaining']}**")
        if STRIPE_CHECKOUT_URL.startswith("https://"):
            st.link_button("Unlock Premium", STRIPE_CHECKOUT_URL, use_container_width=True)
            st.caption("Premium access is not activated automatically. A verified payment integration is required.")
        else:
            st.caption("Premium checkout is not configured.")

    st.divider()
    st.subheader("Sponsored")
    st.write("Ad placements can be added here after an ad provider is configured.")

st.subheader("Build your video concept")
prompt = st.text_area(
    "Describe the video you want to make",
    placeholder="A quiet morning routine in a sunlit kitchen, filmed like a documentary...",
    height=120,
)

option_col, duration_col = st.columns(2)
with option_col:
    visual_style = st.selectbox(
        "Visual style",
        ["Cinematic", "Documentary", "Minimal", "Playful", "Product showcase"],
    )
with duration_col:
    duration = st.selectbox("Target duration", ["15 seconds", "30 seconds", "60 seconds"])

can_create_draft = st.session_state["is_premium"] or st.session_state["drafts_remaining"] > 0
if st.button("Create storyboard draft", type="primary", disabled=not can_create_draft):
    if not prompt.strip():
        st.warning("Add a description before creating a draft.")
    else:
        if not st.session_state["is_premium"]:
            st.session_state["drafts_remaining"] -= 1

        st.subheader("Storyboard draft")
        st.write(f"**Concept:** {prompt.strip()}")
        st.write(f"**Style:** {visual_style}  ·  **Duration:** {duration}")

        scene_col1, scene_col2, scene_col3 = st.columns(3)
        with scene_col1:
            st.markdown("**01 · Opening**")
            st.write("Establish the setting and introduce the main subject.")
        with scene_col2:
            st.markdown("**02 · Main beat**")
            st.write("Show the key action or idea with a clear visual focus.")
        with scene_col3:
            st.markdown("**03 · Closing**")
            st.write("End on a memorable image that reinforces the concept.")

        st.caption("Demo output only. Connect a video-generation service to render a finished video.")
elif not can_create_draft:
    st.warning("You have used today's free storyboard drafts.")
