# ფუნქცია ამოწმებს თუ test არის original-ის ანაგრამა
def is_anagram(test, original):
    if len(test) != len(original):
        return False
        # თუ test-ის სირგძე არ უდრის original-ისას, ფუნქცია დააბრუნებს false-ს
    joined = (test + original).lower()
    # ეს test-ს და original-ს აყენებს lowercase-ში
    for char in joined:
        if joined.count(char) % 2 != 0:
            # თუ ამ სტრინგის 2ზე განაყოფის ნაშთი არ უდრის ნულს, ფუნქცია აბრუნებს false-ს
            return False
    return True