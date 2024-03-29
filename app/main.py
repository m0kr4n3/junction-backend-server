import uvicorn
import logging
import os
from src.db.init_db import init_db
from src.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




if __name__ == "__main__":
        
    logger.info("Creating initial data")
    db = SessionLocal()
    init_db(db)
    logger.info("Initial data created")
    
    if os.environ.get('PORT') == None:
        os.environ['PORT'] = "8080"

    uvicorn.run("src.api.api:api_router", host="0.0.0.0", port=int(os.environ.get('PORT')), reload=True)
