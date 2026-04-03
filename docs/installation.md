# <img src="../assets/icons/server-solid.png" width="30" /> Installation Guide

<p>
  <img src="https://img.shields.io/badge/Setup-Installation-orange" />
  <img src="https://img.shields.io/badge/Platform-Python-blue" />
  <img src="https://img.shields.io/badge/Status-Supported-green" />
</p>

Follow the steps below to install and run **HostPilot** on your system.

Ensure that Python and required dependencies are available before proceeding.

---

# <img src="../assets/icons/file-solid.png" width="26" /> Step 1 — Clone Repository

Download the HostPilot repository from GitHub.

```
git clone https://github.com/ranjanarnav/HostPilot.git
cd HostPilot
```

This will create a local project directory on your system.

---

# <img src="../assets/icons/gear-solid.png" width="26" /> Step 2 — Install Dependencies

Install all required Python packages using the requirements file.

```
pip install -r requirements.txt
```

Make sure Python **3.9 or higher** is installed before running this command.

---

# <img src="../assets/icons/file-solid.png" width="26" /> Step 3 — Create .env File

Create a `.env` file using the provided template.

```
cp .env.example .env
```

After creating the file, open `.env` and configure the required values.

You must add:

* Discord Bot Token
* Pterodactyl API Key
* Required channel and role IDs
* Panel configuration settings

Refer to the **Configuration Guide** for full details.

---

# <img src="../assets/icons/server-solid.png" width="26" /> Step 4 — Run HostPilot

Start the bot using Python.

```
python bot.py
```

If the configuration is correct, the bot will connect to Discord and begin listening for commands.

---

# <img src="../assets/icons/shield-solid.png" width="26" /> Installation Notes

<p>
  <img src="https://img.shields.io/badge/Python-3.9+-blue" />
  <img src="https://img.shields.io/badge/Internet-Required-orange" />
  <img src="https://img.shields.io/badge/Configuration-Required-red" />
</p>

Before running the bot:

* Ensure Python version **3.9 or higher** is installed
* Verify all dependencies installed successfully
* Confirm `.env` file contains valid credentials
* Ensure network access is available
* Validate Pterodactyl panel connectivity

---

# <img src="../assets/icons/server-solid.png" width="26" /> Expected Result

After successful installation:

* Bot connects to Discord
* Commands become available
* API communication initializes
* Logs appear in configured channels

If issues occur, refer to the **Troubleshooting Guide**.

---
