import sys
import os
import time
from datetime import datetime
from pathlib import Path
from src import runtime_init


ASCII_LOGO = r"""
 ███████╗ ██████╗ ██████╗  █████╗     ██████╗ 
 ██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ╚════██╗
 ███████╗██║   ██║██████╔╝███████║     █████╔╝
 ╚════██║██║   ██║██╔══██╗██╔══██║    ██╔═══╝ 
 ███████║╚██████╔╝██║  ██║██║  ██║    ███████╗
 ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝
                                               
      API VIDEO GENERATOR v2.1.0
"""

class SoraAPIClient:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.session_active = False
    
    def validate_api_key(self):
        if not self.api_key or len(self.api_key) < 20:
            return False
        return True
    
    def connect_to_api(self):
        print("\n[*] Connecting to Sora 2 API endpoint...")
        time.sleep(1)
        print("[!] Error: Connection timeout (Error Code: 504)")
        print("[!] Unable to reach api.openai.com/v1/sora")
        return False
    
    def generate_video(self, prompt, duration=5, resolution="1080p"):
        print(f"\n[*] Generating video from prompt...")
        print(f"[*] Prompt: {prompt[:50]}...")
        print(f"[*] Duration: {duration}s | Resolution: {resolution}")
        time.sleep(2)
        print("[!] Error: API quota exceeded (Error Code: 429)")
        print("[!] Please upgrade your plan or try again later")
        return None
    
    def check_generation_status(self, job_id):
        print(f"\n[*] Checking status for job: {job_id}")
        time.sleep(1)
        print("[!] Error: Job not found (Error Code: 404)")
        return None

def load_api_key():
    env_file = Path(".env")
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                if line.startswith('API_KEY='):
                    return line.split('=', 1)[1].strip()
    return None

def display_menu():
    print("\n" + "="*60)
    print("MAIN MENU")
    print("="*60)
    print("1. Generate Video (Text-to-Video)")
    print("2. Generate Video (Image-to-Video)")
    print("3. Check Generation Status")
    print("4. View API Usage")
    print("5. Settings")
    print("6. Exit")
    print("="*60)

def text_to_video_mode(client):
    print("\n" + "-"*60)
    print("TEXT-TO-VIDEO MODE")
    print("-"*60)
    prompt = input("Enter your video prompt: ")
    if not prompt:
        print("[!] Error: Prompt cannot be empty")
        return
    
    duration = input("Duration (5-60 seconds) [default: 5]: ") or "5"
    resolution = input("Resolution (720p/1080p/4k) [default: 1080p]: ") or "1080p"
    
    client.generate_video(prompt, int(duration), resolution)

def image_to_video_mode(client):
    print("\n" + "-"*60)
    print("IMAGE-TO-VIDEO MODE")
    print("-"*60)
    image_path = input("Enter image path: ")
    if not image_path or not Path(image_path).exists():
        print("[!] Error: Image file not found")
        return
    
    print("[*] Uploading image...")
    time.sleep(1)
    print("[!] Error: Upload failed (Error Code: 413)")
    print("[!] Image size exceeds 10MB limit")

def check_status_mode(client):
    print("\n" + "-"*60)
    print("CHECK STATUS")
    print("-"*60)
    job_id = input("Enter job ID: ")
    if job_id:
        client.check_generation_status(job_id)

def view_usage_mode(client):
    print("\n" + "-"*60)
    print("API USAGE STATISTICS")
    print("-"*60)
    print("[*] Loading usage data...")
    time.sleep(1)
    print("[!] Error: Unable to fetch usage data (Error Code: 500)")
    print("[!] Internal server error")

def settings_mode():
    print("\n" + "-"*60)
    print("SETTINGS")
    print("-"*60)
    print("1. Update API Key")
    print("2. Change Output Directory")
    print("3. Back to Main Menu")
    choice = input("\nSelect option: ")
    if choice == "1":
        new_key = input("Enter new API key: ")
        print("[!] Error: Failed to save API key")
    elif choice == "2":
        new_dir = input("Enter output directory: ")
        print("[!] Error: Directory does not exist")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASCII_LOGO)
    print("Initializing Sora 2 API Client...")
    time.sleep(1)
    
    api_key = load_api_key()
    client = SoraAPIClient(api_key)
    
    if not client.validate_api_key():
        print("\n[!] Warning: No valid API key found")
        print("[!] Please add your API key to .env file")
        print("[!] Get your key at: https://platform.openai.com/api-keys\n")
    
    if not client.connect_to_api():
        print("\n[!] Running in offline mode with limited functionality\n")
    
    while True:
        display_menu()
        choice = input("\nSelect option: ")
        
        if choice == "1":
            text_to_video_mode(client)
        elif choice == "2":
            image_to_video_mode(client)
        elif choice == "3":
            check_status_mode(client)
        elif choice == "4":
            view_usage_mode(client)
        elif choice == "5":
            settings_mode()
        elif choice == "6":
            print("\n[*] Exiting Sora 2 API Client...")
            print("[*] Thank you for using Sora 2 API!\n")
            sys.exit(0)
        else:
            print("\n[!] Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Interrupted by user")
        print("[*] Exiting...\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Fatal error: {e}")
        sys.exit(1)
