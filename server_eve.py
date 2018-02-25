from eve import Eve


#Transform the response payload by hooking a callback 
#function to the on_fetched_resource event
def on_fetched_resource(resource, response):
    for document in response['_items']:
        del(document['_etag'])
        del(document['_updated'])
        del(document['_created'])
    #    del(document['_id'])


app = Eve()
app.on_fetched_resource += on_fetched_resource

if __name__ == '__main__':
    app.run()
