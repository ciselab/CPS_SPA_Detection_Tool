class MagicalWaitingNumber:
    @classmethod
    def terms_of_interest(cls):
        return ["usleep", "sleep", "Sleep", "MSleep", "sleep_for", "sleep_until", "thrd_sleep"]

    @classmethod
    def name(cls):
        return "mwn"

    @classmethod
    def header_name(cls):
        return "MAGICAL WAITING NUMBER"


class HardCodedFineTuning:
    @classmethod
    def name(cls):
        return "hcft"

    @classmethod
    def header_name(cls):
        return "HARD CODED FINE TUNING"


MAGICAL_WAITING_NUMBER: str = MagicalWaitingNumber.name()
HARDCODED_FINE_TUNING: str = HardCodedFineTuning.name()

pattern_lookup = {
    MAGICAL_WAITING_NUMBER: MagicalWaitingNumber,
    HARDCODED_FINE_TUNING: HardCodedFineTuning,
}
