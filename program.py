import os
import urllib.request
import subprocess

def download_file_with_progress(url, destination):
    def reporthook(block_num, block_size, total_size):
        downloaded = block_num * block_size
        if total_size > 0:
            percent = int((downloaded / total_size) * 100)
            print(f"\rDownloading: {percent}%", end='', flush=True)
        else:
            print("\rDownloading...", end='', flush=True)

    urllib.request.urlretrieve(url, destination, reporthook=reporthook)
    print("\nDownload complete.")

def install_program(installer_path):
    cmd = f"{installer_path} batch.exe /S"
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    # Create a dictionary with program names as keys and URLs as values
    programs = {
        'codeblocks': 'https://sourceforge.net/projects/codeblocks/files/Binaries/20.03/Windows/codeblocks-20.03mingw-setup.exe',
        'obs': 'https://cdn-fastly.obsproject.com/downloads/OBS-Studio-30.0-Full-Installer-x64.exe'
        # Add more programs if needed
    }

    for program_name, url in programs.items():
        installer_path = f"{program_name}.exe"

        if not os.path.exists(installer_path):
            print(f"Downloading {program_name}...")
            download_file_with_progress(url, installer_path)
        else:
            print(f"{program_name} already exists. Skipping download.")

        install_program(installer_path)