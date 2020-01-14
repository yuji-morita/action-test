# AdstirNativeVideoListener Interface Reference

ネイティブ動画広告のイベントを通知するリスナーです。  

## Methods


### onLoad
ネイティブ動画広告が正常に読み込まれた時に呼び出されるメソッドです。
```java
public void onLoad();
```

### onFailed
ネイティブ動画広告の読み込みに失敗した時に呼び出されるメソッドです。  
ErrorCodeの詳細については[こちら](#error-code)をご覧ください。
```java
public void onFailed(ErrorCode code);
```

### onStart
ネイティブ動画広告の再生が開始された時に呼び出されるメソッドです。
```java
public void onStart();
```

### onStop
ネイティブ動画広告の再生が停止された時に呼び出されるメソッドです。
```java
public void onStop();
```

### onFinish
ネイティブ動画広告の再生が終了した時に呼び出されるメソッドです。
```java
public void onFinish();
```

### onStartFailed
ネイティブ動画広告の再生に失敗した時に呼び出されるメソッドです。
```java
public void onStartFailed(ErrorCode code);
```

## Error Code

ネイティブ動画広告で通知されるエラーコードの一覧です。不明な点に関してはお問い合わせください。

| エラー名称 | エラー番号 | エラーメッセージ | 発生理由 |
|------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| PREPARE_VIDEO_ERROR | 14100 | Failed to prepare video player. | Playerの準備に失敗した。 |
| IO_ERROR | 14101 | File or network related operation errors. | ファイルまたはネットワーク関連の操作エラー。 |
| TIMED_OUT_ERROR | 14102 | A timeout error occurred. | Playerがタイムアウトした。 |
| MALFORMED_ERROR | 14103 | Bitstream is not conforming to the related coding standard or file spec. | ビットストリームが関連コーディング規格またはファイル仕様に準拠していない。 |
| UNSUPPORTED_ERROR | 14104 | Bitstream is conforming to the related coding standard or file spec, but the media framework does not support the feature. | メディアフレームワークはこの機能をサポートしていない。 |
| NOT_VALID_FOR_PROGRESSIVE_PLAYBACK | 14105 | The video is streamed and its container is not valid for progressive playback. | 動画のコンテナがプログレッシブ再生に対応していない。 |
| UNKNOWN_ERROR | 14106 | Unspecified media player error. | Playerにおいて不明なエラーが発生した。 |
| SERVER_ERROR | 14107 | An error occurred on the video server. | 動画サーバーにエラーが発生した。 |
| VIDEO_NOT_SPECIFIED | 14108 | No video specified. | プレイヤー読み込みの際、ネイティブ動画オブジェクトが指定されていなかった。 |
| NO_FREE_SPACE | 14109 | There is insufficient free space. | 動画取得の際、ディスクの空き容量が不足した。 |
| INCORRECT_FILE_NAME | 14110 | File name is incorrect. | 動画取得の際、保存するファイル名が不正だった。 |
| INCORRECT_URL | 14111 | Url is incorrect. | 動画取得の際、不正なURLが指定された。 |
| OPEN_STREAM_ERROR | 14112 | Unable to open stream. | 動画取得の際、ストリームのオープンに失敗した。 |
| VIDEO_CACHE_ERROR | 14113 | Unable to make video cache. | 動画キャッシュの作成に失敗した。 |
| PLAYER_STATE_ERROR | 14114 | Error playing a video for incorrect state. | Playerが正しくない状態で再生が呼ばれた。 |
| PLAYER_UNAVAILABLE_ERROR | 14115 | Video view is not prepared. | ビューの準備が整っていない状態で再生が呼ばれた。 |
| UNKNOWN_ERROR | 14199 | unknown error. | 不明なエラー。 |


