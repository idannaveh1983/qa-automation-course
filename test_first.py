def test_homepage_title(page):
    page.goto("https://www.ynet.co.il/")
    assert page.title() == "ynet - חדשות, כלכלה, ספורט ובריאות - דיווחים שוטפים מהארץ ומהעולם"