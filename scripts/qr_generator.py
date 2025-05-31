import os

# 🔹 تحديد مسار المجلد داخل WSL
base_path = "/mnt/c/Users/ali/Desktop/STEAM_Nexus_Hub"
os.makedirs(base_path, exist_ok=True)

# 🔹 محتوى السكربت
script_content = """ 
import qrcode
from PIL import Image

# إنشاء باركود بسيط
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data("https://ali-khateb-1.github.io/STEAM_Nexus_Hub/")
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")

# حفظ الصورة داخل المجلد
img.save("/mnt/c/Users/ali/Desktop/STEAM_Nexus_Hub/qr_code.png")

print("✅ تم حفظ الباركود بنجاح داخل WSL!")
"""

# 🔹 تحديد مسار السكربت داخل WSL
script_path = "/mnt/c/Users/ali/Desktop/STEAM_Nexus_Hub/generate_qr.py"

# 🔹 حفظ السكربت داخل المجلد الصحيح
with open(script_path, "w", encoding="utf-8") as f:
    f.write(script_content)

print(f"✅ تم حفظ السكربت داخل WSL في: {script_path}")