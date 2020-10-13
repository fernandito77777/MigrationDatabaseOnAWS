## Run ETL Job

After your data is going to be integrated from database to datalake, now it's time to run ETL job from your data lake to your data warehouse.

1. go to [Glue console](https://console.aws.amazon.com/glue/home?region=us-east-1)
2. click `Jobs` at the left menu
3. click the checkbox at `RedshiftETLJob`
    ![](../../images/TestDataPipeline/ETLJob/3.png)
4. click `Action` and click `Run Job`
    ![](../../images/TestDataPipeline/ETLJob/4.png)

it will take few minutes to run the job.
    ![](../../images/TestDataPipeline/ETLJob/4-2.png)

to check if the job is still running, check the `History` tab
    ![](../../images/TestDataPipeline/ETLJob/4-3.png)

Once it's done, it will change the run status as `Succeeded`
    ![](../../images/TestDataPipeline/ETLJob/4-4.png)

[BACK TO WORKSHOP GUIDE](../../README.md)