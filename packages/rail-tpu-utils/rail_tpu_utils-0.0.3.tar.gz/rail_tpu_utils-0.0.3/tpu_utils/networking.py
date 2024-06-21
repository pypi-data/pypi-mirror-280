import requests
from google.cloud import storage
import logging

def prevent_cross_region(*urls):
    """
    Errors if performing cross-region traffic (which can incur significant networking costs).
    No errors if not running on GCP

    Example:
    ```
        def main(_):
            prevent_cross_region(FLAGS.save_dir, FLAGS.data_dir) 
    ```
    """

    client = None

    def get_vm_location():
        try:
            vm_metadata = requests.get(
                "http://metadata.google.internal/computeMetadata/v1/instance?recursive=true",
                headers={"Metadata-Flavor": "Google"},
            ).json()
            zone = vm_metadata["zone"].rpartition("/")[2]
            return zone
        except Exception as e:
            logging.warning(str(e))
            return None

    def get_bucket_location(path):
        nonlocal client
        if client is None:
            client = storage.Client()
        bucket_name = path.removeprefix("gs://").partition("/")[0]
        try:
            bucket = client.get_bucket(bucket_name)
            return bucket.location
        except Exception as e:
            logging.warning(e)
            logging.warning(
                f"Could not determine bucket location for gs://{bucket_name}"
            )
            return None

    # Only use this if the above method fails
    # def get_bucket_location_hacky(path):
    #     import fnmatch

    #     if fnmatch.fnmatch(path, "*europe*"):
    #         return "EUROPE-WEST4"
    #     elif fnmatch.fnmatch(path, "*central2*"):
    #         return "US-CENTRAL2"
    #     elif fnmatch.fnmatch(path, "*central1*"):
    #         return "US-CENTRAL1"
    #     else:
    #         logging.warning(f"Could not determine bucket location for {path}")
    #         return None

    zone = get_vm_location()
    if zone is None:
        logging.warning("Could not determine zone of VM. Assuming code is not running on Google Cloud")
        zone = "local" # Should error against any Google Cloud Bucket
    match = zone.rpartition("-")[0].upper()
    for url in urls:
        if url.startswith("gs://"):
            location = get_bucket_location(url)
            if location != match:
                raise ValueError(f"URL {url} is in {location} but VM is in {zone}")

