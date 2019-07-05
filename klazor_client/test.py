import klazor_client.client as kc

course = kc.fetch_course(1)
sheet = kc.fetch_sheet(2)
print(sheet)