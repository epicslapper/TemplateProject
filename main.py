import streamlit as st
from pathlib import Path

st.title("Hello World 🎈")
st.subheader("Repository Structure")

def tree(path: Path, prefix=""):
    result = ""
    for p in sorted(path.iterdir()):
        if p.name.startswith(".") and p.name != ".gitignore":
            continue
        result += prefix + p.name + "\n"
        if p.is_dir():
            result += tree(p, prefix + "  ")
    return result

st.text(tree(Path(".")))