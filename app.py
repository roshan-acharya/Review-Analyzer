import streamlit as st
import requests

st.set_page_config(
    page_title="Daraz Review Analyzer",
    layout="wide"
)

st.title("🛒 Daraz Review Topic Analyzer")
st.caption("Topic modeling • sentiment analysis • smart summaries")

url = st.text_input(
    "Daraz Product Link",
    placeholder="https://www.daraz.com.np/products/..."
)

if st.button("Analyze"):
    if not url.strip():
        st.warning("Please enter a valid Daraz product link.")
    else:
        with st.spinner("Scraping reviews & analyzing topics..."):
            res = requests.post(
                "http://localhost:8000/analyze",
                params={"url": url}
            ).json()

        topics = res.get("results", [])

        if not topics:
            st.error("No topics detected.")
        else:
            st.success(f"🔍 {len(topics)} topics identified")

            for idx, t in enumerate(topics, start=1):

                # ---------- TOPIC HEADER ----------
                st.markdown(
                    f"""
                    ### 🔹 {t['topic_name'].title()}
                    """
                )

                col1, col2 = st.columns([1, 1])
                col1.metric("🗂 Reviews", t["count"])
                col2.metric("📊 Sentiment", t["sentiment"].capitalize())

                # ---------- SUMMARY EXPANDER ----------
                with st.expander("📄 View Summary"):
                    st.write(t["summary"])

                    # ---------- REVIEWS EXPANDER ----------
                    with st.expander(f"💬 View {t['count']} Reviews"):
                        for r in t["reviews"]:
                            st.markdown(f"- {r}")

                st.divider()
