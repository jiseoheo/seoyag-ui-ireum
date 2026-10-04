```json
{
  "schema": "seoyag.mdcode.v1",
  "document": {
    "path": "README.md",
    "lifecycle": "active",
    "role": "repository_overview",
    "project": "서약의 이름으로",
    "parse_rule": "Strip outer json code fence, JSON.parse, then consume machine_index and sections in order.",
    "raw_preserved": true
  },
  "machine_index": {},
  "preamble": "",
  "sections": [
    {
      "level": 1,
      "title": "서약의 이름으로",
      "body": "Claude Project를 주 작업장으로, ChatGPT를 교대 작업장으로 사용하는 GitHub 체크포인트 기반 작업공간입니다.\n\n평소에는 Claude Project + Artifact에서 작업하고, 모델 교대·세션 종료·장 완료 때 승인된 변경과 미완료 상태를 GitHub main에 체크포인트로 저장합니다. ChatGPT와 Claude는 서로의 Artifact나 채팅을 전제로 하지 않고 최신 main + STATUS에서 이어갑니다.\n\n모든 AI 모델의 공통 시작점은 [AI_CONTEXT.md](AI_CONTEXT.md) → [START.md](START.md) → [STATUS.md](STATUS.md)입니다. 운영 규칙과 요청별 읽기 순서는 START에서 확인합니다.\n\n| 경로 | 역할 |\n| --- | --- |\n| [manuscript/current.html](manuscript/current.html) | 원고 정본 |\n| [canon/characters.html](canon/characters.html) | 확정 캐릭터 설정 및 기존 후보 표시 |\n| [canon/world.md](canon/world.md) | 확정 세계관 |\n| [meta/chapters.md](meta/chapters.md) | 전체 흐름 탐색 |\n| [meta/style.md](meta/style.md) | 공통 문체·출력·품질 기준 |\n| [service/](service/) | 완성형 놀이 콘텐츠 |\n| [playground/](playground/) | 미확정 아이디어·초안 |\n| [archive/](archive/) | 과거 기록·옛 지침 |\n| [AI_CONTEXT.md](AI_CONTEXT.md) | 모든 AI 모델의 공통 기계 판독 라우터 |\n| [manifest.json](manifest.json) | 경로·장 앵커 색인 |\n| [instructions/](instructions/) | 두 모델에 같은 진입점을 안내하는 호환 파일 |\n\n모델별 루트 지침과 옛 경로는 공통 진입점으로 연결됩니다.\n"
    }
  ],
  "raw_markdown": "# 서약의 이름으로\n\nClaude Project를 주 작업장으로, ChatGPT를 교대 작업장으로 사용하는 GitHub 체크포인트 기반 작업공간입니다.\n\n평소에는 Claude Project + Artifact에서 작업하고, 모델 교대·세션 종료·장 완료 때 승인된 변경과 미완료 상태를 GitHub main에 체크포인트로 저장합니다. ChatGPT와 Claude는 서로의 Artifact나 채팅을 전제로 하지 않고 최신 main + STATUS에서 이어갑니다.\n\n모든 AI 모델의 공통 시작점은 [AI_CONTEXT.md](AI_CONTEXT.md) → [START.md](START.md) → [STATUS.md](STATUS.md)입니다. 운영 규칙과 요청별 읽기 순서는 START에서 확인합니다.\n\n| 경로 | 역할 |\n| --- | --- |\n| [manuscript/current.html](manuscript/current.html) | 원고 정본 |\n| [canon/characters.html](canon/characters.html) | 확정 캐릭터 설정 및 기존 후보 표시 |\n| [canon/world.md](canon/world.md) | 확정 세계관 |\n| [meta/chapters.md](meta/chapters.md) | 전체 흐름 탐색 |\n| [meta/style.md](meta/style.md) | 공통 문체·출력·품질 기준 |\n| [service/](service/) | 완성형 놀이 콘텐츠 |\n| [playground/](playground/) | 미확정 아이디어·초안 |\n| [archive/](archive/) | 과거 기록·옛 지침 |\n| [AI_CONTEXT.md](AI_CONTEXT.md) | 모든 AI 모델의 공통 기계 판독 라우터 |\n| [manifest.json](manifest.json) | 경로·장 앵커 색인 |\n| [instructions/](instructions/) | 두 모델에 같은 진입점을 안내하는 호환 파일 |\n\n모델별 루트 지침과 옛 경로는 공통 진입점으로 연결됩니다.\n"
}
```
