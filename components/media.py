import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import numpy as np
from pydub import AudioSegment
import io

def audio_recorder_component():
    """A component to record audio from the user's microphone."""
    webrtc_ctx = webrtc_streamer(
        key="audio-recorder",
        mode=WebRtcMode.SENDONLY,
        audio_receiver_size=1024,
        media_stream_constraints={"video": False, "audio": True},
    )

    if not webrtc_ctx.state.playing:
        return None

    if webrtc_ctx.audio_receiver:
        audio_frames = []
        while True:
            try:
                audio_frame = webrtc_ctx.audio_receiver.get_frame(timeout=1)
                audio_frames.append(audio_frame)
            except Exception as e:
                break

        if not audio_frames:
            return None

        sound_chunk = AudioSegment.empty()
        for audio_frame in audio_frames:
            sound = AudioSegment(
                data=audio_frame.to_ndarray().tobytes(),
                sample_width=audio_frame.format.bytes_per_sample,
                frame_rate=audio_frame.sample_rate,
                channels=len(audio_frame.layout.channels),
            )
            sound_chunk += sound

        if len(sound_chunk) > 0:
            buffer = io.BytesIO()
            sound_chunk.export(buffer, format="wav")
            buffer.seek(0)
            return buffer
    return None

def show_media_page(translations):
    st.subheader(translations["record_audio"])

    audio_buffer = audio_recorder_component()

    if audio_buffer is not None:
        st.audio(audio_buffer, format='audio/wav')
        return audio_buffer

    st.subheader(translations["upload_audio"])
    uploaded_file = st.file_uploader(
        "Upload a WAV, MP3, or M4A file",
        type=["wav", "mp3", "m4a"]
    )

    return uploaded_file
