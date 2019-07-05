import klazor_client.client as kc

course = kc.fetch_course(1)
print(course.title)