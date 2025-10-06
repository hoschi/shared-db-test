# Data Model

This document outlines the data models for the `notes_system` and `video_analysis` schemas.

## `notes_system` Schema

### `notes`
- `id` (Integer, Primary Key)
- `title` (String, Not Null)
- `content_markdown` (Text)
- `created_at` (DateTime, Default: now)
- `updated_at` (DateTime, Default: now, On Update: now)

### `tags`
- `id` (Integer, Primary Key)
- `name` (String, Unique, Not Null)
- `color` (String)

### `note_tags` (Junction Table)
- `note_id` (Integer, Foreign Key to `notes.id`, Primary Key)
- `tag_id` (Integer, Foreign Key to `tags.id`, Primary Key)

### `attachments`
- `id` (Integer, Primary Key)
- `note_id` (Integer, Foreign Key to `notes.id`, Not Null)
- `filename` (String, Not Null)
- `file_path` (String, Not Null)
- `mime_type` (String)
- `created_at` (DateTime, Default: now)

### `note_versions`
- `id` (Integer, Primary Key)
- `note_id` (Integer, Foreign Key to `notes.id`, Not Null)
- `version_number` (Integer, Not Null)
- `content_markdown` (Text)
- `created_at` (DateTime, Default: now)

## `video_analysis` Schema

### `videos`
- `id` (Integer, Primary Key)
- `youtube_video_id` (String, Unique, Not Null)
- `title` (String, Not Null)
- `metadata` (JSONB)
- `created_at` (DateTime, Default: now)
- `updated_at` (DateTime, Default: now, On Update: now)

### `transcripts`
- `id` (Integer, Primary Key)
- `video_id` (Integer, Foreign Key to `videos.id`, Not Null)
- `language` (String, Not Null)
- `content` (Text)
- `created_at` (DateTime, Default: now)

### `analyses`
- `id` (Integer, Primary Key)
- `video_id` (Integer, Foreign Key to `videos.id`, Not Null)
- `prompt_id` (Integer, Foreign Key to `ai_prompts.id`)
- `analysis_result` (JSONB)
- `status` (String, Default: 'pending')
- `created_at` (DateTime, Default: now)

### `ai_prompts`
- `id` (Integer, Primary Key)
- `name` (String, Unique, Not Null)
- `prompt_text` (Text, Not Null)
- `created_at` (DateTime, Default: now)
