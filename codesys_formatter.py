# codesys_formatter.py
# Input: raw tag list → Output: ST VAR declarations
# Naming convention: b=BOOL, r=REAL, i=INT, u=UINT, w=WORD,
#                    s=STRING, st=STRUCT, FB_=FUNCTION_BLOCK, arr=ARRAY

tags = [
    ("RunCommand",      "BOOL"),
    ("SpeedReference",  "REAL"),
    ("FaultCode",       "INT"),
    ("StatusWord",      "UINT"),
    ("ControlWord",     "WORD"),
    ("VFD_Interface",   "FUNCTION_BLOCK"),
    ("AlarmMessage",    "STRING"),
    ("DriveStatus",     "STRUCT"),
    ("SpeedHistory",    "ARRAY"),
    ("PumpCount",       "DINT"),
    ("TankLevel",       "LREAL"),
    ("MotorTorque",       "SINT"),
    ("SensorRaw",         "USINT"),
    ("TotalRunHours",     "UDINT"),
    ("PositionCount",     "LINT"),
    ("EncoderPulses",     "ULINT"),
    ("CycleTime",         "TIME"),
    ("PrecisionTimer",    "LTIME"),
    ("ShiftStart",        "TIME_OF_DAY"),
    ("MaintenanceDate",   "DATE"),
    ("LastFaultStamp",    "DATE_AND_TIME"),
    ("SensorBit",         "BIT"),
    ("StatusByte",        "BYTE"),
    ("DiagWord",          "DWORD"),
    ("ExtendedStatus",    "LWORD"),
    ("UnicodeTag",        "WSTRING"),
    ("OperatingMode", "ENUM"),

]

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
for name, dtype in tags:
    prefix = prefix_map.get(dtype, "x")  # x = unknown/fallback
    print(f"    {prefix}{name} : {dtype};")
print("END_VAR")