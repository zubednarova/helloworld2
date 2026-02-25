import streamlit as st
import os

st.set_page_config(page_title="Hello World – Keboola Data App", page_icon="🟡")

st.title("👋 Hello World")
st.subheader("Keboola Data App — Python/JS Image")

st.success("✅ App is running successfully inside the `keboola/data-app-python-js` container.")

st.markdown("---")
st.markdown("### Environment")

# Show a few safe env vars to confirm secrets wiring works
kbc_url = os.environ.get("KBC_URL", "*(not set)*")
st.write(f"**KBC_URL:** `{kbc_url}`")

st.markdown("---")
st.markdown(
    "This is the minimal Hello World template. "
    "Replace `streamlit_app.py` with your own app logic."
)
