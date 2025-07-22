# Folk Studio

Folk Studio is a Streamlit web app for collecting user voice recordings of folk songs, along with key metadata. It is designed to be mobile-first, offline-friendly, and deployable on Hugging Face Spaces.

## Features

-   **User Authentication:** Register and login with a username, password, and native place.
-   **Multilingual UI:** Supports English, Hindi, Telugu, Tamil, Kannada, and Bengali.
-   **Audio Recording and Uploading:** Record audio using the microphone or upload audio files (`.wav`, `.mp3`, `.m4a`).
-   **Metadata Collection:** Collects metadata for each recording, including folk type, region, and user information.
-   **Offline-First:** The app is designed to work without an internet connection. Recording and uploading work offline.
-   **Optional AI Lyrics Generator:** An optional feature to generate lyrics using the Groq API. This feature is only available with an internet connection.

## Project Structure

```
.
├── app.py
├── components
│   ├── login.py
│   └── media.py
├── config
│   └── config.py
├── core
│   ├── ai.py
│   ├── auth.py
│   └── storage.py
├── recordings
├── requirements.txt
├── translations
│   ├── bn.json
│   ├── en.json
│   ├── hi.json
│   ├── kn.json
│   ├── ta.json
│   └── te.json
└── README.md
```

## How to Run

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/folk-studio.git
    cd folk-studio
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure the Groq API key (optional):**

    Open `config/config.py` and replace `"YOUR_GROQ_API_KEY"` with your actual Groq API key.

4.  **Run the app:**

    ```bash
    streamlit run app.py
    ```

## Deployment on Hugging Face Spaces

This app is designed to be deployed on Hugging Face Spaces using the Streamlit template.

1.  Create a new Space on Hugging Face.
2.  Select the "Streamlit" template.
3.  Link your GitHub repository.
4.  The app will be automatically deployed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
