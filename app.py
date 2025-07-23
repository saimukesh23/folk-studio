import streamlit as st
import json
from components.login import show_login_page
from core.auth import init_db
from config.config import LANGUAGES

def load_translations(language_code):
    with open(f"translations/{language_code}.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    init_db()

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "language" not in st.session_state:
        st.session_state.language = "en"

    # Load translations based on session state, default to 'en'
    translations = load_translations(st.session_state.language)

    if not st.session_state.logged_in:
        show_login_page(translations)
    else:
        st.sidebar.title("Folk Studio")
        language_name = st.sidebar.selectbox(
            translations["select_language"],
            options=list(LANGUAGES.keys()),
            index=list(LANGUAGES.values()).index(st.session_state.language)
        )
        selected_language_code = LANGUAGES[language_name]

        if st.session_state.language != selected_language_code:
            st.session_state.language = selected_language_code
            translations = load_translations(st.session_state.language)
            st.experimental_rerun()

        st.title(translations["app_title"])
        st.write(f"Welcome, {st.session_state.username}!")

        from components.media import show_media_page
        from core.storage import save_audio_file, save_metadata
        from core.ai import check_internet_connection, generate_lyrics
        import pandas as pd

        # Main content
        uploaded_file = show_media_page(translations)

        if uploaded_file:
            st.audio(uploaded_file, format='audio/wav')

            with st.form("metadata_form"):
                folk_type = st.selectbox(translations["folk_type"], ["", "Lavani", "Baul", "Bihu", "Burrakatha"])
                region = st.selectbox(translations["region"], ["", "Maharashtra", "Assam", "Telangana"])

                submitted = st.form_submit_button(translations["submit"])

                if submitted:
                    if folk_type and region:
                        filepath, filename = save_audio_file(uploaded_file)

                        metadata = {
                            "username": st.session_state.username,
                            "native_place": st.session_state.native_place,
                            "selected_language": st.session_state.language,
                            "audio_filename": filename,
                            "audio_filepath": filepath,
                            "timestamp": pd.to_datetime("now"),
                            "folk_type": folk_type,
                            "region": region
                        }
                        save_metadata(metadata)
                        st.success("Your recording and metadata have been saved!")
                    else:
                        st.error("Please select a Folk Type and Region.")

        # AI Lyrics Generator
        if check_internet_connection():
            st.subheader(translations["ai_lyrics_generator"])
            prompt = st.text_area("Enter a prompt for the AI to generate lyrics (e.g., 'a song about a river in a village')")
            if st.button("Generate Lyrics"):
                if prompt:
                    lyrics = generate_lyrics(prompt)
                    if lyrics:
                        st.text_area("Generated Lyrics", lyrics, height=200)
                else:
                    st.warning("Please enter a prompt.")
        else:
            st.info(translations["internet_needed"])

        if st.sidebar.button(translations["logout"]):
            st.session_state.logged_in = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()
