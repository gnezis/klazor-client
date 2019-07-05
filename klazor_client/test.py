import klazor_client.client as kc

kc.config(
    API_URL='http://127.0.0.1:8000/api',
)
course = kc.fetch_course(1)
print(course)
print(course['topic_set'])
