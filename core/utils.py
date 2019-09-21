from ipware import get_client_ip

from core.config import KEYWORD_SOLUTIONS
from core.models import SolutionTry


def get_ip(request):
    return get_client_ip(request)[0]


def _check_solution_found():
    # Get all solutions that have 8 correct answers
    all_correct =  SolutionTry.objects.filter(
        correct_count=8,
    )

    # Compare solutions AGAIN (just to be 100% sure the puzzle has been solved)
    for s in all_correct:
        keywords = ",".join(list(sorted(s.keywords.split(","))))
        solution = ",".join(list(sorted(KEYWORD_SOLUTIONS)))
        if keywords == solution:
            return True

    return False
