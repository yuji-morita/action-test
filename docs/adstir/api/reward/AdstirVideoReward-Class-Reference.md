# AdstirVideoReward Class Reference

動画リワード広告を呼び出すためのクラスです。

## Constructor
### AdstirVideoReward
管理画面から取得したメディアIDと枠Noを設定してください。

```java
public AdstirVideoReward(Activity activity, String mediaId, int spotNo) 
```

* Parameters

|パラメータ||
|---|---|
|activity|アクティビティ|
|mediaId|メディアID|
|spotNo|枠No|

## Static Methods

### init

!!! warning "Deprecated"
    このメソッドの代わりに[こちら](../AdstirVideoAds-Class-Reference.md#init)をご利用ください

広告の初期化を行います。[コンストラクタ](#AdstirVideoReward)より前に呼び出してください。

```java
public static void init(Activity activity, String mediaId, int[] spotNoArray)
```

* Parameters

|パラメータ||
|---|---|
|activity|Activity|
|mediaId|メディアID|
|spotNoArray|枠Noの配列|

### setMediaUserID

!!! warning "Deprecated"
    このメソッドの代わりに[こちら](../AdstirVideoAds-Class-Reference.md#setmediauserid)をご利用ください

インセンティブを付与するユーザーのIDを指定します。
サーバーサイドで成果通知を受け取る場合は指定が必須となります。
ユーザIDには、ユーザーを一意に識別できるID(半角英数記号)を指定してください。

```java
public static void setMediaUserID(String userId)
```

* Parameters

|パラメータ||
|---|---|
|userID|ユーザID|

## Instance Methods

### setAdstirVideoRewardListener
リスナーを設定します。広告の読み込み時、リワードの取得時に実行する処理などを指定することが出来ます。  
AdstirVideoRewardListenerの詳細については[こちら](AdstirVideoRewardListener-Interface-Reference.md)をご覧ください。

```java
public void setAdstirVideoRewardListener(AdstirVideoRewardListener listener)
```

* Parameters

|パラメータ||
|---|---|
|listener|リスナー|

### setAppVersion
御社のアプリのバージョンを指定することができます。任意の文字列を指定してください。

```java
public void setAppVersion(String appVersion)
```

* Parameters

|Parameters||
|---|---|
|appVersion|アプリのバージョン|

### setLocation

ユーザーの位置情報を指定することが出来ます。

```java
public void setLocation(Location location)
```

* Parameters

|パラメータ||
|---|---|
|location|Locationインスタンス|

### load

設定された情報にもとづいて、広告の読み込みを行います。

```java
public void load()
```

### canShow
動画広告の再生可否を判定します。

```java
public boolean canShow()
```

* Returns

|戻り値||
|---|---|
|boolean|動画広告の再生可否|

### showRewardVideo

動画広告の再生を開始します。

```java
public void showRewardVideo()
```

### pause

動作を一時停止します。
ActivityのonPauseでご使用ください。

```java
public void pause()
```

### resume

動作の一時停止を解除します。
ActivityのonResumeでご使用ください。

```java
public void resume()
```

### destroy

インスタンスを破棄します。
ActivityのonDestoryでご使用ください。

```java
public void destroy()
```