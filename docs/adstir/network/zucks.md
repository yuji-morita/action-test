# Zucks広告の導入

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
ZucksのSDKは、SwipeInterstitialSDKBundledのパッケージに同梱されております。  
作成された動画枠の`スワイプインタースティシャルSDK (Android / AAR形式)`より取得いただけます。

#### SDKの組み込み
初期設定の[SDKの手動組み込み](../init/manual_integration.md)の完了後、下記の手順で追加してください。

1. File -> New -> New Module -> Import .JAR/.AAR Package より`ZucksAdNetworkSDK-x.x.x.jar`, `androidwebviewmediation-adapter-zucks.aar`を追加します。
2. File -> Project Structure -> Dependencies -> app より`ZucksAdNetworkSDK-x.x.x`, `androidwebviewmediation-adapter-zucks`を追加します。
