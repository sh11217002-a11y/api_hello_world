from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_index() -> str:
    return """
    <html>
        <head>
            <title>FastAPI Hello</title>
        </head>
        <body>
            <h1>Welocome</h1>
            <p>Opne the interactive API does at http://URL/docs.</p>
        </body>
    </html>
    """



@app.get("/greet{name}")
async def greet_user(nema: str) -> dict[str, str]:
    return {
        "message": f"Hello, {nema} !",
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
