# AdstirVideoAds Class Reference
動画リワード広告と全画面インタースティシャル広告の初期化を行うクラスです。

## Instance Methods

### init

動画リワード広告、全画面インタースティシャル広告の初期化を行います。  
[動画リワード広告のコンストラクタ](reward/AdstirVideoReward-Class-Reference.md#adstirvideoreward)および、[全画面インタースティシャル広告のコンストラクタ](interstitial/AdstirInterstitial-Class-Reference.md#adstirinterstitial)より前に呼び出してください。

```java
public static void init(Activity activity, String mediaId, int[] spotNoArray)
```

* Parameters

|パラメータ||
|---|---|
|activity|アクティビティ|
|mediaId|メディアID|
|spotNoArray|動画リワード広告と全画面インタースティシャル広告の枠Noの配列|

### setMediaUserID

インセンティブを付与するユーザーのIDを指定します。  
サーバーサイドで成果通知を受け取る場合は指定が必須となります。  
動画リワード広告を利用しない場合は設定する必要はありません。  
ユーザIDには、ユーザーを一意に識別できるID(半角英数記号)を指定してください。  

```java
public static void setMediaUserID(String userId)
```

* Parameters

|パラメータ||
|---|---|
|userID|ユーザID|

### getMediaUserID

インセンティブを付与するユーザーのIDを取得します。

```java
public static String getMediaUserID()
```

* Returns

|戻り値||
|---|---|
|String|ユーザーID|