# Windows Server AD Project Documentation

## Overview
This project involves deploying and configuring a secure Windows Server 2022 environment with Active Directory and essential server roles. 
The goal is to create a functional and secure system for user management and demonstrate its effectiveness to a client. 
Key users like Alice and Bob are integrated into the environment to showcase role-based access and security principles.
In this repository you will find a document with a walkthrough of all the configurations.

---

## Learning Objectives

- Install and configure Windows Server 2022.
- Set up and manage user accounts within Active Directory.
- Configure Active Directory for centralized user management.
- Apply granular permissions to users (e.g., Alice and Bob) based on security principles.
- Install and configure essential server roles:
  - Internet Information Services (IIS)
  - Domain Name System (DNS)
  - Dynamic Host Configuration Protocol (DHCP)

---

## Environment Setup

### **Resources**
- Virtualization Software: VirtualBox
- Required:
  - Windows Server 2022

### **Virtual Machines**
1. **Domain Controller VM:** Hosts Active Directory and essential roles (DNS, DHCP).
2. **Server VM:** Hosts IIS for specific applications.
3. **Client VMs:** Used for access and monitoring.

*Note: If resources are limited, you can use one server as the domain controller and one client machine.*

---

## Step-by-Step Guide

### **1. System Preparation**
- Set up VirtualBox and create VMs for the server and clients.
- Install Windows Server 2022 evaluation on the Server VM and Domain Controller VM.
- Configure basic settings (e.g., network, hostname).

---

### **2. Active Directory Setup**
- Promote the Domain Controller VM to a domain controller.
- Create a new Active Directory forest and domain structure.
- Configure DNS services on the Domain Controller VM.
- Organize user and group management by creating Organizational Units (OUs).
- Join the Server VM and Client VMs to the Active Directory domain.

---

### **3. User Management**
- Create user accounts in Active Directory:
  - **Alice:** Administrator role assigned to a dedicated OU.
  - **Bob:** Standard user with access to `/Users/Bob` folder, assigned to a specific OU.
- Use Group Policy Objects (GPOs) to configure user settings.
- Apply security principles to grant granular permissions based on roles.

---

### **4. Server Roles Configuration**

#### **4.1 IIS for Alice**
- Install and configure IIS on the Server VM for Alice's web application/service.
- Implement security best practices:
  - Secure permissions
  - Web Application Firewalls (WAFs)
  - Role-based access for Alice as an admin.
- Test the application and verify accessibility for authorized users.

#### **4.2 DNS**
- Verify DNS functionality in the Active Directory environment.
- Configure conditional forwarders or integrate with external DNS if necessary.

#### **4.3 DHCP**
- Install and configure DHCP for automatic IP assignment.
- Integrate DHCP with Active Directory for dynamic DNS updates.

---

### **5. Client-Side Access and Reporting**
- Connect Client VMs to the server using domain credentials (Alice and Bob).
- Test access levels:
  - Alice should have administrative privileges.
  - Bob should have limited access.

---

## Customization Options
- **Additional Users:** Create more users with varying access levels for further testing.
- **Roles and Services:** Include additional server roles as needed.

---

## Conclusion
This project demonstrates the deployment and management of a secure Windows Server environment with Active Directory. 
It highlights essential server roles and user management to ensure functionality in a realistic scenario.
