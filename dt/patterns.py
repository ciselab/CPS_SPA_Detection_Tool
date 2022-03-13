class MagicalWaitingNumber:
    @classmethod
    def terms_of_interest(cls):
        return ["usleep", "sleep", "Sleep", "MSleep", "sleep_for", "sleep_until", "thrd_sleep"]

    @classmethod
    def name(cls):
        return "mwn"


class HardCodedFineTuning:
    @classmethod
    def name(cls):
        return "hcft"


MAGICAL_WAITING_NUMBER: str = MagicalWaitingNumber.name()
HARDCODED_FINE_TUNING: str = HardCodedFineTuning.name()
