# from sqlalchemy.orm import Session

# from project.ecprice import models
# from project.config import engine_psql as engine


# def seed_data():
#     with Session(autoflush=False, bind=engine) as db:

#         # Brand
#         alphavit = models.Brand(brand="alphavit")
#         alphavit.sku = []

#         procto_glyvenol = models.Brand(brand="procto_glyvenol")
#         procto_glyvenol.sku = []

#         klimalanin = models.Brand(brand="klimalanin")
#         klimalanin.sku = []

#         polydexa = models.Brand(brand="polydexa")
#         polydexa.sku = []

#         # Sku
#         alphavit_dlya_muzhchin = models.Sku(name="alphavit_dlya_muzhchin")
#         alphavit_dlya_muzhchin.cards = []
#         alphavit.sku.append(alphavit_dlya_muzhchin)

#         alphavit_50_plus = models.Sku(name="alphavit_50_plus")
#         alphavit_50_plus.cards = []
#         alphavit.sku.append(alphavit_50_plus)

#         procto_glyvenol_svechi = models.Sku(name="procto_glyvenol_svechi")
#         procto_glyvenol_svechi.cards = []
#         procto_glyvenol.sku.append(procto_glyvenol_svechi)

#         procto_glyvenol_krem = models.Sku(name="procto_glyvenol_krem")
#         procto_glyvenol_krem.cards = []
#         procto_glyvenol.sku.append(procto_glyvenol_krem)

#         klimalanin_60 = models.Sku(name="klimalanin_60")
#         klimalanin_60.cards = []
#         klimalanin.sku.append(klimalanin_60)

#         klimalanin_30 = models.Sku(name="klimalanin_30")
#         klimalanin_30.cards = []
#         klimalanin.sku.append(klimalanin_30)

#         polideksa_kapli_ushnie = models.Sku(name="polideksa_kapli_ushnie")
#         polideksa_kapli_ushnie.cards = []
#         polydexa.sku.append(polideksa_kapli_ushnie)

#         polideksa_sprei_nazalnii = models.Sku(name="polideksa_sprei_nazalnii")
#         polideksa_sprei_nazalnii.cards = []
#         polydexa.sku.append(polideksa_sprei_nazalnii)

#         # Pharmacy
#         eapteka = models.Pharmacy(name="eapteka", )
#         eapteka.cards = []
#         eapteka.sites_data = []

#         asna = models.Pharmacy(name="asna", )
#         asna.cards = []
#         asna.sites_data = []

#         zdravcity = models.Pharmacy(name="zdravcity", )
#         zdravcity.cards = []
#         zdravcity.sites_data = []

#         aptekaru = models.Pharmacy(name="aptekaru", )
#         aptekaru.cards = []
#         aptekaru.sites_data = []

#         # PharmacySitesData
#         asna_1 = models.PharmacySitesData(comment='cookie_1', is_cookies_expired_by_401_error=False, cookies={"cookie_name":  'PHPSESSID=36DsBapCF1QRj52WahRwB0UFdKVjgAXA; BITRIX_SM_SALE_UID=3082725505; selected_pharmacy=-1; _ym_uid=1684733348598322715; _ym_d=1684733348; BX_USER_ID=1101ee6e2217a15b27c63c6e9c3a7385; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; flocktory-uuid=63ff74d0-723c-48ef-ae0e-5307e19f215b-7; _a_d3t6sf=du6UE6CbfehndrhatVzDHRzW; FIRST_USE=true; search_history=GN2VUK7GIUPQYLVUQOZQ7X2D56XIHQ3G3XBQFKYIWJVXVMXK77AYLOAYX7Z3MFOM5IF3WKT3Z2M4BJVHKA3C7CHFOM6JUOP3XQ2DCWA; delivery_city_id=289; FAVORITE_PHARM_SWITCH=NO; mindboxDeviceUUID=689993ec-4995-4fba-a192-7472940e1ffb; directCrm-session=%7B%22deviceGuid%22%3A%22689993ec-4995-4fba-a192-7472940e1ffb%22%7D; _gid=GA1.2.1622512204.1685373423; _ym_isad=1; my_auto_region_id=46; my_auto_domain=www; ASNA.APP.token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJodHRwczpcL1wvd3d3LmFzbmEucnUiLCJhdWQiOiJodHRwczpcL1wvd3d3LmFzbmEucnUiLCJqdGkiOiI0ZjFnMjNhMTJhYSIsImlhdCI6MTY4NTM3NDUwNCwiZXhwIjoxNjg1NDYwOTA0LCJjbGllbnRJZCI6IjI2ZjI3NWVmLWQ5YWUtNDI2Yi05NjNiLWE4ZDYxNTBmYTVjYSIsInVzZXJJZCI6MCwiZGV2aWNlSWQiOm51bGwsImZVc2VySWQiOjMwODI3MjU1MDUsInB1c2hUb2tlbiI6bnVsbCwiYWxsb3dlZEVudGl0aWVzIjpbXSwiYmFubmVkRW50aXRpZXMiOlsiIl0sIm9zTmFtZSI6bnVsbCwiZGV2aWNlTWFudWZhY3R1cmVyIjpudWxsfQ.WEIwvdJy6dadw2vCYQjcD9hrc12nxakUooqE2_wAgLA; acceptance_cookies=1; qrator_jsr=1685408323.068.c6G6Jyu4lgV4J6UM-hdjdghsn2sugoceuqi065vj65ahdaahb-00; qrator_jsid=1685408323.068.c6G6Jyu4lgV4J6UM-b0gd2afmj12d55n1keigna17j47f62mf; qrator_ssid=1685408323.736.W5S3Jpw6YxIOEHvq-vnmg9iteqvdt089ma4nu96ui1tgldveh; isAsnaCookieRegion=true; ssr_storage_ab_test=0; gtm_init_time=1685408324160; gtm-session-start-time=1685408323613; gtm_DOM_time=1685408324175; _ga=GA1.2.183298528.1684733348; _gat_UA-63917087-1=1; _clck=5b95x1|2|fc1|0|1237; _clsk=zjzs7v|1685408326569|1|1|y.clarity.ms/collect; _ga_MPGG3927SG=GS1.1.1685408324.6.0.1685408329.55.0.0; BITRIX_SM_PK=%2Fdesktop%2Fpharmacy__city__region_46%2F; asna-analytics-service-anon-key=47ec4bed-840d-4082-a3c5-a85968da3834; asna-analytics-service-session-key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhc25hLWFuYWx5dGljcyIsImV4cCI6MTY4NTQxMTkyOSwianRpIjoiMDAzNmJlNzMtOGNhZi00Y2M0LWEzYmEtM2NiNTAzOGEwZWY4IiwiaWF0IjoxNjg1NDA4MzI5LCJpc3MiOiJhc25hLWFuYWx5dGljcyIsInN1YiI6InNlc3Npb24iLCJhIjp7IkRldmljZUlEIjoiZTVlYTU4M2UtNGI4Mi00Mjk5LTkwZTEtNzA4MjdkZDc3NGNhIn19.bJM0A5LcRwdb4NiQn59EQffhVWZ3kaVJXWc1j12y1cg'})
#         asna_2 = models.PharmacySitesData(comment='cookie_2', is_cookies_expired_by_401_error=False, cookies={"cookie_name":  'selected_pharmacy=-1; _ym_uid=1684733348598322715; _ym_d=1684733348; BX_USER_ID=1101ee6e2217a15b27c63c6e9c3a7385; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; flocktory-uuid=63ff74d0-723c-48ef-ae0e-5307e19f215b-7; _a_d3t6sf=du6UE6CbfehndrhatVzDHRzW; FIRST_USE=true; search_history=GN2VUK7GIUPQYLVUQOZQ7X2D56XIHQ3G3XBQFKYIWJVXVMXK77AYLOAYX7Z3MFOM5IF3WKT3Z2M4BJVHKA3C7CHFOM6JUOP3XQ2DCWA; FAVORITE_PHARM_SWITCH=NO; mindboxDeviceUUID=689993ec-4995-4fba-a192-7472940e1ffb; directCrm-session=%7B%22deviceGuid%22%3A%22689993ec-4995-4fba-a192-7472940e1ffb%22%7D; ASNA.APP.token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRmMWcyM2ExMmFhIn0.eyJpc3MiOiJodHRwczpcL1wvd3d3LmFzbmEucnUiLCJhdWQiOiJodHRwczpcL1wvd3d3LmFzbmEucnUiLCJqdGkiOiI0ZjFnMjNhMTJhYSIsImlhdCI6MTY4NTM3NDUwNCwiZXhwIjoxNjg1NDYwOTA0LCJjbGllbnRJZCI6IjI2ZjI3NWVmLWQ5YWUtNDI2Yi05NjNiLWE4ZDYxNTBmYTVjYSIsInVzZXJJZCI6MCwiZGV2aWNlSWQiOm51bGwsImZVc2VySWQiOjMwODI3MjU1MDUsInB1c2hUb2tlbiI6bnVsbCwiYWxsb3dlZEVudGl0aWVzIjpbXSwiYmFubmVkRW50aXRpZXMiOlsiIl0sIm9zTmFtZSI6bnVsbCwiZGV2aWNlTWFudWZhY3R1cmVyIjpudWxsfQ.WEIwvdJy6dadw2vCYQjcD9hrc12nxakUooqE2_wAgLA; acceptance_cookies=1; _clck=5b95x1|2|fc1|0|1237; qrator_jsr=1688266998.169.tI8g1GRMFQF7JVdr-cusk30oj1k0p2prg5kuqkgm7ft33hh7o-00; qrator_jsid=1688266998.169.tI8g1GRMFQF7JVdr-ratotejhvsrmfc2m2boom2vrm0ph9hj5; isAsnaCookieRegion=true; ssr_storage_ab_test=4; BITRIX_SM_SALE_UID=0; my_auto_region_id=46; gtm_init_time=1688267002199; gtm-session-start-time=1688267000429; gtm_DOM_time=1688267002215; _gid=GA1.2.1315187720.1688267003; _gat_UA-63917087-1=1; _ga=GA1.2.183298528.1684733348; _ym_isad=1; _ga_MPGG3927SG=GS1.1.1688267002.8.0.1688267003.59.0.0; PHPSESSID=LvyzbEm8wy2qexcpePGvTmU3qo1nndHH; BITRIX_SM_PK=%2Fdesktop%2Fpharmacy__city__region_46%2F; asna-analytics-service-anon-key=c96f923a-c06e-4aee-8961-748b88ea29bf; asna-analytics-service-session-key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhc25hLWFuYWx5dGljcyIsImV4cCI6MTY4ODI3MDYwNSwianRpIjoiYmNkYzNiNGYtNDFkYy00MDJkLTg2ZjYtMDBlYWU1ZTdkNGEwIiwiaWF0IjoxNjg4MjY3MDA1LCJpc3MiOiJhc25hLWFuYWx5dGljcyIsInN1YiI6InNlc3Npb24iLCJhIjp7IkRldmljZUlEIjoiOGM2ZjVjOGEtMDRkMC00NmI4LTllN2UtZmFlYjE1YmQ1MTkzIn19.cLN8BeCFOiCSDoNrlXaw0tPqcgIp1fd9ir7yn3zas10; qrator_ssid=1688267005.835.h4LGLS0wYh4oN8tl-v1dj5305m8trhq8o3hq9pf5pbon3eaie'})
#         asna.sites_data.extend([asna_1, asna_2])

#         # City
#         moscow = models.City(name="moscow")
#         moscow.cards = []

#         saint_peterburg = models.City(name="saint_peterburg")
#         saint_peterburg.cards = []

#         ekaterinburb = models.City(name="ekaterinburb")
#         ekaterinburb.cards = []

#         # Card
#         ##
#         asna_procto_glyvenol_krem_moscow = models.Card(url="https://www.asna.ru/cards/prokto-glivenol_n10_suppozitorii_novartis_farma_sas.html", )
#         asna_procto_glyvenol_krem_moscow.snapshots = []
#         asna.cards.append(asna_procto_glyvenol_krem_moscow)
#         procto_glyvenol_krem.cards.append(asna_procto_glyvenol_krem_moscow)
#         moscow.cards.append(asna_procto_glyvenol_krem_moscow)

#         asna_procto_glyvenol_krem_saint_peterburg = models.Card(url="https://spb.asna.ru/cards/prokto-glivenol_30g_krem_novartis_konsyumer_khels.html", )
#         asna_procto_glyvenol_krem_saint_peterburg.snapshots = []
#         asna.cards.append(asna_procto_glyvenol_krem_saint_peterburg)
#         procto_glyvenol_krem.cards.append(asna_procto_glyvenol_krem_saint_peterburg)
#         saint_peterburg.cards.append(asna_procto_glyvenol_krem_saint_peterburg)

#         asna_procto_glyvenol_krem_ekaterinburb = models.Card(url="https://ekaterinburg.asna.ru/cards/prokto-glivenol_30g_krem_novartis_konsyumer_khels.html", )
#         asna_procto_glyvenol_krem_ekaterinburb.snapshots = []
#         asna.cards.append(asna_procto_glyvenol_krem_ekaterinburb)
#         procto_glyvenol_krem.cards.append(asna_procto_glyvenol_krem_ekaterinburb)
#         ekaterinburb.cards.append(asna_procto_glyvenol_krem_ekaterinburb)

#         db.add_all([alphavit, procto_glyvenol, klimalanin, polydexa])
#         db.commit()
