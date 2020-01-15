# よくある質問

## アプリケーション起動時にクラッシュしてしまう

AndroidManifestにAdMobアプリIDを記述しなければアプリケーション起動時にクラッシュいたします。
[こちら](https://developers.google.com/admob/android/quick-start?hl=ja#update_your_androidmanifestxml)を参考にAndroidManifestの更新をお願いします。

## 広告の読み込みに失敗してしまう

アプリケーションをリリースする前に同じ端末等のみで広告を読み込み続けた場合、広告配信が停止してしまう可能性がございます。
[開発時にはテスト端末を追加する](https://developers.google.com/admob/android/test-ads?hl=ja#add_your_test_device)より、広告リクエスト時にデバイスIDの設定をおこなってください。  
こちらの設定をおこなった際には、アプリケーションのリリース前には該当コードの削除をお願いいたします。