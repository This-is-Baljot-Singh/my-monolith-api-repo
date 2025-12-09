
from fastapi import APIRouter, Query, Response
import qrcode
import io

router = APIRouter(prefix="/qrcode", tags=["QRCode Generator"])

@router.get("/generate", summary="Generate QR code from text")
async def generate_qrcode(data: str = Query(..., min_length=1, description="Text to encode in QR code")):
    """Generate a QR code PNG image from the provided text."""
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return Response(content=buf.read(), media_type="image/png")
