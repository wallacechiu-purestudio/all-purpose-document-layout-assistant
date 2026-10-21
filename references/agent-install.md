# 本地安裝指南

## 推薦：Skills CLI
先確認已安裝 Node.js/npm，再在終端機執行：

```bash
npx skills add https://github.com/wallacechiu-purestudio/all-purpose-document-layout-assistant --skill all-purpose-document-layout-assistant --agent codex claude-code --global --copy
```

CLI 版本與支援的 Agent 名稱可能更新；若命令參數不同，依 CLI 提示選擇目標 Agent。

## 手動安裝
下載 repository ZIP 並解壓縮，將 `SKILL.md`、`references/`、`assets/`（若有）放在同一個 Skill 資料夾中。

常見全域位置：
- Codex：`~/.codex/skills/all-purpose-document-layout-assistant/`
- Claude Code：`~/.claude/skills/all-purpose-document-layout-assistant/`

確認 Skill 資料夾根目錄有 `SKILL.md`，重新載入 Agent，並以「請使用全能文稿排版助手 Skill，幫我……」測試。

## Google AI Studio
複製 `AI-STUDIO-INSTRUCTIONS.md` 全文到可接受自訂指令的欄位，再在 New App／主要提示欄描述本次任務與提供的素材。若該介面沒有獨立自訂指令欄，將規範與任務要求合併貼入提示。複製功能不會自動修改 AI Studio 設定或上傳資料。
