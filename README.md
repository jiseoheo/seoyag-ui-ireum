# 서약의 이름으로 — shared AI workspace

Claude와 GPT가 같은 원고와 상태를 공유하기 위한 저장소입니다.

## 구조
```
manuscript/current.html   실제 원고(정본)
meta/worklog.html         상세 작업 기록
meta/characters.html      상세 캐릭터/진행 규칙
extras/noel.html          노엘의 견문록
docs/                     이전 이어가기 안내
manifest.json             경로와 Notion 링크
AI_WORKFLOW.md            공통 작업 규칙
AGENTS.md                  GPT용 시작 규칙
CLAUDE.md                  Claude용 시작 규칙
```

## Notion
- 작업 허브: https://app.notion.com/p/3ee1485c92b481c89c74de5de06e3305
- Chapters: https://app.notion.com/p/1f41bf73767741948b2dc0791f4b20d1
- Characters: https://app.notion.com/p/5fd54367d78b413ba0e664fa61c93689
- Revision Issues: https://app.notion.com/p/37830e5285a84793927c23cb88081895
- Timeline: https://app.notion.com/p/6901ced3d31643e2ac587661038d08d6
- World Settings: https://app.notion.com/p/a5902ca12b11445da7da613a9f6f28f8

## 첫 GitHub 설정
1. GitHub에서 private repository를 하나 만든다. 권장 이름: `seoyag-ui-ireum`.
2. 이 폴더의 내용 전체를 저장소 루트에 올린다.
3. GPT/Claude에 GitHub와 Notion 연결 권한을 준다.
4. 이후 원고는 GitHub, 상태/검색은 Notion을 정본으로 삼는다.

## 수정 단위
초기에는 기존 HTML 표현을 보존하기 위해 원고를 `current.html` 하나로 유지한다. 장별 파일 분리는 수정이 진행되는 장부터 점진적으로 도입한다.
