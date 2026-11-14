"""Speaker embedding adapter using Resemblyzer. Requires a clean WAV recording."""
import numpy as np

def extract_voice_embedding(audio_file):
    try:
        import soundfile as sf
        from resemblyzer import VoiceEncoder, preprocess_wav
        audio, sr=sf.read(audio_file)
        if audio.ndim>1: audio=audio.mean(axis=1)
        wav=preprocess_wav(audio,sr=sr)
        if len(wav)<16000: raise ValueError("Please provide at least one second of audio.")
        encoder=VoiceEncoder()
        return encoder.embed_utterance(wav).astype(float).tolist()
    except ImportError as e:
        raise RuntimeError("Voice recognition is optional. Install requirements-ml.txt.") from e

def compare_embeddings(a,b,threshold=0.75):
    if not a or not b: return False
    x=np.asarray(a,dtype=float); y=np.asarray(b,dtype=float)
    denom=np.linalg.norm(x)*np.linalg.norm(y)
    return bool(denom and np.dot(x,y)/denom >= threshold)
