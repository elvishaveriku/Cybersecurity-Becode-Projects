
# Library Server Project

This project sets up an Ubuntu-based library server to provide network services, web hosting, and backups for a local library. The server is configured as a VirtualBox virtual machine and provides DHCP, DNS, a local web page, and secure remote access through SSH.

## Project Overview

1. **Virtual Machines Setup**:
   - Ubuntu Server for services.
   - Ubuntu Workstation for testing and client use.
   - Both VMs use two network adapters:
     - **Adapter 1 (NAT)** for internet access.
     - **Adapter 2 (Internal Network)** for local network services.

2. **Services Configured**:
   - **DHCP**: Provides IP addresses for the local network.
   - **DNS**: Resolves internal domain names and forwards external queries.
   - **Web Server (Nginx)**: Hosts a local webpage for library access.
   - **Backup**: Weekly backup of configuration files for all services.
   - **SSH**: Enables remote management of the server.

---

## Step-by-Step Configuration

### 1. DHCP Server
- **Install DHCP**:
  ```bash
  sudo apt update && sudo apt install isc-dhcp-server
  ```
- **Configure DHCP Range**: Edited `/etc/dhcp/dhcpd.conf` to define the IP range and DNS options.
- **Set Network Interface**: Configured DHCP to listen only on the internal network interface.
- **Commands**:
  ```bash
  sudo systemctl restart isc-dhcp-server
  ```

### 2. DNS Server (BIND)
- **Install BIND**:
  ```bash
  sudo apt install bind9
  ```
- **Configure Forwarding**: Added external DNS servers (e.g., Google DNS) in `/etc/bind/named.conf.options`.
- **Set Up Internal Zone**: Created internal DNS zone (`example.local`) in `/etc/bind/named.conf.local` and defined internal hosts.
- **Test**:
  ```bash
  nslookup host1.example.local 192.168.56.1
  ```

### 3. Web Server (Nginx)
- **Install Nginx**:
  ```bash
  sudo apt install nginx -y
  ```
- **Create Webpage**: Added `index.html` with a welcome message in `/var/www/html`.
- **Test**: Accessed the web page at `http://192.168.56.1` from the workstation.

### 4. Weekly Backup
- **Backup Script**: Created `backup_configs.sh` to archive configuration files for DHCP, DNS, and Nginx.
- **Cron Job**: Scheduled weekly backups using cron.
  ```bash
  0 2 * * 0 /usr/local/bin/backup_configs.sh
  ```

### 5. SSH Configuration
- **Install OpenSSH**:
  ```bash
  sudo apt install openssh-server -y
  ```
- **Secure SSH**: Disabled root login and enabled SSH for remote management.
- **Test Remote Access**:
  ```bash
  ssh user@192.168.56.1
  ```

---

## Testing and Validation

After configuration, the following tests were performed to ensure proper functionality:
- **DHCP**: Workstation received an IP address from the server.
- **DNS**: Internal and external DNS resolution verified using `nslookup`.
- **Web Server**: Local webpage was accessible.
- **Backup**: Backup script created a compressed archive in `/backups`.
- **SSH**: Remote access to the server was successfully established.

## Requirements
- **VirtualBox**: For virtual machine management.
- **Ubuntu Server 24.04** and **Ubuntu Workstation**.
- **Packages**:
  - `isc-dhcp-server`
  - `bind9`
  - `nginx`
  - `openssh-server`

---

## Author
This project was completed by [Your Name] as part of a library server setup and configuration assignment.

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.
