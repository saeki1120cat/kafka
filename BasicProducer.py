# 用來接收從 Consumer instance 發出的 error 訊息
def error_cb(err):
    sys.stderr.write(f'Error: {err}')
    

# 主程式進入點
if __name__ == '__main__':
    # 步驟1. 設定要連線到 Kafka 集群的相關設定
    props = {
        # 尋找 Kafka 集群在那裡
        'bootstrap.servers': 'localhost:9092',    # 置換成要連接的 Kafka 集群
        'error_cb': error_cb,                     # 設定接收 error 訊息的 callback 函數
        'max.in.flight.requests.per.connection': 1
    }

    # 步驟2. 產生一個 Kafka 的 Producer 的實例
    producer = Producer(props)

    # 步驟3. 指定想要發佈訊息的 topic 名稱
    topicName = 'kafka_test.test'
    msgCount = 1000
    try:
        print('Start sending messages ...')

        # produce(topic, [value], [key], [partition], [on_delivery], [timestamp], [headers])
        for i in range(0, msgCount):
            producer.produce(topicName, key=str(i), value=f'msg_{i}')
            producer.poll(0)  # 呼叫 poll 來讓 client 程式去檢查內部的 Buffer

            print(f'key={i}, value=msg_{i}')
            time.sleep(1)  # 讓主執行緒停個 1 秒

        print('Send ' + str(msgCount) + ' messages to Kafka')

    except BufferError as e:
        # 錯誤處理
        sys.stderr.write(
            f'Local producer queue is full ({len(producer)} messages awaiting delivery): try again\n'
        )

    except Exception as e:
        sys.stderr.write(str(e))

    # 步驟5. 確認所有在 Buffer 裡的訊息都己經送出去給 Kafka 了
    producer.flush(10)
    print('Message sending completed!')
