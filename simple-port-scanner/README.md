# 🔍 TCP Connect Port Scanner

A simple **TCP Connect Scan** tool built in Python.  
This scanner attempts to connect to specified ports on a target host and reports whether they are **open** or **closed**.  

---

## 🚀 Features
- TCP **connect() scan** (no raw sockets required)  
- Scan a **range of ports** or individual ports  
- **Multi-threaded** for faster scanning  
- Service name detection (`socket.getservbyport`)  
- Clean, formatted output  

---

## Working
- Uses Python’s built-in `socket` module  
- For each port:
  - Tries to complete a TCP 3-way handshake  
  - If successful → port is **OPEN**  
  - If refused/timeout → port is **CLOSED/FILTERED**
    
- This type of scan is slower and more detectable than SYN scans (like Nmap),  
  but is beginner-friendly and requires no root privileges.  
