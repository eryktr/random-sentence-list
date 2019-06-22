class Validator:
    MINIMUM_LENGTH = 30

    @staticmethod
    def _is_long_enough(sentence):
        return len(sentence) >= Validator.MINIMUM_LENGTH

    @staticmethod
    def _is_not_equation(sentence: str):
        return not any(c in sentence for c in ["\\", "=", "+", "-", "*", "/", ":"])

    @staticmethod
    def _has_no_quotes(sentence: str):
        return "\"" not in sentence

    @staticmethod
    def _is_single_line(sentence: str):
        return "\n" not in sentence

    @staticmethod
    def is_valid_sentence(sentence):
        return Validator._is_long_enough(sentence) \
               and Validator._is_not_equation(sentence) \
               and Validator._is_single_line(sentence) \
               and Validator._has_no_quotes(sentence)
