# dataforum-2016
Spark in the Cloud, a practical introduction. My talk at Budapest Data Forum 2016

# How to start Spark on EMR
1. Create an EMR cluster
2. Make sure that the Security group of the Master Node accepts connections on port 8889 and 4040
3. SSH into the master node
4. Execute the following commands
   ```
   sudo pip install s3cmd==1.6.1 ipython[notebook]==4.1.0 py4j==0.9.2
   
   export PYSPARK_SUBMIT_ARGS="--master yarn"
   export PYSPARK_DRIVER_PYTHON_OPTS='notebook --port=8889 --no-browser --ip='*''
   export IPYTHON=1
   pyspark
   ```
5. You will be able to access your notebook at the master node's port 8889
6. If you want to access the Spark UI on the master node's port 4040, you will need to set up an [EMR socks proxy](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-connect-master-node-proxy.html).
7. Say hello at [zoltan@datapao.com](mailto:zoltan@datapao.com) if you liked it!
