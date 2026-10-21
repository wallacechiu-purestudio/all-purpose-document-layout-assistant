# Guizang PPT 模板效能整合手冊

本手冊把「引用上游 Skill 的規則」與「真正執行上游 HTML 模板」分開。它是 v2.1.0 的核心工作流程。

## 1. 先釐清：上游不是五套完整模板

上游 Guizang PPT Skill 的主要可執行 deck 是兩套完整 HTML：
- `assets/template.html`：Editorial／電子雜誌 × E-ink，含背景 shader、字體、頁面骨架、翻頁與演講者模式。
- `assets/template-swiss.html`：Swiss／瑞士國際主義，含獨立網格、版型 class、主題色、翻頁與演講者模式。

其餘重要資源是配套資料庫，而不是可互換的五套完整 HTML：
- `references/layouts.md`：Editorial 版型目錄與使用規則。
- `references/layouts-swiss.md`：Swiss 版型目錄。
- `references/themes.md`、`references/themes-swiss.md`：主題色。
- `references/components.md`：元件語法。
- `references/presenter-mode.md`：演講者模式、講稿、計時、觀眾屏同步與現場控制。
- `references/checklist.md`、`references/swiss-layout-lock.md`：驗收與 Swiss 版型鎖定規則。
- `assets/motion.min.js`：本地動效資源。

本衍生版提出的五種選項（Swiss Grid、Editorial、E-ink、Academic、Workshop）是**本專案額外的視覺預設／工作流程選項**，不應宣稱為上游提供的五套完整模板。前兩者應直接使用上游完整模板；Academic／Workshop 是衍生版的自有設計系統，可借鑑上游排版原則，但不能假裝已經是上游模板。

## 2. 關鍵限制：System Instructions 不會自動載入 GitHub 檔案

在 Google AI Studio 的 System Instructions 中寫入 GitHub 路徑，不等於把該路徑的 HTML、CSS、JS 與 references 放進模型上下文。除非使用者明確將相關檔案上傳／加入專案上下文，或執行環境有真正可用的檔案讀取工具，否則模型無法直接「使用」這些本地模板。

因此，產出品質不佳時，不應只把提示詞寫得更長。必須先確認模型實際取得完整模板原始碼。

## 3. 三種環境的正確執行方式

### A. Codex／Claude Code 等可讀取工作目錄的 Agent

1. 先讀本地 `SKILL.md`。
2. 依任務讀取對應的完整 HTML 模板、layout database、theme、components、presenter mode 與 checklist。
3. 將完整 HTML 模板複製到專案輸出路徑，再替換 `<!-- SLIDES_HERE -->` 等指定佔位區。
4. 從正確的 layout database 選取已登記的頁面骨架，按頁面溝通任務配置版型。
5. 保留上游必要的 CSS、shader、翻頁、演講者模式與資源引用；不得把完整模板縮減成幾個普通卡片。
6. 執行專案內驗證腳本，並依環境能力進行瀏覽器測試；未執行的測試不得宣稱通過。

### B. Google AI Studio（無 GitHub 檔案讀取工具）

1. 不可只貼 `AI-STUDIO-INSTRUCTIONS.md` 後期待它自動讀取 GitHub。
2. 將以下檔案作為專案上下文／附件提供：`assets/template.html`、`assets/template-swiss.html`、對應的 layouts、themes、components 與 presenter-mode 文件。
3. 若介面無法加入全部檔案，先決定使用 Editorial 或 Swiss 其中一套，至少提供該完整模板及相對應 layout database；不要只提供範本截圖或提示詞摘要。
4. 明確要求模型把選定的完整模板程式碼整合到生成 App／HTML 中，並檢查輸出程式碼確實含有模板中的結構、CSS 與互動，而非只生成相似外觀。
5. 若目標是讓 App 本身提供樣板切換，必須在 App 程式碼中實作模板渲染器／樣板資料與切換狀態；單靠生成提示詞不會自動帶來互動功能。

### C. 只有一段提示詞、不能讀檔的環境

誠實告知無法直接使用上游原始模板；可以生成衍生風格，但不能聲稱已完整運用上游 HTML／演講者模式／WebGL 資源。建議改用可讀取倉庫的 Agent，或先把模板作為附件提供。

## 4. 生成網頁 PPT 的必走流程

### 第一步：需求與風格

確認受眾、簡報目的、時長／頁數、來源素材、圖片需求、語言及風格。資訊充分就直接開始；缺少會影響設計的關鍵資訊時才提問。

### 第二步：選擇「真正的基底模板」

- Editorial／E-ink：使用完整 `assets/template.html` + `references/layouts.md` + `references/themes.md`。
- Swiss／Grid：使用完整 `assets/template-swiss.html` + `references/layouts-swiss.md` + `references/themes-swiss.md`。
- Academic／Workshop：使用本衍生版模板或依需求建立獨立設計系統；不能把它標示成上游原始模板。

**一份 deck 只能選一套上游基底模板。** 不可混用兩套模板中同名但語義不同的 class。

### 第三步：建立內容架構與版型分配表

先輸出內部規劃表：頁碼、單頁主旨、支持證據、選用 layout ID、圖片槽位／比例、主題色、來源。不同頁面依任務使用不同版型，不可整份簡報都是相同卡片。Swiss 風格需遵守 `swiss-layout-lock.md`，正文頁使用登記的 S01–S22 骨架。

### 第四步：把內容放進原模板

- 保留模板原有的整體 DOM、CSS、背景 shader、鍵盤翻頁、總覽、演講者模式與講稿資料契約。
- 只替換指定的 slide 區塊、內容資料、標題、來源及講稿。
- 不可因為「方便」而改成簡單的 `<div class="card">` 清單，或只仿造模板配色。
- 需要圖片時，先定義槽位，再按 `references/image-prompts.md` 產圖；使用者提供的截圖要遵守保真規則。

### 第五步：品質檢查

至少檢查：
- 版型是否來自正確的 layout database。
- 模板專屬 class 是否正確、兩套上游模板是否被混用。
- 16:9 比例、文字溢位、圖像裁切、對比、字級、頁面節奏。
- 鍵盤翻頁、總覽、演講者模式與匯出等功能是否保留。
- 事實、數據、引文及來源是否有根據。
- HTML 是否能獨立開啟、資源是否可用。
- 實際執行哪些測試、哪些未測試，需如實列出。

## 5. 多樣樣板選擇器的架構建議

若產品需要使用者自行選擇五套風格，請把「五套風格選項」視為產品層的 renderer／theme selector，而不是假設上游有五個模板：

| 選項 | 建議實作 |
|---|---|
| Swiss Grid | 上游 Swiss 模板 + Swiss layouts + Swiss themes |
| Editorial | 上游 Editorial 模板 + Editorial layouts + Editorial themes |
| E-ink 極簡 | 以 Editorial 模板為基底的明確 E-ink theme／layout preset；需保持可辨識的差異 |
| Academic 經典 | 衍生版獨立模板／renderer，適合論文、方法、結果與參考文獻 |
| Workshop 活力 | 衍生版獨立模板／renderer，適合任務、流程、活動與評量 |

六組配色應作為各 renderer 的獨立 theme tokens，套用到所有頁面、圖表、頁碼、背景與控制元件。切換時只改視覺 tokens／layout preset，不得重寫內容資料。

如果產品真正需要將 Editorial 與 Swiss 完整模板即時互切，需設計明確的 template adapter 或分離 renderer，不能只用 CSS 改一個 class 來宣稱已切換完整模板。

## 6. 交付聲明

使用下列明確描述之一：
- 「已直接使用上游完整 HTML 模板與相應版型資料庫」：只有確實讀取並沿用原始程式碼時可用。
- 「以衍生版樣板實作類似視覺風格」：只借鑑原則或做 CSS 模擬時使用。
- 「未能載入上游原始模板」：執行環境沒有檔案讀取能力時使用。

來源： https://github.com/op7418/guizang-ppt-skill
