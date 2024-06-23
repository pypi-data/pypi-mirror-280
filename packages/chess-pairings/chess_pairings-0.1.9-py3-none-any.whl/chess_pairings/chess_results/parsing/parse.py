from haskellian import Either, Left
from bs4 import BeautifulSoup
from chess_pairings import GroupPairings
from .type import find_type
from ..errors import ParsingError


def parse_rounds(soup: BeautifulSoup) -> Either[ParsingError, GroupPairings]:
  match find_type(soup):
    case None:
      return Left(ParsingError('No tournament type found'))
    case 'Round robin':
      from .single_robin import parse_single_round_robin
      return parse_single_round_robin(soup).mapl(ParsingError)
    case 'Swiss-System':
      from .single_swiss import parse_single_swiss
      return parse_single_swiss(soup).mapl(ParsingError)
  
