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

print("VAR")
with open("tags.csv", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader: 
        name = row["name"]
        dtype = row["dtype"]
        prefix = prefix_map.get(dtype, "x")  # x = unknown/fallback
        print(f"    {prefix}{name} : {dtype};")
print("END_VAR")