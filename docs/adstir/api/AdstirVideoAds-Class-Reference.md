# AdstirVideoAds Class Reference

動画視聴型インセンティブ広告及び全画面インタースティシャル広告の初期化用クラスです。

## Class Methods
* [+prepareWithMedia:spots:](#preparewithmediaspots)
* [+setMediaUserID:](#setmediauserid)
* [+mediaUserID](#mediauserid)

***

### +prepareWithMedia:spots:
動画視聴型インセンティブ広告及び全画面インタースティシャル広告の初期化を行います。


```objc
+ (void)prepareWithMedia:(NSString *)media spots:(NSArray *)spots
```

#### Parameters
* _media_
    * メディアID

* _spots_
    * 動画視聴型インセンティブ広告及び全画面インタースティシャル広告のスポットID

***

### +setMediaUserID:
メディアユーザIDを設定します。メディアユーザーIDを設定していない場合は、動画リワード利用時の[成果のコールバックURLへの通知](https://github.com/united-adstir/AdStir-Integration-Guide-Android/wiki/%E5%8B%95%E7%94%BB%E3%82%A4%E3%83%B3%E3%82%BB%E3%83%B3%E3%83%86%E3%82%A3%E3%83%96%E4%BB%98%E4%B8%8E%E3%82%92%E3%82%B3%E3%83%BC%E3%83%AB%E3%83%90%E3%83%83%E3%82%AFURL%E3%81%B8%E9%80%9A%E7%9F%A5%E3%81%99%E3%82%8B)を行いません。

```objc
+ (void)setMediaUserID:(NSString *)mediaUserID
```

#### Parameters

* _mediaUserID_
  * メディアユーザID

***

### +mediaUserID
メディアユーザIDを取得します。

```objc
+ (NSString *)mediaUserID
```

#### Returns

* _NSString *_
  * メディアユーザID
