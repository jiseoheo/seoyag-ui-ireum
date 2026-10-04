```json
{
  "schema": "seoyag.mdcode.v1",
  "document": {
    "path": "archive/structure-261003/repository-readme.md",
    "lifecycle": "archive",
    "role": "archive_overview",
    "project": "서약의 이름으로",
    "parse_rule": "Strip outer json code fence and JSON.parse.",
    "raw_preserved": true,
    "use_for_current_state": false
  },
  "machine_index": {
    "archive_policy": {
      "historical_only": true,
      "current_state_authority": false,
      "recover_only_when_explicitly_needed": true
    }
  },
  "preamble": "",
  "sections": [
    {
      "level": 1,
      "title": "서약의 이름으로 — shared AI workspace",
      "body": "GPT와 Claude가 같은 작품 구조를 쓰도록 정리한 저장소입니다.\n"
    },
    {
      "level": 2,
      "title": "시작",
      "body": "새 세션은:\n1. `START.md`\n2. `STATUS.md`\n3. 요청에 필요한 자료만 추가 조회\n"
    },
    {
      "level": 2,
      "title": "현재 구조",
      "body": "```\nSTART.md                    공통 운영 규칙\nSTATUS.md                   현재 위치와 미완료 작업\n\nmanuscript/current.html     유일한 원고 정본\n\ncanon/characters.html       확정 캐릭터 설정\ncanon/world.md              확정 세계관\n\nmeta/chapters.md            전체 장편 지도\nmeta/style.md               공통 문체/출력 기준\n\nservice/                    완성된 편지·견문록·소품형 페이지\nplayground/                 미확정 아이디어/선택 보관\narchive/                    과거 작업기록과 이전 지침\n```\n"
    },
    {
      "level": 2,
      "title": "핵심 규칙",
      "body": "- GitHub main의 `manuscript/current.html`이 현재 원고다.\n- 지속 설정은 사용자가 확정한 것만 CANON으로 기록한다.\n- 즉흥 대화는 기본적으로 저장하지 않는다.\n- 원고는 사용자 승인 후에만 수정한다.\n- 현재 작업 상태는 `STATUS.md` 하나에서만 관리한다.\n- 과거 변경 이유와 버전은 Git history를 우선한다.\n"
    },
    {
      "level": 2,
      "title": "서비스 페이지",
      "body": "`service/`는 노엘의 견문록, 편지, 초대장, 장부 같은 완성된 놀이형 페이지용이다.\n서비스 페이지는 정본을 표현할 수 있지만, 그 자체가 새 정본을 결정하지는 않는다.\n"
    },
    {
      "level": 2,
      "title": "Claude",
      "body": "Claude가 GitHub를 직접 읽을 수 없는 환경에서는 최신 프로젝트 파일을 Claude 프로젝트에 제공한다.\n운영 순서는 동일하게 `START → STATUS → 필요한 자료`다.\n"
    }
  ],
  "raw_markdown": "# 서약의 이름으로 — shared AI workspace\n\nGPT와 Claude가 같은 작품 구조를 쓰도록 정리한 저장소입니다.\n\n## 시작\n새 세션은:\n1. `START.md`\n2. `STATUS.md`\n3. 요청에 필요한 자료만 추가 조회\n\n## 현재 구조\n```\nSTART.md                    공통 운영 규칙\nSTATUS.md                   현재 위치와 미완료 작업\n\nmanuscript/current.html     유일한 원고 정본\n\ncanon/characters.html       확정 캐릭터 설정\ncanon/world.md              확정 세계관\n\nmeta/chapters.md            전체 장편 지도\nmeta/style.md               공통 문체/출력 기준\n\nservice/                    완성된 편지·견문록·소품형 페이지\nplayground/                 미확정 아이디어/선택 보관\narchive/                    과거 작업기록과 이전 지침\n```\n\n## 핵심 규칙\n- GitHub main의 `manuscript/current.html`이 현재 원고다.\n- 지속 설정은 사용자가 확정한 것만 CANON으로 기록한다.\n- 즉흥 대화는 기본적으로 저장하지 않는다.\n- 원고는 사용자 승인 후에만 수정한다.\n- 현재 작업 상태는 `STATUS.md` 하나에서만 관리한다.\n- 과거 변경 이유와 버전은 Git history를 우선한다.\n\n## 서비스 페이지\n`service/`는 노엘의 견문록, 편지, 초대장, 장부 같은 완성된 놀이형 페이지용이다.\n서비스 페이지는 정본을 표현할 수 있지만, 그 자체가 새 정본을 결정하지는 않는다.\n\n## Claude\nClaude가 GitHub를 직접 읽을 수 없는 환경에서는 최신 프로젝트 파일을 Claude 프로젝트에 제공한다.\n운영 순서는 동일하게 `START → STATUS → 필요한 자료`다.\n"
}
```
