import pandas as pd
class DataFormat:
    @staticmethod
    def convert_to_dataframe_gdshe(data, properties={}):
        if 'asOfDate' in properties:
            del properties['asOfDate']
        print(properties)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 1)

        flattened_data = {}
        all_subkeys = set()

        for main_key, sub_dict in data.items():
            for sub_key, value_list in sub_dict.items():
                all_subkeys.add(sub_key)
                if sub_key not in flattened_data:
                    flattened_data[sub_key] = {}
                for values in value_list:
                    if main_key not in flattened_data[sub_key]:
                        flattened_data[sub_key][main_key] = []
                    flattened_data[sub_key][main_key].append(values)


        for sub_key in all_subkeys:
            for main_key in data.keys():
                if main_key not in flattened_data[sub_key]:
                    flattened_data[sub_key][main_key] = [['', '']]


        rows = []
        for sub_key, main_key_data in flattened_data.items():

            max_length = max(len(values) for values in main_key_data.values())

            for i in range(max_length):
                row = {'Identifier': sub_key}
                date = ''
                for main_key in data.keys():
                    values = main_key_data[main_key]
                    if i < len(values):
                        row[main_key] = values[i][0]

                        if len(values[i]) > 1 and values[i][1]:
                            date = values[i][1]

                    else:
                        row[main_key] = ''

                row['asOfDate'] = date
                for prop_key, prop_value in properties.items():
                    row[prop_key] = prop_value
                rows.append(row)


        df = pd.DataFrame(rows)

        property_columns = list(properties.keys())
        response_columns = [col for col in df.columns if col not in ['Identifier', 'asOfDate'] + property_columns]

        columns_order = ['Identifier'] + ['asOfDate'] + response_columns + property_columns
        df = df[columns_order]
        df.index = range(1, len(df) + 1)

        response_color = 'lightyellow'
        property_color = 'lightblue'

        header_styles = [
            {'selector': 'th.col0',
             'props': [('background-color', response_color), ('text-align', 'center'), ('border', '1px solid black'),
                       ('text-transform', 'uppercase')]},
            {'selector': 'th.col1',
             'props': [('background-color', response_color), ('text-align', 'center'), ('border', '1px solid black'),
                       ('text-transform', 'uppercase')]}
        ]

        for i, col in enumerate(response_columns, start=2):
            header_styles.append({'selector': f'th.col{i}',
                                  'props': [('background-color', response_color), ('text-align', 'center'),
                                            ('border', '1px solid black'), ('text-transform', 'uppercase')]})

        for i, col in enumerate(property_columns, start=2 + len(response_columns)):
            header_styles.append({'selector': f'th.col{i}',
                                  'props': [('background-color', property_color), ('text-align', 'center'),
                                            ('border', '1px solid black'), ('text-transform', 'uppercase')]})

        df_styled = df.style.set_table_styles(
            header_styles + [
                {'selector': 'td', 'props': [('text-align', 'center'), ('border', '1px solid black')]}
            ]
        ).set_properties(**{'text-align': 'center'})

        return df_styled

    @staticmethod
    def convert_to_dataframe_pit(data, properties={}):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 1)

        flattened_data = {}
        all_subkeys = set()

        for main_key, sub_dict in data.items():
            for sub_key, value_list in sub_dict.items():
                all_subkeys.add(sub_key)
                if sub_key not in flattened_data:
                    flattened_data[sub_key] = {}
                for values in value_list:
                    if main_key not in flattened_data[sub_key]:
                        flattened_data[sub_key][main_key] = []
                    flattened_data[sub_key][main_key].append(values)

        for sub_key in all_subkeys:
            for main_key in data.keys():
                if main_key not in flattened_data[sub_key]:
                    flattened_data[sub_key][main_key] = [['', '']]

        rows = []
        for sub_key, main_key_data in flattened_data.items():

            max_length = max(len(values) for values in main_key_data.values())

            for i in range(max_length):
                row = {'Identifier': sub_key}


                for main_key in data.keys():
                    values = main_key_data[main_key]
                    if i < len(values):
                        row[main_key] = values[i][0]

                    else:
                        row[main_key] = ''



                for prop_key, prop_value in properties.items():
                    row[prop_key] = prop_value
                rows.append(row)


        df = pd.DataFrame(rows)

        property_columns = list(properties.keys())
        has_as_of_date = 'asOfDate' in properties

        if has_as_of_date:
            property_columns.remove('asOfDate')
            columns_order = ['Identifier', 'asOfDate'] + [col for col in df.columns if
                                                          col not in property_columns + ['Identifier',
                                                                                         'asOfDate']] + property_columns
        else:
            columns_order = ['Identifier'] + [col for col in df.columns if
                                              col not in property_columns + ['Identifier']] + property_columns

        df = df[columns_order]
        df.index = range(1, len(df) + 1)

        response_color = 'lightyellow'
        property_color = 'lightblue'

        header_styles = [
            {'selector': 'th.col0',
             'props': [('background-color', response_color), ('text-align', 'center'), ('border', '1px solid black'),
                       ('text-transform', 'uppercase')]}
        ]

        if has_as_of_date:
            header_styles.append({'selector': 'th.col1',
                                  'props': [('background-color', response_color), ('text-align', 'center'),
                                            ('border', '1px solid black'), ('text-transform', 'uppercase')]})
            response_start_index = 2
        else:
            response_start_index = 1

        # Add styles for response columns
        for i, col in enumerate(columns_order[response_start_index:response_start_index + len(data)],
                                start=response_start_index):
            header_styles.append({'selector': f'th.col{i}',
                                  'props': [('background-color', response_color), ('text-align', 'center'),
                                            ('border', '1px solid black'), ('text-transform', 'uppercase')]})

        # Add styles for property columns
        for i, col in enumerate(columns_order[response_start_index + len(data):],
                                start=response_start_index + len(data)):
            header_styles.append({'selector': f'th.col{i}',
                                  'props': [('background-color', property_color), ('text-align', 'center'),
                                            ('border', '1px solid black'), ('text-transform', 'uppercase')]})

        df_styled = df.style.set_table_styles(
            header_styles + [
                {'selector': 'td', 'props': [('text-align', 'center'), ('border', '1px solid black')]}
            ]
        ).set_properties(**{'text-align': 'center'})

        return df_styled

    @staticmethod
    def convert_to_dataframe_generic(data, properties={}):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 1)
        flattened_data = {}
        all_subkeys = set()

        for main_key, sub_dict in data.items():
            for sub_key, value_list in sub_dict.items():
                all_subkeys.add(sub_key)
                if sub_key not in flattened_data:
                    flattened_data[sub_key] = {}
                for values in value_list:
                    if main_key not in flattened_data[sub_key]:
                        flattened_data[sub_key][main_key] = []
                    flattened_data[sub_key][main_key].append(values)

        for sub_key in all_subkeys:
            for main_key in data.keys():
                if main_key not in flattened_data[sub_key]:
                    flattened_data[sub_key][main_key] = [['', '']]

        rows = []
        for sub_key, main_key_data in flattened_data.items():

            max_length = max(len(values) for values in main_key_data.values())

            for i in range(max_length):
                row = {'Identifier': sub_key}

                for main_key in data.keys():
                    values = main_key_data[main_key]
                    if i < len(values):
                        row[main_key] = values[i][0]

                    else:
                        row[main_key] = ''

                for prop_key, prop_value in properties.items():
                    row[prop_key] = prop_value
                rows.append(row)

        df = pd.DataFrame(rows)

        property_columns = list(properties.keys())
        has_as_of_date = 'asOfDate' in properties

        if has_as_of_date:
            property_columns.remove('asOfDate')
            columns_order = ['Identifier', 'asOfDate'] + [col for col in df.columns if
                                                          col not in property_columns + ['Identifier',
                                                                                         'asOfDate']] + property_columns
        else:
            columns_order = ['Identifier'] + [col for col in df.columns if
                                              col not in property_columns + ['Identifier']] + property_columns

        df = df[columns_order]
        df.index = range(1, len(df) + 1)

        response_color = 'lightyellow'
        property_color = 'lightblue'

        header_styles = [
            {'selector': 'th.col0',
             'props': [('background-color', response_color), ('text-align', 'center'), ('border', '1px solid black'),
                       ('text-transform', 'uppercase')]}
        ]

        if has_as_of_date:
            header_styles.append({'selector': 'th.col1',
                                  'props': [('background-color', response_color), ('text-align', 'center'),
                                            ('border', '1px solid black'), ('text-transform', 'uppercase')]})
            response_start_index = 2
        else:
            response_start_index = 1

        # Add styles for response columns
        for i, col in enumerate(columns_order[response_start_index:response_start_index + len(data)],
                                start=response_start_index):
            header_styles.append({'selector': f'th.col{i}',
                                  'props': [('background-color', response_color), ('text-align', 'center'),
                                            ('border', '1px solid black'), ('text-transform', 'uppercase')]})

        # Add styles for property columns
        for i, col in enumerate(columns_order[response_start_index + len(data):],
                                start=response_start_index + len(data)):
            header_styles.append({'selector': f'th.col{i}',
                                  'props': [('background-color', property_color), ('text-align', 'center'),
                                            ('border', '1px solid black'), ('text-transform', 'uppercase')]})

        df_styled = df.style.set_table_styles(
            header_styles + [
                {'selector': 'td', 'props': [('text-align', 'center'), ('border', '1px solid black')]}
            ]
        ).set_properties(**{'text-align': 'center'})

        return df_styled





