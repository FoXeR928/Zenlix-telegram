import uvicorn
from app import app
from config import site_host, site_port


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=site_host,
        port=site_port,
    )