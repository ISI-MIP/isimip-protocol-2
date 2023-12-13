ISIMIP2 simulation protocol
===========================

This project builds sector-specific machine-readable ISIMIP2 protocols from a common data source. This works like the [ISIMIP3 protocol](https://github.com/ISI-MIP/isimip-protocol-3).

The output files are found at https://protocol2.isimip.org.


Setup
-----

Setup Python3 and Git as explained in the [ISIMIP3 protocol](https://github.com/ISI-MIP/isimip-protocol-3/blob/main/README.md). Pandoc is not needed here. No further Python requirements need to be installed.


Build
-----

```bash
make  # should work on Linux/macOS

sh build.sh     # Linux/macOS/WSL
call build.cmd  # Windows cmd
```

On Windows, a double click on `build.cmd` should also build the protocol.

The output files are located in `output`.
