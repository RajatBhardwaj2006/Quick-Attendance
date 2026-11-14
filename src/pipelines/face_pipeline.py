"""Face embedding adapter. Install requirements-ml.txt to enable face_recognition.

This module deliberately does not pretend to recognize a face when the ML dependency
or a usable face is missing. Store embeddings only after explicit student consent.
"""
import numpy as np

def extract_face_embedding(image_file):
    try:
        import face_recognition
        from PIL import Image
        image=Image.open(image_file).convert("RGB")
        arr=np.asarray(image)
        encodings=face_recognition.face_encodings(arr)
        if len(encodings)!=1:
            raise ValueError(f"Expected exactly one face; detected {len(encodings)}.")
        return encodings[0].astype(float).tolist()
    except ImportError as e:
        raise RuntimeError("Face recognition is optional. Install requirements-ml.txt and the platform dependencies.") from e

def compare_embeddings(a,b,tolerance=0.48):
    if not a or not b: return False
    import numpy as np
    return bool(np.linalg.norm(np.asarray(a,dtype=float)-np.asarray(b,dtype=float)) <= tolerance)
