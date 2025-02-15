from os import path
import subprocess

def format_markdown(file_path: str, prettier_version: str):
    abs_path = path.abspath(file_path)
    subprocess.run(f"npx prettier@{prettier_version} {abs_path} --write --parser markdown", shell=True, check=True)
    # TODO - Check if the file is formatted using the prettier_version