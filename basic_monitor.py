import time
import psutil
import tkinter as tk
from requests import get   
import pynvml
def display_usage():
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    net_io_counters = psutil.net_io_counters()
    max_cpu = 100  # Maximum CPU usage value
    max_mem = 100  # Maximum Memory usage value
    max_gpu = 100

    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()
    gpu_usage = 0
    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
        gpu_usage += utilization.gpu
    pynvml.nvmlShutdown()
    cpu_percent = min(cpu_usage, max_cpu)
    mem_percent = min(mem_usage, max_mem)
    gpu_percent = min(gpu_usage, max_gpu)

    # Update the labels for CPU and Memory usage
    cpu_label.config(text=f"CPU Usage: {cpu_usage:.2f}%")
    mem_label.config(text=f"MEM Usage: {mem_usage:.2f}%")
    gpu_label.config(text=f"GPU Usage: {gpu_usage}%")

    # Update the bars and their outlines for CPU and Memory
    update_bar(cpu_canvas, cpu_percent, max_cpu)
    update_bar(mem_canvas, mem_percent, max_mem)
    update_bar(gpu_canvas, gpu_percent, max_gpu)

    # Update the labels for incoming and outgoing packets
    incoming_label.config(text=f"Incoming Packets: {net_io_counters.packets_recv}")
    outgoing_label.config(text=f"Outgoing Packets: {net_io_counters.packets_sent}")
    
    ip_addr = get('https://api.ipify.org').text
    ip_label.config(text=f"Your Ip address is: {ip_addr}")

    root.after(800, display_usage)

def update_bar(canvas, value, max_value):
    # Clear existing bars and outlines
    canvas.delete("bar")
    canvas.delete("outline")

    # Create an outline starting at 0% and ending at 100%
    canvas.create_rectangle(0, 0, 100, 20, outline="black", width=1, tags="outline")
    # Create a filled rectangle for the bar
    bar_width = min(value / max_value * 100, 100)
    canvas.create_rectangle(0, 0, bar_width, 20, fill="black", tags="bar")

root = tk.Tk()
root.title("Sticks Monitor")
root.geometry("400x300")  # Set the console size

# Create labels for CPU and Memory usage
cpu_label = tk.Label(root, text="", width=30)
mem_label = tk.Label(root, text="", width=30)
gpu_label = tk.Label(root, text="", width=30)

# Create canvas widgets for CPU and Memory bars
cpu_canvas = tk.Canvas(root, width=100, height=20)
mem_canvas = tk.Canvas(root, width=100, height=20)
gpu_canvas = tk.Canvas(root, width=100, height=20)

# Create labels for incoming and outgoing packets
incoming_label = tk.Label(root, text="", width=30)
outgoing_label = tk.Label(root, text="", width=30)

#creating labels for Ip
ip_label = tk.Label(root, text="", width=30)

# Pack widgets
cpu_label.pack()
cpu_canvas.pack()
mem_label.pack()
mem_canvas.pack()
gpu_label.pack()
gpu_canvas.pack()
incoming_label.pack()
outgoing_label.pack()
ip_label.pack()

root.after(800, display_usage)
root.mainloop()
