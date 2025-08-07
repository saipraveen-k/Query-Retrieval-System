from fastapi import APIRouter, HTTPException, Request, BackgroundTasks
from pydantic import BaseModel
from typing import Dict, Any
import logging
import json
from datetime import datetime

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/webhook", tags=["webhook"])

class WebhookPayload(BaseModel):
    event_type: str
    data: Dict[str, Any]
    timestamp: datetime = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

@router.post("/receive")
async def receive_webhook(payload: WebhookPayload, request: Request, background_tasks: BackgroundTasks):
    """
    Receive and process webhook events
    
    Example payload:
    {
        "event_type": "document_uploaded",
        "data": {
            "document_id": "doc_123",
            "filename": "example.pdf"
        }
    }
    """
    try:
        # Log the webhook event
        logger.info(f"Received webhook: {payload.event_type}")
        logger.info(f"Payload: {payload.dict()}")
        
        # Process webhook based on event type
        background_tasks.add_task(process_webhook_event, payload)
        
        return {
            "status": "received",
            "event_id": f"evt_{datetime.now().timestamp()}",
            "message": "Webhook processed successfully"
        }
        
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/test")
async def test_webhook():
    """Test endpoint to verify webhook is working"""
    return {
        "status": "webhook endpoint is active",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "POST": "/webhook/receive",
            "GET": "/webhook/test"
        }
    }

@router.get("/health")
async def webhook_health():
    """Health check for webhook service"""
    return {
        "status": "healthy",
        "service": "webhook",
        "timestamp": datetime.now().isoformat()
    }

async def process_webhook_event(payload: WebhookPayload):
    """Process different webhook events"""
    try:
        if payload.event_type == "document_uploaded":
            # Handle document upload event
            logger.info(f"Processing document upload: {payload.data}")
            # Add your document processing logic here
            
        elif payload.event_type == "query_submitted":
            # Handle query submission event
            logger.info(f"Processing query: {payload.data}")
            # Add your query processing logic here
            
        elif payload.event_type == "retrieval_completed":
            # Handle retrieval completion event
            logger.info(f"Processing retrieval: {payload.data}")
            # Add your retrieval processing logic here
            
        else:
            logger.warning(f"Unknown event type: {payload.event_type}")
            
    except Exception as e:
        logger.error(f"Error processing webhook event: {str(e)}")
