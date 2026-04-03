# <img src="../assets/icons/file-solid.png" width="28" /> Frequently Asked Questions (FAQ)

<p>
  <img src="https://img.shields.io/badge/Support-FAQ-orange" />
  <img src="https://img.shields.io/badge/Documentation-Helpful-blue" />
  <img src="https://img.shields.io/badge/Status-Active-green" />
</p>

This section answers common questions about HostPilot usage, configuration, and functionality.

---

# <img src="../assets/icons/server-solid.png" width="26" /> General Questions

## Does HostPilot support multiple servers?

Yes. HostPilot supports managing **multiple servers** through the Pterodactyl panel API.

You can create, monitor, and manage multiple server instances depending on your panel configuration and available resources.

---

## Can I customize commands?

Yes. All commands are **modular** and stored inside the `cogs/` directory.

You can:

* Modify existing commands
* Add new command modules
* Extend functionality without changing the core bot logic

This modular structure allows easy customization and scalability.

---

## Is HostPilot open-source?

Yes. HostPilot is designed to be **open-source**, extensible, and customizable.

Developers can:

* Modify the codebase
* Add new features
* Improve integrations
* Adapt the system for different hosting workflows

---

# <img src="../assets/icons/gear-solid.png" width="26" /> Development Questions

## Where are commands located?

All command modules are stored in:

```
cogs/
```

Each file inside this directory represents a functional module of the bot.

Example:

```
cogs/
│
├── money.py
├── ptero.py
├── status.py
├── utilities.py
```

---

## Can I add new features?

Yes. New features can be added by creating new modules inside the `cogs/` directory.

The modular architecture ensures that additional functionality can be integrated without affecting existing modules.

---

# <img src="../assets/icons/shield-solid.png" width="26" /> Support Notes

<p>
  <img src="https://img.shields.io/badge/Documentation-Regularly_Updated-blue" />
  <img src="https://img.shields.io/badge/Support-Community_Friendly-green" />
</p>

If you encounter issues:

* Review the documentation files
* Check configuration settings
* Verify API credentials
* Refer to troubleshooting guides

---
