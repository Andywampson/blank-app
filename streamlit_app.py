import streamlit as st
import time

# --- CONFIGURATION ---
BOSS_NAME = "dr.dryy"
BOSS_SECRET_KEY = "dryy_boss_override_2026"  

# 🔗 PASTE YOUR LIVE STRIPE PAYMENT LINK HERE WHEN READY
STRIPE_CHECKOUT_URL = "https://stripe.com"

# 📺 GOOGLE ADSENSE CODE FOR MONETIZATION
ADSENSE_HTML_CODE = """
<div style="background-color:#FFF3CD;padding:20px;border-radius:10px;border:1px solid #FFEBAA;text-align:center;">
    <h4 style="color:#856404;margin:0;">SPONSORED ADVERTISEMENT</h4>
    <p style="color:#856404;">[Real Ad Banner Area: Google AdSense Code Injected Here]</p>
</div>
"""

# --- INITIALIZE SYSTEM STATES ---
if "is_premium" not in st.session_state:
    st.session_state["is_premium"] = False
if "daily_free_generations" not in st.session_state:
    st.session_state["daily_free_generations"] = 3
if "system_status" not in st.session_state:
    st.session_state["system_status"] = "ONLINE"

st.set_page_config(page_title=f"{BOSS_NAME}'s Video Studio", layout="wide")

# --- 👑 THE GLOBAL BOSS BANNER ---
if st.session_state["system_status"] == "ONLINE":
    st.markdown(f"""
    <div style="background-color:#000000;padding:15px;border-radius:8px;border:2px solid #FFD700;text-align:center;margin-bottom:20px;">
        <h3 style="color:#FFD700;margin:0;font-family:monospace;letter-spacing:2px;">👑 SYSTEM STATUS: OPERATIONAL</h3>
        <p style="color:#FFFFFF;margin:5px 0 0 0;font-size:14px;">Notice: <strong>{BOSS_NAME} is the boss.</strong> The owner reserves the absolute right to remove anyone or terminate any session at any moment without notice.</p>
    </div>
    """, unsafe_allow_code=True)
else:
    st.markdown(f"""
    <div style="background-color:#721C24;padding:25px;border-radius:8px;border:2px solid #F5C6CB;text-align:center;margin-bottom:20px;">
        <h2 style="color:#F8D7DA;margin:0;font-family:monospace;">🚨 SYSTEM TERMINATED BY {BOSS_NAME.upper()}</h2>
        <p style="color:#F8D7DA;margin:10px 0 0 0;font-size:16px;">The boss has pulled the plug. All current user sessions have been revoked.</p>
    </div>
    """, unsafe_allow_code=True)
    
    with st.sidebar:
        st.subheader("🔑 Boss Emergency Core")
        boss_key = st.text_input("Enter Boss Key to Restart:", type="password")
        if st.button("🔄 Restart Mainframes"):
            if boss_key == BOSS_SECRET_KEY:
                st.session_state["system_status"] = "ONLINE"
                st.success("System restored by the Boss.")
                st.rerun()
    st.stop()

# --- SIDEBAR: USER ACCOUNT & SECRET BOSS PANEL ---
with st.sidebar:
    st.header("👤 Your Account")
    
    if st.session_state["is_premium"]:
        st.success("💎 PREMIUM ACCESS UNLOCKED")
    else:
        st.warning("🆓 Free Tier Member")
        st.write(f"Remaining Free Videos Today: **{st.session_state['daily_free_generations']}**")
        st.markdown("### 💰 Premium Pass: **$3.00**")
        
        # 💳 STRIPE PAYWALL BUTTON
        st.markdown(f'<a href="{STRIPE_CHECKOUT_URL}" target="_blank" style="text-decoration:none;"><button style="width:100%;background-color:#6772E5;color:white;border:none;padding:10px;border-radius:5px;cursor:pointer;font-weight:bold;">💳 Unlock with Stripe</button></a>', unsafe_allow_code=True)
        st.caption("Clicking above opens Stripe securely in a new window. Once paid, return here.")
            
    st.markdown("---")
    
    # 🔒 THE SECRET OVERRIDE PANEL
    st.subheader("🕶️ Boss Command Core")
    boss_input = st.text_input("Verify Boss Identity (Enter Password):", type="password")
    if boss_input == BOSS_SECRET_KEY:
        st.success(f"Identity Verified. Standing by, {BOSS_NAME}.")
        if st.button("🛑 KICK EVERYONE & SHUT DOWN SYSTEM"):
            st.session_state["system_status"] = "TERMINATED"
            st.rerun()
        if st.button("🎁 Grant Yourself Free Premium Access"):
            st.session_state["is_premium"] = True
            st.rerun()

# --- MAIN APP INTERFACE ---
st.title(f"🎬 {BOSS_NAME.upper()}'s $3 AI Video Generator")

main_col, ad_col = st.columns()

with main_col:
    prompt = st.text_input("Describe the video you want to create:")
    
    if st.button("🚀 Generate Video"):
        if not prompt.strip():
            st.warning("Please enter a prompt first.")
        elif not st.session_state["is_premium"] and st.session_state["daily_free_generations"] <= 0:
            st.error(f"❌ Out of free generations! Pay $3.00 via Stripe in the sidebar, or request manual clearance from {BOSS_NAME}.")
        else:
            # 📺 AD INTERSTITIAL FOR FREE TIERS
            if not st.session_state["is_premium"]:
                st.info("📺 Loading Sponsored Advertisement... (Unlock Premium to skip)")
                ad_placeholder = st.empty()
                with ad_placeholder.container():
                    st.markdown(ADSENSE_HTML_CODE, unsafe_allow_code=True)
                time.sleep(6)  
                ad_placeholder.empty()
                st.session_state["daily_free_generations"] -= 1

            # GENERATION ENGINE
            st.write("⚙️ Running video scripts on the mainframes...")
            time.sleep(3) 
            st.success("✅ Video completed successfully!")

# --- DISPLAY SIDEBAR ADS ---
with ad_col:
    if not st.session_state["is_premium"]:
        st.markdown("### Sponsored Links")
        st.markdown(ADSENSE_HTML_CODE, unsafe_allow_code=True)
