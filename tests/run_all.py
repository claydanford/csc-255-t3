from tests.test_logic import *

if __name__ == "__main__":
    test_check_winner_x_top_row()
    test_check_winner_o_middle_row()
    test_check_winner_x_diagonal()
    test_check_winner_none()
    test_get_winning_line_returns_triple()
    test_get_winning_line_none()
    test_is_draw_true()
    test_is_draw_false_winner()
    test_is_draw_false_not_full()
    test_is_valid_move_empty_cell()
    test_is_valid_move_occupied_cell()
    test_is_valid_move_out_of_range()
    test_get_empty_indices_all_empty()
    test_get_empty_indices_none_empty()
    test_get_empty_indices_partial()
    print("All tests passed.")
