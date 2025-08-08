import requests
import json
from datetime import datetime

# Configuration - using ngrok URL
WEBHOOK_URL = "https://71f243ddc018.ngrok-free.app/webhook/receive"

def test_webhook_receive():
    """Test the webhook receive endpoint"""
    payload = {
        "event_type": "document_uploaded",
        "data": {
            "document_id": "doc_test_123",
            "filename": "test_document.pdf",
            "user_id": "user_456"
        },
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def test_webhook_health():
    """Test the webhook health endpoint"""
    try:
        response = requests.get("https://71f243ddc018.ngrok-free.app/webhook/health")
        print(f"Health Check Status: {response.status_code}")
        print(f"Health Response: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def test_webhook_test():
    """Test the webhook test endpoint"""
    try:
        response = requests.get("https://71f243ddc018.ngrok-free.app/webhook/test")
        print(f"Test Status: {response.status_code}")
        print(f"Test Response: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    print("Testing Webhook Health...")
    test_webhook_health()
    
    print("\nTesting Webhook Test...")
    test_webhook_test()
    
    print("\nTesting Webhook Receive...")
    test_webhook_receive()
