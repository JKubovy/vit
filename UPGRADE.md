This file contains information relevant to upgrading VIT from one version to another. Breaking changes between major versions, and significant changes between release versions will be addressed.

*Note: for upgrade issues prior to VIT 1.3, please see the [legacy changelog](https://github.com/scottkosty/vit/blob/1.3/CHANGES)*.

# v2.0.0

Complete ground up rewrite in Python, feature-complete with VIT 1.x.

### New features:

 * Advanced tab completion
 * Per-column colorization with markers *(see [COLOR.md](COLOR.md))*
 * Intelligent sub-project indenting
 * Multiple/customizable themes *(see [CUSTOMIZE.md](CUSTOMIZE.md))*
 * Override/customize column formatters *(see [CUSTOMIZE.md](CUSTOMIZE.md))*
 * Fully-customizable key bindings *(see [CUSTOMIZE.md](CUSTOMIZE.md))*
 * Table-row striping
 * Show version/context/report execution time in status area
 * Customizable config dir *(see [CUSTOMIZE.md](CUSTOMIZE.md))*
 * Comand line bash completion wrapper *(see [INSTALL.md](INSTALL.md))*
 * Context support
 * Taskd sync support

 This release also changes the software license from GPL to MIT.

### Breaking changes:

 * Configuration has been moved from ```${HOME}/.vitrc``` to ```${HOME}/.vit/config.ini``` -- the location of the config directory can be customized, see [CUSTOMIZE.md](CUSTOMIZE.md) for details.
 * The format of the configuration file has changed, customizations in the legacy ```.vitrc``` file will need to be manually ported to the new format. The [config.sample.ini](https://github.com/scottkosty/vit/blob/2.x/vit/config/config.sample.ini) file is *heavily* commented, and should contain reference to everything you need to migrate the legacy configuration. If no ```config.ini``` exists in the VIT configuration directory, VIT will offer the option to install the sample config upon startup -- this is the easiest way to get started with porting and customization.