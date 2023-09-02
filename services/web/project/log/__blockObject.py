# from typing import List
# from abc import ABC, abstractmethod

# from project.config import session_psql
# from project.ecprice.models import Card

# class CardsToFill(ABC):
#     @abstractmethod
#     def get_cards(self) -> List[Card]:
#         pass

# class AsnaCards(CardsToFill):
#     @classmethod
#     def get_cards(csl):
#         with session_psql.begin() as session:
#             cards = session.query(Card).filter_by(pharmacy_id=1).all()
#             session.expunge_all()
#             return cards