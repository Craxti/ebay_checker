import os

DELETE_FILES: str = "{__pycache__, parser/__pycache__, logs.log}"


os.system(f"sudo rm -rf {DELETE_FILES}")
print("cleared!")
