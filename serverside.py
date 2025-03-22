# region imports
from AlgorithmImports import *
# endregion
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.api_route("/order", methods=["GET", "HEAD"])
async def get_order():
    """
    Trader calls this to get the next order.
    Example response: {"buy": 100, "sell": 0}
    """

    return {"buy": 0.1, "sell": 0}

@app.api_route("/report", methods=["GET", "HEAD"])
async def report_status(request: Request):
    """
    Trader calls this to report current status via headers.
    """
    report = dict(request.headers)

    print(f"Report received from trader: {report}")
    return JSONResponse({"status": "ok", "message": "Report received"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)