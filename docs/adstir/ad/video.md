# 動画リワード広告

動画広告の視聴完了時にユーザーにインセンティブを付与することができます。

### 1. メディアユーザIDの設定を行う

サーバーサイドで成果通知を受け取る場合、メディアユーザーIDを設定します。
メディアユーザIDの設定は、`動画リワード広告の読み込み`よりも前までに設定する必要があります。

```objc
[AdstirVideoAds setMediaUserID:[[UIDevice currentDevice].identifierForVendor UUIDString]]; // ここでは例として、Vendor IDを指定していますが、任意のIDが利用可能です。
```

### 2. 動画広告の初期化を行う

`AdstirVideoAds prepareWithMedia`を使い、プロジェクトで利用する全ての動画広告の初期化を同時に行います。動画リワード広告とフルスクリーン広告を併用する場合は、同時に初期化を行う必要があります。

```objc
[AdstirVideoAds prepareWithMedia:@"メディアID" spots:@[@枠No1, @枠No2]];
```

### 3. 動画リワード広告のインスタンスを生成

`AdstirVideoReward`のインスタンスを生成します。
```objc
AdstirVideoReward *aVideoReward = [[AdstirVideoReward alloc] initWithMedia:@"メディアID" spot:枠No];
```

### 4. デリゲートの実装(オプション)

```objc

- (void)viewDidLoad
{
    [super viewDidLoad];
        :
    aVideoReward.delegate = self;
        :
}

/** 動画の読み込み完了イベントを受け取ります */
- (void)adstirVideoRewardDidLoad:(AdstirVideoReward *)videoReward
{
}

/** 動画の再生準備に失敗した際に呼び出されます */
- (void)adstirVideoReward:(AdstirVideoReward *)videoReward didFailToLoadWithError:(NSError *)error
{
}

/** 動画の再生開始イベントを受け取ります */
- (void)adstirVideoRewardDidStart:(AdstirVideoReward *)videoReward
{
}

/** 動画のインセンティブ付与の完了イベントを受け取ります */
- (void)adstirVideoRewardDidComplete:(AdstirVideoReward *)videoReward
{
}

/** 動画再生のキャンセルイベントを受け取ります */
- (void)adstirVideoRewardDidCancel:(AdstirVideoReward *)videoReward
{
}

/** 動画再生ビューが閉じられたことを受け取ります */
- (void)adstirVideoRewardDidClose:(AdstirVideoReward *)videoReward
{
}

```

### 5. 動画リワード広告の読み込み

動画リワード広告の読み込みを行います。

```objc
[aVideoReward load];
```

### 6. 動画リワード広告の再生

読み込みが完了した動画リワード広告を再生します。
動画の再生を行うViewControllerを渡してください。
動画の再生後、もう一度動画を再生するためには`5.動画リワード広告の読み込み`を行う必要があります。

```objc
if ([aVideoReward canShow]) {
    [aVideoReward showFromViewController:self]];
}
```

### SDKの実装例

ここでは、単純な実装についてのサンプルを提示します。
まず、Storyboard上に、`UIButton`と`UILabel`を配置し、`UIButton`をのOutletとActionを`showVideoButton`と`showVideoButtonDidTouchUpInside`にそれぞれ接続し、`UILabel`のOutletをstatusLabelに接続してください。

- AppDelegate

```Objective-c tab=
@import AdstirAds;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    /* 他の初期化コード */

    // サーバーサイドで成果通知を受け取る場合、メディアユーザーIDを設定します。
    [AdstirVideoAds setMediaUserID:[[UIDevice currentDevice].identifierForVendor UUIDString]]; // ここでは例として、Vendor IDを指定していますが、任意のIDが利用可能です。

    // メディアIDと、このアプリ内で利用する動画インセンティブメニューの枠IDとインタースティシャル広告の枠IDをすべて指定します。
    // 動画リワードとインタースティシャルを併用する場合はどちらの枠Noも指定してください。
    [AdstirVideoAds prepareWithMedia:@"メディアID" spots:@[@枠No, @枠No]];

    return YES;
}
```

```swift tab=
// ...
import AdstirAds
// ...
class AppDelegate: UIResponder, UIApplicationDelegate {
// ...
   func application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {
        /* 他の初期化コード */
        // サーバーサイドで成果通知を受け取る場合、メディアユーザーID(半角英数記号)を設定します。
        AdstirVideoAds.setMediaUserID(UIDevice.currentDevice().identifierForVendor?.UUIDString) // ここでは例として、Vendor IDを指定していますが、任意のIDが利用可能です。
        
        // メディアIDと、このアプリ内で利用する動画インセンティブメニューの枠IDとインタースティシャル広告の枠IDをすべて指定します。
        // 動画リワードとインタースティシャルを併用する場合はどちらの枠Noも指定してください。
        AdstirVideoAds.prepare(withMedia:"メディアID", spots: [枠No, 枠No])
        return true
    }
// ...
}
```

- ViewController

```Objective-c tab=
@import AdstirAds;

@interface FooViewController () <AdstirVideoRewardDelegate>

@property (weak, nonatomic) IBOutlet UILabel *statusLabel;
@property (weak, nonatomic) IBOutlet UIButton *showVideoButton;

@property (nonatomic, strong) AdstirVideoReward *videoReward;

@property (nonatomic, assign) BOOL isVideoRewardCompleted;

@end

@implementation FooViewController

- (void)viewDidLoad
{
    AdstirVideoReward *aVideoReward = [[AdstirVideoReward alloc] initWithMedia:@"メディアID" spot:枠No];
    aVideoReward.delegate = self;
    
    self.videoReward = aVideoReward;

    self.statusLabel.text = @"Loading...";
    [self.videoReward load];
}

/** リワード広告を表示するボタンのターゲットメソッド */
- (IBAction)showVideoButtonDidTouchUpInside:(id)sender
{
    self.showVideoButton.enabled = NO;
    if ([self.videoReward canShow]) {
        [self.videoReward showFromViewController:self]];
    }
}

- (void)dealloc
{
    // デリゲートを解放します。解放を忘れるとクラッシュする可能性があります。
    self.videoReward.delegate = nil;
    // 広告の制御インスタンスを解放します。
    self.videoReward = nil;
}

#pragma mark -
#pragma mark AdstirVideoRewardDelegate

/** 動画の読み込み完了イベントを受け取ります */
- (void)adstirVideoRewardDidLoad:(AdstirVideoReward *)videoReward
{
    self.statusLabel.text = @"Loaded.";
    self.showVideoButton.enabled = YES;
}

/**
 動画の再生準備に失敗した際に呼び出されます
 */
- (void)adstirVideoReward:(AdstirVideoReward *)videoReward didFailToLoadWithError:(NSError *)error
{
    NSLog(@"動画が読み込めませんでした");
    // 15秒待ってから再読み込みします
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(15.0f * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
        self.statusLabel.text = @"Loading...";
        [self.videoReward load];
    });
}

/** 動画の再生開始イベントを受け取ります */
- (void)adstirVideoRewardDidStart:(AdstirVideoReward *)videoReward
{
    self.statusLabel.text = @"";
}

/** 動画のインセンティブ付与の完了イベントを受け取ります */
- (void)adstirVideoRewardDidComplete:(AdstirVideoReward *)videoReward
{
    self.isVideoRewardCompleted = YES;
}

/** 動画再生のキャンセルイベントを受け取ります */
- (void)adstirVideoRewardDidCancel:(AdstirVideoReward *)videoReward
{
    // 15秒待ってから再読み込みします
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(15.0f * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
        self.statusLabel.text = @"Loading...";
        [self.videoReward load];
    });
}

/** 動画再生ビューが閉じられたことを受け取ります */
- (void)adstirVideoRewardDidClose:(AdstirVideoReward *)videoReward
{
    if (self.isVideoRewardCompleted) {
        self.statusLabel.text = @"Congrats! Got virtual currency!";
    }
    self.isVideoRewardCompleted = NO;

    // 15秒待ってから再読み込みします
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(15.0f * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
        self.statusLabel.text = @"Loading...";
        [self.videoReward load];
    });
}

@end
```

```swift tab=
import UIKit
import AdstirAds

class ViewController: UIViewController, AdstirVideoRewardDelegate {
    
    @IBOutlet weak var statusLabel: UILabel!
    @IBOutlet weak var showVideoButton: UIButton!
    
    var videoReward: AdstirVideoReward?
    var isVideoRewardCompleted = false

    override func viewDidLoad() {
        super.viewDidLoad()

        self.showVideoButton.enabled = false
        
        let videoReward = AdstirVideoReward.init(media: "メディアID", spot: 枠No)
        videoReward?.delegate = self;
        self.videoReward = videoReward;

        self.videoReward?.load()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }

    /** リワード広告を表示するボタンのターゲットメソッド */
    @IBAction func showVideoButtonTouchUpInside(sender: AnyObject) {
        self.showVideoButton.enabled = false
        self.videoReward?.showFromViewController(self)
    }

    /** 動画の読み込み完了イベントを受け取ります */
    func adstirVideoRewardDidLoad(videoReward: AdstirVideoReward!) {
        self.statusLabel.text = "Loaded"
        self.showVideoButton.enabled = true
    }
    
    /** 動画の再生準備に失敗した際に呼び出されます */
    func adstirVideoReward(videoReward: AdstirVideoReward!, didFailToLoadWithError error: NSError!) {
        NSLog("動画が読み込めませんでした")

        // 15秒待ってから再読み込みします
        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (Int64)(15.0f * Double(NSEC_PER_SEC))), dispatch_get_main_queue(), {
            self.statusLabel.text = "Loading...";
            self.videoReward?.load()
        })
    }

    /** 動画の再生開始イベントを受け取ります */
    func adstirVideoRewardDidStart(videoReward: AdstirVideoReward!) {
        self.statusLabel.text = ""
    }

    /** 動画のインセンティブ付与の完了イベントを受け取ります */
    func adstirVideoRewardDidComplete(videoReward: AdstirVideoReward!) {
        self.isVideoRewardCompleted = true
    }

    /** 動画再生のキャンセルイベントを受け取ります */
    func adstirVideoRewardDidCancel(videoReward: AdstirVideoReward!) {
        // 15秒待ってから再読み込みします
        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (Int64)(15.0f * Double(NSEC_PER_SEC))), dispatch_get_main_queue(), {
            self.statusLabel.text = "Loading...";
            self.videoReward?.load()
        })
    }

    func adstirVideoRewardDidClose(videoReward: AdstirVideoReward!) {
        if (self.isVideoRewardCompleted) {
            self.statusLabel.text = "Congrats! Got virtual currency!"
        }
        self.isVideoRewardCompleted = false

        // 15秒待ってから再読み込みします
        dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (Int64)(15.0f * Double(NSEC_PER_SEC))), dispatch_get_main_queue(), {
            self.statusLabel.text = "Loading...";
            self.videoReward?.load()
        })
    }
    
    deinit {
        // デリゲートを解放します。解放を忘れるとクラッシュする可能性があります。
        self.videoReward?.delegate = nil;
        // 広告の制御インスタンスを解放します。
        self.videoReward = nil;
    }
}
```

### 成果のコールバックURLへの通知

adstirでは、インセンティブ付与の通知を、任意のコールバックURLに行うことが可能です。
付与するインセンティブの単位と額は、任意の値に変更可能です。
`AdstirVideoReward.setMediaUserID` でユーザーIDを設定していない場合には通知されませんので、ご注意ください。

[動画インセンティブ付与をコールバックURLに通知する](https://github.com/united-adstir/AdStir-Integration-Guide-Android/wiki/%E5%8B%95%E7%94%BB%E3%82%A4%E3%83%B3%E3%82%BB%E3%83%B3%E3%83%86%E3%82%A3%E3%83%96%E4%BB%98%E4%B8%8E%E3%82%92%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AFURL%E3%81%B8%E9%80%9A%E7%9F%A5%E3%81%99%E3%82%8B)


## ライブラリ詳細

[APIリファレンス](../api/index.md#動画視聴型インセンティブ広告)をご覧ください。
