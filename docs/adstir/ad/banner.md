# バナー広告の導入

320x50, 300x250, 320x100などのサイズのバナーの導入方法です。

## 広告の設置

以下のどちらかの方法で広告を設置してください。

* FooViewController.m

```objective-c tab=
#import <AdstirAds/AdstirAds.h>

@interface FooViewController ()

@property (retain) AdstirMraidView *adstir;

@end

@implementation

- (void)viewDidLoad
{
    // 広告表示位置: タブバーの下でセンタリング、広告サイズ: 320,50 の場合
    CGFloat originX = (self.view.frame.size.width - kAdstirAdSize320x50.size.width) / 2;
    CGFloat originY = [UIApplication sharedApplication].statusBarFrame.size.height;
    AdstirMraidView *aAdstir = [[[AdstirMraidView alloc] initWithAdSize:kAdstirAdSize320x50 origin:CGPointMake(originX, originY)
        media:@"メディアID" spot:枠No] autorelease];
    aAdstir.intervalTime = 広告リフレッシュ秒[整数];
    aAdstir.delegate = self;
    [self.view addSubview:aAdstir];
    self.adstir = aAdstir;
}

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];
    // 広告の読み込みを再開します。
    [self.adstir start];
}

- (void)viewWillDisappear:(BOOL)animated
{
    // 広告の読み込みを停止します。
    [self.adstir stop];
    // この他にも、Viewが非表示になると思われる箇所では、stopを呼び出すことで無駄なインプレッションが発生しません。
}

- (void)dealloc
{
    // デリゲートを解放します。解放を忘れるとクラッシュする可能性があります。
    self.adstir.delegate = nil;
    // 広告ビューを解放します。
    self.adstir = nil;
}

@end
```

``` swift tab=
import AdstirAds

class FooViewController: UIViewController, AdstirMraidViewDelegate {

    var adView: AdstirMraidView? = nil

    override func viewDidLoad() {
        super.viewDidLoad()

        // 広告表示位置: タブバーの下でセンタリング、広告サイズ: 320,50 の場合
        var originY = UIApplication.sharedApplication().statusBarFrame.size.height
        var originX = (self.view.frame.size.width - kAdstirAdSize320x50.size.width) / 2
        var adView = AdstirMraidView(adSize: kAdstirAdSize320x50, origin: CGPointMake(originX, originY), media: "MEDIA-899477da", spot: 2)

        // リフレッシュ秒数を設定します。
        adView.intervalTime = 広告リフレッシュ秒[整数]
        // デリゲートを設定します。
        adView.delegate = self

        // 広告ビューを親ビューに追加します。
        self.view.addSubview(adView)
        self.adView = adView
    }

    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)

        // 広告の読み込みを開始/再開します。
        self.adView?.start()
    }

    override func viewWillDisappear(animated: Bool) {
        super.viewWillDisappear(animated)

        // 広告の読み込みを停止します。
        self.adView?.stop()
        // この他にも、Viewが非表示になると思われる箇所では、stopを呼び出すことで無駄なインプレッションが発生しません。
    }

    deinit {
        // デリゲートを解放します。解放を忘れるとクラッシュする可能性があります。
        self.adView?.delegate = nil
        // 広告ビューを解放します。
        self.adView = nil
    }
}
```

## 設置に当たっての注意点

- iPhone 6/6 Plusに対応したアプリでは、縦向きの際でも画面幅一杯に広告を表示することができません。左右中央にセンタリングして表示するなど、レイアウトの調整をお願い致します。
- ARCを利用している場合は、propertyの宣言をretainから、strongに変更し、autoreleaseを削除してください。
- バージョン2.0.0から、広告ビューがAdstirMraidViewになりました。お手数をおかけいたしますが、変更をお願いいたします。
- バージョン2.0.0から、広告サイズの指定方法が変更になりました。下記の対応している広告サイズを参考に、実装してください。
- バージョン2.0.0から、枠Noの指定方法が文字列から整数(自然数、NSUInteger)に変更になりました。
- Xcodeの仕様で、文字列のままでも警告が出ませんのでご注意ください。

## 対応している広告サイズ

### モバイルバナー(320x50)

kAdstirAdSize320x50を指定します。

### モバイルバナー(320x100)

kAdstirAdSize320x100を指定します。

### レクタングル(300x250)

kAdstirAdSize300x250を指定します。

### カスタム広告サイズ

カスタムの広告サイズを定義することも可能ですが、 当社提供のAdStir CPCでの案件が掲載できない場合がございますので、ご注意ください。

```objc
AdstirSizeFromCGSize(CGSizeMake(468.0f, 60.0f));
```

## ライブラリ詳細

[APIリファレンス](../api/index.md#バナー広告)をご覧ください。