# <img src="../assets/icons/server-solid.png" width="28" /> Architecture Overview

<p>
  <img src="https://img.shields.io/badge/Architecture-Modular-orange" />
  <img src="https://img.shields.io/badge/Design-Scalable-blue" />
  <img src="https://img.shields.io/badge/Pattern-API_Driven-lightgrey" />
</p>

HostPilot follows a **modular and scalable architecture** designed to separate responsibilities, simplify maintenance, and enable easy expansion of features.

---

# <img src="../assets/icons/gear-solid.png" width="26" /> Core Components

The system is structured around several core modules that define the main workflow.

```
bot.py        → Main entry point of the bot
config.py     → Loads environment and configuration settings
cogs/         → Contains command modules and functional components
```

Each component is designed to operate independently while maintaining seamless integration across the system.

---

# <img src="../assets/icons/server-solid.png" width="26" /> Workflow

The primary execution flow follows a structured communication path:

```
Discord → Bot Core → Command Cogs → Pterodactyl API → Server Actions
```

### Flow Description

* **Discord** — User sends command
* **Bot Core** — Receives and routes command
* **Cogs** — Processes logic and executes actions
* **Pterodactyl API** — Performs infrastructure operations
* **Server** — Executes requested tasks

---

# <img src="../assets/icons/shield-solid.png" width="26" /> Design Principles

The architecture is built around strong engineering principles to ensure long-term reliability.

### Modular Structure

Each feature is implemented as a separate module to simplify debugging and development.

### Separation of Concerns

Responsibilities are clearly divided between configuration, logic, and API communication.

### API-Based Communication

All infrastructure actions are handled through structured API requests.

### Scalable Command System

New commands can be added without modifying the existing core structure.

---

# <img src="../assets/icons/file-solid.png" width="26" /> Directory Role Overview

Below is a simplified view of how components are organized.

```
hostpilot/
│
├── bot.py              → Application entry point
├── config.py           → Configuration management
│
├── cogs/               → Feature modules
│   ├── money.py
│   ├── ptero.py
│   ├── status.py
│   ├── utilities.py
│   └── moderation.py
│
├── assets/             → Branding and icons
│
└── docs/               → Documentation files
```

---

# <img src="../assets/icons/server-solid.png" width="26" /> System Characteristics

<p>
  <img src="https://img.shields.io/badge/Maintainability-High-green" />
  <img src="https://img.shields.io/badge/Extensibility-High-blue" />
  <img src="https://img.shields.io/badge/Performance-Optimized-orange" />
</p>

HostPilot architecture ensures:

* Clean modular expansion
* Efficient command execution
* Secure API communication
* Maintainable long-term development

---
