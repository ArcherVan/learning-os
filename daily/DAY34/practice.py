def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


def format_student(name: str, score: int) -> str:
    return f"{name}: {score}"

def get_score() -> int:
    return "100"

def main() -> None:
    total = calculate_total(12.5, 3)
    result = format_student("张三", 95)
    score = get_score()
    print(total)
    print(result)
    print(score)

if __name__ == "__main__":
    main()