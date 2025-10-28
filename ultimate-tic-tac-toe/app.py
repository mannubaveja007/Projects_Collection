import numpy as np
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

class UltimateTicTacToe:
    def __init__(self):
        # Initialize scores and move counts first
        self.scores = {1: 0, -1: 0}  # X and O scores
        self.move_counts = {1: 0, -1: 0}
        self.move_history = []
        self._cached_legal_moves = None  # Cache for legal moves
        self.reset()

    def reset(self):
        self.board = np.zeros((9, 9), dtype=int)
        self.global_board = np.zeros((3, 3), dtype=int)
        self.current_player = 1
        self.next_subboard = None
        self.move_history = []
        self.move_counts = {1: 0, -1: 0}
        self._cached_legal_moves = None  # Invalidate cache
        return self.get_state()

    def check_winner(self, subboard):
        for i in range(3):
            if abs(sum(subboard[i, :])) == 3:
                return np.sign(sum(subboard[i, :]))
            if abs(sum(subboard[:, i])) == 3:
                return np.sign(sum(subboard[:, i]))
        diag1 = subboard[0, 0] + subboard[1, 1] + subboard[2, 2]
        diag2 = subboard[0, 2] + subboard[1, 1] + subboard[2, 0]
        if abs(diag1) == 3:
            return np.sign(diag1)
        if abs(diag2) == 3:
            return np.sign(diag2)
        return 0

    def get_subboard(self, sub_idx):
        row, col = divmod(sub_idx, 3)
        return self.board[row*3:(row+1)*3, col*3:(col+1)*3]

    def update_global_board(self):
        for i in range(9):
            r, c = divmod(i, 3)
            if self.global_board[r, c] == 0:
                winner = self.check_winner(self.get_subboard(i))
                if winner != 0:
                    self.global_board[r, c] = winner

    def get_legal_moves(self):
        # Return cached legal moves if available
        if self._cached_legal_moves is not None:
            return self._cached_legal_moves
        
        legal_moves = []
        
        # Check if the game is already won
        if abs(self.check_winner(self.global_board)) > 0:
            self._cached_legal_moves = legal_moves
            return legal_moves
            
        # Check if we need to play in a specific sub-board or if we can play anywhere
        if self.next_subboard is None or self.global_board[self.next_subboard // 3, self.next_subboard % 3] != 0:
            # Can play in any non-captured sub-board
            for sub_idx in range(9):
                if self.global_board[sub_idx // 3, sub_idx % 3] == 0:
                    sub = self.get_subboard(sub_idx)
                    for i in range(3):
                        for j in range(3):
                            if sub[i, j] == 0:
                                global_r, global_c = (sub_idx//3)*3 + i, (sub_idx%3)*3 + j
                                legal_moves.append((global_r, global_c))
        else:
            # Must play in the specified sub-board
            sub = self.get_subboard(self.next_subboard)
            for i in range(3):
                for j in range(3):
                    if sub[i, j] == 0:
                        global_r, global_c = (self.next_subboard//3)*3 + i, (self.next_subboard%3)*3 + j
                        legal_moves.append((global_r, global_c))
        
        # Cache the computed legal moves
        self._cached_legal_moves = legal_moves
        return legal_moves

    def step(self, r, c):
        if (r, c) not in self.get_legal_moves():
            return False, "Invalid move"
        self.board[r, c] = self.current_player
        self.move_history.append((r, c, self.current_player, self.next_subboard))
        self.move_counts[self.current_player] += 1
        self.next_subboard = (r % 3) * 3 + (c % 3)
        self._cached_legal_moves = None  # Invalidate cache after move
        self.update_global_board()
        winner = self.check_winner(self.global_board)
        # Recompute legal moves once for checking done state
        legal_moves = self.get_legal_moves()
        done = winner != 0 or len(legal_moves) == 0
        if winner != 0:
            self.scores[winner] += 1
        self.current_player *= -1
        return True, self.get_state(done, winner)

    def undo(self):
        if not self.move_history:
            return False, "No moves to undo"
        r, c, player, prev_sub = self.move_history.pop()
        self.board[r, c] = 0
        self.current_player = player
        self.next_subboard = prev_sub
        self.move_counts[player] -= 1
        self._cached_legal_moves = None  # Invalidate cache after undo
        self.update_global_board()
        return True, self.get_state()

    def get_state(self, done=False, winner=0):
        return {
            'board': self.board.tolist(),
            'global_board': self.global_board.tolist(),
            'current_player': self.current_player,
            'done': done,
            'winner': winner,
            'next_subboard': self.next_subboard,
            'legal_moves': self.get_legal_moves(),
            'scores': self.scores,
            'move_counts': self.move_counts
        }

game = UltimateTicTacToe()

HTML_PAGE = '''
<!doctype html>
<html>
<head>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&display=swap');

  body {font-family: 'Caveat', cursive; background-color: #fdfcf7; color: #222; max-width: 800px; margin: 0 auto; padding: 0 20px;}
  table {border-collapse: collapse; margin: 20px auto; box-shadow: 0 0 12px rgba(0,0,0,0.2);}
  td {width: 60px; height: 60px; text-align: center; vertical-align: middle; font-size: 36px;
      cursor: pointer; position: relative; border: 1px solid #444; transition: background 0.2s;}
  td:nth-child(3n) { border-right: 3px solid #000; }
  tr:nth-child(3n) td { border-bottom: 3px solid #000; }
  td:first-child { border-left: 3px solid #000; }
  tr:first-child td { border-top: 3px solid #000; }
  td.empty:hover {background-color: #f1f1c6;}
  td.legal::after {content: ""; width: 14px; height: 14px; border-radius: 50%; background: rgba(0,100,255,0.6);
                   position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);}
  td.highlight {background-color: rgba(255, 230, 150, 0.6) !important;}
  #scoreboard {text-align:center; margin: 15px; font-size: 18px;}
  button {
    padding: 8px 16px;
    margin: 0 5px;
    font-family: 'Caveat', cursive;
    font-size: 18px;
    border: 2px solid #444;
    background-color: #f9f7f0;
    cursor: pointer;
    border-radius: 6px;
    transition: all 0.2s;
  }
  button:hover {
    background-color: #f1f1c6;
  }
  input[type="text"] {
    font-family: 'Caveat', cursive;
    font-size: 16px;
    padding: 5px;
    margin: 0 10px;
    border: 1px solid #444;
    border-radius: 4px;
  }
</style>
</head>
<body>
<h1 style="text-align:center;">Ultimate Tic-Tac-Toe</h1>

<div style="text-align:center; margin-bottom:10px;">
  <label>X Player: <input type="text" id="playerX" value="Player X"></label>
  <label>O Player: <input type="text" id="playerO" value="Player O"></label>
</div>

<div id="scoreboard">
  <div><span id="nameX">Player X</span> (X) – Wins: <span id="scoreX">0</span>, Moves: <span id="movesX">0</span></div>
  <div><span id="nameO">Player O</span> (O) – Wins: <span id="scoreO">0</span>, Moves: <span id="movesO">0</span></div>
</div>

<div id="status" style="text-align:center; font-size:20px;"></div>
<table id="board"></table>

<div style="text-align:center; margin-top:10px;">
  <button onclick="resetGame()">Reset Game</button>
  <button onclick="undoMove()">Undo</button>
</div>

<script>
function drawBoard(state){
    let table = document.getElementById('board');
    table.innerHTML='';
    let legalMoves = new Set(state.legal_moves.map(m => m.join(',')));

    for(let i=0;i<9;i++){
        let row = table.insertRow();
        for(let j=0;j<9;j++){
            let cell = row.insertCell();
            let subRow = Math.floor(i/3);
            let subCol = Math.floor(j/3);
            let subWinner = state.global_board[subRow][subCol];
            let val = state.board[i][j];

            if(subWinner !== 0){
                // whole sub-board is captured → draw big symbol
                cell.innerHTML = (subWinner===1? 'X':'O');
                cell.style.fontSize = "48px";   // make symbol bigger
                cell.style.color = subWinner===1? "#c00" : "#00c";
                cell.style.fontWeight = "bold";
                cell.onclick = null;  // can't play inside captured block
            } else {
                // normal drawing
                cell.innerHTML = val===0? '' : (val===1? 'X':'O');
                if(val===0) cell.classList.add('empty');
                if(legalMoves.has(i+','+j)) cell.classList.add('legal');
                
                if(state.next_subboard!==null){
                    if(subRow===Math.floor(state.next_subboard/3) &&
                       subCol===state.next_subboard%3){
                        cell.classList.add('highlight');
                    }
                }
                cell.onclick = function(){ makeMove(i,j); };
            }
        }
    }

    let xName = document.getElementById('playerX').value;
    let oName = document.getElementById('playerO').value;
    document.getElementById('nameX').innerText = xName;
    document.getElementById('nameO').innerText = oName;

    document.getElementById('scoreX').innerText = state.scores[1];
    document.getElementById('scoreO').innerText = state.scores[-1];
    document.getElementById('movesX').innerText = state.move_counts[1];
    document.getElementById('movesO').innerText = state.move_counts[-1];

    document.getElementById('status').innerText = 'Current player: ' + 
        (state.current_player===1? xName + ' (X)': oName + ' (O)');

    if(state.done){
        if(state.winner===0){
            document.getElementById('status').innerText = 'Draw!';
        }else{
            let winnerName = state.winner===1? xName : oName;
            document.getElementById('status').innerText = winnerName + ' wins!';
        }
    }
}
function makeMove(r,c){
    fetch('/move',{
        method:'POST', 
        headers:{'Content-Type':'application/json'}, 
        body: JSON.stringify({r:r,c:c})
    })
    .then(res=>res.json())
    .then(data=> {
        if(data.error) {
            alert(data.error);
        } else {
            drawBoard(data);
        }
    })
    .catch(err => {
        console.error('Error making move:', err);
        alert('There was an error making your move. Please try again.');
    });
}
function resetGame(){
    fetch('/reset')
    .then(res=>res.json())
    .then(data=> drawBoard(data))
    .catch(err => {
        console.error('Error resetting game:', err);
        alert('There was an error resetting the game. Please refresh the page.');
    });
}

function undoMove(){
    fetch('/undo')
    .then(res=>res.json())
    .then(data=> {
        if(data.error) {
            alert(data.error);
        } else {
            drawBoard(data);
        }
    })
    .catch(err => {
        console.error('Error undoing move:', err);
        alert('There was an error undoing your move. Please try again.');
    });
}
document.getElementById('playerX').addEventListener('input', function(){
    document.getElementById('nameX').innerText = this.value || "Player X";
    // also update current player label live
    let status = document.getElementById('status').innerText;
    if(status.includes("(X)") || status.includes("(O)")){
        if(status.includes("(X)")) {
            document.getElementById('status').innerText = "Current player: " + (this.value || "Player X") + " (X)";
        }
    }
});

document.getElementById('playerO').addEventListener('input', function(){
    document.getElementById('nameO').innerText = this.value || "Player O";
    if(document.getElementById('status').innerText.includes("(O)")){
        document.getElementById('status').innerText = "Current player: " + (this.value || "Player O") + " (O)";
    }
});
window.onload = function(){ resetGame(); };
</script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/reset')
def reset():
    state = game.reset()
    return jsonify(state)

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    success, state = game.step(data['r'], data['c'])
    return jsonify(state if success else {'error':'Invalid move'})

@app.route('/undo')
def undo():
    success, state = game.undo()
    return jsonify(state if success else {'error':'No moves to undo'})

if __name__ == '__main__':
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)
