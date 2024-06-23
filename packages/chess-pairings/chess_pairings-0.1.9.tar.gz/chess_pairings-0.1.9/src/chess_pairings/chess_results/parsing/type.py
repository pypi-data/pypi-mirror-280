from typing import Literal, Sequence, get_args
from bs4 import BeautifulSoup

TournamentType = Literal['Swiss-System', 'Round robin']
TOURNAMENT_TYPES: Sequence[TournamentType] = get_args(TournamentType) # type: ignore

def find_type(soup: BeautifulSoup) -> TournamentType | None:
  try:
    type = soup.find(string='Tournament type').find_next().get_text() # type: ignore
    if type in TOURNAMENT_TYPES:
      return type # type: ignore
  except:
    ...

