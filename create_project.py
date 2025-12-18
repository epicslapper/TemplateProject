from pathlib import Path

# Use current directory as the project folder
project_dir = Path(".").resolve()

files = {
    ".gitignore": ".venv/\n__pycache__/\n.idea/\n.DS_Store\n.env\n",
    "main.py": """import streamlit as st
from pathlib import Path

st.title("Hello World 🎈")
st.subheader("Repository Structure")

def tree(path: Path, prefix=""):
    result = ""
    for p in sorted(path.iterdir()):
        if p.name.startswith(".") and p.name != ".gitignore":
            continue
        result += prefix + p.name + "\\n"
        if p.is_dir():
            result += tree(p, prefix + "  ")
    return result

st.text(tree(Path(".")))""",
    "requirements.txt": "streamlit\n",
    "runtime.txt": "python-3.13\n",
    "readme.md": f"# {project_dir.name}\nStreamlit project template\n"
}

for name, content in files.items():
    path = project_dir / name
    path.write_text(content)

print(f"Project '{project_dir.name}' is now populated with template files! 🎉")
