<div align="center">
  <br />
  <img src="assets/logo.png" alt="mshLogo" width="30%"/>
  <h1>myshell</h1>
  <p>
    A CLI tool to manage and distribute custom scripts and use them in your daily work.
  </p>
</div>

<!-- Badges -->
<div align="center">
   <a href="https://github.com/cophilot/msh/releases">
       <img src="https://img.shields.io/github/v/release/cophilot/msh?display_name=tag" alt="current realease" />
   </a>
   <a href="https://github.com/cophilot/msh/actions/workflows/ci.yml">
       <img src="https://github.com/cophilot/msh/actions/workflows/ci.yml/badge.svg" alt="CI" />
   </a>
   <a href="https://github.com/cophilot/msh/blob/master/LICENSE">
       <img src="https://img.shields.io/github/license/cophilot/msh" alt="license" />
   </a>
   <a href="https://github.com/cophilot/msh/stargazers">
       <img src="https://img.shields.io/github/stars/cophilot/msh" alt="stars" />
   </a>
   <a href="https://github.com/cophilot/msh/commits/master">
       <img src="https://img.shields.io/github/last-commit/cophilot/msh" alt="last commit" />
   </a>
</div>

---

**For a full guide please visit the [msh-docs](https://myshell.philipp-bonin.com/).**

---

-   [Concept](#concept)
-   [Installation](#installation)
-   [Update](#update)
-   [Uninstall](#uninstall)
-   [Development](#development)
-   [Extensions](#extensions)
-   [Release Notes](#release-notes)

---

## Concept

myshell is a CLI tool to manage and distribute custom scripts and use them in your daily work as native commands. It stores all scripts inside `~/.myshell` folder and adds this to the path. This way, you can use your scripts as native commands in your terminal. myhsell also enables easy git integration to share your scripts with others and sync them across multiple devices.

---

## Installation

Run the following command to install `msh`:

```bash
curl -s https://raw.githubusercontent.com/cophilot/msh/main/install | bash -s
```

---

## Update

Run the following command to update `msh`:

```bash
msh-update
```

---

## Uninstall

Run the following command to uninstall `msh`:

```bash
msh-uninstall
```

If the script is not found, you can manually run the script from `$MSH_HOME/bin/msh-uninstall`.

---

## Development

If you want to contribute to this project, you can find the development guide in the [msh-docs](https://myshell.philipp-bonin.com/development).

---

## Extensions

You can load predefined collections of scripts into your msh installation. This extension provide useful scripts for your daily work. To see all available extensions, visit the [msh-docs](https://myshell.philipp-bonin.com/extensions).

---

## [Release Notes](https://github.com/cophilot/msh/blob/master/CHANGELOG.md)

### [v1.1.1](https://github.com/cophilot/msh/milestone/7)

-   Added git status when running the `details` command [#33](https://github.com/cophilot/msh/issues/33)
-   Added `-interactive` flag for the `new` command [#35](https://github.com/cophilot/msh/issues/35)

---

by [Philipp B.](https://github.com/cophilot)
