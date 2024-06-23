try:
    received_data = r"['127.0.0.1', '127.0.0.1'],ping"
    parts = received_data.split(']', )
    headers = parts[0].strip('[').replace("'",'').split(', ')
    extracted_data = parts[1].strip(',')
    extracted_data = extracted_data.split(',',1)
    keyword = extracted_data[0]
    if len(extracted_data) > 1:
        payload = extracted_data[1]
    else:
        payload = ''
        
    print("Headers:", headers)
    print("Keyword:", keyword)
    print("Payload:", payload)
except:
    print(f"Received unexpected data format: {received_data}")

