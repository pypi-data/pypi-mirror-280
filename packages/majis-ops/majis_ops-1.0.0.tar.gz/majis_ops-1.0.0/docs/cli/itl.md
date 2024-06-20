MAJIS Command Line Interfaces
=============================

You can use the MAJIS operations toolbox directly in the terminal with a few command line interfaces:
- [`majis-itl`](majis-itl)

:::{Note}
More interface will be added in the future
:::

(majis-itl)=
ITL interface
-------------

```bash
majis-itl --help
```
```text
usage: majis-itl [-h] [-o output.[itl|csv|xlsm]] [-f]
                 [-t "YYYY-MM-DDTHH:MM:SS REF_NAME (COUNT = N)"]
                 [-r "YYYY-MM-DDTHH:MM:SS REF_NAME (COUNT = N)"]
                 [--timeline timeline.xlsm] [--header "# my-custom-header"]
                 [--overlap] [--csv] [--csv-sep separator]
                 [input.itl ...]

MAJIS ITL toolbox

positional arguments:
  input.itl             Input ITL filename(s). If multiple files are provided
                        they will be concatenated.

options:
  -h, --help            show this help message and exit
  -o output.[itl|csv|xlsm], --output output.[itl|csv|xlsm]
                        Output filename, it could be either ITL, CSV or XLSM.
                        If none provided, the results will be displayed (only
                        for ITL and CSV).
  -f, --force           Overwrite the output file if already exists.
  -t "YYYY-MM-DDTHH:MM:SS REF_NAME (COUNT = N)", --time-ref "YYYY-MM-DDTHH:MM:SS REF_NAME (COUNT = N)"
                        Input events time reference(s). If multiple values are
                        required use an `events.evf` file.
  -r "YYYY-MM-DDTHH:MM:SS REF_NAME (COUNT = N)", --relative-to "YYYY-MM-DDTHH:MM:SS REF_NAME (COUNT = N)"
                        Reference time to be used for relative time output.
  --timeline timeline.xlsm
                        Original timeline to append. If no explicit `--output`
                        is provided new observations will be append in this
                        file.
  --header "# my-custom-header"
                        ITL custom file header.
  --overlap             Allow blocks overlap.
  --csv                 Display the ITL as CSV.
  --csv-sep separator   CSV separator (default: ";")
```

Examples
--------
Convert a single ITL with relative time as an absolute CSV ITL file:
```bash
majis-itl relative_time.itl --time-ref "2032-09-24T21:33:36 PERIJOVE_12PJ (COUNT = 1)" --output output.csv
```

Concatenate two ITL with absolute and relative times as an relative ITL file:
```bash
majis-itl absolute_time.itl relative_time.itl --ref-time events.evf --relative-to "2032-09-24T21:33:36 PERIJOVE_12PJ (COUNT = 1)" --output output.itl
```

```{Note}
If no `--output` flag is present, the output is display in the console.
```

Create a new MAJIS timeline (`.xlsm`) from a ITL the default template:
```bash
majis-itl absolute_time.itl --output output.xlsm
```

Edit an existing MAJIS timeline to compute relative time w.r.t. C/A reference:
```bash
majis-itl --timeline timeline.xlsm --relative-to "2032-09-24T21:33:36 PERIJOVE_12PJ (COUNT = 1)"
```

```{Warning}
If no `--output` flag is present, the output will be save in the original template.
```
