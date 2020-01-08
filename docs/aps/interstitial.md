# Amazon Publisher Services(APS)のバナー広告の導入

!!! Warning "はじめに"
    APS SDKの初期化が必要です。[APSの設定](/aps/init)をご覧になり、SDKの初期化を先におこなってください。

## APSバナーへのリクエストを行う

### `DTBAdSize`のインスタンスを生成します

`YOUR_SLOT_UUID`には営業担当がお知らせしたIDを入力してください。
    
```
DTBAdSize *size = [[DTBAdSize alloc] initInterstitialAdSizeWithSlotUUID:@"YOUR_SLOT_UUID"];
```

### `DTBAdLoader`のインスタンスを生成し、`DTBAdSize`を設定する


```
DTBAdLoader *adLoader = [DTBAdLoader new];
[adLoader setSizes：size、nil];
```

### APSの入札リクエストを行う

loadAdを呼び出して入札リクエストを行います。

```
[adLoader loadAd：self];
```

### `DTBAdCallback`の実装を行う

APSが入札した場合はonSuccessが、入札しなかった場合はonFailureが呼ばれます。

APSの入札結果を元に、AdMobへ広告リクエストを行います。

onSuccessが呼ばれた場合は、AdMobへGADCustomEventExtrasを付与して広告リクエストを行い、
onFailureが呼ばれた場合は、AdMobへ追加情報を付与せずにリクエストを行います。
AdMobの実装については[こちら](/admob#広告の実装)をご覧ください。

```
#import <DTBiOSSDK/DTBiOSSDK.h>
@interface ViewController () <GADBannerViewDelegate, DTBAdCallback>
@end

@implementation ViewController
...

#pragma mark - DTBAdCallback
- (void)onFailure: (DTBAdError)error {
    // APSの入札情報は付与しないでAdMobへリクエストを行う
    [self loadAdMobBannerAdsWithExtras:nil];
}

- (void)onSuccess: (DTBAdResponse *)adResponse {
    // APSの入札情報を付与してAdMobへリクエスト行う
    NSString *amznSlots = adResponse.amznSlots;
    NSDictionary *mediationHints = [adResponse mediationHints];
    GADCustomEventExtras *extras = [[GADCustomEventExtras alloc] init];
    [extras setExtras:mediationHints forLabel:amznSlots];
    [self loadAdMobBannerAdsWithExtras:extras];
}

#pragma mark - AdMobBanner load

- (void)loadAdMobBannerAdsWithExtras: (GADCustomEventExtras *)extras
{
    GADRequest *request = [GADRequest request];
    if (extras != nil) {
        // admobへリクエストを行う際にextraへ登録する
        [request registerAdNetworkExtras:extras];
    }

    // GADInterstitial オブジェクトを生成し、AdMobへリクストを行う。
    googleInterstitial = [[GADInterstitial alloc] initWithAdUnitID:googleAdUnitId];
    [googleInterstitial loadRequest:request];
}
```

### 広告を表示する

広告の準備ができているか確認してから広告を表示します。

```
- (void)showInterstitialAd {
  if (googleInterstitial.isReady){
   [googleInterstitial presentFromRootViewController:self];
  }
}
```