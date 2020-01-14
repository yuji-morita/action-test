# バナー広告の導入

320x50, 300x250, 320x100などのサイズのバナーの導入方法です。

## 対応OS
Android 4.4 以上

## 広告の設置
以下のどちらかの方法で広告を設置してください。

### XMLにて設置
```xml
<com.ad_stir.webview.AdstirMraidView
  media="メディアID"
  spot="枠No"
  adsize="320,50"
  refresh_interval="広告リフレッシュ秒[整数]"
  android:layout_width="wrap_content"
  android:layout_height="wrap_content" />
```
* adsizeは管理画面で登録した枠サイズと同じものを設定してください。

### Javaコードにて設置
```java
com.ad_stir.webview.AdstirMraidView view = new com.ad_stir.webview.AdstirMraidView(
    activity,
    "メディアID",
    枠No,
    com.ad_stir.webview.AdstirMraidView.AdSize.Size320x50,
    広告リフレッシュ秒[整数]);
layout.addView(view);
```
* 第4引数は管理画面で登録した枠サイズと同じものを設定してください。

## ライブラリ詳細

[APIリファレンス](../api/index.md#バナー広告)をご覧ください。