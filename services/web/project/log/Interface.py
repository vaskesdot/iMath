# from project.config import session_psql
# from project.ecprice import types
# from project.ecprice._cards import CardsToFill
# from project.ecprice._parser import CardScraper, CardParser
# from project.ecprice._filler import CardSnapshotFiller

# def fill_cards(cards: CardsToFill) -> types.FillerResult:
#     with session_psql.begin() as session:

#         snapshots_successes = 0
#         snapshots_fails = 0
#         for card in cards:

#             card_scrap = CardScraper(card=card, session=session)
#             card_parse = CardParser(card_scrap=card_scrap)
#             filler = CardSnapshotFiller(card_parse=card_parse)
#             filler.create_Snapshot()
#             filler.fill_card_status()
#             if filler.could_be_parsed_status is True:
#                 snapshots_successes += 1
#             else:
#                 snapshots_fails += 1

#         result = {'cards_given': len(cards),
#                   'snapshots_success': snapshots_successes,
#                   'snapshots_fail': snapshots_fails}
#         return result
