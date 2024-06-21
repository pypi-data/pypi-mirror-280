from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
import httpx
from fastapi.responses import Response

from src.stac import Stac
from src.storage import Storage


router = APIRouter(prefix="/proxy/abc", tags=["proxy"])


@router.get("{subpath:path}")
async def tete(subpath: str):
    # return RedirectResponse(url=f"{subpath}")
    async with httpx.AsyncClient() as client:
        r = await client.get(f"http://localhost:8000{subpath}")
    return Response(r.content, media_type=r.headers["Content-Type"])
