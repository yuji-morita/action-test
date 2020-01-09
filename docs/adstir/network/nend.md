# nend広告の導入

## 対応OS

Android 4.4以上

## SDKの組み込み

### Android Studioによる組み込み(推奨)
アプリケーションレベルのbuild.gradleにmavenリポジトリと依存関係を設定します。

```groovy hl_lines="6 16"
repositories {
    maven { url 'http://cdnp.ad-stir.com/m2' }
    maven { url 'http://fan-adn.github.io/nendSDK-Android-lib/library' }
}

dependencies {
    // 利用するadstirのSDKバージョンを設定します
    def adstir_version = "x.x.x" 
    implementation "com.ad-stir.webviewsdk:adstir-webviewsdk:${adstir_version}"
    implementation "com.ad-stir.mediationadapter:adstir-mediationadapter-nend:${adstir_version}"
    // ご利用されているライブラリが競合した際は下記のバージョンをご利用されているライブラリのバージョンへ書き換えてください。
    // configurations.all {
    //     resolutionStrategy.force "androidx.legacy:legacy-support-v4:x.x.x"
    //     resolutionStrategy.force "androidx.constraintlayout:constraintlayout:x.x.x"
    // }
}
```

### 手動組み込み
#### SDKの準備
nendのSDKは、VideoAdSDKBundledのパッケージに同梱されております。  
作成された動画枠の`動画SDK (Android / AAR形式)`より取得いただけます。

#### SDKの組み込み
初期設定の[SDKの手動組み込み](../init/manual_integration.md)の完了後、下記の手順で追加してください。

1. File -> New -> New Module -> Import .JAR/.AAR Package より`nendSDK-x.x.x.aar`, `androidwebviewmediation-adapter-nend.aar`を追加します。
2. File -> Project Structure -> Dependencies -> app より`nendSDK-x.x.x`, `androidwebviewmediation-adapter-nend`を追加します。
3. アプリケーションレベルのbuild.gradleに依存関係を設定します。

```groovy hl_lines="1 4"
dependencies {
    implementation 'androidx.legacy:legacy-support-v4:1.0.0' // androidx.appcompatが定義済みの場合は不要
    implementation 'androidx.constraintlayout:constraintlayout:1.1.3'
}
```
## ProGuardの設定
ProGuardを使用しているアプリにはproguard-rules.proに、下記の内容を追加してください。  
この記述が無い場合、adstirの機能を正常に利用することができません。

```
-keep class net.nend.** {*;}
-dontwarn net.nend.**
```