# chalice_test

test playing with chalice to create serverless API

Return status

    curl -XGET <endpoint>

Upload file to S3 (requirement s3 setup):

    curl -XPUT <endpoint>/upload/{file_name} --upload-file <file_name> --header "Content-Type:application/octet-stream"
