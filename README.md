<!-- HEADER BANNER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=11111b&height=150&section=header&text=🎙️%20MIC%20CONTROL%20WINDOWS%20TOOL&fontSize=38&animation=twinkling&fontColor=89b4fa&width=100%" alt="Project Header" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OS-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white" />
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Library-Pycaw-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/UI-System_Tray-orange?style=for-the-badge" />
</p>

---

### 📝 รายละเอียดโปรเจกต์ (Project Overview)
**Mic-Control-Windows-Tool** เป็นแอปพลิเคชันยูทิลิตี้สำหรับระบบปฏิบัติการ Windows พัฒนาด้วยภาษา Python เพื่อช่วยให้ผู้ใช้สามารถจัดการ เลือก และควบคุมระดับเสียงหรือสถานะเปิด-ปิดของไมโครโฟน (Microphone Audio Endpoint) ได้อย่างรวดเร็วผ่านทาง **System Tray** โดยไม่ต้องเปิดหน้าต่าง Sound Settings ของ Windows ให้ยุ่งยาก ตัวระบบถูกออกแบบมาให้ทำงานแบบเบื้องหลัง (Background Process) กินทรัพยากรต่ำ และมีความเสถียรสูง ⚡

---

### ✨ ฟีเจอร์เด่น (Key Features)ำ
* 📥 **System Tray Integration:** ทำงานอยู่บนแถบงานระบบ (System Tray) พร้อมเมนูคลิกขวาที่สั่งการได้ทันที
* 🔒 **Single-Instance Locking:** มีระบบป้องกันการเปิดแอปพลิเคชันซ้ำซ้อน (Mutex/Single Instance Lock) เพื่อความปลอดภัยและประหยัดทรัพยากรเครื่อง
* 🎙️ **Pycaw Core Control:** ใช้ไลบรารีระดับล่าง (Low-level Core Audio) ในการจัดการและควบคุม Hardware Endpoint โดยตรง

---

### 🛠️ เทคโนโลยีและเทคนิคที่ใช้ (Architecture & Tech Stack)
* **Core Language:** Python 🐍
* **Audio Management:** `pycaw` (Python Core Audio Windows Library) สำหรับเชื่อมต่อกับ Windows Core Audio APIs
* **UI & Tray Interaction:** `pystray` และ `Pillow` สำหรับจัดการไอคอนและเมนูบน System Tray
* **Process Control:** เทคนิค Single-instance Implementation ป้องกันการรันแอปพลิเคชันทับซ้อนกัน
