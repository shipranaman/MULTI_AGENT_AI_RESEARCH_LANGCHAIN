import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent AI Research System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Research System")
st.write(
    "Enter any research topic. The system will search the web, scrape the best source, "
    "generate a detailed report, and review it using an AI critic."
)

topic = st.text_input(
    "Enter Research Topic",
    placeholder="Example: Impact of AI on Healthcare"
)

if st.button("🚀 Start Research", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Running Multi-Agent Research System..."):

        state = run_research_pipeline(topic)

    st.success("Research Completed Successfully!")

    st.divider()

    with st.expander("🔍 Search Results", expanded=False):
        st.write(state["search_results"])

    with st.expander("📄 Scraped Content", expanded=False):
        st.write(state["scraped_content"])

    st.subheader("📝 Final Research Report")

    st.markdown(state["report"])

    st.divider()

    st.subheader("🧐 Critic Feedback")

    st.markdown(state["feedback"])

    st.download_button(
        label="📥 Download Report",
        data=state["report"],
        file_name="research_report.txt",
        mime="text/plain"
    )