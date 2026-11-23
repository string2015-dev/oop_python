# ping_check.py

import subprocess

targets = [
    "192.168.0.1",
    "8.8.8.8",
    "google.com"    
]

print(f"아침 점검 시작 — 대상 {len(targets)}개")

for target in targets:
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "1000", target],   #windows 
        # ["ping", "-c", "1", "-W", "1", target]         #macOS 용 바꾸기
        capture_output=True
    )

    if result.returncode == 0:
        print(f"[OK] {target}")
    else:
        print(f"[응답 없음] {target}")