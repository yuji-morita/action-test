# AdstirInterstitial Class Reference
全画面インタースティシャル広告を呼び出すクラスです。

## Constructor
### AdstirInterstitial
管理画面から取得したメディアIDと枠Noを設定してください。

```java
public AdstirInterstitial(Activity activity, String mediaId, int spotNo) 
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

広告の初期化を行います。[コンストラクタ](#adstirinterstitial)より前に呼び出してください。


```java
public static void init(Activity activity, String mediaId, int[] spotNoArray)
```

* Parameters

|パラメータ||
|---|---|
|activity|アクティビティ|
|mediaId|メディアID|
|spotNoArray|枠Noの配列|


## Instance Methods

### setAdstirInterstitialListener

リスナーを設定します。広告の読み込み時、リワードの取得時に実行する処理などを指定することが出来ます。  
AdstirInterstitialListenerの詳細については[こちら](AdstirInterstitialListener-Interface-Reference.md)をご覧ください。

```java
public void setAdstirInterstitialListener(AdstirInterstitialListener listener)
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

|パラメータ||
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

### show

ビデオの再生を開始します。

```java
public void show()
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