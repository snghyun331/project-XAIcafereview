import pandas as pd
class DataProcessing():
    def __init__(self, store_name):
        self.store_name = store_name

    def do_something(self):
        self.store_name = 'xxxx'
        ## do_something
        pd.set_option('mode.chained_assignment', None)

        df = pd.read_csv('static/all_review(from Mapo2Songpa).csv')
        store_name = '프릳츠 도화점'
        storeiwant = df[df['카페명'].isin([store_name])]
        # print(storeiwant)
        storeiwant.to_html('templates/store.html')
        # return (store_html)
        # return render_template('stores.html', store_name = store_name, datas =storeiwant)
        return

