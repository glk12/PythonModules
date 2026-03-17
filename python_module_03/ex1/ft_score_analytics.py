from sys import argv


def parse_score(args: list[str]) -> list[int]:
    nums = []
    try:
        for str in args:
            nums.append(int(str))
    except ValueError as e:
        print("Error: Arguments must be numbers")

    return nums

def ft_score_analytics() -> None:
    if len(argv[1:]) < 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    score = parse_score(argv[1:])
    print("=== Player Score Analytics ===")
    print(f"Scores processed: {score}")
    print(f"Total players: {len(score)}")
    print(f"Total score: {sum(score)}")
    print(f"Average score: {(sum(score) / len(score)):.1f}")
    print(f"High score: {max(score)}")
    print(f"Low score: {min(score)}")
    print(f"Score range: {max(score) - min(score)}\n")
    

if __name__ == "__main__":
    ft_score_analytics()