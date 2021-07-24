from .models import Alias


def get_aliases(target, start, end):
    """
    Get a list of aliases for a specific
    target in the specific time range.

    Args:
        target (string): a slugs of other model/app
        start (datetime): start time when alias is active
        end (datetime, None): end time when alias is active or None
    Returns:
        list of active aliases at specific time range

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
    New object is saved to database

    Args:
        existing_alias (Alias): alias objects to replace
        replace_at (datetime): the time point when object is replaced
        new_alias_value (string) new alias value for new alias object

    Returns:
        bool: True if overlap, False if not

    """
    Alias.objects.create(alias=new_alias_value, target=existing_alias[0].target,
                         start=replace_at, end=None)
    alias_to_replace = Alias.objects.get(pk=existing_alias[0].id)
    alias_to_replace.end = replace_at
    alias_to_replace.save()


def check_if_overlap(start1, end1, start2, end2):
    """Check if date ranges overlap.

    Args:
        start1 (datetime): start time of the first
        end1 (datetime) end time of the first range
        start2 (datetime) start time of the second range
        end2 (datetime) end time of the second range
    """
    return start1 <= end2 and end1 >= start2


def check_if_date_is_in_range(str_date, from_date, to_date):
    """Check if specific date is in date range.

    Args:
        str_date (datetime): time point to check
        from_date (datetime): the start of time range
        to_date (datetime): the end of time range
    Returns:
        bool: True if inside time range, False if out
    """
    return str_date > from_date and str_date < to_date
