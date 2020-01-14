# ネイティブ広告の導入

コンテンツにマッチしたレイアウトで掲載できるネイティブ広告の導入方法です。

## 対応OS

Android 4.4 以上

## 広告の設置

### Viewの作成

Viewの作成に関しては、ご自由に実装して頂いて構いません。  
実装方法に制限はありません。Layout XML・Javaコード以外の実装方法でも問題ありません。  
ただし、作成したViewは、[ネイティブ広告ガイドライン](https://github.com/united-adstir/AdStir-Integration-Guide-Web/wiki/%E3%83%8D%E3%82%A4%E3%83%86%E3%82%A3%E3%83%96%E5%BA%83%E5%91%8A%E3%82%AC%E3%82%A4%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3 "ネイティブ広告ガイドライン")に従っている必要があります。

### 広告の取得

onCreate等で広告のリクエストおよびレスポンスの処理を設定します。

このコードは実装の全体をつかむためのサンプルですので、この通りに実装しても動作しません。実際に広告を実装する際は、ライブラリ詳細の項目をよく確認して必要なパラメータの設定及び処理を記述する必要があります。各メソッドの詳細は[APIリファレンス](../../api/index.md#ネイティブ広告)をご覧ください。

```java
private AdstirNativeAd nativead;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.xxxx);

    // インスタンス生成
    nativead = new AdstirNativeAd(activity,"メディアID",枠No);
    // ガイドラインで規定されているスポンサー表記を、表示する通りに設定します。
    nativead.setSponsoredText("PR");
    // 広告レスポンスを受け取るListenerを設定します
    nativead.setListener(new AdstirNativeAdListener(){
        public void onReceive(final AdstirNativeAdResponse response){
        // 広告レスポンスが正常に取得できた時に行う処理を実装
        // AdstirNativeAdListenerのメソッドはすべてバックグラウンドスレッドで動作します。
            runOnUiThread(new Runnable(){
                public void run(){
                    // title
                    TextView titleView = (TextView) findViewById(R.id.xxxx);
                    titleView.setText(response.getTitle());
                    // description
                    TextView descriptionView = (TextView) findViewById(R.id.xxxx);
                    descriptionView.setText(response.getDescription());
                    // icon
                    ImageView iconView = (ImageView) findViewById(R.id.xxxx);
                    response.bindIconToImageView(NativeActivity.this, iconView);
                    // image
                    ImageView imageView = (ImageView) findViewById(R.id.xxxx);
                    response.bindImageToImageView(NativeActivity.this, imageView);
                    imageView.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            response.click();
                        }
                    });
                    // rate
                    TextView rateText = (TextView) findViewById(R.id.xxxx);
                    rateText.setText("rate : " + String.valueOf(response.getRating()));
                    // CTA
                    Button cta = (Button) findViewById(R.id.native_cta);
                    cta.setText(response.getCta());
                    cta.setOnClickListener( new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            response.click();
                        }
                    });
                }
            });
            // 広告を表示するときにimpression()を呼び出します。
            response.impression();
        }
        public void onFailed(){
            // 広告レスポンスが正常に取得できなかった時に行う処理はここに記述します。
        }
    });
    // 広告をリクエストします。
    nativead.getAd();
}
```

### 広告破棄

onDestroy()等でAdstirNativeAdの破棄を指示します。

```java
@Override
protected void onDestroy() {
    nativead.destroy();
    super.onDestroy();
}
```

## ライブラリ詳細

[APIリファレンス](../../api/index.md#ネイティブ広告)をご覧ください。
