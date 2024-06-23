from haskellian import Either
from chess_pairings import GroupPairings
from ._donwload import CHESS_RESULTS, download_pairings
from . import parse_rounds, ScrapingError

async def scrape_pairings(db_key: int, *, base = CHESS_RESULTS) -> Either[ScrapingError, GroupPairings]:
  return (await download_pairings(db_key, base=base)).bind(parse_rounds)