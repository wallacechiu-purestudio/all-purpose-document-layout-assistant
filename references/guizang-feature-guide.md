# Guizang PPT 核心功能使用指南

本專案已納入上游 Guizang PPT Skill 的可重用模板、版型與演講控制資源，並以學術研究、大學教學、繁體中文與可追溯資料的工作流程加以整合。

上游來源：https://github.com/op7418/guizang-ppt-skill
本專案為衍生版本，非上游官方版本。授權與改作範圍請見 `NOTICE.md`、`LICENSE`。

## 1. 兩套真正可執行的簡報模板

### A. Editorial / E-ink
檔案：`assets/template.html`

適合研究敘事、文化與設計研究、案例分享、演講、產品發表與故事型簡報。此模板包含上游實作的排版 CSS、動態背景、頁面翻轉、主題變數、元件樣式、導覽和演講控制介面。

### B. Swiss / Grid
檔案：`assets/template-swiss.html`

適合量化研究、科技、方法流程、比較分析、KPI、資訊視覺化與證據導向簡報。此模板包含瑞士國際主義的網格、字級階梯、單一強調色、登記版型、互動導覽及演講控制機制。

**同一份簡報只能選一套模板。** 兩套模板存在同名但語義不同的 CSS class；不要把 A 的版型類名直接放進 B，反之亦然。

## 2. 可重用的版型資料庫

- `references/layouts.md`：Editorial / E-ink 版型骨架、版型選擇、圖文比例、頁面節奏和模板 class 預檢。
- `references/layouts-swiss.md`：Swiss / Grid 登記版型與嚴格版型規則。
- `references/swiss-layout-lock.md`：Swiss 登記版型的結構限制。
- `references/components.md`：字體、標籤、統計數字、圖像框、引用、動效等元件使用方法。
- `references/themes.md`：Editorial / E-ink 主題色預設。
- `references/themes-swiss.md`：Swiss / Grid 主題色預設。

產生投影片前先決定模板與版型，再把內容填入模板已定義的 class。不得只引用版型名稱卻不實際使用對應結構；不得憑空創造 class。

## 3. 演講者模式與現場控制

兩套模板都整合上游演講者模式功能。實際可用功能取決於模板程式碼、瀏覽器權限與執行環境，交付前仍須測試。

主要能力包括：
- 鍵盤翻頁、頁面導覽、總覽與快捷控制。
- 演講者視圖，顯示目前頁、下一頁、演講備註和頁面目的。
- 以穩定的 `data-slide-id` 對應每頁備註，避免重排後備註錯置。
- 演講計時、逐頁時間與排練相關控制。
- 觀眾畫面同步、同步狀態與中斷後恢復相關機制。
- 視模板提供自動翻頁、雷射筆／圈選、觀眾畫面控制及低功耗模式。

演講備註規範：`references/presenter-mode.md`。
執行前檢查：`references/checklist.md`。

## 4. 動效與離線降級

- `assets/motion.min.js`：上游模板所使用的 Motion 動效本地資源。
- 模板另有 CDN 載入路徑與降級邏輯，但實際離線可用性應依網路環境測試。
- 字型與其他 CDN 資源在離線環境可能無法載入，應保留系統字型 fallback，並如實說明限制。

## 5. 圖片、截圖與地圖元件

- `references/image-prompts.md`：依模板風格與圖片槽位設計配圖提示。
- `references/screenshot-framing.md`：保真截圖、留白與比例調整規則。
- `references/swiss-map-component.md`：Swiss S08 版型的地圖元件擴充。只有內容確實需要地理位置或路線時才使用。

截圖保真優先：使用者要求保留 UI、程式碼、文字或數據時，不得用生成圖片取代原圖內容。

## 6. 產出前的驗證

- `scripts/validate-presenter-mode.mjs <deck.html>`：檢查演講備註與頁面 ID 等結構。
- `scripts/validate-swiss-deck.mjs <deck.html>`：檢查 Swiss 登記版型與相關規則。
- `scripts/check-presenter-runtime-sync.mjs`：檢查兩套模板的演講者模式核心區塊是否一致。
- `scripts/validate_project.py`：檢查本專案必要檔案、版本標記與網站內部連結。

需要 Node.js 的驗證腳本請先安裝相容版本。驗證腳本通過不代表已完成真實瀏覽器的視覺檢查；仍應在目標瀏覽器開啟簡報，測試鍵盤、總覽、演講者視圖、備註保存、觀眾同步、圖片載入、列印和不同螢幕尺寸。

## 7. 快速選擇

| 任務 | 建議模板 |
|---|---|
| 研究故事、文化案例、設計研究、主題演講 | `assets/template.html` |
| 研究數據、方法、流程、KPI、科技與比較分析 | `assets/template-swiss.html` |
| 教學工作坊、PBL 任務、課堂實作 | 依內容選 A 或 B；教學流程仍須清楚標示目標、步驟、時間、產出與評量 |
| 需要演講備註、排練或觀眾畫面同步 | 任一模板，並遵循 `references/presenter-mode.md` |

此專案仍保留學術內容保真、來源追溯、繁體中文、CRAP 雙輪檢查與完整原始碼交付要求；這些是本衍生版在上游網頁 PPT 機制之上的擴充。
