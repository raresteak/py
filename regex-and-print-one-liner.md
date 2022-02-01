# Regex with capture groups and printing one-liner

```
python -c \"import re, sys; re.IGNORECASE; myList=(re.findall(r'(UserName.*UserName).*(Computer.*Computer).*(binaryName(?:.exe..|)\s*someOthertext)', sys.stdin.read())); print('\n'.join(str(x) for x in myList))
```

## Capture group 1

UserName.*Username

## Capture group 2

Computer.*Computer

## Capture group 3 with optional string

binaryName(?:.exe.|)\s*someOthertext

.exe. is optional

