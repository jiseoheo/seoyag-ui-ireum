```json
{
  "schema": "seoyag.mdcode.v1",
  "document": {
    "path": "meta/chapter-summaries.md",
    "lifecycle": "active",
    "role": "derived_chapter_index",
    "project": "서약의 이름으로",
    "parse_rule": "Strip outer json code fence, JSON.parse, then consume machine_index and sections in order.",
    "raw_preserved": true
  },
  "machine_index": {
    "derivation": {
      "source_of_truth": "manuscript/current.html",
      "purpose": "navigation/index only",
      "on_conflict": "manuscript wins"
    }
  },
  "preamble": "",
  "sections": [
    {
      "level": 1,
      "title": "Moved",
      "body": "The current chapter map lives in `meta/chapters.md`.\n"
    }
  ],
  "raw_markdown": "# Moved\n\nThe current chapter map lives in `meta/chapters.md`.\n"
}
```
