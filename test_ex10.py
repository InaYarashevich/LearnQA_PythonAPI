class TestEx10:
    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Phrase '{phrase}' contains more than 15 symbols"
