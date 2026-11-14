import streamlit as st
from supabase import create_client

def get_supabase():
    """Create a per-session client. Keep the secret/service key server-side only."""
    url = st.secrets.get("SUPABASE_URL")
    key = st.secrets.get("SUPABASE_SECRET_KEY") or st.secrets.get("SUPABASE_KEY")
    if not url or not key:
        raise RuntimeError(
            "Supabase credentials missing. Add SUPABASE_URL and SUPABASE_SECRET_KEY "
            "to .streamlit/secrets.toml."
        )
    return create_client(url, key)
