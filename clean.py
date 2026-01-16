# import scrap
def clean_text(text):
    lines = text.split("\n")
    
    cleaned = []
    for line in lines:
        line = line.strip()
        if line.startswith(("GET", "POST", "PUT", "DELETE", "PATCH")):
            cleaned.append(line)
            continue
        if line[:3].isdigit():
            cleaned.append(line)
            continue
        if ":" in line and len(line) < 40:
            cleaned.append(line)
            continue
        if len(line) > 30:
          cleaned.append(line.strip())
          continue
    print("Success!")
    return "\n".join(cleaned)
