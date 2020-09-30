import random

import numpy as np


# Set Game Environment


class tic_tac_toe(object):
    def __init__(self):
        self.board = np.full((3, 3), 2)

    def toss(self):
        """
        users : 0 or 1
        랜덤하게 순서를 정해준다.
        """
        turn = np.random.randint(0, 2, size=1)

        if turn.mean() == 1:
            self.turn_monitor = 1
        elif turn.mean() == 0:
            self.turn_monitor = 0
        return self.turn_monitor

    def move(self, player, coord):
        """
        Movement

        player : 현재 turn인 player(0 or 1)
        coord : player가 놓으려고 하는 위치
        --> 놓으려고 하는 자리가 적합한 자리인지 확인해준다.
        """
        if self.board[coord] != 2 or self.game_status() != 'In Progress' or self.turn_monitor != player:
            raise ValueError("Invalid move")

        # 적합함이 확인 됨
        self.board[coord] = player
        self.turn_monitor = 1 - player  # player 1 --> player 0, player 0 --> player 1

        return self.game_status(), self.board

    def game_status(self):
        """
        게임의 현재 상태 확인

        return : "Won" or "Drawn" or "In Progress"
        """
        for i in range(self.board.shape[0]):
            # player가 한 행에 전부 놓은 경우(along rows)
            if 2 not in self.board[i, :] and len(set(self.board[i, :])) == 1:
                return "Won"
        for j in range(self.board.shape[1]):
            # player가 한 열에 전부 놓은 경우(along columns)
            if 2 not in self.board[:, j] and len(set(self.board[:, j])) == 1:
                return "Won"

        # 대각선 확인(diagonals)
        if 2 not in np.diag(self.board) and len(set(np.diag(self.board))) == 1:
            return "Won"
        if 2 not in np.diag(np.fliplr(self.board)) and len(set(np.diag(np.fliplr(self.board)))) == 1:
            return "Won"

        # Draw 확인(status가 아직 win이 아닐 경우)
        if not 2 in self.board:
            return "Drawn"
        else:
            return "In Progress"

def legal_moves_gen(cur_board_state, turn_monitor):
    """
    :param cur_board_state: 현재 게임판의 상태
    :param turn_monitor: 순서
    :return: 현재 상태에서 놓을 수 있는 coord에 대한 dictionary
    """
    legal_moves_dict = {}
    for i in range(cur_board_state.shape[0]):
        for j in range(cur_board_state.shape[1]):
            if cur_board_state[i, j] == 2: # 아직 빈칸일 때
                board_state_copy = cur_board_state.copy()
                board_state_copy[i, j] = turn_monitor # 여기에 놓을 때
                legal_moves_dict[(i, j)] = board_state_copy.flatten()
    return legal_moves_dict

def move_selector(model, cur_board_state, turn_monitor):
    """
    액션 선택 함수
    :param model: evaluator funtion(evaluate each possible next board state)
    :param cur_board_state:
    :param turn_monitor:
    :return: selected_move, new_board_state, score
    """
    tracker = {}
    legal_moves_dict = legal_moves_gen(cur_board_state, turn_monitor)
    for legal_move_coord in legal_moves_dict:
        score = model.predict(legal_moves_dict[legal_move_coord].reshape(1,9))
        tracker[legal_move_coord] = score
    selected_move = max(tracker, key=tracker.get) # 가장 높은 score
    new_board_state = legal_moves_dict[selected_move]
    score = tracker[selected_move]

    return selected_move, new_board_state, score


def row_winning_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan rowwise and identify coordinate amongst the legal coordinates that will
    result in a winning board state

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to win for the opponent
    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        # check for a win along rows
        for i in range(current_board_state_copy.shape[0]):
            if 2 not in current_board_state_copy[i, :] and len(set(current_board_state_copy[i, :])) == 1:
                selected_move = legal_move_coord
                return selected_move


def column_winning_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan column wise and identify coordinate amongst the legal coordinates that will
    result in a winning board state

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to win for the opponent
    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        for j in range(current_board_state_copy.shape[1]):
            if 2 not in current_board_state_copy[:, j] and len(set(current_board_state_copy[:, j])) == 1:
                selected_move = legal_move_coord
                return selected_move


def diag1_winning_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan diagonal and identify coordinate amongst the legal coordinates that will
    result in a winning board state

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to win for the opponent

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 2 not in np.diag(current_board_state_copy) and len(set(np.diag(current_board_state_copy))) == 1:
            selected_move = legal_move_coord
            return selected_move


def diag2_winning_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan second diagonal and identify coordinate amongst the legal coordinates that will
    result in a winning board state

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to win for the opponent

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 2 not in np.diag(np.fliplr(current_board_state_copy)) and len(
                set(np.diag(np.fliplr(current_board_state_copy)))) == 1:
            selected_move = legal_move_coord
            return selected_move


# ------------#

def row_block_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan rowwise and identify coordinate amongst the legal coordinates
    that will prevent the program
    from winning

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will block 1 from winning

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        for i in range(current_board_state_copy.shape[0]):
            if 2 not in current_board_state_copy[i, :] and (current_board_state_copy[i, :] == 1).sum() == 2:
                if not (2 not in current_board_state[i, :] and (current_board_state[i, :] == 1).sum() == 2):
                    selected_move = legal_move_coord
                    return selected_move


def column_block_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan column wise and identify coordinate amongst the legal coordinates that will prevent 1
    from winning

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will block 1 from winning

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor

        for j in range(current_board_state_copy.shape[1]):
            if 2 not in current_board_state_copy[:, j] and (current_board_state_copy[:, j] == 1).sum() == 2:
                if not (2 not in current_board_state[:, j] and (current_board_state[:, j] == 1).sum() == 2):
                    selected_move = legal_move_coord
                    return selected_move


def diag1_block_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan diagonal 1 and identify coordinate amongst the legal coordinates that will prevent 1
    from winning

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will block 1 from winning

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 2 not in np.diag(current_board_state_copy) and (np.diag(current_board_state_copy) == 1).sum() == 2:
            if not (2 not in np.diag(current_board_state) and (np.diag(current_board_state) == 1).sum() == 2):
                selected_move = legal_move_coord
                return selected_move


def diag2_block_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan second diagonal wise and identify coordinate amongst the legal coordinates that will
    result in a column having only 0s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 2 not in np.diag(np.fliplr(current_board_state_copy)) and (
                np.diag(np.fliplr(current_board_state_copy)) == 1).sum() == 2:
            if not (2 not in np.diag(np.fliplr(current_board_state)) and (
                    np.diag(np.fliplr(current_board_state)) == 1).sum() == 2):
                selected_move = legal_move_coord
                return selected_move


# ---------------#
def row_second_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan rowwise and identify coordinate amongst the legal coordinates that will
    result in a row having two 0s and no 1s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor

        for i in range(current_board_state_copy.shape[0]):
            if 1 not in current_board_state_copy[i, :] and (current_board_state_copy[i, :] == 0).sum() == 2:
                if not (1 not in current_board_state[i, :] and (current_board_state[i, :] == 0).sum() == 2):
                    selected_move = legal_move_coord
                    return selected_move


def column_second_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan column wise and identify coordinate amongst the legal coordinates that will
    result in a column having two 0s and no 1s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor

        for j in range(current_board_state_copy.shape[1]):
            if 1 not in current_board_state_copy[:, j] and (current_board_state_copy[:, j] == 0).sum() == 2:
                if not (1 not in current_board_state[:, j] and (current_board_state[:, j] == 0).sum() == 2):
                    selected_move = legal_move_coord
                    return selected_move


def diag1_second_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan diagonal wise and identify coordinate amongst the legal coordinates that will
    result in a column having two 0s and no 1s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 1 not in np.diag(current_board_state_copy) and (np.diag(current_board_state_copy) == 0).sum() == 2:
            if not (1 not in np.diag(current_board_state) and (np.diag(current_board_state) == 0).sum() == 2):
                selected_move = legal_move_coord
                return selected_move


def diag2_second_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan second diagonal wise and identify coordinate amongst
    the legal coordinates that will result in a column having two 0s and no 1s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where opponent places their mark

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 1 not in np.diag(np.fliplr(current_board_state_copy)) and (
                np.diag(np.fliplr(current_board_state_copy)) == 0).sum() == 2:
            if not (1 not in np.diag(np.fliplr(current_board_state)) and (
                    np.diag(np.fliplr(current_board_state)) == 0).sum() == 2):
                selected_move = legal_move_coord
                return selected_move


def opponent_move_selector(current_board_state, turn_monitor, mode):
    """Function that picks a legal move for the opponent

    Args:
    current_board_state: Current board state
    turn_monitor: whose turn it is to move
    mode: whether hard or easy mode

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead to two 0s being there (and no 1s)

    """
    legal_moves_dict = legal_moves_gen(current_board_state, turn_monitor)

    winning_move_checks = [row_winning_move_check, column_winning_move_check, diag1_winning_move_check,
                           diag2_winning_move_check]
    block_move_checks = [row_block_move_check, column_block_move_check, diag1_block_move_check, diag2_block_move_check]
    second_move_checks = [row_second_move_check, column_second_move_check, diag1_second_move_check,
                          diag2_second_move_check]

    if mode == "Hard":
        random.shuffle(winning_move_checks)
        random.shuffle(block_move_checks)
        random.shuffle(second_move_checks)

        for fn in winning_move_checks:
            if fn(current_board_state, legal_moves_dict, turn_monitor):
                return fn(current_board_state, legal_moves_dict, turn_monitor)

        for fn in block_move_checks:
            if fn(current_board_state, legal_moves_dict, turn_monitor):
                return fn(current_board_state, legal_moves_dict, turn_monitor)

        for fn in second_move_checks:
            if fn(current_board_state, legal_moves_dict, turn_monitor):
                return fn(current_board_state, legal_moves_dict, turn_monitor)

        selected_move = random.choice(list(legal_moves_dict.keys()))
        return selected_move
    ##

    elif mode == "Easy":
        legal_moves_dict = legal_moves_gen(current_board_state, turn_monitor)
        selected_move = random.choice(list(legal_moves_dict.keys()))
        return selected_move
