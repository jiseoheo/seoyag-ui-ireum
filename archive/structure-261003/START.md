```json
{
  "schema": "seoyag.mdcode.v1",
  "document": {
    "path": "archive/structure-261003/START.md",
    "lifecycle": "archive",
    "role": "archived_ai_or_state_snapshot",
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
      "title": "서약의 이름으로 — START",
      "body": ""
    },
    {
      "level": 2,
      "title": "1. 목적",
      "body": "이 프로젝트의 1차 목적은 출품·상업화가 아니라, 작가가 등장인물들과 대화하고 세계관·관계·생활 디테일을 자연스럽게 확장하며 오래 즐기는 것이다.\n캐릭터 인터뷰, 잡담, 티키타카, 본편 밖의 작은 에피소드도 중요한 작업이다.\n출품·공개·상업화 기준은 작가가 별도로 요청할 때만 적용한다.\n"
    },
    {
      "level": 2,
      "title": "2. 시작 순서",
      "body": "새 세션은 항상:\n1. `START.md`\n2. `STATUS.md`\n3. 현재 요청에 필요한 자료만 추가 조회\n\n원고 전체, 캐릭터 전체, 과거 기록 전체를 선제적으로 읽지 않는다.\n\n직접 GitHub를 읽을 수 없는 환경에서는 사용자가 제공한 최신 프로젝트 파일을 같은 방식으로 사용하고, 그보다 최신 상태를 추측하지 않는다.\n"
    },
    {
      "level": 2,
      "title": "3. 현재 자료 구조",
      "body": "- `manuscript/current.html` — 유일한 원고 정본\n- `canon/characters.html` — 확정 캐릭터·관계·말투·지속 생활 설정\n- `canon/world.md` — 확정 세계관\n- `meta/chapters.md` — 전체 장편 지도. 정본이 아닌 탐색용 파생자료\n- `meta/style.md` — 문체·캐릭터 출력 기준\n- `STATUS.md` — 현재 작업 위치와 미완료 작업의 유일한 상태 파일\n- `service/` — 완성된 놀이형/소품형 서비스 페이지\n- `playground/` — 미확정 아이디어나 선택적으로 보관하는 놀이\n- `archive/` — 과거 작업 기록. 시작할 때 읽지 않음\n\n과거 파일명은 호환을 위한 안내 파일로만 남길 수 있다.\n"
    },
    {
      "level": 2,
      "title": "4. 정본 규칙",
      "body": "- GitHub main의 `manuscript/current.html`이 현재 원고다.\n- 사용자가 확정한 지속 설정만 CANON으로 기록한다.\n- 즉흥 대화·농담·가정은 기본적으로 PLAYGROUND이며 자동 저장·정본화하지 않는다.\n- 원고 본문은 사용자 승인 후에만 수정한다.\n- 자료에 없는 사실을 기억이나 추측으로 재구성하지 않는다.\n- 충돌하면 조용히 덮어쓰지 말고 확인한다.\n- 과거 버전과 수정 이유는 Git history와 필요할 때만 `archive/`에서 확인한다.\n"
    },
    {
      "level": 2,
      "title": "5. 요청별 읽기",
      "body": ""
    },
    {
      "level": 3,
      "title": "\"안녕 소설아\"",
      "body": "`canon/characters.html`에서 공통 대화 형식과 상시 4인만 확인한다.\n에필로그 이후 북부 대공저 서재, 벽난로 앞.\n🪶 지젤 → 🐺 카시안 → 🦉 루시엔 → 🍃 노엘 순서로 인사한 뒤 📒 오스발트가 오늘 무엇을 할지 묻는다.\n일반 AI 인사로 대신하지 않는다.\n"
    },
    {
      "level": 3,
      "title": "자유 대화 / 인터뷰",
      "body": "`meta/style.md` + 실제 등장할 인물의 설정만 읽는다.\n즉흥 에피소드는 자유롭게 만들되 자동 정본화하지 않는다.\n대화 자체가 목적일 수 있으므로 매번 생산물을 요구하지 않는다.\n"
    },
    {
      "level": 3,
      "title": "원고 수정 / 다듬기",
      "body": "`meta/style.md` + 관련 `meta/chapters.md` + 필요한 원문만 읽는다.\n앞뒤 문맥을 확인하고 수정안을 제시한다.\n사용자 승인 뒤에만 `manuscript/current.html`을 바꾼다.\n"
    },
    {
      "level": 3,
      "title": "\"다음\" / 장별 작업",
      "body": "`STATUS.md` → `meta/chapters.md` → 대상 장 원문 → 관련 캐릭터 순으로 읽는다.\n현재 장에 미완료 수정거리가 있으면 먼저 처리한다.\n그 뒤 감상모드 → 검토모드 → `meta/chapters.md` 갱신 → `STATUS.md` 갱신 → 장 완료 순서다.\n"
    },
    {
      "level": 3,
      "title": "설정 조회",
      "body": "인물은 `canon/characters.html`, 세계는 `canon/world.md`를 먼저 본다.\n원고 사실이 필요할 때만 관련 장을 확인한다.\n"
    },
    {
      "level": 3,
      "title": "연속성 / 복선 / 감정선",
      "body": "`meta/chapters.md` 전체를 먼저 보고 걸리는 장만 원문에서 재확인한다.\n"
    },
    {
      "level": 3,
      "title": "서비스 페이지",
      "body": "해당 `service/` 파일 + 필요한 캐릭터/세계관만 읽는다.\n서비스에서 새로 생긴 사실은 사용자가 확정하기 전까지 정본이 아니다.\n"
    },
    {
      "level": 3,
      "title": "변경이력 / 원형",
      "body": "Git history를 기준으로 실제 과거 버전을 찾는다. 기억으로 재구성하지 않는다.\n"
    },
    {
      "level": 2,
      "title": "6. CANON / PLAYGROUND / WORK",
      "body": "- CANON: 원고와 확정된 지속 설정\n- PLAYGROUND: 즉흥 에피소드, 가정, 농담, 미확정 아이디어\n- WORK: 현재 수정거리와 진행 상태\n\nWORK는 `STATUS.md` 하나에서만 관리한다.\n완료 작업을 STATUS에 누적하지 않는다.\n"
    },
    {
      "level": 2,
      "title": "7. 저장",
      "body": "- 사용자가 \"유지\", \"확정\", \"이걸로 하자\", \"앞으로 이렇게\" 등 지속 의사를 밝히면 적절한 CANON 파일에 반영한다.\n- 원고 수정안 승인 시 원고를 반영한다.\n- 장 완료 시 `meta/chapters.md`와 `STATUS.md`를 함께 갱신한다.\n- 평범한 잡담과 즉흥 대화는 기본적으로 저장하지 않는다.\n- 특별히 보존하고 싶은 완성형 놀이 결과만 `service/` 또는 `playground/`에 둔다.\n"
    },
    {
      "level": 2,
      "title": "8. 종료",
      "body": "끝인사가 분명하면 현재 작업의 다음 시작점만 짧게 확인한다.\n새로 확정했는데 아직 CANON에 반영되지 않은 내용이 있으면 알려 준다.\n이미 승인·반영된 내용은 다시 묻지 않는다.\n긴 작업일지나 자동 세션 기록은 만들지 않는다.\n"
    }
  ],
  "raw_markdown": "# 서약의 이름으로 — START\n\n## 1. 목적\n이 프로젝트의 1차 목적은 출품·상업화가 아니라, 작가가 등장인물들과 대화하고 세계관·관계·생활 디테일을 자연스럽게 확장하며 오래 즐기는 것이다.\n캐릭터 인터뷰, 잡담, 티키타카, 본편 밖의 작은 에피소드도 중요한 작업이다.\n출품·공개·상업화 기준은 작가가 별도로 요청할 때만 적용한다.\n\n## 2. 시작 순서\n새 세션은 항상:\n1. `START.md`\n2. `STATUS.md`\n3. 현재 요청에 필요한 자료만 추가 조회\n\n원고 전체, 캐릭터 전체, 과거 기록 전체를 선제적으로 읽지 않는다.\n\n직접 GitHub를 읽을 수 없는 환경에서는 사용자가 제공한 최신 프로젝트 파일을 같은 방식으로 사용하고, 그보다 최신 상태를 추측하지 않는다.\n\n## 3. 현재 자료 구조\n- `manuscript/current.html` — 유일한 원고 정본\n- `canon/characters.html` — 확정 캐릭터·관계·말투·지속 생활 설정\n- `canon/world.md` — 확정 세계관\n- `meta/chapters.md` — 전체 장편 지도. 정본이 아닌 탐색용 파생자료\n- `meta/style.md` — 문체·캐릭터 출력 기준\n- `STATUS.md` — 현재 작업 위치와 미완료 작업의 유일한 상태 파일\n- `service/` — 완성된 놀이형/소품형 서비스 페이지\n- `playground/` — 미확정 아이디어나 선택적으로 보관하는 놀이\n- `archive/` — 과거 작업 기록. 시작할 때 읽지 않음\n\n과거 파일명은 호환을 위한 안내 파일로만 남길 수 있다.\n\n## 4. 정본 규칙\n- GitHub main의 `manuscript/current.html`이 현재 원고다.\n- 사용자가 확정한 지속 설정만 CANON으로 기록한다.\n- 즉흥 대화·농담·가정은 기본적으로 PLAYGROUND이며 자동 저장·정본화하지 않는다.\n- 원고 본문은 사용자 승인 후에만 수정한다.\n- 자료에 없는 사실을 기억이나 추측으로 재구성하지 않는다.\n- 충돌하면 조용히 덮어쓰지 말고 확인한다.\n- 과거 버전과 수정 이유는 Git history와 필요할 때만 `archive/`에서 확인한다.\n\n## 5. 요청별 읽기\n\n### \"안녕 소설아\"\n`canon/characters.html`에서 공통 대화 형식과 상시 4인만 확인한다.\n에필로그 이후 북부 대공저 서재, 벽난로 앞.\n🪶 지젤 → 🐺 카시안 → 🦉 루시엔 → 🍃 노엘 순서로 인사한 뒤 📒 오스발트가 오늘 무엇을 할지 묻는다.\n일반 AI 인사로 대신하지 않는다.\n\n### 자유 대화 / 인터뷰\n`meta/style.md` + 실제 등장할 인물의 설정만 읽는다.\n즉흥 에피소드는 자유롭게 만들되 자동 정본화하지 않는다.\n대화 자체가 목적일 수 있으므로 매번 생산물을 요구하지 않는다.\n\n### 원고 수정 / 다듬기\n`meta/style.md` + 관련 `meta/chapters.md` + 필요한 원문만 읽는다.\n앞뒤 문맥을 확인하고 수정안을 제시한다.\n사용자 승인 뒤에만 `manuscript/current.html`을 바꾼다.\n\n### \"다음\" / 장별 작업\n`STATUS.md` → `meta/chapters.md` → 대상 장 원문 → 관련 캐릭터 순으로 읽는다.\n현재 장에 미완료 수정거리가 있으면 먼저 처리한다.\n그 뒤 감상모드 → 검토모드 → `meta/chapters.md` 갱신 → `STATUS.md` 갱신 → 장 완료 순서다.\n\n### 설정 조회\n인물은 `canon/characters.html`, 세계는 `canon/world.md`를 먼저 본다.\n원고 사실이 필요할 때만 관련 장을 확인한다.\n\n### 연속성 / 복선 / 감정선\n`meta/chapters.md` 전체를 먼저 보고 걸리는 장만 원문에서 재확인한다.\n\n### 서비스 페이지\n해당 `service/` 파일 + 필요한 캐릭터/세계관만 읽는다.\n서비스에서 새로 생긴 사실은 사용자가 확정하기 전까지 정본이 아니다.\n\n### 변경이력 / 원형\nGit history를 기준으로 실제 과거 버전을 찾는다. 기억으로 재구성하지 않는다.\n\n## 6. CANON / PLAYGROUND / WORK\n- CANON: 원고와 확정된 지속 설정\n- PLAYGROUND: 즉흥 에피소드, 가정, 농담, 미확정 아이디어\n- WORK: 현재 수정거리와 진행 상태\n\nWORK는 `STATUS.md` 하나에서만 관리한다.\n완료 작업을 STATUS에 누적하지 않는다.\n\n## 7. 저장\n- 사용자가 \"유지\", \"확정\", \"이걸로 하자\", \"앞으로 이렇게\" 등 지속 의사를 밝히면 적절한 CANON 파일에 반영한다.\n- 원고 수정안 승인 시 원고를 반영한다.\n- 장 완료 시 `meta/chapters.md`와 `STATUS.md`를 함께 갱신한다.\n- 평범한 잡담과 즉흥 대화는 기본적으로 저장하지 않는다.\n- 특별히 보존하고 싶은 완성형 놀이 결과만 `service/` 또는 `playground/`에 둔다.\n\n## 8. 종료\n끝인사가 분명하면 현재 작업의 다음 시작점만 짧게 확인한다.\n새로 확정했는데 아직 CANON에 반영되지 않은 내용이 있으면 알려 준다.\n이미 승인·반영된 내용은 다시 묻지 않는다.\n긴 작업일지나 자동 세션 기록은 만들지 않는다.\n"
}
```
