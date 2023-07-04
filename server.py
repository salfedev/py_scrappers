from scrapper import get_grid_reference
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/{postcode}")
async def root(postcode):
    postcode = postcode.replace(" ", "")
    grid_ref = get_grid_reference(postcode)
    return {"message": {"postcode": postcode, "grid_ref": grid_ref}}
