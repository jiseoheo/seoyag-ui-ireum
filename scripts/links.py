#!/usr/bin/env python3
"""LINKS.md 생성: AI가 웹으로 읽을 수 있도록 작업용 파일의 전체 주소(raw)를 나열한다.

claude.ai처럼 "대화에 나온 주소만 열 수 있는" 환경을 위한 목록이다.
main에 저장될 때마다 자동으로 다시 만들어진다.
"""
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://raw.githubusercontent.com/jiseoheo/seoyag-ui-ireum/main/"

GROUPS = [
    ("시작·상태", ["START.md", "STATUS.md", "manifest.json"]),
    ("프로세스 카드", sorted(glob.glob("process/*.md", root_dir=ROOT))),
    ("문체·장별 지도", ["meta/style.md", "meta/chapters.md"]),
    ("설정 (canon)", sorted(glob.glob("canon/*.md", root_dir=ROOT))),
    ("장별 수정사항 (reviews)", sorted(glob.glob("reviews/*.md", root_dir=ROOT))),
    ("2편 노트·아이디어·서비스", ["sequel/ideas.md", "playground/ideas.md", "service/README.md"]),
]


def main():
    with open(os.path.join(ROOT, "manifest.json"), encoding="utf-8") as f:
        chapters = json.load(f)["chapters"]
    lines = [
        "# LINKS",
        "",
        "> 작업용 파일의 전체 주소. GitHub를 웹으로 읽는 AI는 아래 주소를 그대로 연다.",
        "> 자동 생성 파일(`scripts/links.py`). 직접 고치지 않는다.",
        "",
    ]
    for title, paths in GROUPS:
        lines += ["## " + title, ""]
        lines += ["- %s%s" % (BASE, p) for p in paths if os.path.exists(os.path.join(ROOT, p))]
        lines.append("")
    lines += ["## 원고 (장별)", ""]
    lines += ["- %s — %s%s" % (c["title"], BASE, c["file"]) for c in chapters]
    with open(os.path.join(ROOT, "LINKS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
