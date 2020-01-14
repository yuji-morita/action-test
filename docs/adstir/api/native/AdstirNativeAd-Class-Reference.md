# AdstirNativeAd Class Reference

ネイティブ広告のリクエストを行うクラスです。

## Constructor

### AdstirNativeAd
管理画面から取得したメディアIDと枠Noを設定してください。  
コンテキストには、Activityなどを設定してください。 
```java
public AdstirNativeAd(Context context, String mediaId, int spotNo)
```

* Parameters

|パラメータ||
|---|---|
|context|コンテキスト|
|mediaId|メディアID|
|spotNo|枠No|

## Instance Methods

### setSponsoredText
スポンサー表記の設定をします。
[ネイティブ広告ガイドライン](https://github.com/united-adstir/AdStir-Integration-Guide-Web/wiki/%E3%83%8D%E3%82%A4%E3%83%86%E3%82%A3%E3%83%96%E5%BA%83%E5%91%8A%E3%82%AC%E3%82%A4%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3)で規定されているスポンサー表記を実装した通りに設定してください。
```java
public void setSponsoredText(String sponsoredText)
```

* Parameters

|パラメータ||
|---|---|
|sponsoredText|スポンサー表記|

### setListener
ネイティブ広告のレスポンスを受け取るListenerの設定をします。  
AdstirNativeAdListenerの詳細については[こちら](AdstirNativeAdListener-Interface-Reference.md)をご覧ください。

```java
public void setListener(AdstirNativeAdListener listener)
```

* Parameters

|パラメータ||
|---|---|
|listener|リスナー|

### denyVideoOnMobileConnection
モバイル回線を使用している際に動画広告を拒否するかを設定します。
```java
public void denyVideoOnMobileConnection(boolean b)
```

* Parameters

|パラメータ||
|---|---|
|b|trueの際に、モバイル回線の場合には動画広告を拒否します|

### getAd
ネイティブ広告のリクエストを行います。  
必ず全ての設定を行ったあとで呼び出してください。  
```java
public void getAd()
```

### destroy
ネイティブ広告の破棄を行います。  
```java
public void destroy()
```

### setTitleLength

!!! warning "Deprecated"
    現在は設定する必要はありません。

タイトルの設定をします。タイトルを要求するときは設定してください。 

```java
public void setTitleLength(Integer titleLength)
```

* Parameters

|パラメータ||
|---|---|
|titleLength|表示できる最大の文字列長|

### setDescriptionLength

!!! warning "Deprecated"
    現在は設定する必要はありません。

説明文の設定をします。
説明文を要求するときは設定してください。  

```java
public void setDescriptionLength(Integer descriptionLength)
```

* Parameters

|パラメータ||
|---|---|
|descriptionLength|表示できる最大の文字列長|

### setCtaLength

!!! warning "Deprecated"
    現在は設定する必要はありません。

CTAボタンテキストの設定をします。
CTAボタンテキストを要求するときは設定してください。  
```java
public void setCtaLength(Integer ctaLength)
```

* Parameters

|パラメータ||
|---|---|
|ctaLength|最大の文字列長|

### setImage

!!! warning "Deprecated"
    現在は設定する必要はありません。

バナー画像の設定をします。バナー画像を要求するときはtrueを設定してください。  

```java
public void setImage(boolean image)
```

* Parameters

|パラメータ||
|---|---|
|image|バナー画像の有無|

### setIcon

!!! warning "Deprecated"
    現在は設定する必要はありません。

アイコン画像の設定をします。アイコン画像を要求するときはtrueを設定してください。
```java
public void setIcon(boolean icon)
```

* Parameters

|パラメータ||
|---|---|
|icon|アイコン画像の有無|

### setRating

!!! warning "Deprecated"
    現在は設定する必要はありません。

レーティングの設定をします。レーティングを要求するときはtrueを設定してください。
```java
public void setRating(boolean rating)
```

* Parameters

|パラメータ||
|---|---|
|rating|レーティングの有無|

