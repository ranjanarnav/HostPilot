# 🧠 Architecture Overview

HostPilot follows a modular architecture.

---

## Core Components

```
bot.py → Entry point  
config.py → Configuration loader  
cogs/ → Command modules  
```

---

## Workflow

Discord → Bot → Cogs → Pterodactyl API  

---

## Design Principles

- Modular structure  
- Separation of concerns  
- API-based communication  
- Scalable command system