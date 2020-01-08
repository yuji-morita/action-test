# AdColony広告の導入

## 対応OS

iOS 8.0以上

## SDKの準備

AdColonyのSDKは、VideoAdSDKBundledのパッケージに同梱されております。
作成された動画枠の`動画SDK (iOS)`より取得いただけます。

**adstir SDK 2.13.4よりAdColonyはXCode10以上でなければbitcodeが利用できません。**

### CocoaPodsを利用して組み込む場合

CocoaPodsでの導入については[こちら](../init/cocoapods.md)をご覧ください。

AdColonyを利用される場合、Podfileに下記の記述を追記します。  
pathについては、配置しているSDKへのパスに適宜変更してください。

```
pod 'AdStir-Ads-SDK-VideoAdSDKBundled/AdColony', :path => 'AdstirAdsSdkiOS-X.X.X-VideoAdSDKBundled'
```

### CocoaPodsを利用せず組み込む場合

#### プロジェクトへのSDKの追加

1. `AdColony`フォルダを、プロジェクト内の任意の箇所にドラッグ&ドロップします。
1. `Copy items if needed`にチェックを入れます。
1. `Add to targets`欄で、`AdColony`を利用するすべてのターゲットにチェックを入れます。
1. `Finish`をクリックします。

#### ビルド設定の変更

1. プロジェクトファイル設定画面を開きます。
1. 動画広告を組み込むビルドターゲットを選択します。
1. **Build Target**タブを選択します。
1. 画面右側の検索窓に**Other Linker Flags**と入力し、検索します。
1. **Other Linker Flags**欄に、**-ObjC**と **-fobjc-arc**を設定します。  
1. 組み込む対象の全てのビルドターゲットに、同じ設定を行います。  
もしくは、この設定はプロジェクト単位で設定することも可能です。

#### 依存Framework/Libraryの追加

名前|ステータス
----|----
libz.1.2.5.tbd|Required
AudioToolbox.framework|Required
JavaScriptCore.framework|Required
MessageUI.framework|Required
MobileCoreServices.framework|Required
Social.framework|Optional
StoreKit.framework|Optional
WatchConnectivity.framework|Optional
WebKit.framework|Optional

## ATSの設定
Info.plistに下記の記述を追加します。

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <false/>
    <key>NSAllowsLocalNetworking</key>
    <true/>
    <key>NSAllowsArbitraryLoadsInWebContent</key>
    <true/>
</dict>
```