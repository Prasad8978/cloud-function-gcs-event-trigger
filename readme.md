step1: installing functions-framework locally
    1. --> navigate to your project directory
    cd D:\Cloud-DE\GCP\CloudRunFunctions

    2. -->create virtual environmemnt
    python -m venv venv

    3. -->activate the virtual environment on windows
    venv\Scripts\activate 

pip install functions-framework


-> function deployment:
============================
gcloud run deploy python-gcstobq-load-function `
--source . `
--function gcs_to_bq_load_func `
--base-image python313 `
--region us-central1 `
--allow-unauthenticated

-> creating eventarc trinner deployment:
==========================================
gcloud eventarc triggers create gcstriggerevent `
--location=us-central1 `
--destination-run-service=python-gcstobq-load-function `
--destination-run-region=us-central1 `
--event-filters="type=google.cloud.storage.object.v1.finalized" `
--event-filters="bucket=crf-bucket1" `
--service-account=901842086162-compute@developer.gserviceaccount.com 

-> Getting logs:
==================
gcloud run services logs read python-gcptobq-load-function --limit=5 --project primeval-node-456408-u2

OR

gcloud logging read `
'resource.type="cloud_run_revision" AND resource.labels.service_name = "python-gcstobq-load-function"' `
--project=primeval-node-456408-u2 `
--limit=5 `
--format="table(timestamp,textPayload)"

-> Listing the triggers:
===========================
gcloud eventarc triggers list

-> Deleting the trigger:
===========================
gcloud eventarc triggers delete gcstriggerevent --location=us-central1



-> Direct command for deployement GEN2 cloud function from CLI:
======================================================================
gcloud functions deploy gcs_to_bq_load_func_gen2 `
--gen2 `
--runtime python312 `
--region us-central1 `
--source . `
--entry-point gcs_to_load_func `
--trigger-event google.sorage.object.finalise `
--trigger-resource crf-bucket1 `
--allow-nauthenticated 




OR




gcloud functions deploy python-gcs_to_bq_load_func-gen2 `
--gen2 `
--runtime=python310 `
--trigger-event=google.storage.object.finalize `
--trigger-resource=crf-bucket1 `
--region=us-central1 `
--entry-point=gcs_to_bq_load_func `
--source=. `
--project=primeval-node-456408-u2


