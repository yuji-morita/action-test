# スワイプインタースティシャル広告の導入

縦表示アプリに全画面で表示できる広告の導入方法です。

## 対応OS

Android 4.4以上

## 利用上の注意

`縦画面表示かつ全画面で表示されるアプリでご利用を想定しています。表示されるレイアウトのサイズが小さい場合、正常に広告が表示されない可能性があります。`

## 広告の設置

以下のどちらかの方法で広告を設置してください。

### レイアウトのXMLにて設置

```xml
<com.ad_stir.fullscreen.AdstirFullscreenView
    media="メディアID"
    spot="枠No"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

### Javaコードにて設置

1. スワイプインタースティシャル広告のインスタンスを生成
1. リスナーを生成(オプション)
1. スワイプインタースティシャルをレイアウトに配置

#### 1. スワイプインタースティシャル広告のインスタンスを生成

`AdstirFullscreenView`のインスタンスを生成します。

```java
AdstirFullscreenView view = new AdstirFullscreenView(
    activity,
    "メディアID",
    枠No);
```

#### 2. リスナーを生成(オプション)

スワイプインタースティシャル広告のリスナーを設定します。

```java
view.setListener(new AdstirFullscreenView.AdstirFullscreenListener() {
    @Override
    public void onLeaveApplication(AdstirFullscreenView view){
        // スワイプインタースティシャル広告をタップし、ユーザーがアプリケーションから離れた時に呼ばれます。
    }
});
```

#### 3. スワイプインタースティシャル広告をレイアウトに配置

スワイプインタースティシャル広告を表示するレイアウトに1.で作成したインスタンスを配置します。

```java
layout.addView(view);
```

## ライブラリ詳細

[APIリファレンス](../api/index.md#スワイプインタースティシャル広告)をご覧ください。
