import os
import pandas as pd
from datetime import datetime
from config.config import RECORDINGS_DIR, METADATA_FILE

def save_audio_file(uploaded_file):
    if not os.path.exists(RECORDINGS_DIR):
        os.makedirs(RECORDINGS_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{uploaded_file.name}"
    filepath = os.path.join(RECORDINGS_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return filepath, filename

def save_metadata(metadata):
    if not os.path.exists(METADATA_FILE):
        df = pd.DataFrame(columns=metadata.keys())
        df.to_csv(METADATA_FILE, index=False)

    df = pd.read_csv(METADATA_FILE)
    df = df.append(metadata, ignore_index=True)
    df.to_csv(METADATA_FILE, index=False)
