# 全画面インタースティシャル広告の導入

動画 / 静止画 による全画面広告の導入方法です。

## 対応OS

Android4.4以上

## 広告の設定

### 1.動画広告の初期化を行う

はじめ、`AdstirVideoAds.init()`を使い、プロジェクトで利用する全ての動画広告の初期化を同時に行います。　　[動画リワード広告](reward/index.md)と全画面インタースティシャル広告を併用する場合は、同時に初期化を行う必要があります。

```java
// 使用する動画リワードと全画面インタースティシャルの全てのスポットIDについて、初期化処理を行います。
int[] spotIds = { 1, 2 };
AdstirVideoAds.init(this, "MEDIA-xxxxxx", spotIds);
```

### 2.全画面インタースティシャル広告のインスタンスを生成

`AdstirInterstitial`のインスタンスを生成します。
```java
// スポットIDごとにインスタンスを生成します。ここでは1についてのみ生成します。
AdstirInterstitial adstirInterstitial = new AdstirInterstitial(this, "MEDIA-xxxxxx", 2);
```

### 3.リスナーの生成

全画面インタースティシャル広告のイベント通知を行うリスナーのインスタンスを生成します。

```java
// リスナーの定義
private AdstirInterstitialListener listener = new AdstirInterstitialListener() {
    @Override
    public void onLoad(int spot_no) {
      // ロードが完了した時の処理を記述できます。
    }
    @Override
    public void onFailed(int spot_no) {
      // スタートが失敗した時にやりたい処理を記述できます。
    }
    @Override
    public void onStart(int spot_no) {
      // 動画が再生された時にやりたい処理を記述できます。
    }
    @Override
    public void onStartFailed(int spot_no) {
      // 動画の再生が失敗した時にやりたい処理を記述できます。
    }
    @Override
    public void onFinished(int spot_no) {
      // 動画の再生が終了した時にやりたい処理を記述できます。
    }
    @Override
    public void onClose(int spot_no) {
      // 動画が閉じられた時にやりたい処理を記述できます。
    }
  };

// 上で定義したリスナーを登録します。
adstirInterstitial.setAdstirInterstitialListener(listener);
```

### 4.全画面インタースティシャル広告の読み込み

全画面インタースティシャル広告の読み込みを行います。

```java
// 全画面インタースティシャル広告を読み込みます。
adstirInterstitial.load();
```

### 5.全画面インタースティシャル広告の再生

読み込みが完了した全画面インタースティシャル広告を再生します。
動画の再生後、もう一度動画を再生するためには`4.全画面インタースティシャル広告の読み込み`を行う必要があります。

```java
if(adstirInterstitial.canShow()){
    adstirInterstitial.show();
}
```

## 全画面インタースティシャル広告の実装例


```java
// 下記のインポートが必要です
import com.ad_stir.interstitial.AdstirVideoAds;
import com.ad_stir.interstitial.AdstirInterstitial;
import com.ad_stir.interstitial.AdstirInterstitialListener;
  ...
public class MainActivity extends AppCompatActivity {
  ...
  private AdstirInterstitial adstirInterstitial;
  private Button showButton;
  ...
  // 全画面インタースティシャルのリスナーです
  private AdstirInterstitialListener listener = new AdstirInterstitialListener() {
    @Override
    public void onLoad(int spot_no) {
      // ロードが完了した時の処理を記述できます。
      // この例ではロードが完了した時に再生ボタンを有効にします。 
      showButton.setEnabled(true);
    }

    @Override
    public void onFailed(int spot_no) {
      // スタートが失敗した時の処理を記述できます。
    }
    @Override
    public void onStart(int spot_no) {
      // 動画が再生された時の処理を記述できます。
    }
    @Override
    public void onStartFailed(int spot_no) {
      // 動画の再生が失敗した時の処理を記述できます。
    }
    @Override
    public void onFinished(int spot_no) {
      // 動画の再生が終了した時の処理を記述できます。
    }
    @Override
    public void onClose(int spot_no) {
      // 動画が閉じられた時の処理を記述できます。
    }
  };

  @Override
  // 広告の読み込み
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.xxxx);

    // 使用する動画リワードと全画面インタースティシャルの全てのスポットIDについて、初期化処理を行います。
    int[] spotIds = { 1, 2 };
    AdstirVideoAds.init(this, "MEDIA-xxxxxx", spotIds);
    // スポットIDごとにインスタンスを生成します。ここでは1についてのみ生成します。
    adstirInterstitial = new AdstirInterstitial(this, "MEDIA-xxxxxx", 1);
    // 上で定義したリスナーを登録します。
    adstirInterstitial.setAdstirInterstitialListener(listener);
    // 広告を読み込みます。
    adstirInterstitial.load();

    showButton = (Button) findViewById(show_button);
    showButton.setEnabled(false);
    showButton.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View v) {
        // ボタンをタップした時に再生を開始します
        if (adstirInterstitial.canShow()) {
          adstirInterstitial.show();
        }
      }
    });
  }

  // 広告の一時停止等
  @Override
  protected void onResume() {
	  if(adstirInterstitial != null) adstirInterstitial.resume();
	  super.onResume();
  }

  @Override
  protected void onPause() {
	  if(adstirInterstitial != null) adstirInterstitial.pause();
	  super.onPause();
  }

  @Override
  protected void onDestroy() {
	  if(adstirInterstitial != null) adstirInterstitial.destroy();
	  super.onDestroy();
  }
}
```

## ライブラリ詳細

[APIリファレンス](../api/index.md#全画面インタースティシャル広告)をご覧ください。