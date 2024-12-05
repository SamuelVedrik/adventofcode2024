import re


def get_regex_rules(rules: list[str]):
    regex_rules = []
    for rule in rules:
        left, right = rule.split("|")
        regex_rule = re.compile(rf"{left}.*?,{right}")
        regex_rules.append((regex_rule, left, right))
    return regex_rules

def satisfy_rules(rule: re.Pattern, left:str, right:str, page:str):
    return rule.search(page) is not None or (left not in page or right not in page)

def satisfies_all_rules(regex_rules: list[tuple[re.Pattern, str, str]], page:str):
    return all(
        rule.search(page) is not None or (left not in page or right not in page)
        for rule, left, right in regex_rules
    )

def part1(rules, pages):
    regex_rules = get_regex_rules(rules)
    middle_pages = []
    for page in pages:
        if satisfies_all_rules(regex_rules, page):
            split_page = page.split(",")
            middle_pages.append(int(split_page[len(split_page) // 2]))
    print(middle_pages)
    print(sum(middle_pages))

def swap(left: str, right: str, page: str):
    page_list = page.split(",")
    left_page_idx = page_list.index(left)
    right_page_idx = page_list.index(right)
    page_list[left_page_idx], page_list[right_page_idx] = page_list[right_page_idx], page_list[left_page_idx]
    return ",".join(page_list)

def swap_until_correct(regex_rules: list[tuple[re.Pattern, str, str]], page: str):

    while not satisfies_all_rules(regex_rules, page):
        for rule, left, right in regex_rules:
            if not satisfy_rules(rule, left, right, page):
                page = swap(left, right, page)

    return page


def part2(rules: list[str], pages: list[str]):
    regex_rules = get_regex_rules(rules)
    to_fix = [
        page
        for page in pages
        if not satisfies_all_rules(regex_rules, page)
    ]
    fixed = [swap_until_correct(regex_rules, page) for page in to_fix]
    middle_pages = []
    for page in fixed:
        split_page = page.split(",")
        middle_pages.append(int(split_page[len(split_page) // 2]))
    print(middle_pages)
    print(sum(middle_pages))


if __name__ == "__main__":
    input_ = "inputs/day5.txt"
    # input_ = "test_inputs/day5.txt"
    with open(input_) as f:
        text = f.read()
        rules, pages = text.split("\n\n")
        rules = rules.split("\n")
        pages = pages.split("\n")

    # part1(rules, pages)
    part2(rules, pages)
