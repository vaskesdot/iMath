from sqlalchemy.orm import Session

from project.config import engine_psql
from project.config import session_psql
from project.ecprice.models import Card, Pharmacy, City, Sku


def test_sqlalchemy_db_is_correct_card_entry():
    # Base.metadata.create_all(engine)
    with Session(engine_psql) as session:

        # Insert the data
        # Query the database to retrieve the record
        card = session.query(Card).filter_by(
            url="https://www.asna.ru/cards/prokto-glivenol_n10_suppozitorii_novartis_farma_sas.html").first()

        asna = session.query(Pharmacy).filter_by(
            name="asna").first()

        moscow = session.query(City).filter_by(
            name="moscow").first()

        procto_glyvenol_krem = session.query(Sku).filter_by(
            name="procto_glyvenol_krem").first()

        assert card.url == "https://www.asna.ru/cards/prokto-glivenol_n10_suppozitorii_novartis_farma_sas.html"
        assert card.pharmacy_id == asna.id
        assert card.city_id == moscow.id
        assert card.sku_id == procto_glyvenol_krem.id

        assert not card.url == "https://www.as"
        assert not card.pharmacy_id == 212
        assert not card.city_id == 'adfs'
        assert not card.sku_id == 2166

from project.ecprice._parser import CardScraper
def test_get_pharmacy_name_from_CardScraper():

    with Session(engine_psql) as session:
        test_card = session.query(Card).filter_by(url="https://www.asna.ru/cards/prokto-glivenol_n10_suppozitorii_novartis_farma_sas.html").first()
        card = CardScraper(card=test_card, session=session)
        pharmacy_name = card.get_pharmacy_name()
        assert pharmacy_name == 'asna'

def test_decorator_add_parser_to_services():
    from project.ecprice._parser import PharmacyParser
    @PharmacyParser.add_parser('new')
    class NewPharmacy:
        pass

    # breakpoint()
    parsers_by_pharmacy = PharmacyParser.get_parsers_by_pharmacy()
    assert 'new' in PharmacyParser.get_parsers_by_pharmacy()
    assert parsers_by_pharmacy['new'] == NewPharmacy

def test_asna_cards():
    from project.ecprice._cards import AsnaCards
    asna_cards_from_method = AsnaCards.get_cards()
    with session_psql.begin() as session:
        asna_id = session.query(Pharmacy).filter_by(name='asna').first().id
        asna_cards_from_asna_key = session.query(Card).filter_by(pharmacy_id=asna_id).all()
    assert str(asna_cards_from_method) == str(asna_cards_from_asna_key)


def test_main():
    from project.ecprice.main import fill_cards
    from project.ecprice._cards import AsnaCards
    with session_psql.begin() as session:

        card_scrap = CardScraper(card=AsnaCards.get_cards()[0], session=session)
        response = card_scrap.get_card_response()
        breakpoint()

def test_cookies():
    from project.ecprice._parser import CardScraper
    from project.ecprice._cards import AsnaCards
    with session_psql.begin() as session:

        card_scrap = CardScraper(card=AsnaCards.get_cards()[0], session=session)
        cookies = card_scrap._get_cookies_for_pharmacy_site()
        breakpoint()
