# AdstirLoadIconListener Interface Reference

アイコンデータ読み込み用のリスナーです。  
AdstirLoadIconListenerのメソッドはすべてバックグラウンドスレッドで動作します。  
UIを操作する場合はActivity.runOnUiThreadを利用してください。  

## Methods

### onLoad
アイコンの読み込みが成功した時に呼び出されるメソッドです。
```java
public void onLoad(byte[] data);
```

### onFailed
アイコンの読み込みが失敗した時に呼び出されるメソッドです。
```java
public void onFailed();
```
