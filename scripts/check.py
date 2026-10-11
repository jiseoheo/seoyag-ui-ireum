#!/usr/bin/env python3
"""저장소 정합성 점검. 문제가 있으면 목록을 출력하고 exit 1.

  - 장별 원고와 manuscript/current.html이 같은지
  - manifest.json이 가리키는 파일이 모두 있는지
  - 원고의 삽화가 data URI가 아닌 manuscript/images/ 파일을 가리키고, 그 파일이 있는지
  - .md 문서 안의 상대 경로 링크와 `경로` 표기가 실제 파일을 가리키는지
  - START·STATUS·process 카드·프로젝트 안내문이 열라고 하는 파일이 LINKS.md에 모두 있는지
    (claude.ai는 LINKS.md에 적힌 주소만 열 수 있다)
  - 프로젝트 안내문의 Claude용·ChatGPT용 블록이 공통 부분과 버전에서 서로, 그리고 START.md와 맞는지
"""
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
problems = []


def exists(path):
    return os.path.exists(os.path.join(ROOT, path))


def check_manuscript():
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "manuscript.py"), "check"],
                       capture_output=True, text=True)
    if r.returncode:
        problems.append("원고: " + (r.stderr or r.stdout).strip())



def check_images():
    with open(os.path.join(ROOT, "manifest.json"), encoding="utf-8") as f:
        files = [c["file"] for c in json.load(f)["chapters"]]
    for rel in files:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            text = f.read()
        if re.search(r'<img[^>]*src="data:', text):
            problems.append("%s: 삽화가 data URI로 들어 있음(manuscript/images/로 옮길 것)" % rel)
        for src in re.findall(r'<img[^>]*src="([^"]+)"', text):
            if not src.startswith("data:") and not exists(os.path.join("manuscript", src)):
                problems.append("%s: 없는 삽화 %s" % (rel, src))


def check_manifest():
    with open(os.path.join(ROOT, "manifest.json"), encoding="utf-8") as f:
        m = json.load(f)
    paths = list(m["canonical"].values()) + [c["file"] for c in m["chapters"]]
    paths += list(m.get("service", {}).values()) + list(m.get("playground", {}).values())
    paths += m.get("ai_startup_order", [])
    for p in paths:
        if not exists(p):
            problems.append("manifest.json: 없는 파일 %s" % p)


def check_links():
    for md in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        rel = os.path.relpath(md, ROOT)
        if rel.startswith(".git"):
            continue
        base = os.path.dirname(md)
        with open(md, encoding="utf-8") as f:
            text = f.read()
        for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
            if re.match(r"[a-z]+:", target):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, target))):
                problems.append("%s: 끊어진 링크 %s" % (rel, target))
        # `canon/world.md`처럼 저장소 루트 기준으로 적은 경로
        for target in re.findall(r"`((?:canon|meta|process|reviews|sequel|service|playground|manuscript|scripts|instructions)/[^`*\s]*)`", text):
            if not exists(target):
                problems.append("%s: 없는 경로 `%s`" % (rel, target))


# 웹으로 읽지 않는 파일: 자동 생성본·화면 꾸밈·장치·안내 전용 파일
NOT_FOR_WEB = re.compile(r"^(manuscript/current\.html|manuscript/chapters/_|manuscript/images/|scripts/|LINKS\.md$|AGENTS\.md$|CLAUDE\.md$)")


def check_links_md():
    with open(os.path.join(ROOT, "LINKS.md"), encoding="utf-8") as f:
        listed = set(re.findall(r"githubusercontent\.com/[^/]+/[^/]+/[0-9a-f]{40}/(\S+)", f.read()))
    sources = ["START.md", "STATUS.md", "instructions/project-instructions.md"]
    sources += sorted(glob.glob("process/*.md", root_dir=ROOT))
    for src in sources:
        with open(os.path.join(ROOT, src), encoding="utf-8") as f:
            text = f.read()
        base = os.path.dirname(src)
        targets = [os.path.normpath(os.path.join(base, t))
                   for t in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text) if not re.match(r"[a-z]+:", t)]
        targets += re.findall(r"`((?:canon|meta|process|reviews|sequel|service|playground|manuscript|instructions)/[^`*\s]*)`", text)
        for t in sorted(set(targets)):
            if NOT_FOR_WEB.match(t) or not os.path.isfile(os.path.join(ROOT, t)):
                continue
            if t not in listed:
                problems.append("%s: `%s`이 LINKS.md에 없음(scripts/links.py GROUPS에 추가할 것)" % (src, t))


def check_instructions():
    with open(os.path.join(ROOT, "instructions/project-instructions.md"), encoding="utf-8") as f:
        blocks = re.findall(r"```\n(.*?)```", f.read(), re.S)
    commons = [re.split(r"^## (?:Claude|ChatGPT) 전용", b, flags=re.M)[0] for b in blocks]
    if len(blocks) != 2 or commons[0] != commons[1]:
        problems.append("instructions/project-instructions.md: Claude용·ChatGPT용 블록의 공통 부분이 다름")
        return
    version = re.search(r"안내문 버전: (\S+)", commons[0])
    with open(os.path.join(ROOT, "START.md"), encoding="utf-8") as f:
        start = f.read()
    if not version or "현재 안내문 버전은 **%s**" % version.group(1) not in start:
        problems.append("START.md: 현재 안내문 버전이 instructions/project-instructions.md와 다름")


check_manuscript()
check_images()
check_manifest()
check_links()
check_links_md()
check_instructions()
if problems:
    print("\n".join(problems))
    sys.exit(1)
print("OK: 정합성 점검 통과")
