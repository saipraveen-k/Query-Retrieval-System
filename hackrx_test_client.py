import requests
import json

NGROK_URL = "https://71f243ddc018.ngrok-free.app"

def test_hackrx_run():
    url = f"{NGROK_URL}/api/v1/hackrx/run"
    payload = {
        "questions": [
            "Does the policy cover knee surgery in Pune?",
            "What is the waiting period for cataract surgery?"
        ],
        "file_path": "data/BAJAJ.pdf"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    try:
        print("Response JSON:", response.json())
    except Exception as e:
        print("Response Text:", response.text)

if __name__ == "__main__":
    test_hackrx_run()
