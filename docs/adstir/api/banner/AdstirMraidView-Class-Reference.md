# AdstirMraidView Class Reference

バナー広告を呼び出すためのクラスです。

## Constructor

### AdstirMraidView
管理画面から取得したメディアIDと枠Noを設定してください。  
枠サイズは、管理画面で登録した枠サイズと同じものを設定してください。  
AdSizeについては[こちら](AdSize-Class-Reference.md)をご覧ください。  
広告のローテーション時間は60秒になります。

```java
public AdstirMraidView(Activity activity, String mediaId, int spotNo, AdSize size)
```

* Parameters

|パラメータ||
|---|---|
|activity|アクティビティ|
|mediaId|メディアID|
|spotNo|枠No|
|size|枠サイズ|

## Instance Methods
### setListener
リスナーを設定します。
Listenerについては[こちら](Listener-Class-Reference.md)をご覧ください。
```java
public void setListener(Listener listener)
```

* Parameters

|パラメータ||
|---|---|
|listener|リスナー|
