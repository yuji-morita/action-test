# AdstirNativeAdResponse Class Reference

ネイティブ広告のレスポンスクラスです。  

## Instance Methods

### getTitle
タイトルの文字列を返却します。
```java
public String getTitle()
```

* Returns

|戻り値||
|---|---|
|String|タイトル|


### getDescription
説明文の文字列を返却します。
```java
public String getDescription()
```

* Returns

|戻り値||
|---|---|
|String|説明文|

### getCta
CTAボタンテキストの文字列を返却します。
```java
public String getCta()
```

* Returns

|戻り値||
|---|---|
|String|CTAボタンテキスト|

### getImage
バナー画像URLを返却します。
```java
public String getImage()
```

* Returns

|戻り値||
|---|---|
|String|バナー画像URL|

### bindImageToImageView
バナー画像をImageViewに対して設定します。
```java
public void bindImageToImageView(Activity activity, ImageView imageView)
```

* Parameters

|パラメータ||
|---|---|
|activity|アクティビティ|
|imageView|バナー画像を表示するImageView|

### getImageAsBytes
バナー画像のバイト配列での取得を要求します。
```java
public void getImageAsBytes()
```

### setOnLoadImageListener
バナー画像をバイト配列で取得するListenerを設定します。  
AdstirLoadImageListenerの詳細については[こちら](AdstirLoadImageListener-Interface-Reference.md)をご覧ください。
```java
public void setOnLoadImageListener(AdstirLoadImageListener listener)
```

* Parameters

|パラメータ||
|---|---|
|listener|リスナー|

### getIcon
アイコン画像URLを返却します。
```java
public String getIcon()
```

* Returns

|戻り値||
|---|---|
|String|アイコン画像URL|

### bindIconToImageView
アイコン画像をImageViewに対してBitmapを設定します。
```java
public void bindIconToImageView(Activity activity, ImageView imageView)
```

* Parameters

|パラメータ||
|---|---|
|activity|アクティビティ|
|imageView|アイコン画像を表示するImageView|

### getIconAsBytes
アイコン画像のバイト配列での取得を要求します。
```java
public void getIconAsBytes()
```


### setOnLoadIconListener
アイコン画像をバイト配列で取得するListenerを設定します。  
AdstirLoadIconListenerの詳細については[こちら](AdstirLoadIconListener-Interface-Reference.md)をご覧ください。
```java
public void setOnLoadIconListener(AdstirLoadIconListener listener)
```

* Parameters

|パラメータ||
|---|---|
|listener|リスナー|

### getRating
レーティングを返却します。
```java
public double getRating()
```

* Returns

|戻り値||
|---|---|
|double|レーティング|

### getVideo
AdstirNativeVideoオブジェクトを返却します。
```java
public AdstirNativeVideo getVideo()
```

* Returns

|戻り値||
|---|---|
|AdstirNativeVideo|AdstirNativeVideoオブジェクト|

### click
広告がクリックされた際clickメソッドを必ず呼び出してください。
```java
public void click()
```

### impression
広告表示する際impressionメソッドを必ず呼び出してください。
```java
public void impression()
```