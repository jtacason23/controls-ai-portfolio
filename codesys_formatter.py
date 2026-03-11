# codesys_formatter.py
# Input: tags.csv → Output: ST VAR declarations

import csv

prefix_map = {
    "BOOL":           "x",
    "REAL":           "r",
    "INT":            "i",
    "UINT":           "u",
    "WORD":           "w",
    "FUNCTION_BLOCK": "FB_",
    "STRING":         "s",
    "STRUCT":         "STRUCT_",
    "ARRAY":          "ar",
    "DINT":           "di",
    "LREAL":          "lr",
    "SINT":         "si",
    "USINT":        "usi",
    "UDINT":        "udi",
    "LINT":         "li",
    "ULINT":        "uli",
    "TIME":         "t",
    "LTIME":        "lt",
    "TIME_OF_DAY":  "tod",
    "DATE":         "dat",
    "DATE_AND_TIME":"dt",
    "BIT":          "bit",
    "BYTE":         "by",
    "DWORD":        "dw",
    "LWORD":        "lw",
    "WSTRING":      "ws",
    "ENUM":         "ENUM_",
}

output_file = "output_vars.txt"

with open("tags.csv", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open(output_file, "w") as out:
        out.write("VAR\n")
        for row in rows:
            name = row["name"]
            dtype = row["dtype"]
            prefix = prefix_map.get(dtype, "null")
            out.write(f"  {prefix}{name} : {dtype};\n")
        out.write("END_VAR\n")

print(f"Done - saved to {output_file}")