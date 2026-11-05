# Zevero EN → JA glossary

Product-specific terminology for the Zevero carbon accounting platform, extracted from
`src/locales/ja/messages.po`. Use these renderings verbatim — they are the approved product
terms. Do **not** re-derive them from the literal English.

General UI vocabulary (Save, Cancel, Close, Next, Search, Help, Last updated, File…) is
deliberately excluded; translate those normally.

## Contents

- [Rules](#rules) — Latin-script terms and non-obvious conventions
- [Watch out — translations that are NOT literal](#watch-out--translations-that-are-not-literal) — **read this first**
- [Product areas & navigation](#product-areas--navigation)
- [Period Lock (data approval) feature](#period-lock-data-approval-feature)
- [Org structure & entities](#org-structure--entities)
- [Users, roles, teams, permissions](#users-roles-teams-permissions)
- [Emission categories (GHG Protocol)](#emission-categories-ghg-protocol)
- [Activity data & records](#activity-data--records)
- [Emission factors & calculation](#emission-factors--calculation)
- [Reporting](#reporting)
- [Targets (Reduce)](#targets-reduce)
- [Data management, uploads, AutoFill](#data-management-uploads-autofill)
- [Governance & Social (ESG modules)](#governance--social-esg-modules)
- [Integrations](#integrations)
- [Japan-specific (Tokyo Gov)](#japan-specific-tokyo-gov)

---

## Rules

**Never translate / keep as Latin script:**

- `Zevero`, `Zevero Pro`
- `Scope`, `Scope 1`, `Scope 2`, `Scope 3` — kept as `Scope` in JA, **not** `スコープ`.
  So `By Scope` → `Scope別`, `Out of Scope` → `Scope外`, `Scope Breakdown` → `Scope の内訳`.
- `SBTi`, `GHGP`, `ISO 14064`, `ISO 14064-1`
- Units: `tCO₂e`, `kgCO2e`
- Integration vendor names: `Brewman`, `Netsuite`, `Unleashed`
- `API`, `Excel`

**Non-obvious conventions:**

- `Vehicle` as an entity (the thing you register) → `社用車` (company vehicle).
  `Vehicle` inside field labels (type, size, details) → `車両`.
- `Business Division` is an **org unit** (事業部門), never "business" in the commercial sense.
- `Facility` → `施設` (site/premises), never `工場`.
- `Measure`, `Analyse`, `Reduce`, `Reports` are **product areas** (nouns), not verbs.
- `Level` in org/record context → `階層` (hierarchy tier), not `レベル`.
- `Historic Data` / `Historical Data` both → `過去データ`. Treat as one term.
- Success toasts follow `<entity>を作成しました / 更新しました / 削除しました`, not `正常に`.

---

## Watch out — translations that are NOT literal

These are the most common source of wrong output. The JA is intentionally different from
the English.

| EN | JA | Why |
| --- | --- | --- |
| Period Lock / Period Locks | データ承認機能 | Feature name is "data approval", **not** `期間ロック` |
| Back to Period Locks | データ承認に戻る | |
| Go to Period Locks | ロック一覧に移動 | list view, not the feature name |
| Period Locks For Approval | 承認待ちのデータ | |
| Carbon | 活動データ | as a data-scope label = activity data |
| Emissions | 排出量内訳 | page/tab label = breakdown; the plain metric is `排出量` |
| Company Assets | リソース管理 | resource management |
| Assets | 事業・資産 | |
| Emission Factor Library | 金額ベース排出係数データベース | spend-based EF database |
| Spend Based Emissions Factors | 金額ベース排出係数データベース | same thing |
| Reductions | 目標設定 | the Reduce area = target setting |
| Ownership / Ownership status | 施設所有の有無 | whether the facility is owned |
| Control status (utilities) | 水道光熱費管理状況 | `Control Status` (title case) → `管理状況` |
| Guide | お役立ち資料 | resources, not "manual" |
| Operation Guide | 操作説明会録画 | recorded walkthrough |
| Intensity Metric | 指標 | |
| Physical Quantity | 物量ベース | quantity-based (vs spend-based) |
| Primary Data | １次データ | |
| Item Name / Item Description / Item Country | 製品・サービス名 / 製品・サービスの詳細 / 製品・サービスの原産国 | "item" = product or service |
| Matched / Pending (EF matching) | 確定 / 未確定 | confirmed / unconfirmed, not `マッチ済み` |
| From / To (lock request) | 申請者 / 承認者 | requester / approver, not sender/recipient |
| People | 関係者 | involved parties |
| Subdivisions | 区分 | |
| Licensed | ライセンスにより非公開 | hidden due to licensing |
| Locked permanently | 今後変更できなくなります | "can no longer be changed" |
| Stays Live | 更新継続 | keeps updating |
| Take me there | 作成ページへ移動 | |
| Understand Your Impact | 環境への影響を理解する | |
| Reset Password (submit button) | 更新 | |
| Franchise Dates | 日付 | |
| Transport Type | 種類 | |
| Target Notes | メモ | |
| Target Owner | 責任者 | |
| Your Details | ユーザ情報 | |
| Registered Country | 国 | |
| Not operationally controlled | 管理不可能 | |
| Diversity of Total Workforce | ダイバーシティ | |
| Fuel and Energy Related Activities | 燃料・エネルギー関連 | |
| JP Energy Conservation Report | 省エネ法レポート | Japanese Energy Conservation Act report |

**Known inconsistency:** `Out of Scope Emissions` appears as both `Scope外排出量` and
`スコープ外排出量`. Prefer `Scope外排出量`.

**Corrected here — three entries in `messages.po` are wrong.** They use Kangxi *radical*
codepoints instead of the real kanji. The characters look identical but are distinct, so they
break search, sorting, and any string matching against these terms. The tables below have been
corrected; use them as written and treat them as the intended values:

| Term (correct form, as written below) | Wrong codepoint still in `messages.po` | Correct |
| --- | --- | --- |
| 購入した製品・サービス | `⼊` U+2F0A | `入` U+5165 |
| 販売した製品の加工 | `⼯` U+2F2F | `工` U+5DE5 |
| 販売した製品の使用 | `⽤` U+2F64 | `用` U+7528 |

This means the glossary is deliberately no longer a byte-identical mirror of `messages.po` for
these three strings. Until the source file is patched, a term copied straight out of the running
product may not match what is written here, even though it looks the same on screen.

---

## Product areas & navigation

| EN | JA | Note |
| --- | --- | --- |
| Home | ホーム | |
| Measure | 測定 | product area (noun) |
| Analyse | 分析 | product area |
| Reduce | 削減 | product area |
| Reports | レポート | |
| Company Profile | 会社概要 | |
| Data Management | データ管理 | |
| Integrations | システム連携 | |
| User Management | ユーザー管理 | |
| Settings / User Settings | 設定 / ユーザー設定 | |
| Governance | ガバナンス | |
| Social | 社会 | |
| Resources | 資料 | |
| Webinars | ウェビナー | |
| Support | サポート | |
| Recently Visited | 最近閲覧した項目 | |
| Manage Widgets | ウィジェットを管理 | |
| Upgrade to Zevero Pro | Proにアップグレード | |
| Zevero Package | Zeveroパッケージ | |
| Zevero Consultant | Zeveroコンサルタント | |
| Maintenance in Progress | メンテナンス中 | |
| User Manual | 利用者マニュアル | |
| User Survey | 利用者アンケート | |

---

## Period Lock (data approval) feature

| EN | JA | Note |
| --- | --- | --- |
| Period Lock / Period Locks | データ承認機能 | feature name |
| Lock | ロック | |
| Locked | ロック中 | |
| Lock Period | データロック期間 | |
| Lock Mode | ロックの種類 | `Lock mode` (lowercase) → `ロックモード` |
| Lock Type | ロックの種類 | |
| Full Lock | フルロック | |
| Activity Input Lock | 活動データ入力ロック | |
| Activity Types to Lock | ロックする活動の種類 | |
| Business Division to be Locked | ロックする事業部門 | |
| Company to be Locked | ロックする会社 | |
| Lock Details | ロック詳細 | |
| Lock History | ロック履歴 | |
| Lock Report | ロックレポート | |
| Lock Approver | ロックの承認者 | |
| Reason for Lock | ロックの理由 | |
| Requestor's Reason For Lock | 申請者のロック理由 | |
| Requestor / Requester | 申請者 | |
| Approver | 承認者 | |
| Requester / Approver | 申請者 / 承認者 | |
| Request Lock / Submit Lock Request | ロックを申請 | |
| Cancel Lock Request | ロックリクエストをキャンセル | |
| Reject Lock Request | ロックリクエストを却下 | |
| Approve Lock | ロックを承認 | |
| Approve and Lock | 承認してロック | |
| Approve as Full Lock | フルロックとして承認 | |
| Approve and Upgrade to Full Lock | 承認してフルロックにアップグレード | |
| Upgrade to Full Lock | フルロックにアップグレード | |
| Submit Upgrade Request | アップグレードリクエストを送信 | |
| Submit Re-lock Request | 再ロックリクエストを送信 | |
| Re-lock | 再ロック | |
| Re-lock Period | 期間を再ロック | |
| Re-lock Approved / Rejected / Cancelled / Submitted | 再ロック承認済み / 再ロック却下 / 再ロックキャンセル済み / 再ロック申請済み | |
| Upgrade Approved - Full Lock Active | アップグレード承認済み - フルロック有効 | |
| Upgrade Rejected / Upgrade Cancelled | アップグレード却下 / アップグレードキャンセル済み | |
| Submitted For Approval | 承認申請済み | |
| Submitted For Approval - Full Lock | 承認申請済み - フルロック | |
| Approved - Lock Active | 承認済み - ロック有効 | |
| Approved - Full Lock Active | 承認済み - フルロック有効 | |
| Approved - Activity Input Lock Active | 承認済み - 活動データ入力ロック有効 | |
| Pending lock | ロック承認待ち | |
| Pending re-lock (approval) | 再ロック承認待ち | |
| Pending upgrade approval | アップグレード承認待ち | |
| Locked · upgrade pending | ロック中・アップグレード承認待ち | |
| Needs your approval | あなたの承認待ち | |
| Your requests | 自分の申請 | |
| You requested | あなたが申請 | |
| Remove Lock | ロックを削除 | |
| Temporarily Unlock | 一時的にロック解除 | `Temporarily unlocked` → `一時ロック解除中` |
| This period is locked | この期間はロックされています | |
| All locks / No matching locks / No period locks | すべてのロック / 一致するロックがありません / ロックがありません | |
| Snapshot captured at approval | 承認時のデータを保存します | pattern: `<event>時のデータを保存します` |
| Snapshot captured at submission | 申請時のデータを保存します | |
| Snapshot captured at re-lock request | 再ロック申請時のデータを保存します | |
| Snapshot captured at upgrade request | アップグレード申請時のデータを保存します | |
| What Full Lock Does | フルロックの動作 | |
| What Activity Input Lock Does | 活動データ入力ロックの動作 | |
| After You Submit / After You Approve | 送信後に起こること / 承認後に起こること | |
| What's Covered | 対象範囲 | |
| Remind on / Send a reminder | リマインド日 / リマインダーを送信 | |
| Download Lock Report | ロックレポートをダウンロード | |
| View audit log | 監査ログを表示 | |

---

## Org structure & entities

| EN | JA | Note |
| --- | --- | --- |
| Business Division | 事業部門 | validation msgs also use `事業区分`, `事業部` |
| Business Divisions | 事業部門 | |
| Business Division Level | 事業部門の階層 | |
| Business Division Comparison | 事業部門の比較 | |
| Business Division/Facilities Included | 含まれる事業部門/施設 | |
| Parent Division / Primary Company | 親会社 | |
| Direct Parent in Company Hierarchy | 会社階層における直接の親会社 | |
| Entity / Sub Entity | 事業体 / サブ事業体 | |
| Subdivisions | 区分 | |
| Facility | 施設 | |
| Company Facility / Company Facilities | 施設 / 会社施設 | |
| Facility Template | 施設テンプレート | |
| Facility Operations | 施設の運営 | |
| Facility Comparison | 施設の比較 | |
| Facility move in date / Move In Date | 施設使用開始日 / 使用開始日 | |
| Move Out Date | 退去日 | |
| I have moved out | 施設退去済み | |
| Floor Area / Occupied Floor Area | 床面積 / 専有床面積 | |
| Ownership Status | 所有状態 | but bare `Ownership status` → `施設所有の有無` |
| Allocation percentage of facility | 施設の配分率 | |
| Franchise / Franchises | フランチャイズ | |
| I have closed this franchise | このフランチャイズを閉鎖しました | |
| Investment / Investments | 投資 | |
| I have sold this investment | この投資を売却しました | |
| Equity Percentage | 株式の割合 | |
| Vehicle / Vehicles | 社用車 | entity = company vehicle |
| Vehicle Type | 社用車の種類 | |
| Vehicle Details / Vehicle Type and Size | 車両の詳細 / 車両の種類とサイズ | field labels use `車両` |
| Vehicle Attribution | 車両の紐付け | |
| Vehicle Identifier / Equipment Identifier | 車両識別子 / 設備識別子 | |
| Log Vehicle Use / Edit Vehicle Use | 車両使用を入力 / 車両使用の編集 | |
| I no longer operate this vehicle | この車両はもう使用していません | |
| Company-wide | 全社 | |
| Registered Location | 登録地 | |
| Location Based / Location-Based | ロケーション基準 | |
| Market Based / Market-Based | マーケット基準 | lowercase variants use `市場ベース` / `ロケーションベース` |

---

## Users, roles, teams, permissions

| EN | JA | Note |
| --- | --- | --- |
| Roles & Permissions | ロールと権限 | |
| Role | ロール | not `役割` |
| User Role / User Roles | ユーザーロール | |
| Default Role | デフォルトロール | |
| Role Description / Role Name | ロール説明 / ロール名 | |
| Feature Permissions | 機能権限 | |
| Workspace Owner | ワークスペースオーナー | top-level role |
| Admin | 管理者 | |
| User | ユーザー | |
| Auditor | 監査者 | |
| Consultant | コンサルタント | |
| Team / User Teams | チーム | |
| Default Team | デフォルトのチーム | |
| Access | 権限 | |
| All Access | 制限なし | |
| No Environment Access | 環境へのアクセスがありません | |
| Select an Environment | 環境を選択 | |
| Remove Access | アクセス権を削除 | |
| Approver Permission Revoked | 承認者権限の取り消し | |
| Approver Changed | 承認者変更 | |
| Invite Users | ユーザーを招待 | |
| Job Title | 役職 | |
| Assignee / Unassigned | 担当者 / 担当者なし | |
| Assign Task | タスクを割り当てる | |

---

## Emission categories (GHG Protocol)

| EN | JA | Note |
| --- | --- | --- |
| Scope 1 / Scope 2 / Scope 3 | Scope 1 / Scope 2 / Scope 3 | Latin, unchanged |
| Scope Breakdown | Scope の内訳 | |
| In-Scope Emissions | Scope内排出量 | |
| Out-of-Scope Emissions | Scope外排出量 | |
| Optional Emissions | 任意の排出量 | |
| GHGP Category | GHGPカテゴリ | |
| Carbon Categories / Emission Categories | 排出カテゴリ | |
| Category Group | カテゴリグループ | |
| Stationary Combustion | 固定燃焼 | |
| Mobile Combustion | 移動燃焼 | |
| Fugitive Emissions | 漏洩排出 | `Fugitive Emitter` → `漏洩排出` |
| Process Emissions | プロセス排出 | |
| Purchased Electricity | 購入した電気 | |
| Purchased Heat and Steam | 購入した熱・蒸気 | |
| Purchased Goods and Services | 購入した製品・サービス | |
| Purchased Goods (Spend-Based) | 購入した商品 (金額ベース) | |
| Purchased Goods (Quantity-Based) | 購入した商品 (数量ベース) | |
| Capital Goods | 資本財 | spend-based variant: `資本財（金額ベース）` |
| Fuel and Energy Related Activities | 燃料・エネルギー関連 | `Fuel Energy Related Activities` → `燃料・エネルギー関連活動` |
| Upstream Transportation and Distribution | 運輸・配送（上流） | |
| Downstream Transportation and Distribution | 輸送、配送（下流） | note: different verb from upstream |
| Waste Generated in Operations | 事業から出る廃棄物 | |
| Business Travel | 出張 | |
| Employee Commute / Employee Commutes | 従業員の通勤 | |
| Upstream Leased Assets | リース資産（上流） | |
| Downstream Leased Assets | リース資産（下流） | |
| Franchises | フランチャイズ | |
| Investments | 投資 | |
| Processing of Sold Products | 販売した製品の加工 | |
| Use of Sold Products | 販売した製品の使用 | |
| End of Life of Sold Products | 販売した製品の廃棄 | |
| Sold Products | 販売した製品 | |
| Upstream / Downstream | 上流 / 下流 | |

---

## Activity data & records

| EN | JA | Note |
| --- | --- | --- |
| Activity Data / Activity Records | 活動データ | |
| Activity Type | 活動の種類 | |
| Activity Data Files | 活動データファイル | |
| Records | レコード | |
| Add Record | 記録を追加 | |
| Earliest record / Latest record | 最も古いデータ / 最新のデータ | |
| Total Records | 総レコード数 | |
| Manual Entry | 手動入力 | |
| Electricity Type | 電気の種類 | |
| Fuel Type / Fuel Used | 燃料の種類 / 使用燃料 | |
| Refrigerant Type | 冷媒の種類 | |
| Waste Material Type / Waste Type | 廃棄物の種類 | |
| Water Type | 水の種類 | |
| Process Emissions Type | プロセス排出タイプ | |
| Treatment / Treatment Type | 処理 / 処理方法 | |
| Consumption | 消費量 | |
| Energy Consumed / Energy Generated | エネルギー消費量 / 発電量 | |
| Sold Energy | 売電量 | |
| Leaked Amount | 漏洩量 | |
| Process waste percentage | 工程廃棄物の割合 | |
| Waste % | 廃棄物の割合 | |
| Spend / Spend Based | 金額 / 金額ベース | |
| Spend Category | 支出区分 | `Provider Spend Category` → `プロバイダー支出区分` |
| Mass per Item (kg) | アイテムあたりの質量（kg） | |
| Supplier / Supplier Country | サプライヤ / サプライヤの国 | selector text uses `サプライヤー` |
| Transport Method / Transport Details | 交通手段 / 交通手段の詳細 | |
| Number of Travellers | 利用人数 | `Travellers` → `乗客数` |
| Date of Travel / Travel Name | 出張日 / 出張名 | |
| Courier | 宅配業者 | |
| Date of Use / Date in Use | 使用日 | |
| Operational Date | 運用開始日 | `Vehicle Operational Date` → `車両運用日` |
| Evidence / Upload Evidence | 証拠 / エビデンスをアップロード | |
| Commute Survey | 通勤アンケート | |
| Employee Commute Survey Link | 従業員の通勤排出量アンケートリンク | |
| Survey Period | アンケート期間 | |

---

## Emission factors & calculation

| EN | JA | Note |
| --- | --- | --- |
| Emission Factor / Emissions Factor | 排出係数 | |
| Emission Factor Name / Source / Year | 排出係数名 / 排出係数ソース / 排出係数年 | |
| Custom emission factor | カスタム排出係数 | |
| Emission Factor Library | 金額ベース排出係数データベース | |
| EF Matching Status | 排出係数マッチングステータス | |
| Unmatched EF Records | 排出係数が未マッチのレコード | |
| Matched / Pending | 確定 / 未確定 | |
| Calculation Level | 計算レベル | |
| Data Quality | データ品質 | |
| Averaged Data | 平均値 | `This data is averaged` → `このデータは平均値です` |
| Primary Data | １次データ | |
| Associated Emissions | 関連排出量 | |
| Individual Emission | 個別の排出 | |
| Emissions Over Time | 排出量の推移 | |
| Highest Emitter / Highest Emitters | 最大排出 / 排出量上位 | |
| Emissions by Business Division | 事業部門別の排出量 | |
| Emissions by Facility | 施設別の排出量 | |
| Emissions by Category | カテゴリ別排出量 | |
| Category & Item Breakdown | カテゴリ・項目別内訳 | |
| Item Breakdown | 項目別内訳 | |
| % of category / % of total | カテゴリ内の割合 / 合計に占める割合 | |
| of total emissions | 総排出量に対する割合 | |
| vs Last Reporting Year-To-Date | 前報告年度累計との比較 | |
| Unit of Measurement / Unit Measurement | 測定単位 | |

---

## Reporting

| EN | JA | Note |
| --- | --- | --- |
| Reporting Period | 報告期間 | |
| Carbon Reporting Period | 排出量報告期間 | |
| Governance Reporting Period | ガバナンスの報告期間 | |
| Social Reporting Period | 社会の報告期間 | |
| Reporting Year | 報告年 | validation uses `報告年度` |
| Baseline Year | 基準年 | |
| Reporting Approach | 報告方法 | |
| Reporting Level | 報告レベル | |
| Period Covers | 対象期間 | |
| Primary period / Compare period | 基準期間 / 比較期間 | |
| Carbon Report | 排出量レポート | |
| Emission Reports | 排出量レポート | |
| Category Report | カテゴリレポート | |
| Scope Report | Scopeレポート | |
| Disclosure Report / Disclosure Reports | 開示レポート | |
| Governance Report / Governance Reports | ガバナンスレポート | |
| Social Report / Social Reports | 社会レポート | |
| Data Report | レポート | |
| ISO 14064 Report | ISO 14064レポート | |
| ISO 14064-1 Report | ISO 14064-1 レポート | |
| JP Energy Conservation Report | 省エネ法レポート | |
| Generated Reports | 生成したレポート | |
| Report Summary | レポートの概要 | |
| Report Type | レポートの種類 | |
| Download coverage report | カバレッジレポートをダウンロード | |
| Full Year / Previous Full Years | 通年 / 過去の通年 | |
| 1st Half / 2nd Half | 上半期 / 下半期 | |
| Quarter 1–4 | 第1四半期〜第4四半期 | |
| Monthly / Yearly | 月次 / 年次 | |
| Time Period Format | 期間形式 | |

---

## Targets (Reduce)

| EN | JA | Note |
| --- | --- | --- |
| Reductions | 目標設定 | area name = target setting |
| Target Setting / Setting Your Target | 目標設定 | |
| Company Target | 会社目標 | |
| SBTi - Company Target | SBTi - 会社目標 | |
| SBTi Aligned / Non SBTi Aligned | SBTiに準拠 / SBTiに準拠なし | |
| Near Term Target Year | 短期目標の年 | |
| Long Term Target Year | 長期目標の年 | |
| Target Type | 目標の種類 | |
| Target Owner | 責任者 | |
| Target Notes | メモ | |
| Target Projection | 目標予測 | |
| Emission Target Forecast | 排出量目標予測 | |
| Target Guide | 目標ガイドライン | |
| Scope 1 & 2 Reduction % | Scope 1 および 2の削減 % | |
| Scope 3 Reduction % | Scope 3の削減% | |
| Intensity Metric | 指標 | |
| Absolute | 絶対値 | |

---

## Data management, uploads, AutoFill

| EN | JA | Note |
| --- | --- | --- |
| Historic Data / Historical Data | 過去データ | |
| Historical Data Records | 過去データ | |
| Historical Data Upload | 過去データアップロード | |
| Historic Data Deletion | 過去データ削除 | |
| Disable Historic Data | 過去データを無効化 | |
| Excel Upload / Excel Template | Excelアップロード / Excelテンプレート | |
| Facility Upload Files | 施設のアップロードファイル | |
| Queued Files / My Files | ファイル一覧 | |
| Relevant Files | 関連するファイル | |
| Uploads Processing | アップロード処理中 | |
| Uploaded By | アップロード者 | |
| AutoFill Data | データを自動入力 | |
| AutoFill Data From File / From Images | ファイルからデータを自動入力 / 画像からデータを自動入力 | |
| AutoFill Categories | 自動入力カテゴリ | |
| AutoFill Active | 自動入力有効 | |
| Reading AutoFill File | 自動入力ファイルの読み込み中 | |
| Use autofill file as evidence | 自動入力ファイルをエビデンスとして使用する | |
| Scan Files | 画像ファイルをスキャン | |
| Save as template / Use Template | テンプレートとして保存 / テンプレートを使用 | |
| Emission Category Template | 排出カテゴリテンプレート | |
| Zevero facility template | Zevero施設テンプレート | |
| Zevero historic template | Zevero過去データテンプレート | |

---

## Governance & Social (ESG modules)

| EN | JA | Note |
| --- | --- | --- |
| Governance Data / Social Data | ガバナンスデータ / 社会データ | |
| Governance Record Level | ガバナンスデータの記録階層 | `Level` = hierarchy tier |
| Social Record Level | 社会データの記録階層 | |
| Governance Categories / Social Categories | ガバナンスカテゴリ / 社会カテゴリ | |
| Governance Category Template | ガバナンスカテゴリテンプレート | |
| Social Category Template | 社会カテゴリテンプレート | |
| Social Profile | 社会プロフィール | |
| Governance Data Deletion / Social Data Deletion | ガバナンスデータの削除 / 社会データの削除 | |
| Anti-Corruption | 腐敗防止 | |
| Anti-Competitive Practices | 反競争的行為 | |
| Occupational Health & Safety | 労働安全衛生 | + `マネジメント` for Management |
| Diversity of Total Workforce | ダイバーシティ | |
| Hiring / Total No. of Hires | 新規採用 / 採用人数合計 | |
| Turnover / Total Turnover | 離職率 / 総離職率 | **not** revenue |
| Training Hours | 研修時間 | |
| Dissemination policy | 情報の配布ポリシー | |
| Person Responsible | 責任者 | |

---

## Integrations

| EN | JA | Note |
| --- | --- | --- |
| Integration / Integrations | システム連携 | |
| Connect / Disconnect | 連携 / 連携解除 | |
| Connect Your Brewman Account | Brewmanアカウント連携 | pattern: `<vendor>アカウント連携` |
| Not Connected | 未接続 | |
| Account Connected | アカウントが接続されました | |
| Get Your Credentials | クレデンシャルを取得 | |
| Access Token | アクセス・トークン | |
| Consumer Key / Consumer Secret | コンシューマー・キー / コンシューマー・シークレット | |
| Token Secret | トークン・シークレット | |
| API Key / API Token / API ID | APIキー / APIトークン / API ID | |
| Account ID / Tenant ID | アカウントID / テナントID | |
| Provider | プロバイダー | |

---

## Japan-specific (Tokyo Gov)

| EN | JA | Note |
| --- | --- | --- |
| (bureau name) | 局名 | JA-only field, no EN source |
| (section name) | 課名 | JA-only field |
| (department name) | 部門名 | JA-only field |
