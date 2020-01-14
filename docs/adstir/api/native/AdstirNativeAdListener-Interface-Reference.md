# AdstirNativeAdListener Interface Reference

ネイティブ広告用のリスナーです。  
AdstirNativeAdListenerのメソッドはすべてバックグラウンドスレッドで動作します。  
UIを操作する場合はActivity.runOnUiThreadを利用してください。  

## Methods

### onReceive
広告レスポンスが正常に取得できた時に呼び出されるメソッドです。
```java
public void onReceive(AdstirNativeAdResponse response);
```

### onFailed
広告レスポンスが正常に取得できなかった時に呼び出されるメソッドです。
```java
public void onFailed();
```
