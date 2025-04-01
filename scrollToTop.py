import streamlit as st


def scrollToTop():
    st.markdown(
        """
        <script>
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
        </script>
        """,
        unsafe_allow_html=True,
    )


def create_scroll_to_top_button(key_suffix=""):
    unique_key = f"scroll_to_top_{key_suffix}"

    st.markdown(
        "<h1 style='text-align: center;'></h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p></p>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(
        [0.7, 0.15, 0.15]
    )

    with col3:
        if st.button("⬆️ Move to Top", key=unique_key):
            scrollToTop()
