---
type: note
title: Minecraft PvP Video Review Workflow
created: '2026-05-03'
updated: '2026-05-03'
tags:
  - minecraft
  - pvp
  - project/minecraft-pvp
  - workflow
  - docs
status: active
lang: en
feeds_into:
  - projects/minecraft-pvp/README.md
  - projects/minecraft-pvp/notes/minecraft-pvp-operating-sheet.md
---
> **TL;DR**: Use Flashback for recording, then use a frame-extraction workflow inspired by `bradautomates/claude-video` to review short PvP clips visually instead of relying on transcript-style summaries.

## Growth Contract
- Parent branch: [[projects/minecraft-pvp/README]]
- Node role: workflow leaf
- First parent link: [[projects/minecraft-pvp/README]]
- Growth trigger: split into tooling setup, review rubric, or fight-review reports after 3+ real review sessions accumulate.
- Forbidden contents: full raw frame dumps, entire match transcripts, cinematic editing notes, and generic YouTube/video automation unrelated to Minecraft PvP review.
- Source/evidence boundary: this note summarizes the usable workflow; raw exports remain in `/home/r1ceg/mc recording` and Flashback replays remain under the CurseForge `pvpp/flashback/replays` folder.

## Source Tool

Ingested tool:

```text
repo: https://github.com/bradautomates/claude-video
installed skill path: /home/r1ceg/.codex/skills/watch
skill name: watch
purpose: make an LLM inspect video by extracting frames and optional transcript
```

Core method:

```text
video URL or local MP4
  -> yt-dlp if URL
  -> ffmpeg/ffprobe inspect and extract frames
  -> optional captions or Whisper transcript
  -> model reads timestamped frames
  -> answer from visual evidence
```

For Minecraft PvP, transcript is mostly irrelevant. The useful part is frame extraction.

## Current Local State

```text
Flashback recording: working
Flashback auto-start: enabled
Flashback hotbar recording: enabled
local export folder: /home/r1ceg/mc recording
installed Codex skill: /home/r1ceg/.codex/skills/watch
skill discovery: requires Codex restart to invoke by name
manual ffmpeg path: /home/r1ceg/.venvs/video-review/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2
user-local ffmpeg/ffprobe: partially installed under /home/r1ceg/.local/bin before dependency setup was stopped
missing for full watch skill: yt-dlp on PATH, plus Whisper key only if audio transcription is needed
```

## Review Pipeline

Default loop:

```text
1. Play with Flashback auto-recording.
2. Press marker after death, bad trade, panic, or weird loss.
3. Export only the relevant fight if possible.
4. Run frame extraction on the MP4.
5. Review contact sheet first.
6. Extract dense frames around the mistake window.
7. Label the failure.
8. Convert the label into one next drill.
```

Failure labels:

```text
spacing
aim
panic jump
panic click
hotbar collapse
bad terrain
late heal
late pearl
bad commit
shield mistake
cooldown rhythm
```

## Export Rules

Do:

```text
10-45 second clips
720p
60 FPS
no audio
max bitrate off
one fight per export when possible
```

Avoid:

```text
whole-session exports
maximum bitrate
cinematic camera paths
keyframes/export artistry during training time
```

The underlying Flashback replay `.zip` is the source of truth and is usually tiny compared with MP4 exports.

## Tool Choice

Use the `watch` skill for:

```text
YouTube/video URLs after dependency setup is finished
local MP4 review once ffmpeg/ffprobe are visible on PATH
caption/transcript videos when audio matters
```

Use the manual ffmpeg path for:

```text
Minecraft PvP clips right now
frames-only review
fast contact sheets
focused dense extraction around timestamps
```

## Operating Rule

```text
The goal is not to make the agent watch everything.
The goal is to find one repeatable failure pattern per session.
```

For week one, review only the worst 1-3 fights.

## Review Reports

- [[projects/minecraft-pvp/notes/minecraft-pvp-review-2026-05-03-first-duels]]

## Related

- [[projects/minecraft-pvp/README]]
- [[projects/minecraft-pvp/notes/minecraft-pvp-operating-sheet]]
- [[projects/minecraft-pvp/notes/minecraft-pvp-first-14-days]]
