# 全能文稿排版助手｜Academic & Teaching Edition

> 繁體中文 AI Agent Skill：將學術研究與大學教學內容整理成清楚、可信、可檢查、可維護的簡報、講義、研究報告與 HTML 文稿。

**v0.3.0 · AGPL-3.0-only · Codex / Claude Code / Google AI Studio**

## 快速使用

### Codex、Claude Code 與其他支援的 AI Agent

在已安裝 Node.js/npm 的終端機執行：

    npx skills add https://github.com/wallacechiu-purestudio/all-purpose-document-layout-assistant --skill all-purpose-document-layout-assistant --agent codex claude-code --global --copy

更多方式請參考 [本地安裝指南](references/agent-install.md)。

### Google AI Studio

開啟 [AI Studio 指令檔](AI-STUDIO-INSTRUCTIONS.md)，複製全文到可接受自訂指令的欄位，再在 New App／提示欄描述本次任務與提供的素材。也可以從 GitHub Pages 首頁一鍵複製。

### 下載

- [Skill 專用 ZIP](dist/all-purpose-document-layout-assistant-skill-v0.3.0.zip)
- 完整原始碼：GitHub 頁面上點 **Code → Download ZIP**。

## 設計方法

1. 先確認目的、受眾、來源素材、輸出形式與限制。
2. 規劃資訊架構與每頁／每節的主要訊息。
3. 依任務選擇一致的視覺系統：A 編輯雜誌式、B 瑞士網格式、C 教學工作坊式。
4. 依 CRAP 四原則（Contrast、Repetition、Alignment、Proximity）檢查兩輪。
5. 保留研究證據、原始數據、引文與可追溯來源；不捏造資料。
6. 交付時清楚說明驗證範圍及尚未實際驗證的項目。

## 專案檔案

- SKILL.md：AI Agent 核心規範
- AI-STUDIO-INSTRUCTIONS.md：Google AI Studio 專用指令
- references/crap-checklist.md：CRAP 兩輪驗收清單
- references/layout-patterns.md：三套視覺系統與版型模式
- assets/academic-deck-template.html：HTML 網頁簡報模板
- NOTICE.md、LICENSE：來源聲明與授權

## GitHub Pages

至 Settings → Pages → Build and deployment，選擇 Deploy from a branch，分支 main、資料夾 /(root)，儲存後等候部署完成。

## 來源與授權

本專案參考並改裝自 [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)，保留來源聲明並以 AGPL-3.0-only 發布。本專案為衍生改作，非原作者官方版本。詳見 [NOTICE.md](NOTICE.md)。

## 本地驗證

在專案根目錄執行：

    python3 scripts/build_skill_zip.py
    python3 scripts/validate_project.py

這些腳本只能檢查檔案結構、連結與基本格式，不能代替瀏覽器視覺驗收或對 AI 生成內容的品質測試。
