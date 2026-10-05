# 기타 요청

> 수다·퇴고·감상 밖의 요청(설정 조회, 흐름 개정, 연속성 확인, 서비스, 변경이력)과 문서 역할 안내.

## 설정 조회
인물은 `canon/characters.md`(기본)와 `canon/characters-extra.md`(소환 인물·생일·기념일·인터뷰 사실), 세계는 `canon/world.md`를 먼저 본다.
원고 사실이 필요할 때만 관련 장을 확인한다.
인물 파일의 "모른다"·"봉인"은 그 인물이 모른다는 뜻이지 설정이 없다는 뜻이 아니다. canon에 답이 없거나 "모른다"·"봉인"만 있으면 `sequel/ideas.md`도 확인한 뒤에 "미정"이라고 답한다.

## 전체 흐름 개정
`meta/chapters.md` 전체 + 관련 장 원문을 읽는다. 검토한 장만 감상 체감과 사실 확인을 합쳐 요약을 보강한다.

## 연속성 / 복선 / 감정선
`meta/chapters.md` 전체를 먼저 보고 걸리는 장만 원문에서 재확인한다.

## 서비스 페이지
해당 `service/` 파일 + 필요한 캐릭터/세계관만 읽는다.
사용자가 서비스/HTML 결과물을 "보여줘", "열어줘", "실행본 보여줘"처럼 요청하면 설명이나 코드 일부 대신 실제 실행 가능한 결과물을 우선 제공한다.
서비스 페이지는 정본을 표현할 수 있지만, 그 자체가 새 정본을 결정하지 않는다. 서비스에서 새로 생긴 사실은 사용자가 확정하기 전까지 정본이 아니다.

## 변경이력 / 원형
Git history를 기준으로 실제 과거 버전을 찾는다. 기억으로 재구성하지 않는다.

## 원고 장치
- 원고 수정은 해당 장 파일에만 한다. `current.html`은 저장 후 자동으로 맞춰진다(`scripts/manuscript.py`, `.github/workflows/manuscript.yml`). 실수로 `current.html`만 고쳐도 장별 파일로 자동 반영되지만, 같은 저장에서 둘을 다르게 고치면 자동 점검이 실패로 표시된다.
- 삽화 그림은 `manuscript/images/`에 파일로 두고, 원고에는 `<img src="images/파일이름">`처럼 경로만 적는다(경로는 `current.html` 기준). 그림을 data URI로 원고에 넣으면 Claude Project 지식 용량을 넘으므로 넣지 않는다. 전달 묶음이 data URI 조각이면 Claude Code가 그림을 파일로 꺼내 넣는다. 프로젝트 지식에는 `manuscript/images/`를 넣지 않는다(그림 속 글자는 `alt`에 있다).
- `scripts/`, `.github/` — 원고 자동 맞춤과 정합성 점검 장치. main에 저장할 때마다 자동으로 돈다. 작업 중에는 읽지 않는다.

## 문서 역할과 호환
운영·읽기 규칙은 `START.md`, 저장 절차는 `process/checkpoint.md`에 둔다. 출력 형식·문체·품질 기준은 `meta/style.md`, 현재 작업 상태는 `STATUS.md`, 장별 수정사항은 `reviews/`, 프로세스별 진행 순서는 `process/`에 둔다.
`AGENTS.md`, `CLAUDE.md`는 `START.md`로 안내만 한다. `instructions/project-instructions.md`는 Claude·ChatGPT 프로젝트 설정에 넣는 공통 시작 안내다.
`manifest.json`은 경로와 장 앵커를 찾는 기계용 색인이며 운영 규칙이나 현재 상태를 별도로 저장하지 않는다.
캐릭터 HTML의 기존 인물별 설정과 후보 분류는 보존한다. 아직 세계관 정본으로 분리하지 않은 기존 사실은 추측으로 이관하지 않는다.
과거 자료가 필요한 경우에만 Git history를 확인한다. 옛 기록(archive, worklog)은 Git history에만 남아 있다.
과거 파일명은 호환을 위한 안내 파일로만 남길 수 있다.
