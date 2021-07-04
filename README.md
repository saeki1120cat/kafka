# Apache Kafka

Apache Kafka 是針對 big data streaming 處理而設計，可以輕易達到每秒上萬等級 requests，並因其採用分散式架構，方便水平擴張，提供高可靠性、可用性與擴展性，且將資料存放於硬碟空間。
* 特色：
1. 對於災難性恢復具有很高的能力
2. 資源使用平衡
3. 叢集式管理
4. 介於各AP間的中間層系統

* 核心名詞：
  * Broker : 一台 kafka 的機器，一組 kafka 可以包含 1~n 個 broker
  * Clusters : 多個 Brokers 連接在一起稱之為 Cluster，Cluster 中存在一個 controller(動態建立)，負責分配 partitions 與監控 brokers 狀態。
  * Zookeepr : https://zookeeper.apache.org/ , kafka 必須使用 zookeeper 來進行一些管理 
  * Topics : 在 Kafka 中 topic 就像是 database 中的 table，為不同資料的類別名稱。
  * Partitions : 對於 kafka 來說，這是一個 “物理上” 儲存訊息的單位．一個 topic可以被分為 1~n 個 partition
  * Producers : 對應publish系統的概念，Producers可以新增資料到 topic。
  * Consumers : 對應subscribe系統的概念，Consumers負責從資料讀取 topic。
  * Retention : Retention 是指 Kafka 可以設定的存放在磁碟中的一段時間，預設是 7 天或是資料量大於 1 GB 就會自動刪除一些資料。Kafka 可以針對不同 topic 設定不同 Retention。
  * Multiple Clusters : Kafka 支援 Multiple Clusters，主要是為了可以提高可用性與安全性，如建立cluster 於不同的資料中心，並提供了稱之為 MirrorMaker 的工具讓你輕易在 clusters 之間複製資料。

## Kafka指令

* Create
```
kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test
```
建立一個新的 topic。 -透過-zookeeper 則是指定管理的 zookeper。--topic 指定 topic 的名稱叫做 test； 透過 --partitions 設定這個 topic 要切成 1 個 partition； --replication-factor 則是說這個 topic 要有 1 份備份；

* List
```
kafka-topics --list --zookeeper zookeeper:2181
```
可以看看現在有哪些建立起來的 topic。

* Describe
```
kafka-topics --describe --zookeeper zookeeper:2181 --topic test
```
查看 topic的詳細資料

* Delete
```
kafka-topics --delete --zookeeper zookeeper:2181 --topic test
```
刪除 topic

## 在 python使用Kafka
* 安裝 confluent_kafka
