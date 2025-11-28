import os
import re

# === CONFIGURATION ===
folder_path = r"C:\Users\myepi\Desktop\Els"
file_extension = ".xml"

# Regex patterns
enabled_pattern = re.compile(r'Enabled="true"', re.IGNORECASE)
pattern_value = re.compile(r'Pattern="\d+"', re.IGNORECASE)  # Matches Pattern="anything"

for root, _, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(file_extension):
            filepath = os.path.join(root, filename)

            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            updated = False

            # Step 1: Replace Enabled="true" → Enabled="false"
            if re.search(enabled_pattern, content):
                content = re.sub(enabled_pattern, 'Enabled="false"', content)
                updated = True

            # Step 2: Replace any Pattern="number" → Pattern="0"
            if re.search(pattern_value, content):
                content = re.sub(pattern_value, 'Pattern="0"', content)
                updated = True

            if updated:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"✅ Updated: {filepath}")
            else:
                print(f"⚠️ No changes made to {filepath}")

print("🎉 All done!")
