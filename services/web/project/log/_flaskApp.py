from flask import Blueprint

log = Blueprint('log', __name__, template_folder='templates', static_folder='static')



# import random
#
# from flask import Blueprint
# import pandas as pd
# from flask import Flask, render_template, redirect, url_for, request, g
# from sqlalchemy import Table
#
# from project.config import engine_sqlite, metadata_sqlite, connection_sqlite
# from project import forms
#
#
# climate = Blueprint('climate', __name__, template_folder='templates', static_folder='static')
#
# @climate.route('/test')
# def test():
#     return 'hello'
#
# def _get_countries_names() -> list:
#     tables = list(metadata_sqlite.tables.values())
#     tables = tables[:212]
#
#     country_names = []
#
#     for country in tables:
#         table_name = str(country)
#
#         country_names.append(table_name.split('.')[0])
#
#     return country_names
#
#
# def _get_pivot_table_countries_warmed_from_1860_by_2020(ascending: bool):
#     my_table = Table('how_much_degree_countries_warmed_from_1860_by_2020', metadata_sqlite, autoload=True,
#                      autoload_with=engine_sqlite)
#     cursor = connection_sqlite.execute(my_table.select())
#     table_data = cursor.fetchall()
#     table_columns = list(cursor.keys())
#
#     df = pd.DataFrame(columns=table_columns, data=table_data)
#     df = df.sort_values('degrees', ascending=ascending).dropna()
#     df['position'] = [i + 1 for i in range(len(df))]
#     table_data = df.loc[:, ['position', 'country', 'degrees']].values
#
#     return table_data
#
#
# def _get_country_table(country: str):
#     country_name = f"{country}.txt"
#
#     try:
#         my_table = Table(country_name, metadata_sqlite, autoload=True,
#                          autoload_with=engine_sqlite)
#     except TypeError:
#         my_table = Table("France.txt", metadata_sqlite, autoload=True,
#                          autoload_with=engine_sqlite)
#     cursor = connection_sqlite.execute(my_table.select())
#     table_data = cursor.fetchall()
#     table_columns = list(cursor.keys())
#
#     df = pd.DataFrame(columns=table_columns, data=table_data)
#     return df
#
# @climate.errorhandler(404)
# def not_found(error):
#     context = {
#         'title': 'Sorry, Page Not Found',
#         'description': 'Check your link to resolve the issue'
#     }
#
#     return render_template('climate/error.html', context=context)
#
#
# @climate.errorhandler(500)
# def server_error(error):
#
#     context = {
#         'title': "Oh, The Site can't handle the request ",
#         'description': 'We will try to resolve the problem, we promise you :) '
#     }
#
#     return render_template('climate/error.html', context=context)
#
#
# @climate.route('/')
# def index():
#     return redirect(url_for('climate.select_country_how_will_change_over_years'))
#
#
# @climate.route('/countries_most_affected_by_climate_change', methods=['GET'])
# def most_affected():
#     title = 'Countries most affected by climate change'
#     description = 'Since 1860 by 2020 the world has warmed by 1.3°C. ' \
#                   'Find out countries with highest average climate rising:'
#
#     table_data = _get_pivot_table_countries_warmed_from_1860_by_2020(ascending=False)
#
#     output_information = 'As you can see, in terms of average climate increases, the Eastern Europe ' \
#                          'region (areas near Baltic Sea) has been most affected so far.'
#
#     context = {
#         'title': title,
#         'description': description,
#         'output_information': output_information,
#         'columns': ['#', 'Country', 'Degrees Rise'],
#         'data': table_data,
#     }
#
#     return render_template('climate/countries_list.html', context=context)
#
#
# @climate.route('/countries_least_affected_by_climate_change', methods=['GET'])
# def least_affected():
#     title = 'Countries least affected by climate change'
#     description = 'Since 1860 by 2020 the world has warmed by 1.3°C. ' \
#                   'Find out countries with lowest average climate rising:'
#
#     table_data = _get_pivot_table_countries_warmed_from_1860_by_2020(ascending=True)
#
#     output_information = 'As you can see, in terms of average climate increases, the South Asian ' \
#                          'region (areas near India) has been less affected so far. But for this region, ' \
#                          'even this small increase is critical: due to high default temperatures, ' \
#                          'dense population, and the location of many cities near water level, ' \
#                          'settlements here are especially vulnerable in the future.'
#
#     context = {
#         'title': title,
#         'description': description,
#         'output_information': output_information,
#         'columns': ['#', 'Country', 'Degrees Rise'],
#         'data': table_data,
#     }
#
#     return render_template('climate/countries_list.html', context=context)
#
# @climate.route('/how_will_average_temperature_change', methods=['GET', 'POST'])
# def select_country_how_will_change_over_years():
#     title = 'How Will Average Temperature Change'
#     description = 'Select the country and after how many years you are interested in the changing'
#
#     countries_names = _get_countries_names()
#
#     form_select_country = forms.Select_country()
#
#     if form_select_country.is_submitted():
#         country = form_select_country.country.data
#         over_years = form_select_country.over_years.data
#         return redirect(
#             url_for('climate.get_result_how_will_change_in_some_country', **{'country': country, 'over_years': over_years}))
#
#
#     context = {
#         'title': title,
#         'description': description,
#         'countries_names': countries_names,
#         'form': form_select_country,
#     }
#
#
#     return render_template('climate/will_select.html', context=context)
#
#
# @climate.route('/how_will_average_temperature_change_in', methods=['GET'])
# def get_result_how_will_change_in_some_country():
#     country = request.args.get('country', default='USA')
#     over_years = int(request.args.get('over_years', default=77))
#
#     title = f'How Will Average Temperature Change in {country} in {over_years} years'
#
#     table_data = _get_country_table(country)
#
#     try:
#         best_case_forecast_from_2023 = table_data.query(f'Year == {2023 + over_years}').SSP1_2_6.array[0] - \
#                                        table_data.query(f'Year == 2023').SSP1_2_6.array[0]
#         best_case_forecast_from_2023 = best_case_forecast_from_2023.round(2)
#         best_case_forecast_from_1860 = table_data.query(f'Year == {2023 + over_years}').SSP1_2_6.array[0]
#
#         intermediate_case_forecast_from_2023 = table_data.query(f'Year == {2023 + over_years}').SSP2_4_5.array[0] - \
#                                                table_data.query(f'Year == 2023').SSP2_4_5.array[0]
#         intermediate_case_forecast_from_2023 = intermediate_case_forecast_from_2023.round(2)
#         intermediate_case_forecast_from_1860 = table_data.query(f'Year == {2023 + over_years}').SSP2_4_5.array[0]
#
#         worst_case_forecast_from_2023 = table_data.query(f'Year == {2023 + over_years}').SSP3_7_0.array[0] - \
#                                         table_data.query(f'Year == 2023').SSP3_7_0.array[0]
#         worst_case_forecast_from_2023 = worst_case_forecast_from_2023.round(2)
#         worst_case_forecast_from_1860 = table_data.query(f'Year == {2023 + over_years}').SSP3_7_0.array[0]
#
#     except IndexError:
#         over_years = 5
#         best_case_forecast_from_2023 = table_data.query(f'Year == {2023 + over_years}').SSP1_2_6.array[0] - \
#                                        table_data.query(f'Year == 2023').SSP1_2_6.array[0]
#         best_case_forecast_from_2023 = best_case_forecast_from_2023.round(2)
#         best_case_forecast_from_1860 = table_data.query(f'Year == {2023 + over_years}').SSP1_2_6.array[0]
#
#         intermediate_case_forecast_from_2023 = table_data.query(f'Year == {2023 + over_years}').SSP2_4_5.array[0] - \
#                                                table_data.query(f'Year == 2023').SSP2_4_5.array[0]
#         intermediate_case_forecast_from_2023 = intermediate_case_forecast_from_2023.round(2)
#         intermediate_case_forecast_from_1860 = table_data.query(f'Year == {2023 + over_years}').SSP2_4_5.array[0]
#
#         worst_case_forecast_from_2023 = table_data.query(f'Year == {2023 + over_years}').SSP3_7_0.array[0] - \
#                                         table_data.query(f'Year == 2023').SSP3_7_0.array[0]
#         worst_case_forecast_from_2023 = worst_case_forecast_from_2023.round(2)
#         worst_case_forecast_from_1860 = table_data.query(f'Year == {2023 + over_years}').SSP3_7_0.array[0]
#
#     worst_case = f'With high emissions (high warming scenario), by {2023 + over_years} year {country} will warm by {worst_case_forecast_from_2023} degrees compared to 2023 levels and {worst_case_forecast_from_1860} degrees compared to 1860 levels.'
#     intermediate_case = f'Intermediate emissions trajectory: by {2023 + over_years} year {country} will warm by {intermediate_case_forecast_from_2023} degrees compared to 2023 levels and {intermediate_case_forecast_from_1860} degrees compared to 1860 levels.'
#     best_case = f'With significantly lower greenhouse gas emissions, by {2023 + over_years} year {country} will warm by {best_case_forecast_from_2023} degrees compared to 2023 levels and {best_case_forecast_from_1860} degrees compared to 1860 levels.'
#
#     description_best = 'SSP1-2.6 – represented by the green curve – with significantly lower greenhouse gas emissions, assumes net zero carbon dioxide worldwide by ~2080. Under this scenario, overall average global warming is expected to reach approximately 1.8°C by 2100.'
#     description_intermediate = 'SSP2-4.5 – represented by the orange curve – an intermediate emissions trajectory. This assumes that modern emissions levels stay approximately consistent through 2050, before gradually declining.  Under this scenario, net zero is not reached by 2100, and global average warming is expected to have reached approximately 2.7°C by 2100 and still be rising.  Among the scenarios, this is the closest to the world’s current behavior on emissions.'
#     description_worst = 'SSP3-7.0 – represented by the blue curve – a high emissions, high warming scenario, that assumes the world not only fails to curtail greenhouse gas emissions, but that emissions continue to rise. Under this scenario, carbon dioxide emissions are assumed to double by 2100; average global temperatures would reach approximately 3.6°C above pre-industrial baseline, more than doubling current levels of warming.'
#
#     columns = list(table_data.columns)[1:]
#
#     figure = table_data.plot(x='Year', y=['SSP3_7_0', 'SSP2_4_5', 'SSP1_2_6']).get_figure()
#
#     figure_id = random.randint(1, 1000)
#     figure_path = f'project/static/images/{figure_id}.png'
#     figure_name = f"{figure_id}.png"
#     figure.savefig(figure_path)
#     g.current_figure = figure_id
#
#     context = {
#         'title': title,
#         'columns': columns,
#         'data': table_data.values,
#         'best_case': best_case,
#         'intermediate_case': intermediate_case,
#         'worst_case': worst_case,
#         'description_best': description_best,
#         'description_intermediate': description_intermediate,
#         'description_worst': description_worst
#     }
#
#     return render_template('climate/will_result.html', context=context, figure=figure_name)
