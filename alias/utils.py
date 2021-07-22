from datetime import tzinfo
from .models import Alias
import pytz


def get_aliases(target, start, end):
    """
    Get a list of aliases for a specific
    target in the specific time range.
    """
    aliases_target = Alias.objects.filter(target=target)
    aliases_in_range = [
        alias for alias in aliases_target if check_if_date_is_in_range(alias.start, start, end)
        and check_if_date_is_in_range(alias.end, start, end)
    ]
    validated_aliases = []
    temp = dict()
    for elem in aliases_in_range:
        if elem.alias in temp.keys():
            temp_alias = temp[elem.alias]
            start, end = (elem.start, elem.end)
            if not check_if_overlap(temp_alias.start, temp_alias.end, start, end):
                validated_aliases.append(elem)
        else:
            validated_aliases.append(elem)
            temp[elem.alias] = elem
    return validated_aliases


def replace_alias_at(existing_alias, replace_at, new_alias_value):
    """
    Replace an existing alias with a new one at a specific time point.
    """
    Alias.objects.create(value=new_alias_value, target=existing_alias.target,
                         start=replace_at, end=None)
    alias_to_replace = Alias.objects.get(existing_alias.id)
    alias_to_replace.end = replace_at
    alias_to_replace.save()


def check_if_overlap(start1, end1, start2, end2):
    """
    Check if date ranges overlap.
    """
    return start1 <= end2 and end1 >= start2


def check_if_date_is_in_range(str_date, from_date, to_date):
    """
    Check if specific date is in date range.
    """
    return str_date > from_date and str_date < to_date
