import tkinter as tk
import keyboard
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL, CoInitialize, CoUninitialize
import threading
import pystray
from PIL import Image
import os
import sys
import socket
import time 

try:
    lock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lock_socket.bind(('127.0.0.1', 65432)) 
except socket.error:
    os._exit(0)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def get_mic_control():
    try:
        CoInitialize()
        devices = AudioUtilities.GetMicrophone()
        if not devices:
            return None
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        return volume
    except Exception as e:
        return None

def get_current_mic_name():
    """ดึงชื่อไมโครโฟนที่ถูกต้องโดยการเทียบ ID อุปกรณ์"""
    try:
        CoInitialize()
        default_mic = AudioUtilities.GetMicrophone()
        if not default_mic:
            return "No Microphone Found"
        
        default_mic_id = default_mic.GetId()
        
        all_devices = AudioUtilities.GetAllDevices()
        for device in all_devices:
            if device.id == default_mic_id:
                return device.FriendlyName
                
        return "Default Microphone"
    except Exception as e:
        return "Unknown Microphone"
    finally:
        CoUninitialize()

def update_status(is_muted):
    try:
        icon_file = "off.ico" if is_muted else "on.ico"
        icon_path = resource_path(icon_file)
        
        if os.path.exists(icon_path):
            new_icon = Image.open(icon_path)
        else:
            color = (231, 76, 60) if is_muted else (46, 204, 113)
            new_icon = Image.new('RGB', (64, 64), color=color)
            
        tray_icon.icon = new_icon

        bg_color = "#e74c3c" if is_muted else "#2ecc71"
        text = "Microphone OFF" if is_muted else "Microphone ON"
        status_label.config(text=text, bg=bg_color)
    except Exception as e:
        print(f"Update Status Error: {e}")

last_toggle_time = 0

def toggle_mic():
    global last_toggle_time
    current_time = time.time()
    
    if current_time - last_toggle_time < 0.3:
        return
    last_toggle_time = current_time

    volume = get_mic_control()
    if volume:
        try:
            new_mute = not volume.GetMute()
            volume.SetMute(new_mute, None)
            
            root.after(0, lambda: update_status(new_mute))
        except Exception as e:
            print(f"Toggle Error: {e}")
        finally:
            CoUninitialize()

def auto_refresh_mic_info():
    """ฟังก์ชันเช็คชื่อไมค์แบบ Real-time และอัปเดต UI ถ้ามีการเปลี่ยนแปลง"""
    try:
        current_name = get_current_mic_name()
        current_text = f"🎤 Mic: {current_name}"
        
        if mic_name_label.cget("text") != current_text:
            mic_name_label.config(text=current_text)
            
            vol = get_mic_control()
            if vol:
                update_status(vol.GetMute())
                CoUninitialize()
                
    except Exception as e:
        pass
    finally:
        root.after(2000, auto_refresh_mic_info)

def quit_window(icon, item):
    tray_icon.stop()
    root.after(0, root.destroy)
    os._exit(0)

def show_window(icon, item):
    root.after(0, root.deiconify)

def withdraw_window():
    root.withdraw()

root = tk.Tk()
root.title("Mic Control")
root.geometry("350x150")
root.attributes("-topmost", True)
root.protocol('WM_DELETE_WINDOW', withdraw_window)

status_label = tk.Label(root, text="READY", font=("Arial", 16, "bold"), fg="white", bg="#2ecc71")
status_label.pack(expand=True, fill="both")

info_frame = tk.Frame(root, bg="#2c3e50")
info_frame.pack(fill="x", side="bottom")

mic_name_label = tk.Label(info_frame, text="🎤 Mic: Loading...", font=("Arial", 9), fg="white", bg="#2c3e50", wraplength=330)
mic_name_label.pack(pady=(6, 2))

shortcut_label = tk.Label(info_frame, text="⌨️ Shortcut: Ctrl + Alt + M", font=("Arial", 10, "bold"), fg="#f1c40f", bg="#2c3e50")
shortcut_label.pack(pady=(0, 6))

try:
    start_icon_path = resource_path("on.ico")
    if os.path.exists(start_icon_path):
        image_on = Image.open(start_icon_path)
    else:
        image_on = Image.new('RGB', (64, 64), color=(46, 204, 113))
except:
    image_on = Image.new('RGB', (64, 64), color=(46, 204, 113))

menu = pystray.Menu(
    pystray.MenuItem('Show Window', show_window),
    pystray.MenuItem('Exit', quit_window)
)
tray_icon = pystray.Icon("MicControl", image_on, "Mic Control", menu)

def run_tray():
    tray_icon.run()

root.after(100, auto_refresh_mic_info)

keyboard.add_hotkey('ctrl+alt+m', toggle_mic)

threading.Thread(target=run_tray, daemon=True).start()

root.withdraw()
root.mainloop()