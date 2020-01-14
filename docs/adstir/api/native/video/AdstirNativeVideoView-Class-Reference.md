# AdstirNativeVideoView Class Reference

ネイティブ動画広告のクラスです。  

## Instance Methods

### load
AdstirNativeVideoをセットして、動画広告を読み込みます。

```java
public void load(AdstirNativeVideo adstirNativeVideo)
```

* Parameters

|パラメータ||
|---|---|
|adstirNativeVideo|動画の再生を行うAdstirNativeVideoのインスタンス|

### setAdstirNativeVideoListener
ネイティブ動画広告のイベントを受け取るリスナーの設定をします。
AdstirNativeVideoListenerの詳細については[こちら](AdstirNativeVideoListener-Interface-Reference.md)をご覧ください。

```java
public void setAdstirNativeVideoListener(AdstirNativeVideoListener listener)
```

* Parameters

|パラメータ||
|---|---|
|listener|リスナー|

### release
動画広告を解放します。

```java
public void release()
```