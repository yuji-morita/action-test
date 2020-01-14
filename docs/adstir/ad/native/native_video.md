# ネイティブ動画広告の導入

メディアのコンテンツにマッチしたレイアウトで動画広告も掲載できるネイティブ広告です。
動画広告が案件切れの場合はAdstirNativeVideoViewにバナー画像が表示されます。

ネイティブ動画をご利用される場合は営業担当にご相談ください。

## 対応OS

Android 5.0 以上
(Android 4.4の端末には動画の代わりにバナーが表示されます。)

## 広告の設置

### Viewの作成

Viewの作成に関しては、ご自由に実装して頂いて構いません。  実装方法に制限はありません。Layout XML・Javaコード以外の実装方法でも問題ありません。ただし、作成したViewは、[ネイティブ広告ガイドライン](https://github.com/united-adstir/AdStir-Integration-Guide-Web/wiki/%E3%83%8D%E3%82%A4%E3%83%86%E3%82%A3%E3%83%96%E5%BA%83%E5%91%8A%E3%82%AC%E3%82%A4%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3 "ネイティブ広告ガイドライン")に従っている必要があります。

### 動画View（AdstirNativeVideoView）の作成

Layout XMLまたは、Javaコードにて作成してください。

#### XMLにて作成

```xml
<com.ad_stir.nativead.video.AdstirNativeVideoView
    android:id="@+id/native_video"
    android:layout_width="320dp"
    android:layout_height="180dp" />
```

#### JAVAコードにて作成

```java
float density = getResources().getDisplayMetrics().density;
videoView = new AdstirNativeVideoView(activity);
ViewGroup.LayoutParams params = new ViewGroup.LayoutParams(
	(int) (density * 320), (int) (density * 180));

ViewGroup native_video_wrapper = findViewById(R.id.native_video_wrapper);
native_video_wrapper.addView(videoView, params);
```

### 広告の取得

onCreate等で広告のリクエストおよびレスポンスの処理を設定します。

このコードは実装の全体をつかむためのサンプルですので、この通りに実装しても動作しません。実際に広告を実装する際は、ライブラリ詳細の項目をよく確認して必要なパラメータの設定及び処理を記述する必要があります。各メソッドの詳細は[APIリファレンス](../../api/index.md#ネイティブ広告)をご覧ください。

```java
private AdstirNativeAd nativead;
private AdstirNativeVideoView videoView;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.xxxx);

    // インスタンス生成
    nativead = new AdstirNativeAd(activity,"メディアID",枠No);
    // ガイドラインで規定されているスポンサー表記を、表示する通りに設定します。
    nativead.setSponsoredText("PR");
    // 広告レスポンスを受け取るListenerを設定します。
    nativead.setListener(new AdstirNativeAdListener(){
        public void onReceive(final AdstirNativeAdResponse response){
        // 広告レスポンスが正常に取得できた時に行う処理を実装します。
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
                    // rate
                    TextView rateText = (TextView) findViewById(R.id.xxxx);
                    rateText.setText("rate : " + String.valueOf(response.getRating()));
                    // video
                    videoView = (AdstirNativeVideoView) view.findViewById(R.id.xxxx);
                    videoView.load(response.getVideo());
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
    // モバイル回線使用時に、動画を拒否する場合にはtrueを設定します。
    nativead.denyVideoOnMobileConnection(true);
    // 広告をリクエストします。
    nativead.getAd();
}
```

### 広告破棄

onDestroy()等でAdstirNativeAd、AdstirNativeVideoViewの破棄を指示します。

```java
@Override
protected void onDestroy() {
    super.onDestroy();
    if(nativead != null) {
        nativead.destroy();
    }
    if(videoView != null) {
        videoView.release();
    }
}
```

## ライブラリ詳細

[APIリファレンス](../../api/index.md#ネイティブ広告)をご覧ください。
