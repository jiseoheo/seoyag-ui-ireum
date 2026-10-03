# AI 작업 규칙 — 서약의 이름으로

## 기준 저장소
- 실제 원고: `manuscript/current.html`
- 작업 기록: `meta/worklog.html`
- 상세 캐릭터 설정: `meta/characters.html`
- 노엘의 견문록: `extras/noel.html`
- 상태/검색용 인덱스: Notion (`manifest.json` 참고)

## 읽기 최소화 원칙
1. 원고 전체를 매번 읽지 않는다.
2. 먼저 Notion Revision Issues에서 필요한 수정거리만 찾는다.
3. Chapters에서 대상 장과 경로를 확인한다.
4. 대상 장의 본문과 관련 인물 설정만 읽는다.
5. 세계관 설정이 필요한 경우에만 World Settings 또는 `meta/characters.html`의 관련 구간을 읽는다.

## 쓰기 원칙
- 원고가 바뀌면 GitHub의 `manuscript/current.html`을 갱신한다.
- 설정 변경이면 `meta/characters.html` 또는 관련 파일도 갱신한다.
- 수정 완료 후 Notion Revision Issues 상태를 `반영완료`로 바꾸고 Chapters 상태/미완료 수를 갱신한다.
- 기존 설정을 임의로 보정하거나 새 사실을 만들지 않는다. 자료에 없으면 확인 필요로 남긴다.

## 단축 명령
- `/다음`: 다음 미완료 Revision Issue → 해당 장 문맥 확인 → 수정안 제시. 승인 후 GitHub/Notion 동시 반영.
- `/다듬기`: 사건·정보를 유지하고 지정 범위 문장만 다듬기.
- `/연속성`: 관련 장·Timeline·Characters·World Settings만 조회해 충돌 검사.
- `/설정조회`: Characters/World Settings 우선 조회.
- `/원형`: Git 이력에서 가장 오래된 실제 버전을 찾고 재구성하지 않기.
- `/변경이력`: Git diff/commit 기준으로 변경 경로 설명.

## 현재 위치
- 서장~13장 장별 수정·검토 완료. 다만 일부 과거 장에 잔여 수정거리가 있음.
- 현재 다음 차례는 14장.
