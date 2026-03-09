# codesys_formatter.py
# Input: raw tag list → Output: ST VAR declarations
# Naming convention: b=BOOL, r=REAL, i=INT, u=UINT, w=WORD, FB_=FUNCTION_BLOCK

tags = [
    ("RunCommand", "BOOL"),
    ("SpeedReference", "REAL"),
    ("FaultCode", "INT"),
    ("StatusWord", "UINT"),
    ("ControlWord", "WORD"),
    ("VFD_Interface", "FUNCTION_BLOCK"),
]

prefix_map = {
    "BOOL": "x",
    "REAL": "r",
    "INT": "i",
    "UINT": "u",
    "WORD": "w",
    "FUNCTION_BLOCK": "FB_",
}

print("VAR")
for name, dtype in tags:
    prefix = prefix_map.get(dtype, "x")
    if dtype == "FUNCTION_BLOCK":
        print(f"    {prefix}{name} : {dtype};")
    else:
        print(f"    {prefix}{name} : {dtype};")
print("END_VAR")

