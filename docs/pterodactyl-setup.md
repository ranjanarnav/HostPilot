# <img src="../assets/icons/server-solid.png" width="30" /> Pterodactyl Setup Guide

<p>
  <img src="https://img.shields.io/badge/Integration-Pterodactyl-orange" />
  <img src="https://img.shields.io/badge/API-Required-blue" />
  <img src="https://img.shields.io/badge/Connection-Supported-green" />
</p>

HostPilot connects to your **Pterodactyl panel** using secure API credentials.

This guide explains how to generate an API key and configure it properly.

---

# <img src="../assets/icons/file-solid.png" width="26" /> Step 1 — Login to Panel

Open your Pterodactyl panel in your web browser.

Example:

```
https://your-panel-url
```

Use your panel credentials to log in.

Ensure you have permission to create API keys.

---

# <img src="../assets/icons/gear-solid.png" width="26" /> Step 2 — Generate API Key

Navigate to the API credentials section inside your account.

Follow this path:

```
Account → API Credentials → Create New Key
```

After creating the key:

* Copy the generated API key
* Store it securely
* Do not share it publicly

---

# <img src="../assets/icons/shield-solid.png" width="26" /> Step 3 — Add API Key to .env

Open your `.env` file and add the following entry:

```
PTERO_API_KEY=your_api_key_here
```

Also ensure the panel URL is configured:

```
PTERO_PANEL_URL=https://your-panel-url
```

These values are required for API communication.

---

# <img src="../assets/icons/server-solid.png" width="26" /> Step 4 — Test Connection

After configuring the API key:

Start the bot:

```
python bot.py
```

Then run a server-related command inside Discord.

If configured correctly:

* Server information will be retrieved
* API connection will succeed
* No authentication errors will appear

---

# <img src="../assets/icons/shield-solid.png" width="26" /> Configuration Notes

<p>
  <img src="https://img.shields.io/badge/Security-Important-red" />
  <img src="https://img.shields.io/badge/API-Key_Required-blue" />
</p>

Before testing the connection:

* Verify panel URL is correct
* Confirm API key is valid
* Ensure API permissions are enabled
* Check internet connectivity
* Restart bot after updating `.env`

---

# <img src="../assets/icons/server-solid.png" width="26" /> Expected Result

After successful configuration:

* HostPilot connects to Pterodactyl
* Server commands function correctly
* Server data becomes accessible
* Infrastructure automation is enabled

If issues occur, refer to the **Troubleshooting Guide**.

---
