# 서약의 이름으로 — shared AI workspace

GPT와 Claude가 같은 작품 구조를 쓰도록 정리한 저장소입니다.

## 시작
새 세션은:
1. `START.md`
2. `STATUS.md`
3. 요청에 필요한 자료만 추가 조회

## 현재 구조
```
START.md                    공통 운영 규칙
STATUS.md                   현재 위치와 미완료 작업

manuscript/current.html     유일한 원고 정본

canon/characters.html       확정 캐릭터 설정
canon/world.md              확정 세계관

meta/chapters.md            전체 장편 지도
meta/style.md               공통 문체/출력 기준

service/                    완성된 편지·견문록·소품형 페이지
playground/                 미확정 아이디어/선택 보관
archive/                    과거 작업기록과 이전 지침
```

## 핵심 규칙
- GitHub main의 `manuscript/current.html`이 현재 원고다.
- 지속 설정은 사용자가 확정한 것만 CANON으로 기록한다.
- 즉흥 대화는 기본적으로 저장하지 않는다.
- 원고는 사용자 승인 후에만 수정한다.
- 현재 작업 상태는 `STATUS.md` 하나에서만 관리한다.
- 과거 변경 이유와 버전은 Git history를 우선한다.

## 서비스 페이지
`service/`는 노엘의 견문록, 편지, 초대장, 장부 같은 완성된 놀이형 페이지용이다.
서비스 페이지는 정본을 표현할 수 있지만, 그 자체가 새 정본을 결정하지는 않는다.

## Claude
Claude가 GitHub를 직접 읽을 수 없는 환경에서는 최신 프로젝트 파일을 Claude 프로젝트에 제공한다.
운영 순서는 동일하게 `START → STATUS → 필요한 자료`다.
