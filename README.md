# Telegram Controlled Home Automation System

This project allows you to control home appliances using a Telegram bot and a Raspberry Pi. It was developed as part of a final year project at Government Polytechnic for Girls, Surat.

## 💡 Overview
The system enables users to send commands via the Telegram app to switch devices (LED, fan, bulb, tubelight) ON or OFF. It leverages the Raspberry Pi GPIO pins and Python scripting to interface with a relay module controlling the appliances.

## ✨ Features
- Control multiple household devices from anywhere via the internet.
- Use a simple Telegram chat interface.
- Accessible for people with disabilities.
- Modular and extensible design for adding more devices.
- Reduces energy waste by allowing remote shutdown.

## 🛠️ Hardware Requirements
- Raspberry Pi 3 Model B+
- MicroSD card (with Raspberry Pi OS installed)
- 4-Channel Relay Module
- Jumper Wires
- HDMI display (monitor or TV)
- USB Mouse & Keyboard
- 5V/2.5A power supply

## 💻 Software Requirements
- Python 3
- Telegram account & bot token
- Required Python libraries:
  - `RPi.GPIO`
  - `telepot`

## 📝 Installation & Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/kmeriya-123/Telegram-Home-Automation.git
   cd Telegram-Home-Automation
