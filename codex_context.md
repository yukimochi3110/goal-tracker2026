# GOAL_TRACKER2026

## 概要
年間目標・毎日の習慣チェック・体組成データを管理するWebアプリ。Firebase でリアルタイム同期。GitHub Pages でホスティング。

## 技術スタック
- HTML / CSS / JavaScript（フレームワークなし、バニラJS）
- Firebase（Authentication + Firestore）
- Google Sign-In（ホワイトリスト制）
- Google Fonts（Noto Sans JP）
- Git 管理済み / GitHub Pages デプロイ

## ファイル構成
```
GOAL_TRACKER2026/
├── index.html          ← アプリ本体（CSS・JSすべて内包）
├── favicon.svg
├── apple-touch-icon.png
├── GOAL_TRACKER_SPEC.md  ← 詳細仕様書
├── make_icon.py
└── patch_css.py
```

## 主な機能
1. **月間カレンダーページ** — 習慣チェック（◎/◯/✗/−）、達成率リング、ストリーク表示、デイリーメモ
2. **年間サマリーページ** — 年間目標テキスト、月別達成率テーブル（80%+=緑、50%+=黄、<50%=赤）
3. **体組成データページ** — 体重・体脂肪率・体年齢の入力・グラフ・履歴
4. **設定モーダル** — 目標名・アイコン・カラー・頻度（毎日/平日のみ/週末のみ/月次）のカスタマイズ

## デフォルト目標
- 早起き（sunrise, moss, 平日）
- 運動（run, coral, 毎日）
- 読書（book, sky, 毎日）
- 副業（briefcase, plum, 平日）

## Firebase データ構造
```
/users/{userId}/
├── goals/                    ← 目標定義
├── checks/{year-month}/{day-goalId}  ← デイリーチェック値
├── memos/{year-month}/{day}  ← デイリーメモ
├── monthMemos/{year-month}   ← 月次サマリーメモ
├── yearGoals/{year}          ← 年間目標テキスト
├── yearMemos/{year}          ← 年間メモ
└── bodyData/{year-month}     ← 体組成データ
```

## デザイン仕様
- メインカラー: モスグリーン `#5B8C6F`
- レスポンシブ: max-width 540px（モバイルファースト）
- ライト/ダークモード対応（CSSカスタムプロパティ）
- `prefers-reduced-motion` 考慮済み

## 注意事項
- CSS は単一の `<style>` タグに内包（`patch_css.py` でビルド）
- `GOAL_TRACKER_SPEC.md` に詳細仕様あり（変更前に必ず参照）
- ビルドツール不要、ブラウザで直接開いて動作確認できる
