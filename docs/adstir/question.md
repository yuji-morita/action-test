# よくある質問

## レポートに表示回数が反映されません

開発版とリリース版のパッケージ名が異なる場合、一部の提携ネットワークで実績の取得が行われないことがございます。
その際は、リリース版と同じパッケージ名に変更いただいた上でテストいただくか、開発版とリリース版のパッケージ名が異なる旨を添えていただき、レポート数値について営業担当にお問い合わせください。

## 「You may not prepare AdstirInterastitial.」と表示される

初期化処理が行われていません。  
`AdstirInterstitial.prepare(withMedia:, spots:)`もしくは`+ [AdstirInterstitial prepareWithMedia:spots]`を利用して必ず初期化を実施してください。