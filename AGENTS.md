```json
{
  "schema": "seoyag.mdcode.v1",
  "document": {
    "path": "AGENTS.md",
    "lifecycle": "active",
    "role": "ai_entrypoint",
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
      "required": true,
      "instruction": "Parse every .md as seoyag.mdcode.v1 JSON and follow AI_CONTEXT routing."
    }
  },
  "preamble": "",
  "sections": [
    {
      "level": 1,
      "title": "Compatibility",
      "body": "Read [START.md](START.md), then [STATUS.md](STATUS.md).\n"
    }
  ],
  "raw_markdown": "# Compatibility\n\nRead [START.md](START.md), then [STATUS.md](STATUS.md).\n"
}
```
