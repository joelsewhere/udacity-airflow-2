## Project Description

You work for a marketing company, that manages webpage and sale analytics for multiple websites. You’ve been asked to write the following airflow jobs

### 1) Conversion Events
For each lead conversion event, different variables need to be tracked, causing data schemas to differ by event type. Your company has previously written individual dags for each event type. You have been tasked with refactoring these dags into a single airflow job that uses AWS Glue for managing the varying schemas, and supports the dynamic creation of new conversion events, when they occur.

Your companies Ops department occasionally pushed backfills for missing records. To support this, you must add Parameter form triggers for conversion event collections. 

### 2) Machine learning models
Your company’s analytics team have built three machine learning models that need to be run at different schedules. For this, you will write a single airflow dag that uses branching for activating each model at their set schedule. Machine learning models should be scheduled to run on a batched cadence and triggered by updates to their relevant datasets.


### 3) Sale Events
Each website has its own API for collecting completed sale events. The websites your company manages marketing for can change. Write a dag that runs dynamically parallelized api collections for currently supported websites


### 4) Analytical Transformations
The dags above store data in separate schemas according to the website that generates the records. Write a dag that unions data into a global analytical schema. 
