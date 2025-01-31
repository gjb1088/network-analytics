import sys
import matplotlib.pyplot as plt

# Input values from arguments
latency = float(sys.argv[1]) if sys.argv[1] != "N/A" else None
download_speed = float(sys.argv[2]) if sys.argv[2] != "N/A" else None

# Define home averages for comparison
home_latency_avg = 25  # in ms
home_download_avg = 50  # in Mbps

# Generate Latency Line Graph
if latency:
    plt.figure(figsize=(6, 4))
    plt.plot(["Current"], [latency], marker="o", label="Your Latency", color="blue")
    plt.axhline(y=home_latency_avg, color="red", linestyle="--", label="Home Avg (25 ms)")
    plt.title("Network Latency (Your Performance vs. Home Avg)", fontsize=14)
    plt.ylabel("Milliseconds (ms)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig("/tmp/latency_line_graph.png", bbox_inches="tight", dpi=150)
    plt.close()

# Generate Download Speed Line Graph
if download_speed:
    plt.figure(figsize=(6, 4))
    plt.plot(["Current"], [download_speed], marker="o", label="Your Speed", color="green")
    plt.axhline(y=home_download_avg, color="red", linestyle="--", label="Home Avg (50 Mbps)")
    plt.title("Download Speed (Your Performance vs. Home Avg)", fontsize=14)
    plt.ylabel("Speed (Mbps)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig("/tmp/download_speed_line_graph.png", bbox_inches="tight", dpi=150)
    plt.close()
