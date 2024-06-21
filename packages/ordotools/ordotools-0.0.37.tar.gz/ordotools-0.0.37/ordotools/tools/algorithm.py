from copy import deepcopy

from importlib import import_module

from ordotools.tools.feast import Feast

from ordotools.tools.helpers import LiturgicalYearMarks
from ordotools.tools.helpers import days
from ordotools.tools.helpers import ladys_office
from ordotools.tools.helpers import leap_year

from ordotools.tools.translations import Translations
from ordotools.tools.temporal import Temporal

from ordotools.sanctoral.diocese.roman import Sanctoral

# import logging


# logging.basicConfig(level=logging.DEBUG)


class LiturgicalCalendar:

    def __init__(self, year, diocese, language, country=""):
        self.year = year
        self.diocese = diocese
        self.language = language
        # WARN: theoretically we could have more than one transfer
        self.transfers = None
        self.temporal = Temporal(self.year).return_temporal()

    def expand_octaves(self, feast: Feast) -> dict:
        octave = ()
        day = 2
        while day < 9:
            # NOTE: since we already have the feast object,
            #       we can just make a function to set the date.
            #       We also have to empty the commemorations.
            new_feast = Feast(
                feast.date+days(day-1),
                {
                    "code": feast.code+1,
                    "rank": [feast.rank_n, feast.rank_v],
                    "infra_octave_name": feast.infra_octave_name,
                    "day_in_octave": feast.day_in_octave,
                    "color": feast.color,
                    "mass": feast.mass,
                    "com_1": feast.com_1 if feast.com_1 is not None else {},
                    "com_2": feast.com_2 if feast.com_2 is not None else {},
                    "com_3": feast.com_3 if feast.com_3 is not None else {},
                    "matins": {},
                    "lauds": {},
                    "prime": {},
                    "little_hours": {},
                    "vespers": feast.vespers,
                    "compline": {},
                    "nobility": feast.nobility,
                    "office_type": feast.office_type,
                    "fasting": feast.fasting,
                }
            )
            # TODO: all this can be handled above
            if day == 8:
                new_feast.day_in_octave = day
            else:
                new_feast.day_in_octave = day
            new_feast.fasting = False
            new_feast.rank_v = "feria"
            new_feast.rank_n = 18 if day < 6 else 13
            new_feast.reset_commemorations()
            octave += (new_feast,)
            day += 1
        return octave

    def find_octave(self, year: tuple) -> tuple:
        temporals = [feast["code"] for feast in self.temporal.values()]
        for candidate in year:
            if candidate.code in temporals:
                continue
            elif candidate.octave is True:
                octave = self.expand_octaves(deepcopy(candidate))
                year = self.add_feasts(master=year, addition=octave)
        return year

    def commemorate(self, feast: Feast, com: Feast) -> Feast:
        feast.com_1 = com.feast_properties
        feast.com_1 = {
            "code": feast.code,
            "rank": [feast.rank_n, feast.rank_v],
            "infra_octave_name": feast.infra_octave_name,
            "day_in_octave": feast.day_in_octave,
            "color": feast.color,
            "mass": feast.mass,
            "com_1": feast.com_1 if feast.com_1 is not None else {},
            "com_2": feast.com_2 if feast.com_2 is not None else {},
            "com_3": feast.com_3 if feast.com_3 is not None else {},
            "matins": {},
            "lauds": {},
            "prime": {},
            "little_hours": {},
            "vespers": feast.vespers,
            "compline": {},
            "nobility": feast.nobility,
            "office_type": feast.office_type,
            "fasting": feast.fasting,
        }
        return feast

    def rank_by_nobility(self, feast_1: Feast, feast_2: Feast) -> dict:
        for x in range(6):
            if feast_1.nobility[x] < feast_2.nobility[x]:
                return {'higher': feast_1, 'lower': feast_2}
            elif feast_1.nobility[x] > feast_2.nobility[x]:
                return {'higher': feast_2, 'lower': feast_1}
            else:
                pass
        return {'higher': feast_1, 'lower': feast_2}

    def rank(self, dynamic: Feast, static: Feast) -> Feast:
        if dynamic.rank_n == static.rank_n:
            return self.rank_by_nobility(dynamic, static)['higher']
        else:
            candidates = {dynamic.rank_n: dynamic, static.rank_n: static}
            higher = candidates[sorted(candidates)[0]]
            lower = candidates[sorted(candidates)[1]]
            # print(f"HIGHER =\t{higher.name}, {higher.rank_n}")
            # print(f"LOWER  =\t{lower.name}, {lower.rank_n}\n")
            if lower.rank_n >= 22:
                pass
            if lower.rank_n == 19:
                return self.commemorate(feast=higher, com=lower)
            if higher.rank_n <= 4:
                if lower.rank_n == 3:
                    self.transfers = higher
                    return lower
                if lower.rank_n <= 10:
                    self.transfers = lower
                    return higher
                else:
                    return higher
            elif higher.rank_n <= 9:
                if lower.rank_n <= 10:
                    self.transfers = lower
                    return higher
                else:  # HACK: This is just to get the Queenship transfer to work
                    return self.commemorate(feast=higher, com=lower)
            elif 14 <= lower.rank_n <= 16:
                return self.commemorate(feast=higher, com=lower)
            else:
                return self.commemorate(feast=higher, com=lower)

    def transfer_feast(self, feast: Feast) -> Feast:
        return self.rank(dynamic=self.transfers, static=feast)

    # NOTE: before refactoring, compilation in 0.940s
    #       after refactoring... 0.258s
    def build_feasts(self, candidates: dict) -> dict:
        feasts = ()
        for date, data in candidates.items():
            feast = Feast(date, data, lang=self.language)
            feasts += (feast,)
        return feasts

    def initialize(self, to_initialize: list):
        inititalized = {
            "temporal": (),
            "sanctoral": (),
        }
        for i, dictionary in enumerate(to_initialize):
            if i == 0:
                inititalized["temporal"] += self.build_feasts(dictionary)
            else:
                inititalized["sanctoral"] += self.build_feasts(dictionary)
        return inititalized

    def add_feasts(self, master: tuple, addition: tuple) -> dict:
        calendar = ()
        master_expanded = {}
        for feast in master:
            master_expanded.update({feast.date: feast})
        addition_expanded = {}
        for feast in addition:
            addition_expanded.update({feast.date: feast})
        # we might be able to speed things up here using set()

        # def intersections(set_1, set_2):
        #     the_set_1 = set(set_1)
        #     the_set_2 = set(set_2)
        #     return the_set_1.intersection(the_set_2)

        for date in master_expanded.keys():
            if date in addition_expanded.keys():
                feast = self.rank(
                    dynamic=addition_expanded[date],
                    static=master_expanded[date]
                )
            else:
                feast = master_expanded[date]
            if self.transfers is not None:
                # FIXME: this is where the problem starts
                result = self.transfer_feast(
                    feast
                )
                if result.code == feast.code:
                    pass
                else:
                    self.transfers = None
                    result.date = feast.date
                    feast = result
            calendar += (feast,)
        return calendar

    def our_ladys_saturday(self, calendar: tuple) -> dict:
        """
        Adds Office of the Blessed Virgin Mary on Saturdays.

        In omnibus Sabbatis per annum extra Adventum et Quadragesimam, ac nisi
        Quatuor tempora aut Vigilia; occurrant, vel nisi fieri debeat de Feria propter
        Officium alicujus Dominica; aliquando infra Hebdomadam ponendum , ut in Rubrica
        de Dominicis dictum est; et nisi fiat Officium novem Lectionum, vel de Octava
        Pascha; et Pentecostes, semper fit Officium de sancta Maria, eo modo, quo fit de
        Festo Simplici, quemadmodum circa finem Breviarii disponitur. De Festo autem
        Simplici, in Sabbato occurrente, fit tantum commemoratio.
        """
        year = list(calendar)
        office = ladys_office  # TODO: add this according to the season
        for pos, feast in enumerate(year):
            if feast.date.strftime("%w") == str(6):
                first_advent = LiturgicalYearMarks(self.year).first_advent
                last_advent = LiturgicalYearMarks(self.year).last_advent
                lent_begins = LiturgicalYearMarks(self.year).lent_begins
                lent_ends = LiturgicalYearMarks(self.year).lent_ends
                if lent_begins <= feast.date <= lent_ends:
                    continue
                elif first_advent <= feast.date <= last_advent:
                    continue
                else:
                    if feast.rank_n > 20:
                        # FIX: there should be a commemoration here for the replaced feast?
                        year[pos] = Feast(feast.date, office, lang=self.language)
                    else:
                        continue
        return tuple(year)

    def add_translation(self, compiled_calendar: Feast) -> list:
        year = []
        translations = Translations()
        for feast in compiled_calendar:
            feast.name = translations.translations()[feast.code][self.language]
            print(feast.name)
            if isinstance(feast.com_1["name"], int):
                feast.com_1 = translations.translations()[feast.com_1["name"]][self.language]
            year.append(feast)
        return year

    def build(self) -> list:
        saints = Sanctoral(self.year)
        if self.diocese == 'roman':
            sanctoral = saints.data if leap_year(self.year) is False else saints.leapyear()
        else:
            diocese = import_module(
                f"sanctoral.diocese.{self.diocese}",
            )
            sanctoral = diocese.Diocese(self.year).calendar()
        initialized = self.initialize([self.temporal, sanctoral])
        full_calendar = self.add_feasts(initialized["temporal"], initialized["sanctoral"])
        full_calendar = self.our_ladys_saturday(full_calendar)
        full_calendar = self.find_octave(year=full_calendar)
        full_calendar = self.add_translation(full_calendar)

        return full_calendar
