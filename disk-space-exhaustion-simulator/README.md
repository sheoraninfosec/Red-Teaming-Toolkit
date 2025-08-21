# 💾 Disk Space Exhaustion Simulator

A **Red Team simulation script** (PowerShell) that demonstrates the impact of **disk space exhaustion** — a form of resource exhaustion attack — on NTFS volumes.  

> ⚡ **Use Case:** Designed for **academic research** and **controlled red/blue team labs** only.  

---

## ⚠️ Disclaimer
> 🚨 **Warning:** Running this script will deliberately consume disk space until exhaustion.  

- **DO NOT** execute on your personal or production machine.  
- Use **only inside disposable lab environments or VMs**.  
- The author/maintainer assumes **no liability** for misuse.  
- Purpose is **strictly educational and defensive research**.  

---

## 🎯 Objectives
This simulator helps in understanding **how resource exhaustion impacts systems** and how defenders can detect/respond.  

✔️ Demonstrates:
- Attacker behavior: uncontrolled file creation and storage flooding.  
- Defender observables:
  - 📂 Unusual file creation activity
  - 📉 Sudden drop in available disk space
  - 📝 Windows Event Logs / Sysmon alerts
  - 🔒 Permission tampering & hidden files  

---

## 🔧 Requirements:

  - 🖥 **Windows environment** (tested on Windows 10/11 with PowerShell)  
  - 💽 NTFS-formatted volume(s)  
  - 🔑 Administrator privileges (for permission modification steps)  

  - Take a **snapshot before execution** for easy rollback  
