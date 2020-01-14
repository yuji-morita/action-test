# 動画リワード広告

## 対応OS

Android4.1以上(Andoid4.4以上推奨)

## 広告の設定

### 1.メディアユーザIDの設定を行う
サーバーサイドで成果通知を受け取る場合、メディアユーザーIDを設定します。  
メディアユーザIDの設定は、`動画リワード広告の読み込み`よりも前までに設定する必要があります。

```java
// サーバーサイドで成果通知を受け取る場合、メディアユーザーIDを設定します。
// ここでは例として、メールアドレスを指定していますが、任意のID(半角英数記号)が利用可能です。
AdstirVideoAds.setMediaUserID("xxx@xxx.xx"); 
```

### 2.動画広告の初期化を行う

はじめに、`AdstirVideoAds.init()`を使い、プロジェクトで利用する全ての動画広告の初期化を同時に行います。  
動画リワード広告と[全画面インタースティシャル広告](../interstitial.md)を併用する場合は、同時に初期化を行う必要があります。

```java
// 使用する動画リワードと全画面インタースティシャルの全てのスポットIDについて、初期化処理を行います。
int[] spotIds = { 1, 2 };
AdstirVideoAds.init(this, "MEDIA-xxxxxx", spotIds);
```

### 3.動画リワード広告のインスタンスを生成

`AdstirVideoReward`のインスタンスを生成します。
```java
// スポットIDごとにインスタンスを生成します。ここでは1についてのみ生成します。
AdstirVideoReward adstirVideoReward = new AdstirVideoReward(this, "MEDIA-xxxxxx", 1);
```

### 4.リスナーの生成

動画リワード広告のイベント通知を行うリスナーのインスタンスを生成します。

```java
// リスナーの定義
AdstirVideoRewardListener listener = new AdstirVideoRewardListener() {
    // 広告の読み込みが完了した際に再生を開始します。
    public void onLoad(int spot_no) {
        // 動画の読み込みが完了した時の処理を書きます
    }
    public void onFailed(int spot_no) {
        // 動画の読み込みが失敗した時の処理を書きます
    }
    public void onStart(int spot_no) {
        // 動画の再生が開始した時の処理を書きます
    }
    public void onStartFailed(int spot_no) {
        // 動画の再生が失敗した時の処理を書きます
    }
    public void onFinished(int spot_no) {
        // 動画の再生が終了した時の処理を書きます
    }
    public void onReward(int spot_no) {
        // リワードが発生した時の処理を書きます
    }
    public void onRewardCanceled(int spot_no) {
        // リワードの発生が失敗した時の処理を書きます
    }
    public void onClose(int spot_no) {
        // 動画がとじらられた時の処理を書きます
    }
};

// 上で定義したリスナーを登録します。
adstirVideoReward.setAdstirVideoRewardListener(listener);
```

### 5.動画リワード広告の読み込み

動画リワード広告の読み込みを行います。

```java
// 動画リワード広告を読み込みます。
adstirVideoReward.load();
```

### 6.動画リワード広告の再生

読み込みが完了した動画リワード広告を再生します。
動画の再生後、もう一度動画を再生するためには`5.動画リワード広告の読み込み`を行う必要があります。

```java
// 再生可能状態を確認してから再生します。
if(adstirVideoReward.canShow()){
    adstirVideoReward.showRewardVideo();
}
```

## 動画リワード広告の実装例

動画リワード広告の実装例になります。

```java
// 下記のインポートが必要です
import com.ad_stir.interstitial.AdstirVideoAds;
import com.ad_stir.videoreward.AdstirVideoReward;
import com.ad_stir.videoreward.AdstirVideoRewardListener;

private static final String TAG = "Adstir";

private boolean isRewarded = false;
private AdstirVideoReward adstirVideoReward;

// リスナーの定義
private AdstirVideoRewardListener listener = new AdstirVideoRewardListener() {
    // 広告の読み込みが完了した際に再生を開始します。
    public void onLoad(int spot_no) {
      // ロードが完了した時の処理を記述できます。
      // この例ではロードが完了した時に再生ボタンを有効にします。 
      showButton.setEnabled(true);
    }

    public void onFailed(int spot_no) {
        // スタートが失敗した時の処理を記述できます。
    }
    public void onStart(int spot_no) {
        // 動画が再生された時の処理を記述できます。
    }
    public void onStartFailed(int spot_no) {
        // 動画の再生が失敗した時の処理を記述できます。
    }
    public void onFinished(int spot_no) {
        // 動画の再生が終了した時の処理を記述できます。
    }
    public void onReward(int spot_no) {
        // リワードが付与された時の処理を記述できます。
        isRewarded = true;
    }
    public void onRewardCanceled(int spot_no) {
        // リワードが付与されなかった時の処理を記述できます。
    }
    public void onClose(int spot_no) {
        // 動画が閉じられた時の処理を記述できます。
    }
};


@Override
// 広告の読み込み
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.xxxx);

    // サーバーサイドで成果通知を受け取る場合、メディアユーザーIDを設定します。
    // ここでは例として、メールアドレスを指定していますが、任意のID(半角英数記号)が利用可能です。
    AdstirVideoAds.setMediaUserID("xxx@xxx.xx"); 
    // 使用する動画リワードと全画面インタースティシャルの全てのスポットIDについて、初期化処理を行います。
    int[] spotIds = { 1, 2 };
    AdstirVideoAds.init(this, "MEDIA-xxxxxx", spotIds);
    // スポットIDごとにインスタンスを生成します。ここでは1についてのみ生成します。
    adstirVideoReward = new AdstirVideoReward(this, "MEDIA-xxxxxx", 1);
    // 上で定義したリスナーを登録します。
    adstirVideoReward.setAdstirVideoRewardListener(listener);
    // 広告を読み込みます。
    adstirVideoReward.load();

    showButton = (Button) findViewById(show_button);
    showButton.setEnabled(false);
    showButton.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View v) {
        // ボタンをタップした時に再生を開始します
        if (adstirVideoReward.canShow()) {
            adstirVideoReward.show();
        }
      }
    });
}

// 広告の一時停止等
@Override
protected void onResume() {
    if(adstirVideoReward != null) {
        adstirVideoReward.resume();
    }
    if(isRewarded) {
        isRewarded = false;
        Log.d(TAG, "Reward success.");
    }
    super.onResume();
}

@Override
protected void onPause() {
    if(adstirVideoReward != null) adstirVideoReward.pause();
    super.onPause();
}

@Override
protected void onDestroy() {
    if(adstirVideoReward != null) adstirVideoReward.destroy();
    super.onDestroy();
}
```

## ライブラリ詳細

[APIリファレンス](../../api/index.md#動画リワード広告)をご覧ください。

## 成果のコールバックURLへの通知

adstirでは、インセンティブ付与の通知を、任意のコールバックURLに行うことが可能です。
付与するインセンティブの単位と額は、任意の値に変更可能です。
`AdstirVideoAds.setMediaUserID("xxx@xxx.xx");` でユーザーIDを設定していない場合には通知されませんので、ご注意ください。

[動画インセンティブ付与をコールバックURLに通知する](callback.md)
