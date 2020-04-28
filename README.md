# udacity_data_streaming_sf_crimes

Second project of Udacity's Data Stream Nanodegree

## Screenshots

### Kafka Console Consumer
![](images/kafka-console-consumer-screenshot.png)

### Spark Progress Report
![](images/spark-progress-report-screenshot.png)

### Spark UI
![](images/spark-ui-streaming-screenshot.png)

## Questions

### Question 1

I tested `maxRatePerPartition` and `maxOffsetPerTrigger`. 

When we increase the value of `maxRatePerPartition` the latency drops and the throughput increases.

When we decrease the value of `maxOffsetPerTrigger` the latency increases and the throughput decreases.

These answers were evaluated `inputRowsPerSecond` and `processedRowsPerSecond`

### Question 2

Best values:
    * `maxRatePerPartition`: 300;
    * `maxOffserPerTrigger`: 200;

These are the values that give higher `inputRowsPerSecond` and `processedRowsPerSecond`. I have also evaluated if these metrics were similar, meaning we can process the same amount of data that arrives.