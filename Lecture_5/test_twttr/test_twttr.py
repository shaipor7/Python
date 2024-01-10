from twttr import shorten

def test_assert():
    assert shorten("POR") == "PR"
    assert shorten("Por") == "Pr"
    assert shorten("123P") == "123P"
    assert shorten("...") == "..."
