class Identifier:
    def validate_identifier(self, s: str) -> bool:
        if s is None or len(s) == 0 or len(s) > 6:
            return False

        if not self.is_letter(s[0]):
            return False

        for ch in s[1:]:
            if not self.is_letter_or_digit(ch):
                return False

        return True

    def is_letter(self, ch: str) -> bool:
        return ('A' <= ch <= 'Z') or ('a' <= ch <= 'z')

    def is_letter_or_digit(self, ch: str) -> bool:
        return self.is_letter(ch) or ('0' <= ch <= '9')
