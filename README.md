# 全能文稿排版助手｜Academic & Teaching Edition

> 繁體中文 AI Agent Skill：將學術研究與大學教學內容整理成清楚、可信、可檢查、可維護的履歷／CV、研究報告、簡報、講義與 HTML 文稿；並直接整合 Guizang PPT 的兩套完整網頁簡報模板、版型資料庫、主題色、元件與演講者模式。

**v2.0.0 · AGPL-3.0-only · Codex / Claude Code / Google AI Studio**

## 30 秒開始

### 安裝至 Codex／Claude Code

先確認本機已安裝 Node.js/npm，再在終端機執行：

```bash
npx skills add https://github.com/wallacechiu-purestudio/all-purpose-document-layout-assistant --skill all-purpose-document-layout-assistant --agent codex claude-code --global --copy
```

若 CLI 參數有變，請依安裝工具當下的提示選擇目標 Agent。手動安裝方式見 [references/agent-install.md](references/agent-install.md)。

### Google AI Studio

1. 開啟 [AI-STUDIO-INSTRUCTIONS.md](AI-STUDIO-INSTRUCTIONS.md)。
2. 將全文複製至 AI Studio 可接受自訂指令的欄位。
3. 再在 New App／主要提示欄描述單次任務，並提供實際資料。
4. 若介面沒有獨立自訂指令欄，將規範與當次任務一起貼入提示。

首頁提供一鍵複製入口。它只會複製文字，不會自動更改 AI Studio 設定或上傳資料。

### 下載至本地電腦

點 GitHub 頁面的 **Code → Download ZIP**，或直接下載：

[下載完整專案 ZIP](https://github.com/wallacechiu-purestudio/all-purpose-document-layout-assistant/archive/refs/heads/main.zip)

解壓縮後，將 `SKILL.md`、`references/` 及需要的 `assets/` 放進 Skill 資料夾。常見全域位置：

- **Codex**：`~/.codex/skills/all-purpose-document-layout-assistant/`
- **Claude Code**：`~/.claude/skills/all-purpose-document-layout-assistant/`

確認 Skill 資料夾根目錄有 `SKILL.md`，再重新載入 Agent。更多細節見 [本地安裝指南](references/agent-install.md)。

## 多模式工作介面與 16:9 學術簡報

v2.0.0 新增可操作的簡報樣板與配色選擇器：五套樣板（Swiss Grid、Editorial、E-ink 極簡、Academic 經典、Workshop 活力）及六組配色（Ink & Paper、Swiss Blue、Forest、Burgundy、Ocean Teal、Warm Neutral），可獨立選擇並即時套用至全部投影片，切換不改動內容。 新版新增四種可切換模式（瑞士國際網格、雜誌電子墨水、教學與工作坊、16:9 學術簡報）以及 CRAP 檢核、列印／PDF、下載單檔 HTML 規格。範例見 [多模式 HTML 工作介面](assets/multimode-document-studio-template.html)，完整行為規格見 [multimode-workspace.md](references/multimode-workspace.md)。這些是本衍生版新增的整合功能；AI Studio 不會僅憑 GitHub 路徑自動載入倉庫檔案，因此 System Instructions 內也直接包含必要規格。

## 網頁 PPT 核心資產

本專案不只保留 Guizang PPT 的設計理念，亦已將其可重用的模板、版型與現場演講控制資源納入倉庫：

- `assets/template.html`：Editorial／E-ink 完整模板。
- `assets/template-swiss.html`：Swiss／Grid 完整模板。
- `assets/motion.min.js`：本地動效資源。
- `references/layouts.md`、`references/layouts-swiss.md`：版型資料庫。
- `references/themes.md`、`references/themes-swiss.md`、`references/components.md`：主題色與元件指南。
- `references/presenter-mode.md`、`references/checklist.md`、`references/swiss-layout-lock.md`：講者模式與品質規則。
- `references/guizang-feature-guide.md`：功能導覽、使用流程與驗證方式。
- `scripts/validate-presenter-mode.mjs`、`scripts/validate-swiss-deck.mjs`、`scripts/check-presenter-runtime-sync.mjs`：簡報結構與模板檢查工具。

使用前請依簡報類型選一套模板，並閱讀相對應的版型文件；兩套模板不可混用。詳細使用方式見 [Guizang 功能整合指南](references/guizang-feature-guide.md)。

## 核心工作流程

1. 讀取真實素材，確認目的、受眾、使用場景與限制。
2. 規劃資訊架構與每頁／每節的主要訊息。
3. 依內容選擇 A 編輯雜誌式、B 瑞士網格式或 C 教學工作坊式視覺系統。
4. 依 CRAP 四原則（Contrast、Repetition、Alignment、Proximity）進行兩輪檢核。
5. 依任務交付完整履歷／CV、研究報告，或含完整原始碼、README、依賴／授權資訊及驗證狀態的簡報專案。
6. 保留研究證據、原始數據、引文與可追溯來源，不捏造資料。
7. 交付成品，說明檢核結果、實際測試範圍與未驗證事項。

## 專案檔案

- [SKILL.md](SKILL.md)：AI Agent 核心規範
- [AI-STUDIO-INSTRUCTIONS.md](AI-STUDIO-INSTRUCTIONS.md)：Google AI Studio 專用指令
- [多模式工作介面規格](references/multimode-workspace.md) 與 [可執行 HTML 範本](assets/multimode-document-studio-template.html)
- [references/crap-checklist.md](references/crap-checklist.md)：CRAP 兩輪驗收清單
- [references/layout-patterns.md](references/layout-patterns.md)：三套視覺系統與版型模式
- [references/deliverable-checklist.md](references/deliverable-checklist.md)：履歷、研究報告與附完整原始碼簡報的交付檢核
- [references/agent-install.md](references/agent-install.md)：本地安裝指南
- [assets/academic-deck-template.html](assets/academic-deck-template.html) 與 [assets/academic-deck.css](assets/academic-deck.css)：網頁簡報模板與樣式
- [index.html](index.html)：一鍵複製與下載入口
- [NOTICE.md](NOTICE.md) 與 [LICENSE](LICENSE)：來源聲明與授權

## 啟用 GitHub Pages

到 **Settings → Pages → Build and deployment**，將 Source 設為 **Deploy from a branch**，Branch 選 `main`，資料夾選 `/(root)`，按 Save。等候 GitHub Pages 完成部署後，就能使用首頁的一鍵複製功能。

GitHub 官方文件：<https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>

## 來源與授權

本專案參考並改作自 [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)。本專案以 AGPL-3.0-only 發布，完整條文見 [LICENSE](LICENSE)，改作範圍見 [NOTICE.md](NOTICE.md)。此專案非原作者官方版本。

## 本地檢查

```bash
python3 scripts/validate_project.py
```

程式檢查不等於瀏覽器視覺驗收；尚未實際測試的項目應如實揭露。
