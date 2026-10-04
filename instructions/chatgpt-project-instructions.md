```json
{
  "schema": "seoyag.mdcode.v1",
  "document": {
    "path": "instructions/chatgpt-project-instructions.md",
    "lifecycle": "active",
    "role": "model_project_instruction",
    "project": "서약의 이름으로",
    "parse_rule": "Strip outer json code fence, JSON.parse, then consume machine_index and sections in order.",
    "raw_preserved": true
  },
  "machine_index": {
    "startup_contract": {
      "universal_entrypoint": "AI_CONTEXT.md",
      "read_order": [
        "AI_CONTEXT.md",
        "START.md",
        "STATUS.md"
      ],
      "required": true
    }
  },
  "preamble": "",
  "sections": [
    {
      "level": 1,
      "title": "공통 프로젝트 시작 안내",
      "body": "GitHub `jiseoheo/seoyag-ui-ireum`의 `main`에서 [START.md](https://github.com/jiseoheo/seoyag-ui-ireum/blob/main/START.md) → [STATUS.md](https://github.com/jiseoheo/seoyag-ui-ireum/blob/main/STATUS.md) 순서로 읽고, 이후에는 START가 지정하는 필요한 자료만 읽는다.\n"
    }
  ],
  "raw_markdown": "# 공통 프로젝트 시작 안내\n\nGitHub `jiseoheo/seoyag-ui-ireum`의 `main`에서 [START.md](https://github.com/jiseoheo/seoyag-ui-ireum/blob/main/START.md) → [STATUS.md](https://github.com/jiseoheo/seoyag-ui-ireum/blob/main/STATUS.md) 순서로 읽고, 이후에는 START가 지정하는 필요한 자료만 읽는다.\n"
}
```
