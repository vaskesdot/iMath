# from sqlalchemy.orm import Session

# from project.config import session_psql
# from project.ecprice import types
# from project.ecprice.models import Card, Snapshot
# from project.ecprice._parser import CardParser

# class CardSnapshotFiller:
#     def __init__(self, card_parse: CardParser):
#         self.card_id = card_parse.get_card_id()
#         self.card_parse = card_parse

#     @property
#     def _card_parse_result(self):
#         return self.card_parse.get_parse_result()

#     @property
#     def could_be_parsed_status(self):
#         return self._card_parse_result['could_be_parsed_status']

#     def create_Snapshot(self):
#         with session_psql.begin() as session:
#             snapshot = Snapshot(price=self._card_parse_result['price'],
#                                 was_successful=self._card_parse_result['could_be_parsed_status'],
#                                 card_id=self.card_id)

#             session.add(snapshot)


#     def fill_card_status(self):

#             with session_psql.begin() as session:
#                     session.query(Card).filter(id=self.card_id).first()\
#                         .update(
#                         {
#                             'could_be_opened_last_status': self._card_parse_result['could_be_opened_status'],
#                             'could_be_opened_last_date': self._card_parse_result['datetime_of_try'],
#                             'could_be_parsed_last_status': self._card_parse_result['could_be_parsed_status'],
#                             'could_be_parsed_last_date': self._card_parse_result['datetime_of_try'],
#                             'last_price': self._card_parse_result['price']
#                          }
#                     )
