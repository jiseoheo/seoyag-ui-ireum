```json
{
  "schema": "seoyag.ai-context.v1",
  "project": "서약의 이름으로",
  "purpose": "Universal machine-readable routing contract for any AI model reading this repository.",
  "markdown_code_schema": {
    "schema": "seoyag.mdcode.v1",
    "parse_steps": [
      "Read the entire .md file.",
      "Remove the outer ```json and closing ``` fence.",
      "JSON.parse the remaining text.",
      "Read document and machine_index first.",
      "Use sections in order for structured navigation.",
      "Use raw_markdown only when exact legacy wording is needed."
    ]
  },
  "startup": {
    "required_order": [
      "AI_CONTEXT.md",
      "START.md",
      "STATUS.md"
    ],
    "model_entrypoints": {
      "ChatGPT": [
        "GPT.md",
        "instructions/chatgpt-project-instructions.md"
      ],
      "Claude": [
        "CLAUDE.md",
        "instructions/claude-project-instructions.md"
      ],
      "OpenAI_Codex": [
        "AGENTS.md"
      ],
      "generic": [
        "AI_WORKFLOW.md",
        "ROUTER.md",
        "CURRENT_STATE.md"
      ]
    },
    "rule": "All entrypoints route to this file; no model-specific file may override canon or current state."
  },
  "source_precedence": [
    {
      "rank": 1,
      "path": "manuscript/current.html",
      "meaning": "sole manuscript canon"
    },
    {
      "rank": 2,
      "path": "canon/characters.html",
      "meaning": "confirmed character, relation, speech and chat continuity canon"
    },
    {
      "rank": 3,
      "path": "canon/world.md",
      "meaning": "confirmed world canon"
    },
    {
      "rank": 4,
      "path": "STATUS.md",
      "meaning": "sole current work position and unfinished-work state"
    },
    {
      "rank": 5,
      "path": "meta/chapters.md",
      "meaning": "derived chapter navigation; manuscript wins on conflict"
    },
    {
      "rank": 6,
      "path": "meta/style.md",
      "meaning": "style, output, chat, appreciation and review rules"
    },
    {
      "rank": 7,
      "path": "playground/ideas.md",
      "meaning": "noncanon ideas until user confirms"
    }
  ],
  "operational_rules": {
    "do_not_read_full_manuscript_by_default": true,
    "use_meta_chapters_first_for_long_context": true,
    "manuscript_edits_require_user_approval": true,
    "do_not_silently_overwrite_conflicts": true,
    "archive_is_historical_only": true,
    "parenthetical_user_text_is_meta_only": true,
    "appreciation_original_must_be_verbatim_and_complete": true,
    "show_runnable_service_output_when_user_says_show_me": true
  },
  "current_state_source": "STATUS.md",
  "all_active_md": [
    "AGENTS.md",
    "AI_WORKFLOW.md",
    "CLAUDE.md",
    "CURRENT_STATE.md",
    "GPT.md",
    "README.md",
    "ROUTER.md",
    "START.md",
    "STATUS.md",
    "canon/world.md",
    "instructions/chatgpt-project-instructions.md",
    "instructions/claude-project-instructions.md",
    "meta/author-notes.md",
    "meta/canon-rules.md",
    "meta/chapter-summaries.md",
    "meta/chapters.md",
    "meta/gpt-writing-guide.md",
    "meta/ideas.md",
    "meta/style.md",
    "playground/README.md",
    "playground/ideas.md",
    "service/README.md"
  ],
  "archive_policy": "Files under archive/ are historical snapshots. They use the same code schema but MUST NOT control current state.",
  "compatibility_contract": "If an AI system discovers any one of AGENTS.md, GPT.md, CLAUDE.md, AI_WORKFLOW.md, ROUTER.md, CURRENT_STATE.md, or instructions/*, it must follow startup.required_order.",
  "write_policy": {
    "default_target": "main",
    "direct_commit_required": true,
    "applies_to_all_models": true,
    "branch_or_pr_default": false,
    "exception": "Only when the user explicitly requests a branch or PR.",
    "prewrite_check": "Read current main before every write and reconcile concurrent changes."
  }
}
```
