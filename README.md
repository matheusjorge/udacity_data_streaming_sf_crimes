# udacity_data_streaming_sf_crimes

Second project of Udacity's Data Stream Nanodegree

## Screenshots

### Kafka Console Consumer
![kafka-console](https://github.com/matheusjorge/udacity_data_streaming_sf_crimes/tree/master/images/kafka-console-consumer-screenshot.PNG)

### Spark Progress Report
![progress-report](https://github.com/matheusjorge/udacity_data_streaming_sf_crimes/tree/master/images/spark-progress-report-screenshot.PNG)

### Spark UI
![spark-ui](https://github.com/matheusjorge/udacity_data_streaming_sf_crimes/tree/master/images/spark-ui-streaming-screenshot.PNG)

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
