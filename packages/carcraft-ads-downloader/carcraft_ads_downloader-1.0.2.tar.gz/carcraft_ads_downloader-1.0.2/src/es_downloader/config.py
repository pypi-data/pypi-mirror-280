import argparse
import logging
import os
from datetime import datetime, timedelta, timezone
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


LOG_DIR_PATH = os.environ.get("LOG_DIR_PATH", "../log_files")
Path(LOG_DIR_PATH).mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    handlers=[TimedRotatingFileHandler(f"{LOG_DIR_PATH}/cli_downloader.log",
                                       when="D", interval=30,
                                       utc=True, backupCount=1),],
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
logger = logging.getLogger()
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                              datefmt="%Y-%m-%d %H:%M:%S")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


URL_ES = os.environ.get("URL_ES", "http://95.181.205.211:9200")
INDEX_ES = os.environ.get("INDEX_ES", "crp55")
URL_ES_CORPTECH = os.environ.get("URL_ES_CORPTECH", "10.10.20.11:9200")
URL_ES_CAROPERATOR = os.environ.get("URL_ES_CAROPERATOR", "http://95.181.205.211:9200")
es_versions_by_url = {
    URL_ES_CAROPERATOR: "7",
    URL_ES_CORPTECH: "8",
}
ES_CLIENT_VERSION = es_versions_by_url.get(URL_ES)

utc_now = datetime.now(tz=timezone.utc)
msk_now = utc_now + timedelta(hours=3)
parser = argparse.ArgumentParser()
parser.add_argument(
    "--start_date",
    default=(msk_now - timedelta(days=1)).strftime("%Y-%m-%d"),
    help="Start date of range when ads were posted or closed."
)
parser.add_argument(
    "--end_date",
    default=msk_now.strftime("%Y-%m-%d"),
    help="End date of range when ads were posted or closed."
)
parser.add_argument(
    "--status", choices=["created", "closed"],
    default="created",
    help="Status type of ads that need to be loaded."
)
parser.add_argument(
    "--seller_type", choices=["1", "2"],
    default="2",
    help="Seller indicator which can take '1' for individuals or '2' for businesses."
)
parser.add_argument(
    '--site_name', choices=['avito', 'drom', 'auto'],
    default="avito",
    help="Source site name which ads needs to be loaded from Elasticsearch dbms."
)

args = parser.parse_args()
start_date = args.start_date
end_date = args.end_date
status = args.status
seller_type = args.seller_type
site_name = args.site_name

QUERY_PARAMS = {
    "start_date": start_date,
    "end_date": end_date,
    "status": status,
    "seller_type": seller_type,
    "site_name": site_name,
}
DOWNLOAD_DIR_PATH = os.environ.get("DOWNLOAD_DIR_PATH", "../downloaded_files")
DOWNLOAD_FILE_PATH = (
    f"{DOWNLOAD_DIR_PATH}"
    f"/{site_name}/{seller_type}/{status}/{start_date}.json"
)
