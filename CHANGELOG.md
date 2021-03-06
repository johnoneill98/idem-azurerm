# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.2] - 2020-06-16

### Added

### Changed

### Fixed

- [#106](https://github.com/eitrtechnologies/idem-azurerm/pull/106) - Fix assignment of built-in policy definitions.

### Deprecated

### Removed

## [2.3.1] - 2020-06-16

### Added

- [#104](https://github.com/eitrtechnologies/idem-azurerm/pull/104) - Updated docs for Getting Started and VM
  Quickstart.

### Changed

### Fixed

- [#105](https://github.com/eitrtechnologies/idem-azurerm/pull/105) - Catch policy assignment exceptions properly.
- [#103](https://github.com/eitrtechnologies/idem-azurerm/pull/103) - Always return a dict on error in exec modules.
- [#102](https://github.com/eitrtechnologies/idem-azurerm/pull/102) - Fix updated language in state modules.

### Deprecated

### Removed

## [2.3.0] - 2020-06-09

### Added

- [#92](https://github.com/eitrtechnologies/idem-azurerm/pull/92) - Added CodeFactor tests.
- [#74](https://github.com/eitrtechnologies/idem-azurerm/pull/74) - Added contributing guide.

### Changed

- [#91](https://github.com/eitrtechnologies/idem-azurerm/pull/91) - Moved azurerm utils under the azurerm directory to
  keep all code in one spot on the hub.
- [#85](https://github.com/eitrtechnologies/idem-azurerm/pull/85) - Changed to use external dict-toolbox for detecting
  changes in dictionaries for states.

### Fixed

- [#98](https://github.com/eitrtechnologies/idem-azurerm/pull/98) - Fixed module docstrings in order to get better
  documentation from the autodoc process.
- [#95](https://github.com/eitrtechnologies/idem-azurerm/pull/95) - Fixed resource group "get" errors after the change
  in logic from #89.
- [#89](https://github.com/eitrtechnologies/idem-azurerm/pull/89) - Fixed unnecessary execution modules calls in the
  resource group states.
- [#86](https://github.com/eitrtechnologies/idem-azurerm/pull/86) - Fixed README documentation about credential usage.
- [#84](https://github.com/eitrtechnologies/idem-azurerm/pull/84) - Fixed decode of unicode characters in error.
  messages from msrestazure.

### Deprecated

### Removed

## [2.2.0] - 2020-05-27

### Added

- [#71](https://github.com/eitrtechnologies/idem-azurerm/pull/71) - Added acct support for exec modules.
- [#68](https://github.com/eitrtechnologies/idem-azurerm/pull/68) - Added basic module docs.
- [#62](https://github.com/eitrtechnologies/idem-azurerm/pull/62) - Added a model for integration tests.

### Changed

### Fixed

- [#76](https://github.com/eitrtechnologies/idem-azurerm/pull/76) - Pinned new idem version.
- [#75](https://github.com/eitrtechnologies/idem-azurerm/pull/75) - Cleaned up some references to legacy Salt code and
  added some transparent requisites to ensure proper ordering of deployment.

### Deprecated

### Removed

## [2.1.0] - 2020-05-14

### Added

- [#61](https://github.com/eitrtechnologies/idem-azurerm/pull/61) - Added pre-commit to enforce black formatting and
  ran black to reformat code
- [#60](https://github.com/eitrtechnologies/idem-azurerm/pull/60) - Added support for passing credentials through the
  [acct](https://gitlab.com/saltstack/pop/acct) plugin
- [#58](https://github.com/eitrtechnologies/idem-azurerm/pull/58) - Added code of conduct

### Changed

### Fixed

### Deprecated

### Removed

## [2.0.0] - 2020-05-04

### Added

- [#53](https://github.com/eitrtechnologies/idem-azurerm/pull/53) - Added virtual machine "cleanup"
  functionality similar to that present in salt-cloud.
- [#47](https://github.com/eitrtechnologies/idem-azurerm/pull/47) - Added virtual machine creation
  functionality to create feature parity with salt-cloud, plus more.
- [#35](https://github.com/eitrtechnologies/idem-azurerm/pull/35) - Added virtual machine extension execution
  and state modules.
- [#33](https://github.com/eitrtechnologies/idem-azurerm/pull/33) - Added PostgreSQL replica and location-based
  performance tier support.
- [#26](https://github.com/eitrtechnologies/idem-azurerm/pull/26) - Added PostgreSQL log files, virtual network
  rules, and server security alert policies operations.
- [#25](https://github.com/eitrtechnologies/idem-azurerm/pull/25) - Added initial PostgreSQL support for basic
  deployments.
- [#20](https://github.com/eitrtechnologies/idem-azurerm/pull/20) - Added execution and state modules for
  deploying keys to Key Vaults.
- [#19](https://github.com/eitrtechnologies/idem-azurerm/pull/19) - Added Management Group execution and state
  modules.
- [#13](https://github.com/eitrtechnologies/idem-azurerm/pull/13) - Added Log Analytics Workspace management
  execution and state modules.
- [#10](https://github.com/eitrtechnologies/idem-azurerm/pull/10) - Added encrypted disk functionality to
  virtual machines.
- [#9](https://github.com/eitrtechnologies/idem-azurerm/pull/9) - Added Redis execution and state modules for
  management of the hosted service in Azure.
- [#7](https://github.com/eitrtechnologies/idem-azurerm/pull/7) - Added execution and state modules for Key
  Vault management.
- [#6](https://github.com/eitrtechnologies/idem-azurerm/pull/6) - Added diagnostic setting and management lock
  state modules.
- [#5](https://github.com/eitrtechnologies/idem-azurerm/pull/5) - Added storage execution and state modules for
  storage account and storage container management.
- Added support for Azure Identity Provider credentials.

### Changed

- [#57](https://github.com/eitrtechnologies/idem-azurerm/pull/57) - Changed azurearm references and renamed to
  idem-azurerm to match pip
- [#29](https://github.com/eitrtechnologies/idem-azurerm/pull/29) - Added function aliases for list functions,
  changing the way they are referenced.

### Fixed

- [#42](https://github.com/eitrtechnologies/idem-azurerm/pull/42) - Fixed reference to salt modules for file
  handling in Policy modules.
- [#27](https://github.com/eitrtechnologies/idem-azurerm/pull/27) - Allowed keyword arguments for absent states
  in order to prevent throwing errors and more closely mirror the present states.

### Deprecated

### Removed

## [1.0.0] - 2019-11-14

### Added

- Initial release of execution and state modules from Salt along with some additional functionality ported from
  salt-cloud for virtual machines.

[2.3.2]: https://github.com/eitrtechnologies/idem-azurerm/compare/v2.3.1...v2.3.2
[2.3.1]: https://github.com/eitrtechnologies/idem-azurerm/compare/v2.3.0...v2.3.1
[2.3.0]: https://github.com/eitrtechnologies/idem-azurerm/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/eitrtechnologies/idem-azurerm/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/eitrtechnologies/idem-azurerm/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/eitrtechnologies/idem-azurerm/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/eitrtechnologies/idem-azurerm/releases/tag/v1.0.0
