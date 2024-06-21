# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)[^1].

<!---
Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

-->

## [Unreleased]

## [1.0.11] - 2024-06-20

### Fixed

* All version specifiers of [PEP 440](https://peps.python.org/pep-0440/#version-specifiers) can be used for extensions.

## [1.0.10] - 2024-05-31

### Added

* Handle specific version number for extensions from pypi.

## [1.0.9] - 2024-05-22

### Added

* MacOS support to manage installation and execution of Libreflow instances

## [1.0.8] - 2024-05-16

### Added

* Support project environment variables
* Issue #9
  * Indentation on user settings json files
* Issue #15
  * If the login is an email address, only the username part is kept.

## [1.0.7] - 2024-05-15

### Fixed

* Issue #11
  * Added a exception for `HTTPError` and `RequestException` to avoid crashes when connection or authentification error has occured.
  * Handle recent changes of Overseer API error codes for user token.
  * Current user cache is now cleared when user token is invalid or expired.
* Issue #7
  * Current user is now properly setted when user settings folder do not exist.
* Issue #14
  * Append libreflow extensions with the correct pattern in the environment variable.

* Connection status to a server is updated when hovering a server.

## [1.0.6] - 2024-05-07

### Added

* Shell script to start a Libreflow instance on Linux.

## [1.0.5] - 2024-04-29

### Fixed

* Site name is now correctly defined on libreflow starting script (`bat` or `sh` file)
* Install dir is now correctly used for installing libreflow instance

## [1.0.4] - 2024-04-29

### Added

* An environment variable `LF_LAUNCHER_POETRY_PATH` can be used to define a specific path for poetry.

## [1.0.3] - 2024-04-29

### Fixed

* Host address for a server can now be a domain name instead of a direct IP address.
  * The default port is `5500` if you don't specify it in the wizard.

## [1.0.0-1.0.2] - 2024-04-25

Initial public commit and pypi setup. This is an early version of Libreflow Launcher.
It includes management of Overseer servers, access to projects (instances of Libreflow) that have been assigned to the user, and can be installed locally on the machine by Poetry.

The user interface is likely to change in the future.