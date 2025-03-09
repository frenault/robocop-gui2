import subprocess
import threading
import os
import json

CONFIG_FILE = "config.txt"
process = None

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def start_robocopy(source, destination, log_text, progress_var):
    global process
    command = f'robocopy "{source}" "{destination}" /TEE /NP /LOG+:.robocopy.log'
    log_text.insert("end", f"Executing: {command}\n", "info")
    progress_var.set(0)
    
    def run():
        global process
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)
        for line in iter(process.stdout.readline, ""):
            log_text.insert("end", line)
            log_text.yview("end")
            update_progress(line, progress_var)
        process.stdout.close()
        process.wait()
        process = None
        load_file_list(log_text)
    
    thread = threading.Thread(target=run)
    thread.start()

def stop_robocopy(log_text):
    global process
    if process:
        process.terminate()
        log_text.insert("end", "Process stopped!\n", "error")
        process = None

def update_progress(line, progress_var):
    if "Percent" in line:
        parts = line.split()
        for part in parts:
            if part.endswith("%") and part[:-1].isdigit():
                progress_var.set(int(part[:-1]))
                break

def load_file_list(log_text):
    if os.path.exists(".robocopy.log"):
        with open(".robocopy.log", "r") as f:
            for line in f:
                if any(ext in line for ext in [".txt", ".jpg", ".png", ".pdf", ".docx", ".xlsx"]):
                    log_text.insert("end", line)

def save_settings(source, destination):
    config = {
        "source": source,
        "destination": destination
    }
    save_config(config)
