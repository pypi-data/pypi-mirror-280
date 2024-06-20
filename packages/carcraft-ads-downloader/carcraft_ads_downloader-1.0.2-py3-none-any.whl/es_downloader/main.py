import json
import logging
import os
import sys
from os.path import dirname

sys.path.append(dirname(dirname(__file__)))

from . import config
from .services.downloader import download_ads

logger = logging.getLogger(__name__)


def main():
    logger.info("Initializing download of ads matching the following parameters:\n"
                f"{config.QUERY_PARAMS}")
    try:
        downloaded_ads = download_ads(config.ES_CLIENT_VERSION,
                                      config.URL_ES,
                                      config.INDEX_ES,
                                      config.QUERY_PARAMS)
    except Exception as e:
        logger.error(f"Error during download process: {str(e)}", exc_info=True)
        downloaded_ads = []
    else:
        os.makedirs(os.path.dirname(config.DOWNLOAD_FILE_PATH), exist_ok=True)
        with open(config.DOWNLOAD_FILE_PATH, 'w') as file:
            json.dump(downloaded_ads, file, ensure_ascii=False)

        logger.info(f"Program exited after downloading {len(downloaded_ads)} ads "
                    f"matching the following parameters:\n{config.QUERY_PARAMS}")


if __name__ == "__main__":
    main()
