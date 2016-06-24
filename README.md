# exporters_bloom_filter
A bloom filter to avoid duplicated items to be used with [Exporters project](https://github.com/scrapinghub/exporters).

## Install

```
pip install exporters_bloom_filter
```


## Configuration example

```
{
    "reader": {
        "name": "exporters.readers.s3_reader.S3Reader",
        "options": {
            "bucket": "YOUR_BUCKET",
            "aws_access_key_id": "YOUR_ACCESS_KEY",
            "aws_secret_access_key": "YOUR_SECRET_KEY",
            "prefix": "exporters-tutorial/sample-dataset"
        }
    },
    "filter": {
        "name": "exporters_bloom_filter.filter.DuplicatesBloomFilter",
        "options": {
            "field": "name"
        }
    },
    "writer":{
        "name": "exporters.writers.fs_writer.FSWriter",
        "options": {
            "filebase": "/tmp/output/"
        }
    }
}
```

This configuration would filter all the items with a duplicated `name` field.

