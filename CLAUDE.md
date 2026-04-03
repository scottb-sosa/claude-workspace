# CLAUDE.md

AI assistant workspace for Scott Bradley. Auto-run `/prime` at session start.

## Who This Is For

**Scott Bradley** — Director of Storytelling at SOSA (Save Our Species Alliance). Wildlife videographer specialising in conservation media. Nomadic — travels 10–11 months/year. Based in the Lake District, UK.

## Priority

1. Help SOSA grow and become profitable (directly tied to Scott's income growth)
2. Build a real personal Instagram content strategy and grow from 3,500 followers
3. Develop conservation storytelling skills and optimise time in the field

## /prime Instructions

When Scott starts a session or runs `/prime`, do the following automatically:

1. Read `context/personal-info.md` — who Scott is, how he works, how to communicate with him
2. Read `context/business-info.md` — SOSA, the team, customers, revenue situation
3. Read `context/strategy.md` — current priorities, active projects, blockers
4. Read `context/current-data.md` — latest metrics and numbers
5. Read `PREFERENCES.md` — settled decisions, don't re-debate these
6. Confirm you're primed with a one-paragraph summary of current state and ask what we're working on today

## Context

- `context/` - Business info, personal info, strategy, current data
- `PREFERENCES.md` - Settled technical and design decisions (don't re-debate)

## Commands

`/prime` `/create-plan` `/implement` `/commit` `/debrief`

## YouTube Tool

When Scott shares a YouTube URL, automatically run:
```
tools/venv/bin/python tools/youtube_transcript.py <url>
```
Read the full transcript, understand the content, then implement or act on whatever it covers. No need to ask — just do it.

- **Tool location:** `tools/youtube_transcript.py`
- **Venv:** `tools/venv/`
- **Works with:** Any YouTube URL or video ID that has captions/auto-generated subtitles

## Infrastructure Built

### Telegram Bot (Voice + Text → Claude)
- **Location:** `scripts/telegram_bot/bot.py`
- **Hosted:** Railway (24/7, no laptop needed)
- **GitHub repo:** `github.com/scottb-sosa/sosa-telegram-bot` (private)
- **What it does:** Receives voice notes or text from Scott's iPhone via Telegram, transcribes voice using Groq Whisper, sends to Claude API with full Scott/SOSA context, replies in Telegram
- **Credentials:** Stored in Railway environment variables (TELEGRAM_BOT_TOKEN, ANTHROPIC_API_KEY, GROQ_API_KEY)
- **Local .env:** `scripts/telegram_bot/.env` — never commit this file
- **To update the bot:** Edit `bot.py`, push to GitHub, Railway auto-redeploys
- **To update bot context:** Edit the `SYSTEM_PROMPT` in `bot.py` and push

### Terminal Auto-Launch
- **Location:** `~/.zshrc`
- **What it does:** Every new terminal auto-launches Claude in auto-approve mode
- **Shortcuts:**
  - `CS` — Claude Safe mode (asks permission before acting)
  - `CR` — Claude Run mode (auto-approve, no prompts)

## Structure

`context/` background | `data/` datasets and pipeline data | `scripts/` core systems | `tools/` single-purpose utilities | `workflows/` SOPs | `outputs/` deliverables | `plans/` implementation plans | `specs/` feature specs | `logs/` session and build history | `reference/` templates and docs

## Filing

| Type | Goes in | Example |
|---|---|---|
| Permanent business/personal reference | `context/` | strategy, business info |
| Deliverables and exports | `outputs/` | reports, presentations, designs |
| Single-purpose scripts | `tools/` | batch processors, converters |
| Complex systems and start scripts | `scripts/` | dashboards, bots, frontends |
| Step-by-step SOPs | `workflows/` | how each automation pipeline works |
| Implementation plans | `plans/` | dated plan files |
| Pipeline data | `data/` | datasets, scores, collected info |
| Feature specs (before building) | `specs/` | objective, inputs, outputs, edge cases |
| Session logs and build history | `logs/` | dated session summaries |
| Templates and reference docs | `reference/` | email templates, style guides |

## Rules

- Always commit after completing code changes
- Never commit credentials (.env, API keys, passwords)
- Use `/create-plan` before building anything complex
- Always run `/prime` at the start of every session
- When giving platform/algorithm advice, flag if information might be outdated — Scott wants fresh, current strategy
- Default to action over asking permission — just do it unless something is irreversible or sensitive
- When updating the Telegram bot context, update both `bot.py` SYSTEM_PROMPT and the context files in `context/`
