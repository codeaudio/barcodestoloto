import cv2
import numpy as np
from pyzbar import pyzbar

from logger import logger


def extract_data_from_barcode(file: bytes) -> dict:
    try:
        nparr = np.fromstring(file, np.uint8)
        img = cv2.imdecode(nparr, cv2.COLOR_BGR2GRAY)
        barcodes = pyzbar.decode(
            img,
            symbols=[pyzbar.ZBarSymbol.CODE128]
        )
        if barcodes:
            return {
                'barcode': ''.join(
                    f'{i + 1}. {barcode.data}'
                    for i, barcode in enumerate(barcodes)
                )
            }
    except Exception as e:
        logger.error(e)
    return {'error': 'barcode код не найден'}
