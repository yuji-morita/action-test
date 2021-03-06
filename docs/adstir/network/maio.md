# maio広告の導入

## 対応OS

Android 4.4以上

## SDKの組み込み

### Android Studioによる組み込み(推奨)
アプリケーションレベルのbuild.gradleにmavenリポジトリと依存関係を設定します。

```groovy hl_lines="6 11"
repositories {
    maven { url 'http://cdnp.ad-stir.com/m2' }
    maven { url 'https://imobile-maio.github.io/maven' }
}

dependencies {
    // 利用するadstirのSDKバージョンを設定します
    def adstir_version = "x.x.x" 
    implementation "com.ad-stir.webviewsdk:adstir-webviewsdk:${adstir_version}"
    implementation "com.ad-stir.mediationadapter:adstir-mediationadapter-maio:${adstir_version}"
}
```

### 手動組み込み
#### SDKの準備
maioのSDKは、VideoAdSDKBundledのパッケージに同梱されております。  
作成された動画枠の`動画SDK (Android / AAR形式)`より取得いただけます。

#### SDKの組み込み
初期設定の[SDKの手動組み込み](../init/manual_integration.md)の完了後、下記の手順で追加してください。

1. File -> New -> New Module -> Import .JAR/.AAR Package より`maio.aar`, `androidwebviewmediation-adapter-maio.aar`を追加します。
2. File -> Project Structure -> Dependencies -> app より`maio`, `androidwebviewmediation-adapter-maio`を追加します。

## ProGuardの設定
ProGuardを使用しているアプリにはproguard-rules.proに、下記の内容を追加してください。  
この記述が無い場合、adstirの機能を正常に利用することができません。

```
-dontwarn jp.maio.**
-keep class jp.maio.** { *; }
-keep interface jp.maio.** { *; }
```