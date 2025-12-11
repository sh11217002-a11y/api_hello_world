from datetime import datetime

@app.get("/greet{name}")
async def greet_user(nema: str) -> dict[str, str]:
    return {
        "message": f"Hello, {nema} !",
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
