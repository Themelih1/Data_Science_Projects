import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://eu-de.dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html?context=wx)
API_KEY = "MY_IAM_API_KEY_HERE"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]


# Hata Kontrolü: Token başarılıysa (200 OK) veya "access_token" varsa devam et


if token_response.status_code == 200 and "access_token" in token_response.json():
    mltoken = token_response.json()["access_token"]
    print("Successfully taken api.")
else:
    # Hata durumunda kodun neden başarısız olduğunu yazdır.
    print(f" Not Successfully api Status code: {token_response.status_code}")
    try:
        print("Yanıt Detayı:", token_response.json())
    except requests.exceptions.JSONDecodeError:
        print("Yanıt Detayı:", token_response.text)
    # Programı burada durdurur
    raise Exception("Token alma işlemi başarısız. Lütfen API Anahtarınızı kontrol edin.")

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE:  manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [
	{
		"fields": [
            "customerID", "gender", "SeniorCitizen", "Partner", "Dependents",
            "tenure", "PhoneService", "MultipleLines", "InternetService",
            "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport",
            "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling",
            "PaymentMethod", "MonthlyCharges", "TotalCharges"
        ],
		"values": [
            [
                "8888-ABCD", "Male", "No", "No", "No",
                5, "Yes", "No", "Fiber optic",
                "No", "No", "No", "No",
                "Yes", "Yes", "Month-to-month", "Yes",
                "Electronic check", 95.95, 479.75
            ]
        ]
	}
]}
response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/churnapi/predictions?version=2021-05-01'
                                 '', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})

print("Scoring response")
try:
    print(response_scoring.json())
except ValueError:
    print(response_scoring.text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")