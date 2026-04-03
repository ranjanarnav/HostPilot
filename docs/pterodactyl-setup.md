# 🖥️ Pterodactyl Setup Guide

HostPilot connects to your Pterodactyl panel using API keys.

---

## Step 1 — Login to Panel

Open your Pterodactyl panel URL.

Example:

```
https://your-panel-url
```

---

## Step 2 — Generate API Key

Go to:

Account → API Credentials → Create New Key  

Copy the API key.

---

## Step 3 — Add API Key to .env

```
PTERO_API_KEY=your_api_key_here  
```

---

## Step 4 — Test Connection

Run the bot and test a server command.

If configured correctly, server data will display.