from tests.test_logic import run_tests as run_logic_tests
from tests.test_ai import run_tests as run_ai_tests
from tests.test_game import run_tests as run_game_tests

if __name__ == "__main__":
    run_logic_tests()
    run_ai_tests()
    run_game_tests()
    print("All tests passed.")
