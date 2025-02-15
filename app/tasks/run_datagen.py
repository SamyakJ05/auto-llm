import subprocess

def run_datagen(email: str):
    try:
        subprocess.run(["uv", "--version"], check=True)
    except subprocess.CalledProcessError:
        subprocess.run(["pip", "install", "uv"], check=True)

    url = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"
    subprocess.run(f"uv run {url} {email}", check=True)
