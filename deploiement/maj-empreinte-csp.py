#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Recalcule l'empreinte SHA-256 du script de index.html et la reporte
dans nginx-tympan.conf et .htaccess. À lancer après chaque nouvelle version."""
import base64, hashlib, pathlib, re, sys

base = pathlib.Path(__file__).resolve().parent
page = (base.parent / "index.html").read_text(encoding="utf-8")
scripts = re.findall(r"<script>(.*?)</script>", page, re.S)
if len(scripts) != 1:
    sys.exit("index.html doit contenir exactement un script intégré.")
h = "'sha256-" + base64.b64encode(hashlib.sha256(scripts[0].encode("utf-8")).digest()).decode() + "'"
for name in ("nginx-tympan.conf", ".htaccess"):
    f = base / name
    f.write_text(re.sub(r"'sha256-[A-Za-z0-9+/=]+'", h, f.read_text(encoding="utf-8")), encoding="utf-8")
print("Empreinte CSP :", h)
