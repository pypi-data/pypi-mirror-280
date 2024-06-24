from sdk import Neuropacs
from PIL import Image
import io
import json

def main():
    # api_key = "your_api_key"
    api_key = "cdXVNIFzEUbSElTpoVoK4SyRrJ7Zj6n6Y6wgApIc"
    server_url = "https://sl3tkzp9ve.execute-api.us-east-2.amazonaws.com/dev"
    product_id = "PD/MSA/PSP-v1.0"
    result_format = "PNG"


    # PRINT CURRENT VERSION
    # version = Neuropacs.PACKAGE_VERSION

    # INITIALIZE NEUROPACS SDK
    # npcs = Neuropacs.init(server_url, server_url, api_key)
    npcs = Neuropacs(server_url, api_key)

    # CREATE A CONNECTION   
    conn = npcs.connect()
    print(conn)

    # CREATE A NEW JOB
    order = npcs.new_job()
    print(order)

    # # # # # UPLOAD A DATASET
    # upload = npcs.upload("../dicom_examples/DICOM_small/woo_I0", "test123", order)
    # datasetID = npcs.upload_dataset("../dicom_examples/DICOM_small", order, order, callback=lambda data: print(data))
    # print(datasetID)

    # # # START A JOB
    # job = npcs.run_job(product_id, "c2597559-4f9f-423a-9c08-2037da36944d")
    # print(job)

    # # # CHECK STATUS
    status = npcs.check_status("c2597559-4f9f-423a-9c08-2037da36944d")
    print(status)

    # GET RESULTS
    results = npcs.get_results(result_format, "c2597559-4f9f-423a-9c08-2037da36944d")
    print(results)

    # image = Image.open(results)

    # # Save the image to a file
    # output_file = 'restored_image.png'
    # image.save(output_file)

    # # Optionally, display the image
    # image.show()
    # print(results)

    

main()