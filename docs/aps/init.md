# Amazon Publisher Services(APS)の初期設定

APSの広告は下記のものに対応しております。

* AdMobバナー
* AdMobインタースティシャル

## プロジェクトへAPSの導入

APSのSDKとアダプター、アドネットワークのSDKとアダプターをプロジェクトへ導入します。

### CocoaPodを利用している場合
Podfileへ下記のものを記述することで、adstirが利用するアドネットワークのSDKとアダプターを一括で導入することができます。

```
pod 'AdStir-Ads-SDK/AdMob-Package'
```

### 手動で導入する場合

営業担当にお問い合わせください。


## APSの初期化

営業担当がお知らせしたAPSのapp idを用いて、下記のように初期化を行います。

```
#import <DTBiOSSDK/DTBiOSSDK.h>
...

[[DTBAds sharedInstance] setAppKey: @"your_app_id"];
```

テスト時には下記のものも追加します。
アプリをリリースする前には下記のコードは削除してください。

```
[[DTBAds sharedInstance] setLogLevel:DTBLogLevelAll];
[[DTBAds sharedInstance] setTestMode:YES];
```

## 広告を実装する

* [バナー広告](banner.md)
* [インタースティシャル広告](interstitial.md)
