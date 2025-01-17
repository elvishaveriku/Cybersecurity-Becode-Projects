# System Monitoring and Notification Tool

## Overview
This Bash script is designed to monitor the performance and health of a Linux server. It displays system metrics and service statuses on a dynamic terminal-based dashboard and sends email notifications for critical resource thresholds. The script logs all output into a dated CSV file for reference and troubleshooting.

---

## Features

1. **Dynamic Dashboard Display**  
   - The script draws a real-time terminal-based dashboard showing key metrics and statuses.
   - Updates occur every 2 seconds for fresh information.

2. **System Metrics Monitoring**  
   - **CPU Usage:** Monitors real-time CPU usage percentage.
   - **Memory Usage:** Tracks memory usage as a percentage of total memory.
   - **Disk Space Usage:** Displays disk usage as a percentage of the root partition.
   - **Network Traffic:** Shows received (Rx) and transmitted (Tx) traffic in kilobytes per second.

3. **System Information Display**  
   - Displays key system information, including:
     - Date and time
     - Hostname
     - Kernel version
     - System uptime
     - Public and private IP addresses
     - Logged-in users

4. **Service Status Monitoring**  
   - Checks and displays the status (`Running` or `Stopped`) of critical services:
     - DHCP server (`isc-dhcp-server`)
     - DNS server (`bind9`)
     - Nginx web server (`nginx`)

5. **Process Monitoring**  
   - Displays the top 5 CPU-consuming processes.
   - Displays the top 5 memory-consuming processes.
   - Limits command names to 44 characters to maintain a neat display.

6. **Critical Alerts and Notifications**  
   - Sets thresholds for CPU, memory, and disk usage (default: 90%).
   - Sends email alerts to a specified address if any resource crosses its threshold.

7. **Logging**  
   - Logs all outputs to a file in the directory `/home/elvis/mytool_logs`.
   - The log file is named with a timestamp for easy identification.

---

## How It Works

### **1. Initialization**
- The script ensures the log directory exists and sets the log file name based on the current timestamp.
- Redirects all script output (stdout and stderr) to the log file using `exec`.

### **2. Dashboard Setup**
- Defines a function `draw_board` to set up the terminal-based dashboard layout.
- Uses ANSI escape codes for colored text to differentiate metrics visually.

### **3. Real-Time Metrics Update**
- Fetches and calculates metrics for:
  - **CPU usage:** From the `top` command.
  - **Memory usage:** From the `free` command.
  - **Disk usage:** From the `df` command.
  - **Network traffic:** From `netstat` for interface `enp0s3` (modifiable for other interfaces).
- Updates system information (e.g., hostname, kernel version) using Linux utilities like `hostname`, `uname`, and `uptime`.

### **4. Service Monitoring**
- Uses `systemctl` to check the status of specified services.
- Displays `Running` in green for active services and `Stopped` in red for inactive services.

### **5. Process Monitoring**
- Extracts top CPU and memory-consuming processes using `ps aux`, sorting by CPU and memory usage, respectively.
- Formats and displays the output within the dashboard.

### **6. Critical Threshold Monitoring**
- Compares current CPU, memory, and disk usage against predefined thresholds.
- If any threshold is exceeded, an email notification is sent using the `mail` command.

### **7. Continuous Updates**
- Runs an infinite loop to refresh metrics every 2 seconds.

---

## Dependencies

### **1. System Utilities**
The script relies on the following Linux utilities:
- `bash`: For scripting
- `top`, `ps`, `df`, `free`: For fetching metrics
- `tput`: For cursor positioning and updating specific dashboard sections
- `systemctl`: For checking service statuses
- `curl`: For fetching the public IP address
- `mail`: For sending email notifications
- `awk`, `sed`, `bc`: For text processing and calculations

### **2. Email Configuration**
- Ensure the `mail` utility is configured and operational on the server.
- Replace the email address (`test@gmail.com`) with the desired recipient for alerts.

---

## Customization

- **Interface:** Modify `enp0s3` in the `netstat` and `ip` commands to match the network interface of your system.
- **Thresholds:** Adjust `CPU_THRESHOLD`, `MEM_THRESHOLD`, and `DISK_THRESHOLD` to set different alert levels.
- **Log Directory:** Change the `LOG_DIR` variable to store logs in a different location.
- **Monitored Services:** Add or remove services in the `check_service_status` calls to monitor additional system services.

---

## Usage

1. **Save the Script**: Save the script as a file (e.g., `monitor.sh`).
2. **Make it Executable**: Run `chmod +x monitor.sh` to make the script executable.
3. **Run the Script**: Execute the script with `./monitor.sh`.

---

## Example Output
- Dashboard displaying real-time metrics, system information, service statuses, and top processes.
- Email alerts when critical resource thresholds are exceeded.
- Log files in `/home/elvis/mytool_logs` for reference.

This script is a robust tool for server monitoring and can be easily extended to include additional metrics or functionalities.

