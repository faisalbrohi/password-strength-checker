import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker")

st.title("🔐 Password Strength Checker")

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) < 8:
        remarks.append("Too short (min 8 characters)")
    else:
        strength += 1

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add special characters")

    if strength <= 2:
        rating = "❌ Weak"
        color = "red"
    elif strength in [3, 4]:
        rating = "⚠️ Moderate"
        color = "orange"
    else:
        rating = "✅ Strong"
        color = "green"

    return rating, remarks, color

password = st.text_input("Enter your password", type="password")

if password:
    rating, suggestions, color = check_password_strength(password)
    st.markdown(f"*Strength*: <span style='color:{color}'>{rating}</span>", unsafe_allow_html=True)

    if suggestions:
        st.markdown("### Suggestions to improve:")
        for tip in suggestions:
            st.markdown(f"- {tip}")
    else:
        st.success("Awesome! Your password is strong.")
