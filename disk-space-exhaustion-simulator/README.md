# Disk Space Exhaustion Simulator

This is a **red team simulation script** written in PowerShell to demonstrate the impact of **disk space exhaustion (resource exhaustion attack)** on NTFS volumes.  
It is intended **only for academic research and controlled lab environments** as part of red team / blue team studies.

---

## ⚠️ Disclaimer
- This script can cause a system to run out of disk space.  
- **Do NOT run on production systems.**  
- Use **only in virtual machines** or disposable lab environments.  
- Author / maintainer is **not responsible** for any misuse.  
- Purpose is strictly **educational and defensive research.**

---

## 🎯 Purpose
- Demonstrates how attackers might attempt to exhaust storage resources.  
- Helps defenders observe:
  - File creation anomalies
  - Sudden disk usage spikes
  - Event log entries (Sysmon, Security, etc.)
  - Permission tampering and file hiding behavior
- Provides a basis for testing **detection and monitoring tools**.

---

## 🔧 Requirements
- Windows environment (tested on Windows 10/11 with PowerShell).  
- NTFS-formatted volumes.  
- Administrator privileges (required for some permission changes).  
- Lab setup (VMware, VirtualBox, Hyper-V, etc.).

---

## ▶️ Usage
1. Clone or download this repository.  
2. Navigate to the script folder:
   ```powershell
   cd red-teaming-toolkit/disk-space-exhaustion-simulator
