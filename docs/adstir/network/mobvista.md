# Mobvista広告の導入

## 対応OS

Android 4.4以上

## SDKの組み込み

### Android Studioによる組み込み(推奨)
アプリケーションレベルのbuild.gradleにmavenリポジトリと依存関係を設定します。

```groovy hl_lines="5 10"
repositories {
    maven { url 'http://cdnp.ad-stir.com/m2' }
}

dependencies {
    // 利用するadstirのSDKバージョンを設定します
    def adstir_version = "x.x.x" 
    implementation "com.ad-stir.webviewsdk:adstir-webviewsdk:${adstir_version}"
    implementation "com.ad-stir.mediationadapter:adstir-mediationadapter-mobvista:${adstir_version}"
}
```

### 手動組み込み
#### SDKの準備
MobvistaのSDKは、VideoAdSDKBundledのパッケージに同梱されております。  
作成された動画枠の`動画SDK (Android / AAR形式)`より取得いただけます。

#### SDKの組み込み
初期設定の[SDKの手動組み込み](../init/manual_integration.md)の完了後、下記の手順で追加してください。

1. File -> New -> New Module -> Import .JAR/.AAR Package より以下のファイルを追加します。
    * `mintegral_common.aar`
    * `mintegral_mtgjscommon.aar`
    * `mintegral_playercommon.aar`
    * `mintegral_reward.aar`
    * `mintegral_videocommon.aar`
    * `mintegral_videojs.aar`
    * `androidwebviewmediation-adapter-mobvista.aar`
1. File -> Project Structure -> app -> Dependencies より以下を追加します。
    * `mintegral_common`
    * `mintegral_mtgjscommon.aar`
    * `mintegral_playercommon`
    * `mintegral_reward`
    * `mintegral_videocommon`
    * `mintegral_videojs`
    * `androidwebviewmediation-adapter-mobvista`


## ProGuardの設定
ProGuardを使用しているアプリにはproguard-rules.proに、下記の内容を追加してください。  
この記述が無い場合、adstirの機能を正常に利用することができません。

```
-keepattributes Signature
-keepattributes *Annotation*
-keep class com.mintegral.** {*; }  
-keep interface com.mintegral.** {*; }  
-keep class android.support.v4.** { *; }  
-dontwarn com.mintegral.**
-keep class **.R$* { public static final int mintegral*; }
-keep class com.alphab.** {*; }
-keep interface com.alphab.** {*; }
```
