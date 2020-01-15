# AdMobメディエーションで利用できるアドネットワーク

adstirのAdMobパッケージには下記のアドネットワークのSDKがパッケージングされております。

アドネットワーク|SDKバージョン|バナー|インタースティシャル|動画リワード|動画リワード(新API)|ネイティブ
---| :-: |:-:|:-:|:-:|:-:|:-:
AdColony|{{ version.adcolony }}| o | o | o | o | -
AppLovin|{{ version.applovin }}| o | o | o | o | o
Facebook|{{ version.facebook }}| o | o | o | o | o
maio    |{{ version.maio     }}| - | o | o | o | -
MoPub   |{{ version.mopub    }}| o | o | o | o | o
nend    |{{ version.nend     }}| o | o | o | o | - 
Tapjoy  |{{ version.tapjoy   }}| - | o | o | o | - 
UnityAds|{{ version.unityads }}| o | o | o | o | - 
FiveAd[^1]|{{ version.fivead }}| o | o | - | o | o

[^1]: これどうしようか

## 追加実装

アドネットワークによっては追加実装が必要なネットワークがございます。下記を参照して実装をお願いします。

### MoPubの追加実装
広告の読み込み前にMoPub SDKを初期化する必要がございます。  
MainActivityのonCreate等で`MoPub.initializeSdk()`を呼び出してください。  
MOPUB_AD_UNIT_IDは営業担当よりおしらせします。  

```java hl_lines="1 2 4 5 6 7 13 14"
import com.mopub.common.MoPub;
import com.mopub.common.SdkConfiguration;

public class MainActivity extends AppCompatActivity {
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        SdkConfiguration sdkConfiguration =
          new SdkConfiguration.Builder("MOPUB_AD_UNIT_ID").build();

        MoPub.initializeSdk(context, sdkConfiguration, null);
    }
}
```