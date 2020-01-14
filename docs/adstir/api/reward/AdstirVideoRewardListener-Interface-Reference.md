# AdstirVideoRewardListener Interface Reference
動画リワード広告の各イベントを通知するリスナーです。

## Methods

### onLoad
広告読み込み完了時に呼び出されます。

```java
public void onLoad(int spot_no)
```

* Parameters

|パラメータ||
|---|---|
|spot_no|枠No|

### onFailed
広告読み込み失敗時に呼び出されます。

```java
public void onFailed(int spot_no)
```

* Parameters

|パラメータ||
|---|---|
|spot_no|枠No|

### onStart
動画再生開始時に呼び出されます。

```java
public void onStart(int spot_no)
```

* Parameters

|パラメータ||
|---|---|
|spot_no|枠No|

### onStartFailed
動画再生失敗時に呼び出されます。

```java
public void onStartFailed(int spot_no)
```

* Parameters

|パラメータ||
|---|---|
|spot_no|枠No|

### onFinished
動画再生終了時に呼び出されます。

```java
public void onFinished(int spot_no)
```

* Parameters

|パラメータ||
|---|---|
|spot_no|枠No|


### onReward
リワード処理完了時に呼び出されます。

```java
public void onReward(int spot_no)
```

* Parameters

|パラメータ||
|---|---|
|spot_no|枠No|

### onRewardCanceled
リワード処理が出来なかった際に呼び出されます。  
対応していないアドネットワークの場合は呼び出されません。

```java
public void onRewardCanceled(int spot_no)
```

* Parameters

|パラメータ||
|---|---|
|spot_no|枠No|

### onClose
動画Viewが閉じられるときに呼び出されます。


```java
public void onClose(int spot_no)
```

* Parameters

|パラメータ||
|---|---|
|spot_no|枠No|

