# MoPub広告の導入

## 対応OS

Android 4.4以上

## SDKの組み込み

### Android Studioによる組み込み(推奨)
アプリケーションレベルのbuild.gradleにコンパイルオプションとmavenリポジトリと依存関係を設定します。

```groovy hl_lines="1 6 13 25"
android {
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

repositories {
    maven { url 'http://cdnp.ad-stir.com/m2' }
    maven { url 'https://imobile-maio.github.io/maven' }
}

dependencies {
    // 利用するadstirのSDKバージョンを設定します
    def adstir_version = "x.x.x" 
    implementation "com.ad-stir.webviewsdk:adstir-webviewsdk:${adstir_version}"
    implementation "com.ad-stir.mediationadapter:adstir-mediationadapter-mopub:${adstir_version}"
    // ご利用されているライブラリが競合した際は下記のバージョンをご利用されているライブラリのバージョンへ書き換えてください。
    // configurations.all {
    //     resolutionStrategy.force "androidx.legacy:legacy-support-v4:x.x.x"
    //     resolutionStrategy.force "androidx.annotation:annotation:x.x.x"
    //     resolutionStrategy.force "androidx.recyclerview:recyclerview:x.x.x"
    //     resolutionStrategy.force "androidx.appcompat:appcompat:x.x.x"
    // }
}
```

### 手動組み込み
#### SDKの準備
MoPubのSDKは、VideoAdSDKBundledのパッケージに同梱されております。  
作成された動画枠の`動画SDK (Android / AAR形式)`より取得いただけます。

#### SDKの組み込み
初期設定の[SDKの手動組み込み](../init/manual_integration.md)の完了後、下記の手順で追加してください。

1. File -> New -> New Module -> Import .JAR/.AAR Package より以下のファイルを追加します。
    * `mopub-sdk-banner-x.x.x.aar`
    * `mopub-sdk-base-x.x.x.aar`
    * `mopub-sdk-interstitial-x.x.x.aar`
    * `mopub-sdk-native-static-x.x.x.aar`
    * `mopub-sdk-rewardedvideo-x.x.x.aar`
    * `androidwebviewmediation-adapter-mopub.aar`

1. File -> Project Structure -> app -> Dependencies より以下を追加します。
    * `mopub-sdk-banner-x.x.x`
    * `mopub-sdk-base-x.x.x`
    * `mopub-sdk-interstitial-x.x.x`
    * `mopub-sdk-native-static-x.x.x`
    * `mopub-sdk-rewardedvideo-x.x.x`
    * `androidwebviewmediation-adapter-mopub`

3. アプリケーションレベルのbuild.gradleに依存関係を設定します。

```groovy hl_lines="1 8"
dependencies {
    implementation "com.mopub.volley:mopub-volley:2.1.0"
    implementation "com.google.android.exoplayer:exoplayer:2.9.5"
    implementation "androidx.legacy:legacy-support-v4:1.0.0"
    implementation "androidx.annotation:annotation:1.1.0"
    implementation "androidx.recyclerview:recyclerview:1.1.0"
    implementation "androidx.appcompat:appcompat:1.1.0"
}
```

## ProGuardの設定
ProGuardを使用しているアプリにはproguard-rules.proに、下記の内容を追加してください。  
この記述が無い場合、adstirの機能を正常に利用することができません。

```
# Keep public classes and methods.
-keepclassmembers class com.mopub.** { public *; }
-keep public class com.mopub.**
-keep public class android.webkit.JavascriptInterface {}

# Explicitly keep any custom event classes in any package.
-keep class * extends com.mopub.mobileads.CustomEventBanner {}
-keep class * extends com.mopub.mobileads.CustomEventInterstitial {}
-keep class * extends com.mopub.nativeads.CustomEventNative {}
-keep class * extends com.mopub.nativeads.CustomEventRewardedAd {}

# Keep methods that are accessed via reflection
-keepclassmembers class ** { @com.mopub.common.util.ReflectionTarget *; }

# Support for Android Advertiser ID.
-keep class com.google.android.gms.common.GooglePlayServicesUtil {*;}
-keep class com.google.android.gms.ads.identifier.AdvertisingIdClient {*;}
-keep class com.google.android.gms.ads.identifier.AdvertisingIdClient$Info {*;}

# Support for Google Play Services
# http://developer.android.com/google/play-services/setup.html
-keep class * extends java.util.ListResourceBundle {
    protected Object[][] getContents();
}

-keep public class com.google.android.gms.common.internal.safeparcel.SafeParcelable {
    public static final *** NULL;
}

-keepnames @com.google.android.gms.common.annotation.KeepName class *
-keepclassmembernames class * {
    @com.google.android.gms.common.annotation.KeepName *;
}

-keepnames class * implements android.os.Parcelable {
    public static final ** CREATOR;
}
```