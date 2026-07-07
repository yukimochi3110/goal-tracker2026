# 目標管理アプリ「Goal Tracker」仕様書

## 概要

年間目標の設定・毎日の習慣チェック・体組成データの記録を一元管理するWebアプリ。
PC・スマホの両方からブラウザでアクセスし、データはFirebaseで自動同期する。

- 公開方法: GitHub Pages（静的サイト）
- データ保存: Firebase Firestore
- 認証: Firebase Authentication（Googleログイン）
- セキュリティ: ホワイトリスト制限（指定Googleアカウントのみログイン可能）
- レスポンシブ対応: PC・スマホ両対応

---

## 技術スタック

- フロントエンド: HTML + CSS + JavaScript（フレームワークなし、またはReact）
- データベース: Firebase Firestore
- 認証: Firebase Authentication（Google Sign-In）
- ホスティング: GitHub Pages
- GitHubアカウント: yukibe846

---

## ページ構成

アプリは3つのメインページ＋設定画面で構成される。

### ページ1: 月間カレンダー（メイン画面）

#### 月ナビゲーション
- 左右矢印で前月・翌月に移動
- 中央に「2026年 4月」のように年月を表示

#### 達成率サマリー（月上部）
- 目標ごとにラジアルリング（円形プログレス、SVGで実装）と達成率（%）を表示
- ラジアルリングの内側に達成率の数値を28px/700で表示（ヒーロー数字）
- リングの下にアイコン＋目標名を表示
- 目標が多い場合は横スクロール対応のフレックスレイアウトで並べる
- ストリーク（連続達成日数）が1日以上の目標には、リング右上に連続日数バッジを表示（例: 「🔥 12」の代わりにSVGの炎アイコン＋数字）

#### カレンダー本体
- 日付が縦に並ぶリスト型カレンダー
- ヘッダー行: 「日付」+ 各目標のアイコン＋目標名（テキスト表示必須）
- 各日の行:
  - 日付（数字＋曜日）
  - 目標ごとのチェック欄: プルダウンで「−」「◎」「◯」「✗」を選択
  - メモボタン: クリックで展開
- 土日は背景色を変える（薄いベージュ系）
- 日曜は赤系、土曜は青系の文字色
- 展開中の日は左ボーダーでハイライト

#### チェック欄の表示
- 「◎」: 目標カラーの薄い背景 + 濃い文字
- 「◯」: 白背景 + 目標カラー文字
- 「✗」: 薄い赤背景 + 赤文字
- 「−」（未入力）: グレー文字

#### メモ欄（日ごと、展開式）
- 1日につき1つのメモ欄（テキストエリア）
- メモ欄の上に目標ボタンを並べる（アイコン＋名前）
- ボタンを押すと `[目標名] ` がメモに挿入される（目標の識別用）
- メモがある日はアイコンで表示

#### 月のまとめメモ
- カレンダーの下にテキストエリアを配置
- その月の振り返りや感想を自由記述

#### 達成率の計算ロジック
- 「◎」と「◯」を達成としてカウント
- 「✗」は未達成
- 「−」（未入力）はカウントしない
- 分母は「その月でその目標をトラッキングすべき日数」（頻度設定に基づく）

---

### ページ2: 年間サマリー

#### 年ナビゲーション
- 左右矢印で前年・翌年に移動

#### 年間目標
- テキストエリアで自由記述

#### 月別達成率テーブル
- 行: 各目標（アイコン＋名前）
- 列: 1月〜12月 + 年間
- 各セルに達成率の数値を表示
- 色分け: 80%以上=緑系、50%以上=黄系、それ以下=赤系

#### 年間メモ
- テキストエリアで自由記述

---

### ページ3: 体組成データ

#### データ入力フォーム
- 年月の選択（プルダウン）
- 入力項目: 体重(kg)、体脂肪率(%)、体内年齢
- 「記録する」ボタン
- 同じ年月のデータがある場合は上書き

#### 推移グラフ
- 体重: 棒グラフ（メインで大きく表示）
- 体脂肪率: 小さめの棒グラフ
- 体内年齢: 小さめの棒グラフ
- 各バーの上に数値を表示
- X軸に月を表示

#### 記録一覧テーブル
- 年月、体重、体脂肪率、体内年齢を表形式で表示
- 各行に削除ボタン

---

### 設定画面（モーダル）

#### 既存目標の一覧
- アイコン＋名前＋頻度ラベル＋削除ボタン

#### 目標の追加フォーム
- 目標名の入力欄
- アイコン選択（SVGラインアイコンを複数用意、グリッド表示で選択）
- カラー選択（6色のカラーパレットから選択）
- 頻度選択（プルダウン）: 毎日 / 平日のみ / 土日のみ / 月1回
- 「追加する」ボタン

---

## 目標の頻度設定

各目標に以下の頻度を設定可能。カレンダー上で対象外の日はチェック欄が「·」（非活性）になる。

| 頻度 | 対象日 |
|------|--------|
| 毎日 | すべての日 |
| 平日のみ | 月〜金 |
| 土日のみ | 土・日 |
| 月1回 | 各月1日のみ |

---

## デザイン仕様

### 全体の方向性
- ナチュラル・クリーンなテイスト
- モスグリーン基調の落ち着いた配色
- 絵文字は一切使わない（SVGラインアイコンを使用）
- ヘッダーやラベルには必ずテキストで目標名を表示する
- 余白を十分に取り、見やすさを重視
- 達成率などの数値は大きく表示して達成感を演出する
- チェック操作時にマイクロアニメーションを付けてフィードバックを明確にする
- ダークモード対応（`prefers-color-scheme: dark` メディアクエリで切り替え）

### カラーパレット

目標ごとに以下6色から選択:

| 名前 | Primary | Light | Mid | Accent |
|------|---------|-------|-----|--------|
| moss | #5B8C6F | #EBF3EE | #A8CCAF | #3D6B4F |
| coral | #C4735A | #F8EDE8 | #E0A890 | #9E5640 |
| sky | #5A8FAD | #E6F0F5 | #8DBDD4 | #3A6F8D |
| plum | #8B6F8E | #F0E8F0 | #B8A0BA | #6B4F6E |
| amber | #B08C3E | #F5F0E0 | #D4BE7A | #8A6C20 |
| slate | #6B7C85 | #E8ECEE | #9AABB5 | #4C5D66 |

### UIパーツの色（CSS変数で定義し、ダークモードで上書き）

ライトモード:
- `--color-bg`: #FFFFFF
- `--color-bg-sub`: #F7FAF8
- `--color-text`: #2D3A32
- `--color-text-sub`: #8A998E
- `--color-border`: #E6EAE6
- `--color-header`: #4A6A52
- `--color-accent`: #5B8C6F
- `--color-weekend-bg`: #FAF7F4
- `--color-sunday`: #B85050
- `--color-saturday`: #5080B0

ダークモード（`@media (prefers-color-scheme: dark)` で上書き）:
- `--color-bg`: #1A1F1C
- `--color-bg-sub`: #242B26
- `--color-text`: #E8EFE9
- `--color-text-sub`: #7A8A7E
- `--color-border`: #323D35
- `--color-header`: #7AB890
- `--color-accent`: #7AB890
- `--color-weekend-bg`: #1F2820
- `--color-sunday`: #D47070
- `--color-saturday`: #70A0D0

### タイポグラフィ
- フォント: Noto Sans JP（Google Fonts）
- アプリ名: 15px, 700, letter-spacing: 3px, uppercase
- ナビゲーション: 13px, ピル型バッジスタイル（アクティブ時はアクセントカラーの背景＋白文字）
- カードヘッダー: 13px, 600
- 本文: 14px, 400
- 達成率の数値（ヒーロー数字）: 28px, 700（月上部サマリーやストリークの連続日数などに使用）
- 月見出し（年月表示）: 20px, 700

### ナビゲーション
- 画面上部または下部にボトムナビゲーションバーを配置（スマホ標準パターン）
- アクティブなタブは目標カラー（アクセント: #5B8C6F）の背景＋白文字のピル型バッジで強調
- 非アクティブタブはサブテキストカラー（--color-text-sub）で控えめに表示

### マイクロアニメーション
- チェック欄で「◎」「◯」「✗」を選択したとき: 0.15sのフェードイン＋軽いスケール（`transform: scale(1.08)` → `1.0`）
- 「◎」選択時: 目標のPrimaryカラーでリップルエフェクト（CSS `@keyframes` で実装）
- ラジアルリングの数値更新時: 0.3sのカウントアップアニメーション
- ストリークバッジの初表示時: バウンスアニメーション（`@keyframes bounce`）
- すべてのアニメーションは `prefers-reduced-motion: reduce` メディアクエリを尊重し、その場合はアニメーションなしにフォールバック

### アイコン（SVGラインアイコン）

以下のアイコンを用意する（stroke-basedのSVGで、色をpropsで変更可能）:

sunrise, run, book, pen, target, heart, star, leaf, moon, coffee, music, briefcase, home, zap, smile, settings

### レスポンシブ対応
- 最大幅: 540px（中央寄せ）
- スマホでも快適に操作できるタップサイズ
- テーブルは横スクロール対応

---

## Firebase データ構造

```
users/{userId}/
  ├── goals/            # 目標の設定
  │   └── {goalId}: {
  │         name: string,
  │         icon: string,
  │         frequency: "daily" | "weekdays" | "weekends" | "monthly",
  │         colorIdx: number,
  │         order: number,
  │         createdAt: timestamp
  │       }
  │
  ├── checks/           # 毎日のチェックデータ
  │   └── {year-month}/
  │       └── {day-goalId}: "◎" | "◯" | "✗" | ""
  │
  ├── memos/            # 日ごとのメモ
  │   └── {year-month}/
  │       └── {day}: string
  │
  ├── monthMemos/       # 月のまとめメモ
  │   └── {year-month}: string
  │
  ├── yearGoals/        # 年間目標
  │   └── {year}: string
  │
  ├── yearMemos/        # 年間メモ
  │   └── {year}: string
  │
  └── bodyData/         # 体組成データ
      └── {year-month}: {
            weight: number | null,
            fat: number | null,
            age: number | null
          }
```

---

## Firebase セキュリティルール

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId}/{document=**} {
      // 本人のみ読み書き可能
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

さらに、Firebase Authentication の設定で、許可するGoogleアカウントをホワイトリストで制限する（実装時に確認）。

---

## セットアップ手順（開発時の参考）

### 1. Firebase プロジェクト作成
1. https://console.firebase.google.com/ にアクセス
2. 新規プロジェクト作成（例: goal-tracker）
3. Firestoreデータベースを有効化（本番モード）
4. Authentication → Google プロバイダを有効化
5. プロジェクト設定からWebアプリを追加、Firebase設定情報を取得

### 2. アプリ開発
1. 上記の仕様に基づいてHTML/CSS/JSを作成
2. Firebase SDK を CDN から読み込み
3. Googleログイン機能を実装
4. Firestoreへの読み書きを実装

### 3. GitHub Pages デプロイ
1. yukibe846 のGitHubリポジトリに push
2. Settings → Pages → デプロイ設定

---

## CSSに関する注意

- CSSは要素ごとに1行で記述する（ゆきえの好みのフォーマット）

例:
```css
.header { display: flex; align-items: center; justify-content: space-between; padding: 10px 16px; }
.card { background: #fff; border-radius: 10px; border: 1px solid #E6EAE6; margin-bottom: 14px; overflow: hidden; }
```

---

## 初期データ（デフォルト目標）

アプリ初回起動時に以下の目標を仮で表示する（ユーザーが自由に変更・削除可能）:

| 目標名 | アイコン | 頻度 | カラー |
|--------|----------|------|--------|
| 早起き | sunrise | 平日のみ | moss |
| 運動 | run | 毎日 | coral |
| 読書 | book | 毎日 | sky |
| 副業 | briefcase | 平日のみ | plum |
