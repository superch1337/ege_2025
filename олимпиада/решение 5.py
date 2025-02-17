# Python

def parse_age(age_str):
    if age_str == '<1':
        return (0, 12)
    elif age_str == '1-5':
        return (12, 60)
    elif age_str == '>5':
        return (60, float('inf'))
    else:
        return None

def categorize_pet(requests, pets):
    match_count = 0
    review_count = 0

    for r_animal, r_breed, r_color, r_age in requests:
        r_age_range = parse_age(r_age)

        for p_animal, p_gender, p_breed, p_color, p_age_months in pets:
            p_age_years = p_age_months // 12

            if (
                (r_animal == p_animal or (r_animal in ["кот", "кошка"] and p_animal == "кошка") or (r_animal in ["пес", "собака"] and p_animal == "собака")) and
                (r_breed == p_breed) and
                (r_color == p_color) and
                (r_age_range[0] <= p_age_months < r_age_range[1])
            ):
                match_count += 1
                continue

            mismatch_count = 0
            if not (r_animal == p_animal or (r_animal in ["кот", "кошка"] and p_animal == "кошка") or (r_animal in ["пес", "собака"] and p_animal == "собака")):
                mismatch_count += 1
            if r_breed != p_breed:
                mismatch_count += 1
            if r_color != p_color:
                mismatch_count += 1
            if not (r_age_range[0] <= p_age_months < r_age_range[1]):
                mismatch_count += 1

            if mismatch_count == 1:
                review_count += 1

    return match_count, review_count

n = int(input())
requests = [input().split() for _ in range(n)]

k = int(input())
pets = [input().split() for _ in range(k)]

pets = [(animal, gender, breed, color, int(age_months)) for animal, gender, breed, color, age_months in pets]

match, review = categorize_pet(requests, pets)

print(f"Это мэтч! - {match}")
print(f"Присмотритесь - {review}")