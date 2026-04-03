<p align="center">
  <img src="assets/banner.png" alt="HostPilot Banner" />
</p>

<p align="center">
  <img src="assets/logo.png" width="80" />
</p>

<h1 align="center">HostPilot</h1>

<p align="center">
  <b>An All-in-One Hosting Management Solution</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-stable-brightgreen" />
  <img src="https://img.shields.io/badge/version-v1.0.0-blue" />
  <img src="https://img.shields.io/badge/python-3.9+-yellow" />
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" />
  <img src="https://img.shields.io/github/stars/ranjanarnav/HostPilot?style=social" />
<img src="https://img.shields.io/github/forks/ranjanarnav/HostPilot?style=social" />
<img src="https://img.shields.io/github/issues/ranjanarnav/HostPilot" />
<img src="https://img.shields.io/github/last-commit/ranjanarnav/HostPilot" />
</p>

<p align="center">
  HostPilot is a powerful <b>Discord-based hosting management system</b> designed to automate server operations using the <b>Pterodactyl API</b>.
  It provides hosting providers with tools to manage servers, log transactions, automate tasks, and monitor infrastructure — all from Discord.
</p>

---


**HostPilot — An All-in-One Hosting Management Solution**

HostPilot is a powerful **Discord-based hosting management system** designed to automate server operations using the **Pterodactyl API**.
It provides hosting providers with tools to manage servers, log transactions, automate tasks, and monitor infrastructure — all from Discord.

---

## Features

### <img src="assets/icons/server-solid.png" width="18" /> Pterodactyl Server Control

* Create, manage, and monitor servers
* Server information retrieval
* Panel integration

---

### <img src="assets/icons/money-solid.png" width="18" /> Money Logging System

* Track transactions
* Log payments automatically
* Generate financial records

---

### <img src="assets/icons/shield-solid.png" width="18" /> Status Monitoring

* Custom server status tracking
* Hosting availability updates
* Real-time status display

---

### <img src="assets/icons/gear-solid.png" width="18" /> Automation System

* Scheduled reminders
* Automated tasks using APScheduler
* Time-based system execution

---

### <img src="assets/icons/file-solid.png" width="18" /> Report Generation

* Generate PDF reports
* Export structured logs
* Organized data tracking

---

### <img src="assets/icons/wallet-solid.png" width="18" /> Role-Based Access

* Permission-based command control
* Admin-only system features

---

## Tech Stack

| Technology      | Usage                     |
| --------------- | ------------------------- |
| Python          | Core programming language |
| discord.py      | Discord bot framework     |
| Pterodactyl API | Server management         |
| APScheduler     | Task scheduling           |
| ReportLab       | PDF generation            |
| Requests        | API communication         |
| python-dotenv   | Environment management    |
| QRCode          | QR generation             |

---

## Installation

### Clone the Repository

```
git clone https://github.com/ranjanarnav/HostPilot.git
cd HostPilot
```

---

### Install Dependencies

```
pip install -r requirements.txt
```

---

### Setup Environment Variables

Create a `.env` file:

```
DISCORD_TOKEN=your_discord_bot_token_here
PTERO_API_KEY=your_pterodactyl_api_key_here

ALLOWED_ROLE_ID=your_allowed_role_id_here
MONEY_LOG_CHANNEL_ID=your_money_log_channel_id_here
REPORT_CHANNEL_ID=your_report_channel_id_here

WEBSITE_LINK=your_website_link_here
PANEL_LINK=your_panel_link_here
BILLING_LINK=your_billing_link_here
DISCORD_INVITE=your_discord_invite_link_here
SUPPORT_LINK=your_support_link_here

PTERO_PANEL_URL=your_pterodactyl_panel_url_here
PTERO_ALLOCATION_ID=your_pterodactyl_allocation_id_here

TIMEZONE=your_timezone_here
```

---

### Run HostPilot

```
python bot.py
```

---

## Project Structure

```
hostpilot/
│   .env
│   bot.py
│   config.py
│   README.md
│   requirements.txt
│
├── assets/
│   └── icons/
│       file-solid.png
│       gear-solid.png
│       money-solid.png
│       server-solid.png
│       shield-solid.png
│       wallet-solid.png
│   └── logo.png
│
├── cogs/
│   branding.py
│   client.py
│   ed_report.py
│   info.py
│   moderation.py
│   money.py
│   ptero-manage.py
│   ptero.py
│   reminder.py
│   serverinfo.py
│   status.py
│   utilities.py
```

---

## Use Cases

HostPilot is ideal for:

* Hosting Providers
* Game Server Hosting Services
* Infrastructure Automation
* Discord-Based Management Systems
* Server Monitoring Workflows

---

## Security Notes

* Never expose `.env` files publicly
* Always rotate API keys if leaked
* Use role-based access control

---

## Requirements

* Python **3.9+**
* Discord Bot Token
* Pterodactyl Panel API Key
* Internet Access

---

## Planned Features

* Web Dashboard Integration
* Advanced Billing System
* Usage Analytics
* Backup Automation
* Multi-Server Support

---

## Version

v1.0.0 — Initial Release

---

## License

MIT License

---

## Author

**Arnav Ranjan**
Backend Systems • Cloud Infrastructure • Platform Engineering

---

## Credits

**Logo Credits:** Freepik — Flaticon
**Icon Credits:** Font Awesome

---

If you find this project useful, consider giving it a **star**.
