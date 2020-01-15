# AdMob広告について

## 前提条件

- Android Studio 3.2以上  
- minSdkVersion 14以上  
- compileSdkVersion 28以上  

## 事前準備

[AdMobのスタートガイド](https://developers.google.com/admob/android/quick-start?hl=ja)を参考に、AdMobの設定をおこなってください。  
Google Mobile Ads SDKは17.2.0以上をお使いください。

### メディエーションの準備

[AdMobメディエーション](https://developers.google.com/admob/android/mediate?hl=ja)を行うために、アドネットワークのSDKとアダプターをプロジェクトへ導入します。

#### Android Studioで導入する場合
アプリケーションレベルのbuild.gradleにmavenリポジトリと依存関係を設定することで、adstirが利用するアドネットワークのSDKとアダプターを一括で導入することができます。

```groovy hl_lines="11 15"
repositories {
    maven { url 'http://cdnp.ad-stir.com/m2' }
    maven { url 'https://adcolony.bintray.com/AdColony' } // adcolony
    maven { url 'https://github.com/glossom-dev/GlossomAds-Android/raw/master' } // adcolsa
    maven { url 'https://imobile-maio.github.io/maven' } // maio
    maven { url 'http://fan-adn.github.io/nendSDK-Android-lib/library' } // nend
    maven { url 'https://s3.amazonaws.com/moat-sdk-builds' } // mopub
    maven { url 'https://imobile.github.io/adnw-sdk-android' } // imobile
}

dependencies {
    // 利用するadstirのSDKバージョンを設定します
    def adstir_version = "x.x.x" 
    implementation "com.ad-stir.mediationadapter:admob-package:${adstir_version}"
}
```

#### 手動で導入する場合

1. [こちら](../adstir/init/manual_integration.md#sdkの手動組み込み)を参考にadstirの動画パッケージを組み込む
1. [AdMobのスタートガイド](https://developers.google.com/admob/android/quick-start?hl=ja#manual_download)を参考にGoogleMobileAds SDKを入れる 
1. adstir SDKにbundleされていないアドネットワークのSDKをダウンロードする
    * [Facebook](https://origincache.facebook.com/developers/resources/?id=audience-network-sdk-5.6.0.zip)
1. AdMobメディエーションで利用できる各アドネットワークのアダプターをダウンロードする
    * [AdColony](https://google.bintray.com/mobile-ads-adapters-android/com/google/ads/mediation/adcolony/4.1.0.0/adcolony-4.1.0.0.aar)
    * [AppLovin](https://google.bintray.com/mobile-ads-adapters-android/com/google/ads/mediation/applovin/9.10.5.0/applovin-9.10.5.0.aar)
    * [Facebook](https://google.bintray.com/mobile-ads-adapters-android/com/google/ads/mediation/facebook/5.6.0.0/facebook-5.6.0.0.aar)
    * [maio](https://google.bintray.com/mobile-ads-adapters-android/com/google/ads/mediation/maio/1.1.10.0/maio-1.1.10.0.aar)
    * [MoPub](https://google.bintray.com/mobile-ads-adapters-android/com/google/ads/mediation/mopub/5.10.0.0/mopub-5.10.0.0.aar)
    * [nend](https://google.bintray.com/mobile-ads-adapters-android/com/google/ads/mediation/nend/5.3.0.0/nend-5.3.0.0.aar)
    * [Tapjoy](https://google.bintray.com/mobile-ads-adapters-android/com/google/ads/mediation/tapjoy/12.3.4.0/tapjoy-12.3.4.0.aar)
    * [UnityAds](https://google.bintray.com/mobile-ads-adapters-android/com/google/ads/mediation/unity/3.3.0.0/unity-3.3.0.0.aar)
1. ダウンロードした各SDKをプロジェクトへ追加する

## 広告の実装

AdMobの実装ガイドをご覧ください

* [バナー](https://developers.google.com/admob/android/banner?hl=ja)
* [インタースティシャル](https://developers.google.com/admob/android/interstitial?hl=ja)
* [ネイティブ](https://developers.google.com/admob/android/native/start?hl=ja)
* [動画リワード](https://developers.google.com/admob/android/rewarded-ads?hl=ja)

また、アドネットワークによっては追加で実装する必要がございます。 [追加実装](network#追加実装)をご覧になり、実装をお願いします。

### テストデバイスの追加
[開発時にはテスト端末を追加する](https://developers.google.com/admob/android/test-ads?hl=ja#add_your_test_device)より、広告リクエスト時にデバイスIDの設定をおこなってください。  
こちらの設定をおこなった際には、アプリケーションのリリース前には該当コードの削除をお願いいたします。
