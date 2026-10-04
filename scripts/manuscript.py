#!/usr/bin/env python3
"""장별 원고 파일과 한 권짜리 manuscript/current.html을 서로 맞춘다.

  python3 scripts/manuscript.py build   장별 파일 → current.html
  python3 scripts/manuscript.py split   current.html → 장별 파일
  python3 scripts/manuscript.py check   둘이 한 글자도 다르지 않은지 확인 (다르면 exit 1)

장 순서와 파일 이름은 manifest.json의 chapters 목록이 정한다.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "manuscript", "current.html")
PARTS = os.path.join(ROOT, "manuscript", "chapters")
HEAD = os.path.join(PARTS, "_head.html")
TAIL = os.path.join(PARTS, "_tail.html")


def read(path):
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def chapters():
    with open(os.path.join(ROOT, "manifest.json"), encoding="utf-8") as f:
        return json.load(f)["chapters"]


def build_text():
    parts = [read(HEAD)]
    parts += [read(os.path.join(ROOT, c["file"])) for c in chapters()]
    parts.append(read(TAIL))
    return "".join(parts)


def split_text(book):
    """current.html을 머리말·장별 조각·꼬리말로 나눈다. 이어 붙이면 원본과 같다."""
    chs = chapters()
    starts = []
    for c in chs:
        m = re.search(r'<h2 id="%s">' % re.escape(c["anchor"]), book)
        if not m:
            sys.exit("current.html에서 장 제목을 찾지 못함: %s" % c["title"])
        starts.append(m.start())
    if starts != sorted(starts):
        sys.exit("current.html의 장 순서가 manifest.json과 다름")
    found = len(re.findall(r"<h2[ >]", book))
    if found != len(chs):
        sys.exit("current.html의 장 수(%d)가 manifest.json(%d)과 다름" % (found, len(chs)))
    end = book.rindex("</body>")
    bounds = starts + [end]
    out = {HEAD: book[: starts[0]], TAIL: book[end:]}
    for i, c in enumerate(chs):
        out[os.path.join(ROOT, c["file"])] = book[bounds[i] : bounds[i + 1]]
    return out


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "build":
        write(BOOK, build_text())
    elif cmd == "split":
        os.makedirs(PARTS, exist_ok=True)
        for path, text in split_text(read(BOOK)).items():
            write(path, text)
    elif cmd == "check":
        if build_text() != read(BOOK):
            sys.exit("장별 파일과 manuscript/current.html이 다름")
        print("OK: 장별 파일과 current.html이 같음")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
