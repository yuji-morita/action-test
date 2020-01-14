# AdstirLoadImageListener Interface Reference

イメージデータ読み込み用のリスナーです。  
AdstirLoadImageListenerのメソッドはすべてバックグラウンドスレッドで動作します。  
UIを操作する場合はActivity.runOnUiThreadを利用してください。

## Methods

### onLoad
データの読み込みが成功した時に呼び出されるメソッドです。
```java
public void onLoad(byte[] imageData);
```

### onFailed
データの読み込みが失敗した時に呼び出されるメソッドです。
```java
public void onFailed();
```
