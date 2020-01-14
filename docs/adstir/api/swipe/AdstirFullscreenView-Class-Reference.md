# AdstirFullscreenView Class Reference

スワイプインタースティシャル広告を呼び出すクラスです。

## Class Methods


### AdstirFullscreenView
コンストラクタです。管理画面から取得したメディアIDと枠Noを設定してください。

```java
public AdstirFullscreenView(Activity activity, String mediaId, int spotNo)
```

* Parameters

|パラメータ||
|---|---|
|activity|スワイプインタースティシャル広告を配置するアクティビティ|
|mediaId|メディアID|
|spotNo|枠No|

### setListener
リスナーを設定します。
AdstirFullscreenListenerについては[こちら](AdstirFullscreenListener-Class-Reference.md)をご覧ください。
```java
public void setListener(AdstirFullscreenListener listener)
```

* Parameters

|パラメータ||
|---|---|
|listener|リスナー|
