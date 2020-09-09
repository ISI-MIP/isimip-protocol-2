ISIMIP2 simulation protocol
===========================

This project builds sector-specific machine-readable ISIMIP2 protocols from a common data source. This works like the [ISIMIP3 protocol](https://github.com/ISI-MIP/isimip-protocol-2).

The output files are found at https://protocol2.isimip.org.


Local setup
-----------

Setup Python3 and Git as esplained in the [isimip-qc README](https://github.com/ISI-MIP/isimip-qc/blob/master/README.md). Not further packages are needed to be installed.


Local usage
-----------

```bash
make  # should work on Linux/macOS

sh build.sh     # Linux/macOS/WSL
call build.cmd  # Windows cmd
```

On Windows, a double click on `build.cmd` should also build the protocol.
