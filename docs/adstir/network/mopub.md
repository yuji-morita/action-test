# MoPub広告の導入

## 対応OS

iOS 8.0以降

## SDKの準備
バンドル版の入手は、担当または[お問い合わせフォーム](https://ja.ad-stir.com/contact "お問い合わせフォーム")よりご連絡ください。

## プロジェクトへのSDKの追加

### CocoaPodsを利用して組み込む場合

CocoaPodsでの導入については[こちら](../init/cocoapods.md)をご覧ください。

Maioを利用される場合、Podfileに下記の記述を追記します。  
pathについては、配置しているSDKへのパスに適宜変更してください。

```
pod 'AdStir-Ads-SDK-VideoAdSDKBundled/MoPub', :path => 'AdstirAdsSdkiOS-X.X.X-VideoAdSDKBundled'
```

### CocoaPodsを利用せず組み込む場合
 
 1. `libAdstirAdsMediationAdapter-MoPub.a`、`MoPubSDKFramework.xcframework`を、プロジェクト内の任意の箇所にドラッグ&ドロップします。
 1. `Copy items if needed`にチェックを入れます。
 1. `Add to targets`欄で、adstir SDKを利用するすべてのターゲットにチェックを入れます。
 1. `Finish`をクリックします。
 1. GeneralタブのEmbedded Binariesに`MoPubSDKFramework.xcframework`を追加します。


## ビルド設定の変更

1. プロジェクトファイル設定画面を開きます。
1. 動画広告を組み込むビルドターゲットを選択します。
1. **Build Target**タブを選択します。
1. 画面右側の検索窓に**Other Linker Flags**と入力し、検索します。
1. **Other Linker Flags**欄に、**-ObjC**と設定します。  
MoPub広告を利用するためには、この設定が必須となり、設定がされていない場合は、案件切れ扱いとなってしまいます。
1. 組み込む対象の全てのビルドターゲットに、同じ設定を行います。  
もしくは、この設定はプロジェクト単位で設定することも可能です。

## 依存Framework/Libraryの追加
名前|ステータス
----|----
CoreGraphics.framework|Required
MediaPlayer.framework|Required
StoreKit.framework|Required
Webkit.framework|Optional
