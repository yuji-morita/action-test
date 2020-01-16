# Amazon Publisher Services(APS)のバナー広告の導入

!!! Warning "はじめに"
    APS SDKの初期化が必要です。[APSの設定](/aps/init)をご覧になり、SDKの初期化を先におこなってください。

## APSバナーへのリクエストを行う

### `DTBAdSize`のインスタンスを生成します

広告サイズは実際に表示するバナー広告のサイズを、`YOUR_SLOT_UUID`には営業担当がお知らせしたIDを入力してください。
    
```java
DTBAdSize adSize = new DTBAdSize(320, 50, "YOUR_SLOT_UUID");
```

### `DTBAdLoader`のインスタンスを生成し、`DTBAdSize`を設定する

```java
final DTBAdRequest adLoader = new DTBAdRequest();
adLoader.setSizes(adSize);
```

### APSの入札リクエストを行う

loadAdを呼び出して入札リクエストを行います。

```java

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

    // AdMobへリクエストを行う
    self.bannerView = [[GADBannerView alloc] initWithAdSize:利用するバナーのサイズ];
    self.bannerView.delegate = self;
    self.bannerView.adUnitID = AD_ADMOB_BANNER_ID;
    self.bannerView.rootViewController = [KHMUtility getFrontViewController];
    [self.bannerView loadRequest:request];
}
```




## 実装例

```
#import <DTBiOSSDK/DTBiOSSDK.h>

@interface ViewController () <GADBannerViewDelegate, DTBAdCallback>
@end

@implementation ViewController
- (void)viewDidLoad {
    [super viewDidLoad];

    // 広告サイズと、APSのslot idを指定します。
    DTBAdSize *size = [[DTBAdSize alloc] initBannerAdSizeWithWidth:320 height:50 andSlotUUID:APSのslot id];
    DTBAdLoader *adLoader = [DTBAdLoader new];
    [adLoader setSizes:size, nil];
    [adLoader loadAd:self];
}

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

    // AdMobへリクエストを行う
    self.bannerView = [[GADBannerView alloc] initWithAdSize:利用するバナーのサイズ];
    self.bannerView.delegate = self;
    self.bannerView.adUnitID = AD_ADMOB_BANNER_ID;
    self.bannerView.rootViewController = [KHMUtility getFrontViewController];
    [self.bannerView loadRequest:request];
}
```