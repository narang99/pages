"""
Tests the hypothesis: when a Hindi character name is split into multiple
subword pieces by the tokenizer, and the word is "colored" (i.e. the emotion
vector fires on at least one of its pieces), the later pieces carry higher
activation than the earlier pieces.

Run from the post directory:
    python3 analyze_name_split.py

Requires the emotion-reports/hindi_translated/*.html reports to be present
(these are the ColoredTokens circuitsvis dumps already checked into the repo).
"""

import re
import json
import statistics
from collections import Counter

REPORT_DIR = "emotion-reports/hindi_translated"
EMOTIONS = ["happy", "excited", "kind", "angry", "desperate", "disgusted", "sad"]

# Character names, hand-collected by grepping the raw story text for the
# Hindi "X नाम..." ("named X") pattern across all 7 reports. See the
# name-discovery snippet at the bottom of this file if you want to regenerate
# this list from scratch.
NAMES = [
    "एमी", "सोफिया", "लिली", "बॉब", "सैम", "एमिली",
    "जॉयस", "जैक", "सैली", "बेला", "जॉन",
]

# "Colored" threshold on a single token's projection value. Anything below
# this is treated as noise / not meaningfully activated.
COLOR_THRESHOLD = 15


def parse_report(fname):
    """Extract {story_text: {tokens, values, title}} from a circuitsvis HTML report."""
    content = open(fname, encoding="utf-8").read()
    blocks = re.findall(
        r'render\(\s*"([^"]+)",\s*ColoredTokens,\s*(\{.*?\})\s*\);?\s*</script>',
        content,
        re.S,
    )
    stories = {}
    for title, obj in blocks:
        d = json.loads(obj)
        text = "".join(d["tokens"])
        stories[text] = {"tokens": d["tokens"], "values": d["values"], "title": title}
    return stories


def word_runs(tokens):
    """
    Group a SentencePiece token list into "words": a token starting with the
    SentencePiece leading-space marker '▁' (or the very first token) followed
    by any continuation tokens that don't start with '▁'.
    Returns a list of (start, end_exclusive) index pairs.
    """
    runs = []
    i = 0
    while i < len(tokens):
        if tokens[i].startswith("▁") or i == 0:
            j = i + 1
            while j < len(tokens) and not tokens[j].startswith("▁"):
                j += 1
            runs.append((i, j))
            i = j
        else:
            i += 1
    return runs


def find_name_occurrences(data):
    """Scan every story in every emotion report for occurrences of NAMES."""
    occurrences = []
    for emotion, stories in data.items():
        for text, d in stories.items():
            tokens, values = d["tokens"], d["values"]
            for start, end in word_runs(tokens):
                word = "".join(tokens[start:end]).replace("▁", "")
                if word in NAMES:
                    occurrences.append(
                        {
                            "word": word,
                            "n_pieces": end - start,
                            "values": values[start:end],
                            "emotion": emotion,
                            "context": "".join(
                                tokens[max(0, start - 3): min(len(tokens), end + 3)]
                            ).replace("▁", " "),
                        }
                    )
    return occurrences


def first_second_half(values):
    """Split a token-value list into (first half, second half), floor-split
    at n//2 so odd-length runs put the extra piece in the second half."""
    half = len(values) // 2
    return values[:half], values[half:]


def main():
    data = {e: parse_report(f"{REPORT_DIR}/{e}_report.html") for e in EMOTIONS}

    occurrences = find_name_occurrences(data)
    print(f"Total name occurrences found: {len(occurrences)}")
    print("Piece-count distribution:", Counter(o["n_pieces"] for o in occurrences))
    print()

    colored = [o for o in occurrences if max(o["values"]) > COLOR_THRESHOLD]
    print(f"Colored occurrences (max piece value > {COLOR_THRESHOLD}): "
          f"{len(colored)} / {len(occurrences)}")

    first_means, second_means = [], []
    for o in colored:
        fh, sh = first_second_half(o["values"])
        if not fh or not sh:
            continue  # shouldn't happen since n_pieces >= 2, but be safe
        first_means.append(statistics.mean(fh))
        second_means.append(statistics.mean(sh))

    wins = sum(1 for a, b in zip(first_means, second_means) if b > a)
    ties = sum(1 for a, b in zip(first_means, second_means) if b == a)
    losses = len(first_means) - wins - ties

    print(f"mean first-half value:  {statistics.mean(first_means):.2f}")
    print(f"mean second-half value: {statistics.mean(second_means):.2f}")
    print(f"second half > first half: {wins}/{len(first_means)}")
    print(f"second half = first half: {ties}/{len(first_means)}")
    print(f"second half < first half: {losses}/{len(first_means)}")
    print()

    print("=== Colored occurrences, sorted by name ===")
    for o in sorted(colored, key=lambda o: o["word"]):
        vals = [round(v, 1) for v in o["values"]]
        print(f"{o['word']:8s} n={o['n_pieces']}  values={vals}  "
              f"[{o['emotion']}]  ctx: {o['context']}")


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# Name-discovery snippet (not run by default): how NAMES above was produced.
# Uncomment / adapt if you want to regenerate the candidate list from scratch
# instead of trusting the hardcoded one.
# ---------------------------------------------------------------------------
#
# def discover_names(data):
#     seen = set()
#     candidates = set()
#     for stories in data.values():
#         for text in stories:
#             if text in seen:
#                 continue
#             seen.add(text)
#             readable = text.replace("▁", " ")
#             for m in re.finditer(r"([^\s।,]{2,20})\s+नाम", readable):
#                 candidates.add(m.group(1))
#     return candidates
#
# This pattern relies on the common Hindi phrasing "<Name> नाम का/की ..."
# ("a character named <Name>"). It's a heuristic, not exhaustive - it will
# miss names that are never introduced with this exact phrasing, and it will
# catch some non-name false positives (e.g. pronouns "उसका"/"जिसका" showed up
# and had to be manually filtered out).
